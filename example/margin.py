# !/usr/bin/env python
# coding: utf-8
import logging
import random
from decimal import Decimal as D, ROUND_UP, getcontext

from gate_api import ApiClient, Configuration, Loan, MarginApi, Order, RepayRequest, SpotApi, Transfer, WalletApi
from gate_api.exceptions import GateApiException

from config import RunConfig

logger = logging.getLogger(__name__)


def margin_demo(run_config):
    # type: (RunConfig) -> None
    currency_pair = 'BTC_USDT'
    currency = currency_pair.split("_")[1]

    # Initialize API client
    # Setting host is optional. It defaults to https://api.gateio.ws/api/v4
    config = Configuration(key=run_config.api_key, secret=run_config.api_secret, host=run_config.host_used)
    spot_api = SpotApi(ApiClient(config))
    margin_api = MarginApi(ApiClient(config))
    wallet_api = WalletApi(ApiClient(config))

    # retrieve currency pair last price
    tickers = spot_api.list_tickers(currency_pair=currency_pair)
    assert len(tickers) == 1
    last_price = tickers[0].last
    logger.info("currency pair %s last price %s", currency_pair, last_price)

    pairs = margin_api.list_margin_currency_pairs()
    pair = next(p for p in pairs if p.id == currency_pair)
    loan_amount = D("0") if not pair.min_quote_amount else D(pair.min_quote_amount)

    if pair.min_base_amount:
        min_loan_amount = D(pair.min_base_amount) * D(last_price)
        if loan_amount < min_loan_amount:
            loan_amount = min_loan_amount
    logger.info("minimum loan amount in currency pair %s: %s %s", currency_pair, str(loan_amount), currency)

    getcontext().prec = 8
    getcontext().rounding = ROUND_UP

    # example to lend
    funding_accounts = margin_api.list_funding_accounts(currency=currency)
    lend_amount = loan_amount + D(random.random())
    if len(funding_accounts) == 1 and D(funding_accounts[0].available) >= lend_amount:
        lending_loan = Loan(amount=str(lend_amount), auto_renew=False, days=10, currency=currency, rate="0.002",
                            side='lend')
        created_loan = margin_api.create_loan(lending_loan)
        logger.info("place a lending loan %s with currency %s, rate %s, amount %s", created_loan.id,
                    created_loan.currency, created_loan.rate, created_loan.amount)
        loan_result = margin_api.get_loan(created_loan.id, 'lend')
        if loan_result.status == 'loaned':
            records = margin_api.list_loan_records(loan_result.id)
            for r in records:
                logger.info("loan %s is borrowed with record id %s, amount %s, status: %s", r.loan_id, r.id, r.amount,
                            r.status)
        else:
            margin_api.cancel_loan(created_loan.id, currency)

    assert pair.leverage
    margin = loan_amount / (pair.leverage - 1)
    accounts = margin_api.list_margin_accounts(currency_pair=currency_pair)
    assert len(accounts) == 1
    available = D(accounts[0].quote.available)
    logger.info("available margin balance of currency %s in currency pair %s: %s", currency, currency_pair,
                str(available))
    if margin > available:
        transfer = Transfer(currency_pair=currency_pair, currency=currency, amount=str(margin - available),
                            _from='spot', to='margin')
        wallet_api.transfer(transfer)
        logger.info("transferred %s %s to margin account", transfer.amount, transfer.currency)

    # borrow with minimum rate
    borrow_amount = loan_amount + D(random.random())
    min_rate_item = min(
        filter(lambda x: x.rate and D(x.amount) > borrow_amount, margin_api.list_funding_book(currency)),
        key=lambda x: D(x.rate)
    )
    loan = Loan(side='borrow', currency=currency, rate=min_rate_item.rate, amount=str(borrow_amount),
                days=min_rate_item.days, currency_pair=currency_pair)
    borrowed = margin_api.create_loan(loan)
    logger.info("borrowed %s %s in currency pair %s with rate %s, id %s", borrowed.amount, borrowed.currency,
                borrowed.currency_pair, borrowed.rate, borrowed.id)
    assert borrowed.status == 'loaned'

    # create margin order
    order_amount = spot_api.get_currency_pair(currency_pair).min_quote_amount
    order = Order(account='margin', currency_pair=currency_pair, price=last_price, amount=order_amount or "1",
                  side='sell')
    try:
        created_order = spot_api.create_order(order)
        logger.info("margin order created with id %s, status %s", created_order.id, created_order.status)
    except GateApiException as ex:
        logger.error("failed to create margin order: %s", ex)

    repay_request = RepayRequest(mode='all', currency=currency, currency_pair=currency_pair)
    margin_api.repay_loan(borrowed.id, repay_request)
    for r in margin_api.list_loan_repayments(borrowed.id):
        logger.info("loan %s repaid %s with interest %s", borrowed.id, r.principal, r.interest)
