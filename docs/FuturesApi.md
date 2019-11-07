# gate_api.FuturesApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_futures_order**](FuturesApi.md#cancel_futures_order) | **DELETE** /futures/{settle}/orders/{order_id} | Cancel a single order
[**cancel_futures_orders**](FuturesApi.md#cancel_futures_orders) | **DELETE** /futures/{settle}/orders | Cancel all &#x60;open&#x60; orders matched
[**cancel_price_triggered_order**](FuturesApi.md#cancel_price_triggered_order) | **DELETE** /futures/{settle}/price_orders/{order_id} | Cancel a single order
[**cancel_price_triggered_order_list**](FuturesApi.md#cancel_price_triggered_order_list) | **DELETE** /futures/{settle}/price_orders | Cancel all open orders
[**create_futures_order**](FuturesApi.md#create_futures_order) | **POST** /futures/{settle}/orders | Create a futures order
[**create_price_triggered_order**](FuturesApi.md#create_price_triggered_order) | **POST** /futures/{settle}/price_orders | Create a price-triggered order
[**get_futures_contract**](FuturesApi.md#get_futures_contract) | **GET** /futures/{settle}/contracts/{contract} | Get a single contract
[**get_futures_order**](FuturesApi.md#get_futures_order) | **GET** /futures/{settle}/orders/{order_id} | Get a single order
[**get_my_trades**](FuturesApi.md#get_my_trades) | **GET** /futures/{settle}/my_trades | List personal trading history
[**get_position**](FuturesApi.md#get_position) | **GET** /futures/{settle}/positions/{contract} | Get single position
[**get_price_triggered_order**](FuturesApi.md#get_price_triggered_order) | **GET** /futures/{settle}/price_orders/{order_id} | Get a single order
[**list_futures_account_book**](FuturesApi.md#list_futures_account_book) | **GET** /futures/{settle}/account_book | Query account book
[**list_futures_accounts**](FuturesApi.md#list_futures_accounts) | **GET** /futures/{settle}/accounts | Query futures account
[**list_futures_candlesticks**](FuturesApi.md#list_futures_candlesticks) | **GET** /futures/{settle}/candlesticks | Get futures candlesticks
[**list_futures_contracts**](FuturesApi.md#list_futures_contracts) | **GET** /futures/{settle}/contracts | List all futures contracts
[**list_futures_funding_rate_history**](FuturesApi.md#list_futures_funding_rate_history) | **GET** /futures/{settle}/funding_rate | Funding rate history
[**list_futures_insurance_ledger**](FuturesApi.md#list_futures_insurance_ledger) | **GET** /futures/{settle}/insurance | Futures insurance balance history
[**list_futures_order_book**](FuturesApi.md#list_futures_order_book) | **GET** /futures/{settle}/order_book | Futures order book
[**list_futures_orders**](FuturesApi.md#list_futures_orders) | **GET** /futures/{settle}/orders | List futures orders
[**list_futures_tickers**](FuturesApi.md#list_futures_tickers) | **GET** /futures/{settle}/tickers | List futures tickers
[**list_futures_trades**](FuturesApi.md#list_futures_trades) | **GET** /futures/{settle}/trades | Futures trading history
[**list_liquidates**](FuturesApi.md#list_liquidates) | **GET** /futures/{settle}/liquidates | List liquidation history
[**list_position_close**](FuturesApi.md#list_position_close) | **GET** /futures/{settle}/position_close | List position close history
[**list_positions**](FuturesApi.md#list_positions) | **GET** /futures/{settle}/positions | List all positions of a user
[**list_price_triggered_orders**](FuturesApi.md#list_price_triggered_orders) | **GET** /futures/{settle}/price_orders | List all auto orders
[**update_position_leverage**](FuturesApi.md#update_position_leverage) | **POST** /futures/{settle}/positions/{contract}/leverage | Update position leverage
[**update_position_margin**](FuturesApi.md#update_position_margin) | **POST** /futures/{settle}/positions/{contract}/margin | Update position margin
[**update_position_risk_limit**](FuturesApi.md#update_position_risk_limit) | **POST** /futures/{settle}/positions/{contract}/risk_limit | Update position risk limit


# **cancel_futures_order**
> FuturesOrder cancel_futures_order(settle, order_id)

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
settle = 'btc' # str | Settle currency (default to 'btc')
order_id = '12345' # str | ID returned on order successfully being created

try:
    # Cancel a single order
    api_response = api_instance.cancel_futures_order(settle, order_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_futures_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
 **order_id** | **str**| ID returned on order successfully being created | 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_futures_orders**
> list[FuturesOrder] cancel_futures_orders(settle, contract, side=side)

Cancel all `open` orders matched

Zero-fill order cannot be retrieved 60 seconds after cancellation

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
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract
side = 'ask' # str | All bids or asks. Both included in not specified (optional)

try:
    # Cancel all `open` orders matched
    api_response = api_instance.cancel_futures_orders(settle, contract, side=side)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_futures_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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

# **cancel_price_triggered_order**
> FuturesPriceTriggeredOrder cancel_price_triggered_order(settle, order_id)

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
settle = 'btc' # str | Settle currency (default to 'btc')
order_id = 'order_id_example' # str | ID returned on order successfully being created

try:
    # Cancel a single order
    api_response = api_instance.cancel_price_triggered_order(settle, order_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_price_triggered_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
 **order_id** | **str**| ID returned on order successfully being created | 

### Return type

[**FuturesPriceTriggeredOrder**](FuturesPriceTriggeredOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_price_triggered_order_list**
> list[FuturesPriceTriggeredOrder] cancel_price_triggered_order_list(settle, contract)

Cancel all open orders

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
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract

try:
    # Cancel all open orders
    api_response = api_instance.cancel_price_triggered_order_list(settle, contract)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_price_triggered_order_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
 **contract** | **str**| Futures contract | 

### Return type

[**list[FuturesPriceTriggeredOrder]**](FuturesPriceTriggeredOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_futures_order**
> FuturesOrder create_futures_order(settle, futures_order)

Create a futures order

Zero-fill order cannot be retrieved 60 seconds after cancellation

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
settle = 'btc' # str | Settle currency (default to 'btc')
futures_order = gate_api.FuturesOrder() # FuturesOrder | 

try:
    # Create a futures order
    api_response = api_instance.create_futures_order(settle, futures_order)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->create_futures_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
 **futures_order** | [**FuturesOrder**](FuturesOrder.md)|  | 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_price_triggered_order**
> TriggerOrderResponse create_price_triggered_order(settle, futures_price_triggered_order)

Create a price-triggered order

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
settle = 'btc' # str | Settle currency (default to 'btc')
futures_price_triggered_order = gate_api.FuturesPriceTriggeredOrder() # FuturesPriceTriggeredOrder | 

try:
    # Create a price-triggered order
    api_response = api_instance.create_price_triggered_order(settle, futures_price_triggered_order)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->create_price_triggered_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
 **futures_price_triggered_order** | [**FuturesPriceTriggeredOrder**](FuturesPriceTriggeredOrder.md)|  | 

### Return type

[**TriggerOrderResponse**](TriggerOrderResponse.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_futures_contract**
> Contract get_futures_contract(settle, contract)

Get a single contract

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract

try:
    # Get a single contract
    api_response = api_instance.get_futures_contract(settle, contract)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_futures_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
 **contract** | **str**| Futures contract | 

### Return type

[**Contract**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_futures_order**
> FuturesOrder get_futures_order(settle, order_id)

Get a single order

Zero-fill order cannot be retrieved 60 seconds after cancellation

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
settle = 'btc' # str | Settle currency (default to 'btc')
order_id = '12345' # str | ID returned on order successfully being created

try:
    # Get a single order
    api_response = api_instance.get_futures_order(settle, order_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_futures_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
 **order_id** | **str**| ID returned on order successfully being created | 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_trades**
> list[MyFuturesTrade] get_my_trades(settle, contract=contract, order=order, limit=limit, last_id=last_id)

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
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract, return related data only if specified (optional)
order = 12345 # int | Futures order ID, return related data only if specified (optional)
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
last_id = '12345' # str | Specify list staring point using the last record of `id` in previous list-query results (optional)

try:
    # List personal trading history
    api_response = api_instance.get_my_trades(settle, contract=contract, order=order, limit=limit, last_id=last_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_my_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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

# **get_position**
> Position get_position(settle, contract)

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
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract

try:
    # Get single position
    api_response = api_instance.get_position(settle, contract)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
 **contract** | **str**| Futures contract | 

### Return type

[**Position**](Position.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_triggered_order**
> FuturesPriceTriggeredOrder get_price_triggered_order(settle, order_id)

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
settle = 'btc' # str | Settle currency (default to 'btc')
order_id = 'order_id_example' # str | ID returned on order successfully being created

try:
    # Get a single order
    api_response = api_instance.get_price_triggered_order(settle, order_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_price_triggered_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
 **order_id** | **str**| ID returned on order successfully being created | 

### Return type

[**FuturesPriceTriggeredOrder**](FuturesPriceTriggeredOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_account_book**
> list[FuturesAccountBook] list_futures_account_book(settle, limit=limit, _from=_from, to=to, type=type)

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
settle = 'btc' # str | Settle currency (default to 'btc')
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)
type = 'dnw' # str | Changing Type: - dnw: Deposit & Withdraw - pnl: Profit & Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding - point_dnw: POINT Deposit & Withdraw - point_fee: POINT Trading fee - point_refr: POINT Referrer rebate (optional)

try:
    # Query account book
    api_response = api_instance.list_futures_account_book(settle, limit=limit, _from=_from, to=to, type=type)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_account_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 
 **type** | **str**| Changing Type: - dnw: Deposit &amp; Withdraw - pnl: Profit &amp; Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding - point_dnw: POINT Deposit &amp; Withdraw - point_fee: POINT Trading fee - point_refr: POINT Referrer rebate | [optional] 

### Return type

[**list[FuturesAccountBook]**](FuturesAccountBook.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_accounts**
> FuturesAccount list_futures_accounts(settle)

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
settle = 'btc' # str | Settle currency (default to 'btc')

try:
    # Query futures account
    api_response = api_instance.list_futures_accounts(settle)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]

### Return type

[**FuturesAccount**](FuturesAccount.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_candlesticks**
> list[FuturesCandlestick] list_futures_candlesticks(settle, contract, _from=_from, to=to, limit=limit, interval=interval)

Get futures candlesticks

Return specified contract candlesticks. If prefix `contract` with `mark_`, the contract's mark price candlesticks are returned; if prefix with `index_`, index price candlesticks will be returned.  Maximum of 2000 points are returned in one query. Be sure not to exceed the limit when specifying `from`, `to` and `interval`

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract
_from = 1546905600 # float | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to`to - 100 * interval` if not specified (optional)
to = 1546935600 # float | End time of candlesticks, formatted in Unix timestamp in seconds. Default to current time (optional)
limit = 100 # int | Maximum recent data points returned. `limit` is conflicted with `from` and `to`. If either `from` or `to` is specified, request will be rejected. (optional) (default to 100)
interval = '5m' # str | Interval time between data points (optional) (default to '5m')

try:
    # Get futures candlesticks
    api_response = api_instance.list_futures_candlesticks(settle, contract, _from=_from, to=to, limit=limit, interval=interval)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_candlesticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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
> list[Contract] list_futures_contracts(settle)

List all futures contracts

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
settle = 'btc' # str | Settle currency (default to 'btc')

try:
    # List all futures contracts
    api_response = api_instance.list_futures_contracts(settle)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]

### Return type

[**list[Contract]**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_funding_rate_history**
> list[FundingRateRecord] list_futures_funding_rate_history(settle, contract, limit=limit)

Funding rate history

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)

try:
    # Funding rate history
    api_response = api_instance.list_futures_funding_rate_history(settle, contract, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_funding_rate_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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
> list[InsuranceRecord] list_futures_insurance_ledger(settle, limit=limit)

Futures insurance balance history

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
settle = 'btc' # str | Settle currency (default to 'btc')
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)

try:
    # Futures insurance balance history
    api_response = api_instance.list_futures_insurance_ledger(settle, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_insurance_ledger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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
> FuturesOrderBook list_futures_order_book(settle, contract, interval=interval, limit=limit)

Futures order book

Bids will be sorted by price from high to low, while asks sorted reversely

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract
interval = '0' # str | Order depth. 0 means no aggregation is applied. default to 0 (optional) (default to '0')
limit = 10 # int | Maximum number of order depth data in asks or bids (optional) (default to 10)

try:
    # Futures order book
    api_response = api_instance.list_futures_order_book(settle, contract, interval=interval, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_order_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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

# **list_futures_orders**
> list[FuturesOrder] list_futures_orders(settle, contract, status, limit=limit, last_id=last_id)

List futures orders

Zero-fill order cannot be retrieved 60 seconds after cancellation

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
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract
status = 'open' # str | List orders based on status
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
last_id = '12345' # str | Specify list staring point using the last record of `id` in previous list-query results (optional)

try:
    # List futures orders
    api_response = api_instance.list_futures_orders(settle, contract, status, limit=limit, last_id=last_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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

# **list_futures_tickers**
> list[FuturesTicker] list_futures_tickers(settle, contract=contract)

List futures tickers

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract, return related data only if specified (optional)

try:
    # List futures tickers
    api_response = api_instance.list_futures_tickers(settle, contract=contract)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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
> list[FuturesTrade] list_futures_trades(settle, contract, limit=limit, last_id=last_id)

Futures trading history

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.FuturesApi()
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
last_id = '12345' # str | Specify list staring point using the last record of `id` in previous list-query results (optional)

try:
    # Futures trading history
    api_response = api_instance.list_futures_trades(settle, contract, limit=limit, last_id=last_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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

# **list_liquidates**
> list[FuturesLiquidate] list_liquidates(settle, contract=contract, limit=limit, at=at)

List liquidation history

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
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract, return related data only if specified (optional)
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
at = 0 # int | Specify a liquidation timestamp (optional) (default to 0)

try:
    # List liquidation history
    api_response = api_instance.list_liquidates(settle, contract=contract, limit=limit, at=at)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_liquidates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
 **contract** | **str**| Futures contract, return related data only if specified | [optional] 
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]
 **at** | **int**| Specify a liquidation timestamp | [optional] [default to 0]

### Return type

[**list[FuturesLiquidate]**](FuturesLiquidate.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_position_close**
> list[PositionClose] list_position_close(settle, contract=contract, limit=limit)

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
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract, return related data only if specified (optional)
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)

try:
    # List position close history
    api_response = api_instance.list_position_close(settle, contract=contract, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_position_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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

# **list_price_triggered_orders**
> list[FuturesPriceTriggeredOrder] list_price_triggered_orders(settle, status, contract=contract, limit=limit, offset=offset)

List all auto orders

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
settle = 'btc' # str | Settle currency (default to 'btc')
status = 'status_example' # str | List orders based on status
contract = 'BTC_USD' # str | Futures contract, return related data only if specified (optional)
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # List all auto orders
    api_response = api_instance.list_price_triggered_orders(settle, status, contract=contract, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_price_triggered_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
 **status** | **str**| List orders based on status | 
 **contract** | **str**| Futures contract, return related data only if specified | [optional] 
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

### Return type

[**list[FuturesPriceTriggeredOrder]**](FuturesPriceTriggeredOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_leverage**
> Position update_position_leverage(settle, contract, leverage)

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
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract
leverage = '10' # str | New position leverage

try:
    # Update position leverage
    api_response = api_instance.update_position_leverage(settle, contract, leverage)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_leverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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
> Position update_position_margin(settle, contract, change)

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
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract
change = '0.01' # str | Margin change. Use positive number to increase margin, negative number otherwise.

try:
    # Update position margin
    api_response = api_instance.update_position_margin(settle, contract, change)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_margin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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
> Position update_position_risk_limit(settle, contract, risk_limit)

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
settle = 'btc' # str | Settle currency (default to 'btc')
contract = 'BTC_USD' # str | Futures contract
risk_limit = '10' # str | New position risk limit

try:
    # Update position risk limit
    api_response = api_instance.update_position_risk_limit(settle, contract, risk_limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_risk_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | [default to &#39;btc&#39;]
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

