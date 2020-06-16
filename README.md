# gate-api
APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 4.13.0
- Package version: 4.13.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.gate.io/page/contacts](https://www.gate.io/page/contacts)

## Specific note for 4.8.0

**BREAKING** change:

4.8.0 add new support with different settle currency for futures API(BTC is the only one allowed before), which makes ALL methods in FuturesApi REQUIRE an additional `settle` parameter.

But previous `/futures/xxx` APIs are still preserved for compatibility usage(will be treated as BTC), so if one of the following condition is met:

- Changing all your futures method call to include `settle` is not a big issue for you
- You need to use futures settled in non-BTC currency

then you'd better move to 4.8.0 and changes all your futures method call to pass in `settle` parameter. Otherwise, you can stick to version<=4.7.3,
but will not receive any future API upgrade support

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/gateio/gateapi-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/gateio/gateapi-python.git`)

Then import the package:
```python
import gate_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import gate_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'
# uncomment the next line if using the API with another host
# configuration.host = 'https://some-other-host'
# configuration.proxy = 'http://localhost:1080'  # uncomment to proxy through a http proxy
# configuration.verify_ssl = False  # uncomment to turn off ssl verification
# More connection configuration is available in `Configuration` model.

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
settle = 'btc' # str | Settle currency (default to 'btc')
order_id = '12345' # str | ID returned on order successfully being created

try:
    # Cancel a single order
    api_response = api_instance.cancel_futures_order(settle, order_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_futures_order: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.gateio.ws/api/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*FuturesApi* | [**cancel_futures_order**](docs/FuturesApi.md#cancel_futures_order) | **DELETE** /futures/{settle}/orders/{order_id} | Cancel a single order
*FuturesApi* | [**cancel_futures_orders**](docs/FuturesApi.md#cancel_futures_orders) | **DELETE** /futures/{settle}/orders | Cancel all &#x60;open&#x60; orders matched
*FuturesApi* | [**cancel_price_triggered_order**](docs/FuturesApi.md#cancel_price_triggered_order) | **DELETE** /futures/{settle}/price_orders/{order_id} | Cancel a single order
*FuturesApi* | [**cancel_price_triggered_order_list**](docs/FuturesApi.md#cancel_price_triggered_order_list) | **DELETE** /futures/{settle}/price_orders | Cancel all open orders
*FuturesApi* | [**create_futures_order**](docs/FuturesApi.md#create_futures_order) | **POST** /futures/{settle}/orders | Create a futures order
*FuturesApi* | [**create_price_triggered_order**](docs/FuturesApi.md#create_price_triggered_order) | **POST** /futures/{settle}/price_orders | Create a price-triggered order
*FuturesApi* | [**get_futures_contract**](docs/FuturesApi.md#get_futures_contract) | **GET** /futures/{settle}/contracts/{contract} | Get a single contract
*FuturesApi* | [**get_futures_order**](docs/FuturesApi.md#get_futures_order) | **GET** /futures/{settle}/orders/{order_id} | Get a single order
*FuturesApi* | [**get_my_trades**](docs/FuturesApi.md#get_my_trades) | **GET** /futures/{settle}/my_trades | List personal trading history
*FuturesApi* | [**get_position**](docs/FuturesApi.md#get_position) | **GET** /futures/{settle}/positions/{contract} | Get single position
*FuturesApi* | [**get_price_triggered_order**](docs/FuturesApi.md#get_price_triggered_order) | **GET** /futures/{settle}/price_orders/{order_id} | Get a single order
*FuturesApi* | [**list_futures_account_book**](docs/FuturesApi.md#list_futures_account_book) | **GET** /futures/{settle}/account_book | Query account book
*FuturesApi* | [**list_futures_accounts**](docs/FuturesApi.md#list_futures_accounts) | **GET** /futures/{settle}/accounts | Query futures account
*FuturesApi* | [**list_futures_candlesticks**](docs/FuturesApi.md#list_futures_candlesticks) | **GET** /futures/{settle}/candlesticks | Get futures candlesticks
*FuturesApi* | [**list_futures_contracts**](docs/FuturesApi.md#list_futures_contracts) | **GET** /futures/{settle}/contracts | List all futures contracts
*FuturesApi* | [**list_futures_funding_rate_history**](docs/FuturesApi.md#list_futures_funding_rate_history) | **GET** /futures/{settle}/funding_rate | Funding rate history
*FuturesApi* | [**list_futures_insurance_ledger**](docs/FuturesApi.md#list_futures_insurance_ledger) | **GET** /futures/{settle}/insurance | Futures insurance balance history
*FuturesApi* | [**list_futures_order_book**](docs/FuturesApi.md#list_futures_order_book) | **GET** /futures/{settle}/order_book | Futures order book
*FuturesApi* | [**list_futures_orders**](docs/FuturesApi.md#list_futures_orders) | **GET** /futures/{settle}/orders | List futures orders
*FuturesApi* | [**list_futures_tickers**](docs/FuturesApi.md#list_futures_tickers) | **GET** /futures/{settle}/tickers | List futures tickers
*FuturesApi* | [**list_futures_trades**](docs/FuturesApi.md#list_futures_trades) | **GET** /futures/{settle}/trades | Futures trading history
*FuturesApi* | [**list_liquidates**](docs/FuturesApi.md#list_liquidates) | **GET** /futures/{settle}/liquidates | List liquidation history
*FuturesApi* | [**list_position_close**](docs/FuturesApi.md#list_position_close) | **GET** /futures/{settle}/position_close | List position close history
*FuturesApi* | [**list_positions**](docs/FuturesApi.md#list_positions) | **GET** /futures/{settle}/positions | List all positions of a user
*FuturesApi* | [**list_price_triggered_orders**](docs/FuturesApi.md#list_price_triggered_orders) | **GET** /futures/{settle}/price_orders | List all auto orders
*FuturesApi* | [**update_position_leverage**](docs/FuturesApi.md#update_position_leverage) | **POST** /futures/{settle}/positions/{contract}/leverage | Update position leverage
*FuturesApi* | [**update_position_margin**](docs/FuturesApi.md#update_position_margin) | **POST** /futures/{settle}/positions/{contract}/margin | Update position margin
*FuturesApi* | [**update_position_risk_limit**](docs/FuturesApi.md#update_position_risk_limit) | **POST** /futures/{settle}/positions/{contract}/risk_limit | Update position risk limit
*MarginApi* | [**cancel_loan**](docs/MarginApi.md#cancel_loan) | **DELETE** /margin/loans/{loan_id} | Cancel lending loan
*MarginApi* | [**create_loan**](docs/MarginApi.md#create_loan) | **POST** /margin/loans | Lend or borrow
*MarginApi* | [**get_loan**](docs/MarginApi.md#get_loan) | **GET** /margin/loans/{loan_id} | Retrieve one single loan detail
*MarginApi* | [**get_loan_record**](docs/MarginApi.md#get_loan_record) | **GET** /margin/loan_records/{loan_record_id} | Get one single loan record
*MarginApi* | [**list_funding_accounts**](docs/MarginApi.md#list_funding_accounts) | **GET** /margin/funding_accounts | Funding account list
*MarginApi* | [**list_funding_book**](docs/MarginApi.md#list_funding_book) | **GET** /margin/funding_book | Order book of lending loans
*MarginApi* | [**list_loan_records**](docs/MarginApi.md#list_loan_records) | **GET** /margin/loan_records | List repayment records of specified loan
*MarginApi* | [**list_loan_repayments**](docs/MarginApi.md#list_loan_repayments) | **GET** /margin/loans/{loan_id}/repayment | List loan repayment records
*MarginApi* | [**list_loans**](docs/MarginApi.md#list_loans) | **GET** /margin/loans | List all loans
*MarginApi* | [**list_margin_accounts**](docs/MarginApi.md#list_margin_accounts) | **GET** /margin/accounts | Margin account list
*MarginApi* | [**list_margin_currency_pairs**](docs/MarginApi.md#list_margin_currency_pairs) | **GET** /margin/currency_pairs | List all supported currency pairs supported in margin trading
*MarginApi* | [**merge_loans**](docs/MarginApi.md#merge_loans) | **POST** /margin/merged_loans | Merge multiple lending loans
*MarginApi* | [**repay_loan**](docs/MarginApi.md#repay_loan) | **POST** /margin/loans/{loan_id}/repayment | Repay a loan
*MarginApi* | [**update_loan**](docs/MarginApi.md#update_loan) | **PATCH** /margin/loans/{loan_id} | Modify a loan
*MarginApi* | [**update_loan_record**](docs/MarginApi.md#update_loan_record) | **PATCH** /margin/loan_records/{loan_record_id} | Modify a loan record
*SpotApi* | [**cancel_batch_orders**](docs/SpotApi.md#cancel_batch_orders) | **POST** /spot/cancel_batch_orders | Cancel a batch of orders with an ID list
*SpotApi* | [**cancel_order**](docs/SpotApi.md#cancel_order) | **DELETE** /spot/orders/{order_id} | Cancel a single order
*SpotApi* | [**cancel_orders**](docs/SpotApi.md#cancel_orders) | **DELETE** /spot/orders | Cancel all &#x60;open&#x60; orders in specified currency pair
*SpotApi* | [**create_batch_orders**](docs/SpotApi.md#create_batch_orders) | **POST** /spot/batch_orders | Create a batch of orders
*SpotApi* | [**create_order**](docs/SpotApi.md#create_order) | **POST** /spot/orders | Create an order
*SpotApi* | [**get_currency_pair**](docs/SpotApi.md#get_currency_pair) | **GET** /spot/currency_pairs/{currency_pair} | Get detail of one single order
*SpotApi* | [**get_order**](docs/SpotApi.md#get_order) | **GET** /spot/orders/{order_id} | Get a single order
*SpotApi* | [**list_candlesticks**](docs/SpotApi.md#list_candlesticks) | **GET** /spot/candlesticks | Market candlesticks
*SpotApi* | [**list_currency_pairs**](docs/SpotApi.md#list_currency_pairs) | **GET** /spot/currency_pairs | List all currency pairs supported
*SpotApi* | [**list_my_trades**](docs/SpotApi.md#list_my_trades) | **GET** /spot/my_trades | List personal trading history
*SpotApi* | [**list_order_book**](docs/SpotApi.md#list_order_book) | **GET** /spot/order_book | Retrieve order book
*SpotApi* | [**list_orders**](docs/SpotApi.md#list_orders) | **GET** /spot/orders | List orders
*SpotApi* | [**list_spot_accounts**](docs/SpotApi.md#list_spot_accounts) | **GET** /spot/accounts | List spot accounts
*SpotApi* | [**list_tickers**](docs/SpotApi.md#list_tickers) | **GET** /spot/tickers | Retrieve ticker information
*SpotApi* | [**list_trades**](docs/SpotApi.md#list_trades) | **GET** /spot/trades | Retrieve market trades
*WalletApi* | [**get_deposit_address**](docs/WalletApi.md#get_deposit_address) | **GET** /wallet/deposit_address | Generate currency deposit address
*WalletApi* | [**list_deposits**](docs/WalletApi.md#list_deposits) | **GET** /wallet/deposits | Retrieve deposit records. Time range cannot exceed 30 days
*WalletApi* | [**list_withdrawals**](docs/WalletApi.md#list_withdrawals) | **GET** /wallet/withdrawals | Retrieve withdrawal records. Time range cannot exceed 30 days
*WalletApi* | [**transfer**](docs/WalletApi.md#transfer) | **POST** /wallet/transfers | Transfer between accounts
*WalletApi* | [**transfer_with_sub_account**](docs/WalletApi.md#transfer_with_sub_account) | **POST** /wallet/sub_account_transfers | Transfer between main and sub accounts
*WithdrawalApi* | [**withdraw**](docs/WithdrawalApi.md#withdraw) | **POST** /withdrawals | Withdraw


## Documentation For Models

 - [BatchOrder](docs/BatchOrder.md)
 - [CancelOrder](docs/CancelOrder.md)
 - [CancelOrderResult](docs/CancelOrderResult.md)
 - [Contract](docs/Contract.md)
 - [CurrencyPair](docs/CurrencyPair.md)
 - [DepositAddress](docs/DepositAddress.md)
 - [FundingAccount](docs/FundingAccount.md)
 - [FundingBookItem](docs/FundingBookItem.md)
 - [FundingRateRecord](docs/FundingRateRecord.md)
 - [FuturesAccount](docs/FuturesAccount.md)
 - [FuturesAccountBook](docs/FuturesAccountBook.md)
 - [FuturesCandlestick](docs/FuturesCandlestick.md)
 - [FuturesInitialOrder](docs/FuturesInitialOrder.md)
 - [FuturesLiquidate](docs/FuturesLiquidate.md)
 - [FuturesOrder](docs/FuturesOrder.md)
 - [FuturesOrderBook](docs/FuturesOrderBook.md)
 - [FuturesOrderBookItem](docs/FuturesOrderBookItem.md)
 - [FuturesPriceTrigger](docs/FuturesPriceTrigger.md)
 - [FuturesPriceTriggeredOrder](docs/FuturesPriceTriggeredOrder.md)
 - [FuturesTicker](docs/FuturesTicker.md)
 - [FuturesTrade](docs/FuturesTrade.md)
 - [InsuranceRecord](docs/InsuranceRecord.md)
 - [LedgerRecord](docs/LedgerRecord.md)
 - [Loan](docs/Loan.md)
 - [LoanPatch](docs/LoanPatch.md)
 - [LoanRecord](docs/LoanRecord.md)
 - [MarginAccount](docs/MarginAccount.md)
 - [MarginAccountCurrency](docs/MarginAccountCurrency.md)
 - [MarginCurrencyPair](docs/MarginCurrencyPair.md)
 - [MyFuturesTrade](docs/MyFuturesTrade.md)
 - [Order](docs/Order.md)
 - [OrderBook](docs/OrderBook.md)
 - [Position](docs/Position.md)
 - [PositionClose](docs/PositionClose.md)
 - [PositionCloseOrder](docs/PositionCloseOrder.md)
 - [RepayRequest](docs/RepayRequest.md)
 - [Repayment](docs/Repayment.md)
 - [SpotAccount](docs/SpotAccount.md)
 - [SubAccountTransfer](docs/SubAccountTransfer.md)
 - [Ticker](docs/Ticker.md)
 - [Trade](docs/Trade.md)
 - [Transfer](docs/Transfer.md)
 - [TriggerOrderResponse](docs/TriggerOrderResponse.md)


## Author

support@mail.gate.io


