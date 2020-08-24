# !/usr/bin/env python
# coding: utf-8
import logging
import time
from decimal import Decimal as D, ROUND_UP, getcontext

from gate_api import ApiClient, Configuration, FuturesApi, FuturesOrder, Transfer, WalletApi
from gate_api.exceptions import GateApiException

from config import RunConfig

logger = logging.getLogger(__name__)


def futures_demo(run_config):
    # type: (RunConfig) -> None
    settle = "usdt"
    contract = "BTC_USDT"

    # Initialize API client
    # Setting host is optional. It defaults to https://api.gateio.ws/api/v4
    config = Configuration(key=run_config.api_key, secret=run_config.api_secret, host=run_config.host_used)
    futures_api = FuturesApi(ApiClient(config))

    # update position leverage
    leverage = "3"
    futures_api.update_position_leverage(settle, contract, leverage)

    # retrieve position size
    position_size = 0
    try:
        position = futures_api.get_position(settle, contract)
        position_size = position.size
    except GateApiException as ex:
        if ex.label != "POSITION_NOT_FOUND":
            raise ex

    # set order size
    futures_contract = futures_api.get_futures_contract(settle, contract)
    order_size = 10
    if futures_contract.order_size_min and futures_contract.order_size_min > order_size:
        order_size = futures_contract.order_size_min
    if position_size < 0:
        order_size = 0 - order_size

    # example to update risk limit
    assert futures_contract.risk_limit_base
    assert futures_contract.risk_limit_step
    risk_limit = D(futures_contract.risk_limit_base) + D(futures_contract.risk_limit_step)
    futures_api.update_position_risk_limit(settle, contract, str(risk_limit))

    # retrieve last price to calculate margin needed
    tickers = futures_api.list_futures_tickers(settle, contract=contract)
    assert len(tickers) == 1
    last_price = tickers[0].last
    logger.info("last price of contract %s: %s", contract, last_price)

    getcontext().prec = 8
    getcontext().rounding = ROUND_UP

    assert futures_contract.quanto_multiplier
    margin = order_size * D(last_price) * D(futures_contract.quanto_multiplier) / D(leverage) * D("1.1")
    logger.info("needs margin amount: %s", str(margin))

    # if balance is not enough, transfer from spot account
    available = "0"
    try:
        futures_account = futures_api.list_futures_accounts(settle)
        available = futures_account.available
    except GateApiException as ex:
        if ex.label != "USER_NOT_FOUND":
            raise ex
    logger.info("futures account available: %s %s", available, settle.upper())
    if D(available) < margin:
        if run_config.use_test:
            logger.warning("testnet account balance not enough. make a transferal on web")
            return
        transfer = Transfer(amount=str(margin), currency=settle.upper(), _from='spot', to='futures')
        wallet_api = WalletApi(ApiClient(config))
        wallet_api.transfer(transfer)

    # example to cancel all open orders in contract
    futures_api.cancel_futures_orders(settle, contract)

    # order using market price
    order = FuturesOrder(contract=contract, size=order_size, price="0", tif='ioc')
    try:
        order_response = futures_api.create_futures_order(settle, order)
    except GateApiException as ex:
        logger.error("error encountered creating futures order: %s", ex)
        return
    logger.info("order %s created with status: %s", order_response.id, order_response.status)

    if order_response.status == 'open':
        futures_order = futures_api.get_futures_order(settle, str(order_response.id))
        logger.info("order %s status %s, total size %s, left %s", futures_order.id, futures_order.status,
                    futures_order.size, futures_order.left)
        futures_api.cancel_futures_order(settle, str(futures_order.id))
        logger.info("order %s cancelled", futures_order.id)
    else:
        time.sleep(0.2)
        order_trades = futures_api.get_my_trades(settle, contract=contract, order=order_response.id)
        assert len(order_trades) > 0
        trade_size = 0
        for t in order_trades:
            assert t.order_id == str(order_response.id)
            trade_size += t.size
            logger.info("order %s filled size %s with price %s", t.order_id, t.size, t.price)
        assert trade_size == order_size

        # example to update position margin
        futures_api.update_position_margin(settle, contract, "0.01")
