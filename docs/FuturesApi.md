# gate_api.FuturesApi

All URIs are relative to *https://fx-api.gateio.io/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](FuturesApi.md#cancel_order) | **DELETE** /futures/orders/{order_id} | Cancel a single order
[**cancel_orders**](FuturesApi.md#cancel_orders) | **DELETE** /futures/orders | Cancel all &#x60;open&#x60; orders matched
[**create_order**](FuturesApi.md#create_order) | **POST** /futures/orders | Create a futures order
[**get_futures_contract**](FuturesApi.md#get_futures_contract) | **GET** /futures/contracts/{contract} | Get a single contract
[**get_my_trades**](FuturesApi.md#get_my_trades) | **GET** /futures/my_trades | List personal trading history
[**get_order**](FuturesApi.md#get_order) | **GET** /futures/orders/{order_id} | Get a single order
[**get_position**](FuturesApi.md#get_position) | **GET** /futures/positions/{contract} | Get single position
[**list_futures_account_book**](FuturesApi.md#list_futures_account_book) | **GET** /futures/account_book | Query account book
[**list_futures_accounts**](FuturesApi.md#list_futures_accounts) | **GET** /futures/accounts | Query futures account
[**list_futures_candlesticks**](FuturesApi.md#list_futures_candlesticks) | **GET** /futures/candlesticks | Get futures candlesticks
[**list_futures_contracts**](FuturesApi.md#list_futures_contracts) | **GET** /futures/contracts | List all futures contracts
[**list_futures_funding_rate_history**](FuturesApi.md#list_futures_funding_rate_history) | **GET** /futures/funding_rate | Funding rate history
[**list_futures_insurance_ledger**](FuturesApi.md#list_futures_insurance_ledger) | **GET** /futures/insurance | Futures insurance balance history
[**list_futures_order_book**](FuturesApi.md#list_futures_order_book) | **GET** /futures/order_book | Futures order book
[**list_futures_tickers**](FuturesApi.md#list_futures_tickers) | **GET** /futures/tickers | List futures tickers
[**list_futures_trades**](FuturesApi.md#list_futures_trades) | **GET** /futures/trades | Futures trading history
[**list_orders**](FuturesApi.md#list_orders) | **GET** /futures/orders | List futures orders
[**list_position_close**](FuturesApi.md#list_position_close) | **GET** /futures/position_close | List position close history
[**list_positions**](FuturesApi.md#list_positions) | **GET** /futures/positions | List all positions of a user
[**update_position_leverage**](FuturesApi.md#update_position_leverage) | **POST** /futures/positions/{contract}/leverage | Update position leverage
[**update_position_margin**](FuturesApi.md#update_position_margin) | **POST** /futures/positions/{contract}/margin | Update position margin
[**update_position_risk_limit**](FuturesApi.md#update_position_risk_limit) | **POST** /futures/positions/{contract}/risk_limit | Update position risk limit


# **cancel_order**
> FuturesOrder cancel_order(order_id)

Cancel a single order

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
order_id = '12345' # str | ID returned on order successfully being created

try:
    # Cancel a single order
    api_response = api_instance.cancel_order(order_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID returned on order successfully being created | 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_orders**
> list[FuturesOrder] cancel_orders(contract, side=side)

Cancel all `open` orders matched

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
contract = 'BTC_USD' # str | Futures contract
side = 'ask' # str | All bids or asks. Both included in not specified (optional)

try:
    # Cancel all `open` orders matched
    api_response = api_instance.cancel_orders(contract, side=side)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract | 
 **side** | **str**| All bids or asks. Both included in not specified | [optional] 

### Return type

[**list[FuturesOrder]**](FuturesOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> FuturesOrder create_order(futures_order)

Create a futures order

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
futures_order = gate_api.FuturesOrder() # FuturesOrder | 

try:
    # Create a futures order
    api_response = api_instance.create_order(futures_order)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **futures_order** | [**FuturesOrder**](FuturesOrder.md)|  | 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_futures_contract**
> Contract get_futures_contract(contract)

Get a single contract

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
contract = 'BTC_USD' # str | Futures contract

try:
    # Get a single contract
    api_response = api_instance.get_futures_contract(contract)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_futures_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract | 

### Return type

[**Contract**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_trades**
> list[MyFuturesTrade] get_my_trades(contract=contract, order=order, limit=limit, last_id=last_id)

List personal trading history

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
contract = 'BTC_USD' # str | Futures contract, return related data only if specified (optional)
order = 12345 # int | Futures order ID, return related data only if specified (optional)
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
last_id = '12345' # str | Specify list staring point using the last record of `id` in previous list-query results (optional)

try:
    # List personal trading history
    api_response = api_instance.get_my_trades(contract=contract, order=order, limit=limit, last_id=last_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_my_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract, return related data only if specified | [optional] 
 **order** | **int**| Futures order ID, return related data only if specified | [optional] 
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]
 **last_id** | **str**| Specify list staring point using the last record of &#x60;id&#x60; in previous list-query results | [optional] 

### Return type

[**list[MyFuturesTrade]**](MyFuturesTrade.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> FuturesOrder get_order(order_id)

Get a single order

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
order_id = '12345' # str | ID returned on order successfully being created

try:
    # Get a single order
    api_response = api_instance.get_order(order_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID returned on order successfully being created | 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_position**
> Position get_position(contract)

Get single position

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
contract = 'BTC_USD' # str | Futures contract

try:
    # Get single position
    api_response = api_instance.get_position(contract)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract | 

### Return type

[**Position**](Position.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_account_book**
> list[FuturesAccountBook] list_futures_account_book(limit=limit, _from=_from, to=to, type=type)

Query account book

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)
type = 'dnw' # str | Changing Type  - dnw: Deposit & Withdraw - pnl: Profit & Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding (optional)

try:
    # Query account book
    api_response = api_instance.list_futures_account_book(limit=limit, _from=_from, to=to, type=type)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_account_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 
 **type** | **str**| Changing Type  - dnw: Deposit &amp; Withdraw - pnl: Profit &amp; Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding | [optional] 

### Return type

[**list[FuturesAccountBook]**](FuturesAccountBook.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_accounts**
> FuturesAccount list_futures_accounts()

Query futures account

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))

try:
    # Query futures account
    api_response = api_instance.list_futures_accounts()
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FuturesAccount**](FuturesAccount.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_candlesticks**
> list[FuturesCandlestick] list_futures_candlesticks(contract, _from=_from, to=to, limit=limit, interval=interval)

Get futures candlesticks

Return specified contract candlesticks. If prefix `contract` with `mark_`, the contract's mark price candlesticks are returned; if prefix with `index_`, index price candlesticks will be returned.  Maximum of 2000 points are returned in one query. Be sure not to exceed the limit when specifying `from`, `to` and `interval`

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
contract = 'BTC_USD' # str | Futures contract
_from = 1546905600 # float | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to`to - 100 * interval` if not specified (optional)
to = 1546935600 # float | End time of candlesticks, formatted in Unix timestamp in seconds. Default to current time (optional)
limit = 100 # int | Maximum recent data points returned. `limit` is conflicted with `from` and `to`. If either `from` or `to` is specified, request will be rejected. (optional) (default to 100)
interval = '5m' # str | Interval time between data points (optional) (default to '5m')

try:
    # Get futures candlesticks
    api_response = api_instance.list_futures_candlesticks(contract, _from=_from, to=to, limit=limit, interval=interval)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_candlesticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract | 
 **_from** | **float**| Start time of candlesticks, formatted in Unix timestamp in seconds. Default to&#x60;to - 100 * interval&#x60; if not specified | [optional] 
 **to** | **float**| End time of candlesticks, formatted in Unix timestamp in seconds. Default to current time | [optional] 
 **limit** | **int**| Maximum recent data points returned. &#x60;limit&#x60; is conflicted with &#x60;from&#x60; and &#x60;to&#x60;. If either &#x60;from&#x60; or &#x60;to&#x60; is specified, request will be rejected. | [optional] [default to 100]
 **interval** | **str**| Interval time between data points | [optional] [default to &#39;5m&#39;]

### Return type

[**list[FuturesCandlestick]**](FuturesCandlestick.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_contracts**
> list[Contract] list_futures_contracts()

List all futures contracts

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()

try:
    # List all futures contracts
    api_response = api_instance.list_futures_contracts()
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_contracts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Contract]**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_funding_rate_history**
> list[FundingRateRecord] list_futures_funding_rate_history(contract, limit=limit)

Funding rate history

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
contract = 'BTC_USD' # str | Futures contract
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)

try:
    # Funding rate history
    api_response = api_instance.list_futures_funding_rate_history(contract, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_funding_rate_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract | 
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]

### Return type

[**list[FundingRateRecord]**](FundingRateRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_insurance_ledger**
> list[InsuranceRecord] list_futures_insurance_ledger(limit=limit)

Futures insurance balance history

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)

try:
    # Futures insurance balance history
    api_response = api_instance.list_futures_insurance_ledger(limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_insurance_ledger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]

### Return type

[**list[InsuranceRecord]**](InsuranceRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_order_book**
> FuturesOrderBook list_futures_order_book(contract, interval=interval, limit=limit)

Futures order book

Bids will be sorted by price from high to low, while asks sorted reversely

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
contract = 'BTC_USD' # str | Futures contract
interval = '0' # str | Order depth. 0 means no aggregation is applied. default to 0 (optional) (default to '0')
limit = 10 # int | Maximum number of order depth data in asks or bids (optional) (default to 10)

try:
    # Futures order book
    api_response = api_instance.list_futures_order_book(contract, interval=interval, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_order_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract | 
 **interval** | **str**| Order depth. 0 means no aggregation is applied. default to 0 | [optional] [default to &#39;0&#39;]
 **limit** | **int**| Maximum number of order depth data in asks or bids | [optional] [default to 10]

### Return type

[**FuturesOrderBook**](FuturesOrderBook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_tickers**
> list[FuturesTicker] list_futures_tickers(contract=contract)

List futures tickers

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
contract = 'BTC_USD' # str | Futures contract, return related data only if specified (optional)

try:
    # List futures tickers
    api_response = api_instance.list_futures_tickers(contract=contract)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract, return related data only if specified | [optional] 

### Return type

[**list[FuturesTicker]**](FuturesTicker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_trades**
> list[FuturesTrade] list_futures_trades(contract, limit=limit, last_id=last_id)

Futures trading history

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
contract = 'BTC_USD' # str | Futures contract
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
last_id = '12345' # str | Specify list staring point using the last record of `id` in previous list-query results (optional)

try:
    # Futures trading history
    api_response = api_instance.list_futures_trades(contract, limit=limit, last_id=last_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract | 
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]
 **last_id** | **str**| Specify list staring point using the last record of &#x60;id&#x60; in previous list-query results | [optional] 

### Return type

[**list[FuturesTrade]**](FuturesTrade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> list[FuturesOrder] list_orders(contract, status, limit=limit, last_id=last_id)

List futures orders

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
contract = 'BTC_USD' # str | Futures contract
status = 'open' # str | List orders based on status
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
last_id = '12345' # str | Specify list staring point using the last record of `id` in previous list-query results (optional)

try:
    # List futures orders
    api_response = api_instance.list_orders(contract, status, limit=limit, last_id=last_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract | 
 **status** | **str**| List orders based on status | 
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]
 **last_id** | **str**| Specify list staring point using the last record of &#x60;id&#x60; in previous list-query results | [optional] 

### Return type

[**list[FuturesOrder]**](FuturesOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_position_close**
> list[PositionClose] list_position_close(contract=contract, limit=limit)

List position close history

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
contract = 'BTC_USD' # str | Futures contract, return related data only if specified (optional)
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)

try:
    # List position close history
    api_response = api_instance.list_position_close(contract=contract, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_position_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract, return related data only if specified | [optional] 
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]

### Return type

[**list[PositionClose]**](PositionClose.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_positions**
> list[Position] list_positions()

List all positions of a user

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))

try:
    # List all positions of a user
    api_response = api_instance.list_positions()
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_positions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Position]**](Position.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_leverage**
> Position update_position_leverage(contract, leverage)

Update position leverage

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
contract = 'BTC_USD' # str | Futures contract
leverage = '10' # str | New position leverage

try:
    # Update position leverage
    api_response = api_instance.update_position_leverage(contract, leverage)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_leverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract | 
 **leverage** | **str**| New position leverage | 

### Return type

[**Position**](Position.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_margin**
> Position update_position_margin(contract, change)

Update position margin

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
contract = 'BTC_USD' # str | Futures contract
change = '0.01' # str | Margin change. Use positive number to increase margin, negative number otherwise.

try:
    # Update position margin
    api_response = api_instance.update_position_margin(contract, change)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_margin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract | 
 **change** | **str**| Margin change. Use positive number to increase margin, negative number otherwise. | 

### Return type

[**Position**](Position.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_risk_limit**
> Position update_position_risk_limit(contract, risk_limit)

Update position risk limit

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.FuturesApi(gate_api.ApiClient(configuration))
contract = 'BTC_USD' # str | Futures contract
risk_limit = '10' # str | New position risk limit

try:
    # Update position risk limit
    api_response = api_instance.update_position_risk_limit(contract, risk_limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_risk_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Futures contract | 
 **risk_limit** | **str**| New position risk limit | 

### Return type

[**Position**](Position.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

