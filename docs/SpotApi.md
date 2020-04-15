# gate_api.SpotApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_batch_orders**](SpotApi.md#cancel_batch_orders) | **POST** /spot/cancel_batch_orders | Cancel a batch of orders with an ID list
[**cancel_order**](SpotApi.md#cancel_order) | **DELETE** /spot/orders/{order_id} | Cancel a single order
[**cancel_orders**](SpotApi.md#cancel_orders) | **DELETE** /spot/orders | Cancel all &#x60;open&#x60; orders in specified currency pair
[**create_batch_orders**](SpotApi.md#create_batch_orders) | **POST** /spot/batch_orders | Create a batch of orders
[**create_order**](SpotApi.md#create_order) | **POST** /spot/orders | Create an order
[**get_currency_pair**](SpotApi.md#get_currency_pair) | **GET** /spot/currency_pairs/{currency_pair} | Get detail of one single order
[**get_order**](SpotApi.md#get_order) | **GET** /spot/orders/{order_id} | Get a single order
[**list_candlesticks**](SpotApi.md#list_candlesticks) | **GET** /spot/candlesticks | Market candlesticks
[**list_currency_pairs**](SpotApi.md#list_currency_pairs) | **GET** /spot/currency_pairs | List all currency pairs supported
[**list_my_trades**](SpotApi.md#list_my_trades) | **GET** /spot/my_trades | List personal trading history
[**list_order_book**](SpotApi.md#list_order_book) | **GET** /spot/order_book | Retrieve order book
[**list_orders**](SpotApi.md#list_orders) | **GET** /spot/orders | List orders
[**list_spot_accounts**](SpotApi.md#list_spot_accounts) | **GET** /spot/accounts | List spot accounts
[**list_tickers**](SpotApi.md#list_tickers) | **GET** /spot/tickers | Retrieve ticker information
[**list_trades**](SpotApi.md#list_trades) | **GET** /spot/trades | Retrieve market trades


# **cancel_batch_orders**
> list[CancelOrderResult] cancel_batch_orders(cancel_order)

Cancel a batch of orders with an ID list

Multiple currency pairs can be specified, but maximum 20 orders are allowed per request

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.SpotApi(gate_api.ApiClient(configuration))
cancel_order = [gate_api.CancelOrder()] # list[CancelOrder] | 

try:
    # Cancel a batch of orders with an ID list
    api_response = api_instance.cancel_batch_orders(cancel_order)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->cancel_batch_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_order** | [**list[CancelOrder]**](CancelOrder.md)|  | 

### Return type

[**list[CancelOrderResult]**](CancelOrderResult.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order**
> Order cancel_order(order_id, currency_pair)

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
api_instance = gate_api.SpotApi(gate_api.ApiClient(configuration))
order_id = '12345' # str | ID returned on order successfully being created
currency_pair = 'BTC_USDT' # str | Currency pair

try:
    # Cancel a single order
    api_response = api_instance.cancel_order(order_id, currency_pair)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID returned on order successfully being created | 
 **currency_pair** | **str**| Currency pair | 

### Return type

[**Order**](Order.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_orders**
> list[Order] cancel_orders(currency_pair, side=side, account=account)

Cancel all `open` orders in specified currency pair

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.SpotApi(gate_api.ApiClient(configuration))
currency_pair = 'BTC_USDT' # str | Currency pair
side = 'sell' # str | All bids or asks. Both included in not specified (optional)
account = 'spot' # str | Specify account type. Default to all account types being included (optional)

try:
    # Cancel all `open` orders in specified currency pair
    api_response = api_instance.cancel_orders(currency_pair, side=side, account=account)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->cancel_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | 
 **side** | **str**| All bids or asks. Both included in not specified | [optional] 
 **account** | **str**| Specify account type. Default to all account types being included | [optional] 

### Return type

[**list[Order]**](Order.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch_orders**
> list[BatchOrder] create_batch_orders(order)

Create a batch of orders

Batch orders requirements:  1. custom order field `text` is required 2. At most 4 currency pairs, maximum 5 orders each, are allowed in one request 3. No mixture of spot orders and margin orders, i.e. `account` must be identical for all orders 

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.SpotApi(gate_api.ApiClient(configuration))
order = [gate_api.Order()] # list[Order] | 

try:
    # Create a batch of orders
    api_response = api_instance.create_batch_orders(order)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->create_batch_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**list[Order]**](Order.md)|  | 

### Return type

[**list[BatchOrder]**](BatchOrder.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> Order create_order(order)

Create an order

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.SpotApi(gate_api.ApiClient(configuration))
order = gate_api.Order() # Order | 

try:
    # Create an order
    api_response = api_instance.create_order(order)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**Order**](Order.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency_pair**
> CurrencyPair get_currency_pair(currency_pair)

Get detail of one single order

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.SpotApi()
currency_pair = 'ETH_BTC' # str | Currency pair

try:
    # Get detail of one single order
    api_response = api_instance.get_currency_pair(currency_pair)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->get_currency_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | 

### Return type

[**CurrencyPair**](CurrencyPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> Order get_order(order_id, currency_pair)

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
api_instance = gate_api.SpotApi(gate_api.ApiClient(configuration))
order_id = '12345' # str | ID returned on order successfully being created
currency_pair = 'BTC_USDT' # str | Currency pair

try:
    # Get a single order
    api_response = api_instance.get_order(order_id, currency_pair)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| ID returned on order successfully being created | 
 **currency_pair** | **str**| Currency pair | 

### Return type

[**Order**](Order.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_candlesticks**
> list[list[str]] list_candlesticks(currency_pair, limit=limit, _from=_from, to=to, interval=interval)

Market candlesticks

Maximum of 1000 points are returned in one query. Be sure not to exceed the limit when specifying `from`, `to` and `interval`

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.SpotApi()
currency_pair = 'BTC_USDT' # str | Currency pair
limit = 100 # int | Maximum recent data points returned. `limit` is conflicted with `from` and `to`. If either `from` or `to` is specified, request will be rejected. (optional) (default to 100)
_from = 1546905600 # int | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to`to - 100 * interval` if not specified (optional)
to = 1546935600 # int | End time of candlesticks, formatted in Unix timestamp in seconds. Default to current time (optional)
interval = '30m' # str | Interval time between data points (optional) (default to '30m')

try:
    # Market candlesticks
    api_response = api_instance.list_candlesticks(currency_pair, limit=limit, _from=_from, to=to, interval=interval)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->list_candlesticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | 
 **limit** | **int**| Maximum recent data points returned. &#x60;limit&#x60; is conflicted with &#x60;from&#x60; and &#x60;to&#x60;. If either &#x60;from&#x60; or &#x60;to&#x60; is specified, request will be rejected. | [optional] [default to 100]
 **_from** | **int**| Start time of candlesticks, formatted in Unix timestamp in seconds. Default to&#x60;to - 100 * interval&#x60; if not specified | [optional] 
 **to** | **int**| End time of candlesticks, formatted in Unix timestamp in seconds. Default to current time | [optional] 
 **interval** | **str**| Interval time between data points | [optional] [default to &#39;30m&#39;]

### Return type

**list[list[str]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_currency_pairs**
> list[CurrencyPair] list_currency_pairs()

List all currency pairs supported

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.SpotApi()

try:
    # List all currency pairs supported
    api_response = api_instance.list_currency_pairs()
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->list_currency_pairs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CurrencyPair]**](CurrencyPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_my_trades**
> list[Trade] list_my_trades(currency_pair, limit=limit, page=page, order_id=order_id)

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
api_instance = gate_api.SpotApi(gate_api.ApiClient(configuration))
currency_pair = 'BTC_USDT' # str | Currency pair
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
page = 1 # int | Page number (optional) (default to 1)
order_id = '12345' # str | List all trades of specified order (optional)

try:
    # List personal trading history
    api_response = api_instance.list_my_trades(currency_pair, limit=limit, page=page, order_id=order_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->list_my_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | 
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]
 **page** | **int**| Page number | [optional] [default to 1]
 **order_id** | **str**| List all trades of specified order | [optional] 

### Return type

[**list[Trade]**](Trade.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_order_book**
> OrderBook list_order_book(currency_pair, interval=interval, limit=limit)

Retrieve order book

Order book will be sorted by price from high to low on bids; reversed on asks

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.SpotApi()
currency_pair = 'BTC_USDT' # str | Currency pair
interval = '0' # str | Order depth. 0 means no aggregation is applied. default to 0 (optional) (default to '0')
limit = 10 # int | Maximum number of order depth data in asks or bids (optional) (default to 10)

try:
    # Retrieve order book
    api_response = api_instance.list_order_book(currency_pair, interval=interval, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->list_order_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | 
 **interval** | **str**| Order depth. 0 means no aggregation is applied. default to 0 | [optional] [default to &#39;0&#39;]
 **limit** | **int**| Maximum number of order depth data in asks or bids | [optional] [default to 10]

### Return type

[**OrderBook**](OrderBook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> list[Order] list_orders(currency_pair, status, page=page, limit=limit)

List orders

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.SpotApi(gate_api.ApiClient(configuration))
currency_pair = 'BTC_USDT' # str | Currency pair
status = 'open' # str | List orders based on status  `open` - order is waiting to be filled `finished` - order has been filled or cancelled 
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)

try:
    # List orders
    api_response = api_instance.list_orders(currency_pair, status, page=page, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | 
 **status** | **str**| List orders based on status  &#x60;open&#x60; - order is waiting to be filled &#x60;finished&#x60; - order has been filled or cancelled  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]

### Return type

[**list[Order]**](Order.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_spot_accounts**
> list[SpotAccount] list_spot_accounts(currency=currency)

List spot accounts

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.SpotApi(gate_api.ApiClient(configuration))
currency = 'BTC' # str | Retrieved specified currency related data (optional)

try:
    # List spot accounts
    api_response = api_instance.list_spot_accounts(currency=currency)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->list_spot_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieved specified currency related data | [optional] 

### Return type

[**list[SpotAccount]**](SpotAccount.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tickers**
> list[Ticker] list_tickers(currency_pair=currency_pair)

Retrieve ticker information

Return only related data if `currency_pair` is specified; otherwise return all of them

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.SpotApi()
currency_pair = 'BTC_USDT' # str | Currency pair (optional)

try:
    # Retrieve ticker information
    api_response = api_instance.list_tickers(currency_pair=currency_pair)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->list_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | [optional] 

### Return type

[**list[Ticker]**](Ticker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trades**
> list[Trade] list_trades(currency_pair, limit=limit, last_id=last_id)

Retrieve market trades

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.SpotApi()
currency_pair = 'BTC_USDT' # str | Currency pair
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
last_id = '12345' # str | Specify list staring point using the `id` of last record in previous list-query results (optional)

try:
    # Retrieve market trades
    api_response = api_instance.list_trades(currency_pair, limit=limit, last_id=last_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling SpotApi->list_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | 
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]
 **last_id** | **str**| Specify list staring point using the &#x60;id&#x60; of last record in previous list-query results | [optional] 

### Return type

[**list[Trade]**](Trade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

