# gate_api.SpotApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_currencies**](SpotApi.md#list_currencies) | **GET** /spot/currencies | List all currencies&#39; details
[**get_currency**](SpotApi.md#get_currency) | **GET** /spot/currencies/{currency} | Get details of a specific currency
[**list_currency_pairs**](SpotApi.md#list_currency_pairs) | **GET** /spot/currency_pairs | List all currency pairs supported
[**get_currency_pair**](SpotApi.md#get_currency_pair) | **GET** /spot/currency_pairs/{currency_pair} | Get details of a specifc currency pair
[**list_tickers**](SpotApi.md#list_tickers) | **GET** /spot/tickers | Retrieve ticker information
[**list_order_book**](SpotApi.md#list_order_book) | **GET** /spot/order_book | Retrieve order book
[**list_trades**](SpotApi.md#list_trades) | **GET** /spot/trades | Retrieve market trades
[**list_candlesticks**](SpotApi.md#list_candlesticks) | **GET** /spot/candlesticks | Market candlesticks
[**get_fee**](SpotApi.md#get_fee) | **GET** /spot/fee | Query user trading fee rates
[**get_batch_spot_fee**](SpotApi.md#get_batch_spot_fee) | **GET** /spot/batch_fee | Query a batch of user trading fee rates
[**list_spot_accounts**](SpotApi.md#list_spot_accounts) | **GET** /spot/accounts | List spot accounts
[**create_batch_orders**](SpotApi.md#create_batch_orders) | **POST** /spot/batch_orders | Create a batch of orders
[**list_all_open_orders**](SpotApi.md#list_all_open_orders) | **GET** /spot/open_orders | List all open orders
[**create_cross_liquidate_order**](SpotApi.md#create_cross_liquidate_order) | **POST** /spot/cross_liquidate_orders | close position when cross-currency is disabled
[**list_orders**](SpotApi.md#list_orders) | **GET** /spot/orders | List orders
[**create_order**](SpotApi.md#create_order) | **POST** /spot/orders | Create an order
[**cancel_orders**](SpotApi.md#cancel_orders) | **DELETE** /spot/orders | Cancel all &#x60;open&#x60; orders in specified currency pair
[**cancel_batch_orders**](SpotApi.md#cancel_batch_orders) | **POST** /spot/cancel_batch_orders | Cancel a batch of orders with an ID list
[**get_order**](SpotApi.md#get_order) | **GET** /spot/orders/{order_id} | Get a single order
[**cancel_order**](SpotApi.md#cancel_order) | **DELETE** /spot/orders/{order_id} | Cancel a single order
[**amend_order**](SpotApi.md#amend_order) | **PATCH** /spot/orders/{order_id} | Amend an order
[**list_my_trades**](SpotApi.md#list_my_trades) | **GET** /spot/my_trades | List personal trading history
[**get_system_time**](SpotApi.md#get_system_time) | **GET** /spot/time | Get server current time
[**countdown_cancel_all_spot**](SpotApi.md#countdown_cancel_all_spot) | **POST** /spot/countdown_cancel_all | Countdown cancel orders
[**list_spot_price_triggered_orders**](SpotApi.md#list_spot_price_triggered_orders) | **GET** /spot/price_orders | Retrieve running auto order list
[**create_spot_price_triggered_order**](SpotApi.md#create_spot_price_triggered_order) | **POST** /spot/price_orders | Create a price-triggered order
[**cancel_spot_price_triggered_order_list**](SpotApi.md#cancel_spot_price_triggered_order_list) | **DELETE** /spot/price_orders | Cancel all open orders
[**get_spot_price_triggered_order**](SpotApi.md#get_spot_price_triggered_order) | **GET** /spot/price_orders/{order_id} | Get a price-triggered order
[**cancel_spot_price_triggered_order**](SpotApi.md#cancel_spot_price_triggered_order) | **DELETE** /spot/price_orders/{order_id} | cancel a price-triggered order


# **list_currencies**
> list[Currency] list_currencies()

List all currencies' details

Currency has two forms:  1. Only currency name, e.g., BTC, USDT 2. `<currency>_<chain>`, e.g., `HT_ETH`  The latter one occurs when one currency has multiple chains. Currency detail contains a `chain` field whatever the form is. To retrieve all chains of one currency, you can use use all the details which has the name of the currency or name starting with `<currency>_`.

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)

try:
    # List all currencies' details
    api_response = api_instance.list_currencies()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->list_currencies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Currency]**](Currency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency**
> Currency get_currency(currency)

Get details of a specific currency

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
currency = 'GT' # str | Currency name

try:
    # Get details of a specific currency
    api_response = api_instance.get_currency(currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->get_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency name | 

### Return type

[**Currency**](Currency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_currency_pairs**
> list[CurrencyPair] list_currency_pairs()

List all currency pairs supported

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)

try:
    # List all currency pairs supported
    api_response = api_instance.list_currency_pairs()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All currency pairs retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency_pair**
> CurrencyPair get_currency_pair(currency_pair)

Get details of a specifc currency pair

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
currency_pair = 'ETH_BTC' # str | Currency pair

try:
    # Get details of a specifc currency pair
    api_response = api_instance.get_currency_pair(currency_pair)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tickers**
> list[Ticker] list_tickers(currency_pair=currency_pair, timezone=timezone)

Retrieve ticker information

Return only related data if `currency_pair` is specified; otherwise return all of them

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
currency_pair = 'BTC_USDT' # str | Currency pair (optional)
timezone = 'utc0' # str | Timezone (optional)

try:
    # Retrieve ticker information
    api_response = api_instance.list_tickers(currency_pair=currency_pair, timezone=timezone)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->list_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | [optional] 
 **timezone** | **str**| Timezone | [optional] 

### Return type

[**list[Ticker]**](Ticker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_order_book**
> OrderBook list_order_book(currency_pair, interval=interval, limit=limit, with_id=with_id)

Retrieve order book

Order book will be sorted by price from high to low on bids; low to high on asks

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
currency_pair = 'BTC_USDT' # str | Currency pair
interval = '0' # str | Order depth. 0 means no aggregation is applied. default to 0 (optional) (default to '0')
limit = 10 # int | Maximum number of order depth data in asks or bids (optional) (default to 10)
with_id = False # bool | Return order book ID (optional) (default to False)

try:
    # Retrieve order book
    api_response = api_instance.list_order_book(currency_pair, interval=interval, limit=limit, with_id=with_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->list_order_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | 
 **interval** | **str**| Order depth. 0 means no aggregation is applied. default to 0 | [optional] [default to &#39;0&#39;]
 **limit** | **int**| Maximum number of order depth data in asks or bids | [optional] [default to 10]
 **with_id** | **bool**| Return order book ID | [optional] [default to False]

### Return type

[**OrderBook**](OrderBook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trades**
> list[Trade] list_trades(currency_pair, limit=limit, last_id=last_id, reverse=reverse, _from=_from, to=to, page=page)

Retrieve market trades

You can use `from` and `to` to query by time range, or use `last_id` by scrolling page. The default behavior is by time range.  Scrolling query using `last_id` is not recommended any more. If `last_id` is specified, time range query parameters will be ignored.

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
currency_pair = 'BTC_USDT' # str | Currency pair
limit = 100 # int | Maximum number of records to be returned in a single list.  Default: 100, Minimum: 1, Maximum: 1000 (optional) (default to 100)
last_id = '12345' # str | Specify list staring point using the `id` of last record in previous list-query results (optional)
reverse = False # bool | Whether the id of records to be retrieved should be less than the last_id specified. Default to false.  When `last_id` is specified. Set `reverse` to `true` to trace back trading history; `false` to retrieve latest tradings.  No effect if `last_id` is not specified. (optional) (default to False)
_from = 1627706330 # int | Start timestamp of the query (optional)
to = 1635329650 # int | Time range ending, default to current time (optional)
page = 1 # int | Page number (optional) (default to 1)

try:
    # Retrieve market trades
    api_response = api_instance.list_trades(currency_pair, limit=limit, last_id=last_id, reverse=reverse, _from=_from, to=to, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->list_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | 
 **limit** | **int**| Maximum number of records to be returned in a single list.  Default: 100, Minimum: 1, Maximum: 1000 | [optional] [default to 100]
 **last_id** | **str**| Specify list staring point using the &#x60;id&#x60; of last record in previous list-query results | [optional] 
 **reverse** | **bool**| Whether the id of records to be retrieved should be less than the last_id specified. Default to false.  When &#x60;last_id&#x60; is specified. Set &#x60;reverse&#x60; to &#x60;true&#x60; to trace back trading history; &#x60;false&#x60; to retrieve latest tradings.  No effect if &#x60;last_id&#x60; is not specified. | [optional] [default to False]
 **_from** | **int**| Start timestamp of the query | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[Trade]**](Trade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_candlesticks**
> list[list[str]] list_candlesticks(currency_pair, limit=limit, _from=_from, to=to, interval=interval)

Market candlesticks

Maximum of 1000 points can be returned in a query. Be sure not to exceed the limit when specifying from, to and interval

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
currency_pair = 'BTC_USDT' # str | Currency pair
limit = 100 # int | Maximum recent data points to return. `limit` is conflicted with `from` and `to`. If either `from` or `to` is specified, request will be rejected. (optional) (default to 100)
_from = 1546905600 # int | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to`to - 100 * interval` if not specified (optional)
to = 1546935600 # int | End time of candlesticks, formatted in Unix timestamp in seconds. Default to current time (optional)
interval = '30m' # str | Interval time between data points. Note that `30d` means 1 natual month, not 30 days (optional) (default to '30m')

try:
    # Market candlesticks
    api_response = api_instance.list_candlesticks(currency_pair, limit=limit, _from=_from, to=to, interval=interval)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->list_candlesticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | 
 **limit** | **int**| Maximum recent data points to return. &#x60;limit&#x60; is conflicted with &#x60;from&#x60; and &#x60;to&#x60;. If either &#x60;from&#x60; or &#x60;to&#x60; is specified, request will be rejected. | [optional] [default to 100]
 **_from** | **int**| Start time of candlesticks, formatted in Unix timestamp in seconds. Default to&#x60;to - 100 * interval&#x60; if not specified | [optional] 
 **to** | **int**| End time of candlesticks, formatted in Unix timestamp in seconds. Default to current time | [optional] 
 **interval** | **str**| Interval time between data points. Note that &#x60;30d&#x60; means 1 natual month, not 30 days | [optional] [default to &#39;30m&#39;]

### Return type

**list[list[str]]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee**
> TradeFee get_fee(currency_pair=currency_pair)

Query user trading fee rates

This API is deprecated in favour of new fee retrieving API `/wallet/fee`.

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
currency_pair = 'BTC_USDT' # str | Specify a currency pair to retrieve precise fee rate  This field is optional. In most cases, the fee rate is identical among all currency pairs (optional)

try:
    # Query user trading fee rates
    api_response = api_instance.get_fee(currency_pair=currency_pair)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->get_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Specify a currency pair to retrieve precise fee rate  This field is optional. In most cases, the fee rate is identical among all currency pairs | [optional] 

### Return type

[**TradeFee**](TradeFee.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_spot_fee**
> dict(str, SpotFee) get_batch_spot_fee(currency_pairs)

Query a batch of user trading fee rates

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
currency_pairs = 'BTC_USDT,ETH_USDT' # str | A request can only query up to 50 currency pairs

try:
    # Query a batch of user trading fee rates
    api_response = api_instance.get_batch_spot_fee(currency_pairs)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->get_batch_spot_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pairs** | **str**| A request can only query up to 50 currency pairs | 

### Return type

[**dict(str, SpotFee)**](SpotFee.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_spot_accounts**
> list[SpotAccount] list_spot_accounts(currency=currency)

List spot accounts

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
currency = 'BTC' # str | Retrieve data of the specified currency (optional)

try:
    # List spot accounts
    api_response = api_instance.list_spot_accounts(currency=currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->list_spot_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | [optional] 

### Return type

[**list[SpotAccount]**](SpotAccount.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch_orders**
> list[BatchOrder] create_batch_orders(order)

Create a batch of orders

Batch orders requirements:  1. custom order field `text` is required 2. At most 4 currency pairs, maximum 10 orders each, are allowed in one request 3. No mixture of spot orders and margin orders, i.e. `account` must be identical for all orders 

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
order = [gate_api.Order()] # list[Order] | 

try:
    # Create a batch of orders
    api_response = api_instance.create_batch_orders(order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
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

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request is completed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_open_orders**
> list[OpenOrders] list_all_open_orders(page=page, limit=limit, account=account)

List all open orders

List open orders in all currency pairs.  Note that pagination parameters affect record number in each currency pair's open order list. No pagination is applied to the number of currency pairs returned. All currency pairs with open orders will be returned.  Spot and margin orders are returned by default. To list cross margin orders, `account` must be set to `cross_margin`

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records returned in one page in each currency pair (optional) (default to 100)
account = 'cross_margin' # str | Specify operation account. Default to spot and margin account if not specified. Set to `cross_margin` to operate against margin account.  Portfolio margin account must set to `cross_margin` only (optional)

try:
    # List all open orders
    api_response = api_instance.list_all_open_orders(page=page, limit=limit, account=account)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->list_all_open_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records returned in one page in each currency pair | [optional] [default to 100]
 **account** | **str**| Specify operation account. Default to spot and margin account if not specified. Set to &#x60;cross_margin&#x60; to operate against margin account.  Portfolio margin account must set to &#x60;cross_margin&#x60; only | [optional] 

### Return type

[**list[OpenOrders]**](OpenOrders.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cross_liquidate_order**
> Order create_cross_liquidate_order(liquidate_order)

close position when cross-currency is disabled

Currently, only cross-margin accounts are supported to close position when cross currencies are disabled.  Maximum buy quantity = (unpaid principal and interest - currency balance - the amount of the currency in the order book) / 0.998

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
liquidate_order = gate_api.LiquidateOrder() # LiquidateOrder | 

try:
    # close position when cross-currency is disabled
    api_response = api_instance.create_cross_liquidate_order(liquidate_order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->create_cross_liquidate_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **liquidate_order** | [**LiquidateOrder**](LiquidateOrder.md)|  | 

### Return type

[**Order**](Order.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | order created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> list[Order] list_orders(currency_pair, status, page=page, limit=limit, account=account, _from=_from, to=to, side=side)

List orders

Spot and margin orders are returned by default. If cross margin orders are needed, `account` must be set to `cross_margin`  When `status` is `open`, i.e., listing open orders, only pagination parameters `page` and `limit` are supported and `limit` cannot be larger than 100. Query by `side` and time range parameters `from` and `to` are not supported.  When `status` is `finished`, i.e., listing finished orders, pagination parameters, time range parameters `from` and `to`, and `side` parameters are all supported. Time range parameters are handled as order finish time.

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
currency_pair = 'BTC_USDT' # str | Retrieve results with specified currency pair. It is required for open orders, but optional for finished ones.
status = 'open' # str | List orders based on status  `open` - order is waiting to be filled `finished` - order has been filled or cancelled 
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records to be returned. If `status` is `open`, maximum of `limit` is 100 (optional) (default to 100)
account = 'cross_margin' # str | Specify operation account. Default to spot and margin account if not specified. Set to `cross_margin` to operate against margin account.  Portfolio margin account must set to `cross_margin` only (optional)
_from = 1627706330 # int | Start timestamp of the query (optional)
to = 1635329650 # int | Time range ending, default to current time (optional)
side = 'sell' # str | All bids or asks. Both included if not specified (optional)

try:
    # List orders
    api_response = api_instance.list_orders(currency_pair, status, page=page, limit=limit, account=account, _from=_from, to=to, side=side)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Retrieve results with specified currency pair. It is required for open orders, but optional for finished ones. | 
 **status** | **str**| List orders based on status  &#x60;open&#x60; - order is waiting to be filled &#x60;finished&#x60; - order has been filled or cancelled  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned. If &#x60;status&#x60; is &#x60;open&#x60;, maximum of &#x60;limit&#x60; is 100 | [optional] [default to 100]
 **account** | **str**| Specify operation account. Default to spot and margin account if not specified. Set to &#x60;cross_margin&#x60; to operate against margin account.  Portfolio margin account must set to &#x60;cross_margin&#x60; only | [optional] 
 **_from** | **int**| Start timestamp of the query | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **side** | **str**| All bids or asks. Both included if not specified | [optional] 

### Return type

[**list[Order]**](Order.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> Order create_order(order)

Create an order

You can place orders with spot, margin or cross margin account through setting the `account `field. It defaults to `spot`, which means spot account is used to place orders.  When margin account is used, i.e., `account` is `margin`, `auto_borrow` field can be set to `true` to enable the server to borrow the amount lacked using `POST /margin/loans` when your account's balance is not enough. Whether margin orders' fill will be used to repay margin loans automatically is determined by the auto repayment setting in your **margin account**, which can be updated or queried using `/margin/auto_repay` API.  When cross margin account is used, i.e., `account` is `cross_margin`, `auto_borrow` can also be enabled to achieve borrowing the insufficient amount automatically if cross account's balance is not enough. But it differs from margin account that automatic repayment is determined by order's `auto_repay` field and only current order's fill will be used to repay cross margin loans.  Automatic repayment will be triggered when the order is finished, i.e., its status is either `cancelled` or `closed`.  **Order status**  An order waiting to be filled is `open`, and it stays `open` until it is filled totally. If fully filled, order is finished and its status turns to `closed`.If the order is cancelled before it is totally filled, whether or not partially filled, its status is `cancelled`. **Iceberg order**  `iceberg` field can be used to set the amount shown. Set to `-1` to hide the order completely. Note that the hidden part's fee will be charged using taker's fee rate. 

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
order = gate_api.Order() # Order | 

try:
    # Create an order
    api_response = api_instance.create_order(order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
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

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Order created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_orders**
> list[Order] cancel_orders(currency_pair, side=side, account=account)

Cancel all `open` orders in specified currency pair

If `account` is not set, all open orders, including spot, margin and cross margin ones, will be cancelled.  You can set `account` to cancel only orders within the specified account

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
currency_pair = 'BTC_USDT' # str | Currency pair
side = 'sell' # str | All bids or asks. Both included if not specified (optional)
account = 'spot' # str | Specify account type  - classic account：Default to all account types being included   - portfolio margin account：`cross_margin` only (optional)

try:
    # Cancel all `open` orders in specified currency pair
    api_response = api_instance.cancel_orders(currency_pair, side=side, account=account)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->cancel_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | 
 **side** | **str**| All bids or asks. Both included if not specified | [optional] 
 **account** | **str**| Specify account type  - classic account：Default to all account types being included   - portfolio margin account：&#x60;cross_margin&#x60; only | [optional] 

### Return type

[**list[Order]**](Order.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch cancellation request accepted. Query order status by listing orders |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_batch_orders**
> list[CancelOrderResult] cancel_batch_orders(cancel_order)

Cancel a batch of orders with an ID list

Multiple currency pairs can be specified, but maximum 20 orders are allowed per request

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
cancel_order = [gate_api.CancelOrder()] # list[CancelOrder] | 

try:
    # Cancel a batch of orders with an ID list
    api_response = api_instance.cancel_batch_orders(cancel_order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
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

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch cancellation completed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> Order get_order(order_id, currency_pair, account=account)

Get a single order

Spot and margin orders are queried by default. If cross margin orders are needed or portfolio margin account are used, account must be set to cross_margin.

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
order_id = '12345' # str | Order ID returned, or user custom ID(i.e., `text` field). Operations based on custom ID can only be checked when the order is in orderbook.  When the order is finished, it can be checked within 1 hour after the end of the order.  After that, only order ID is accepted.
currency_pair = 'BTC_USDT' # str | Currency pair
account = 'cross_margin' # str | Specify operation account. Default to spot and margin account if not specified. Set to `cross_margin` to operate against margin account.  Portfolio margin account must set to `cross_margin` only (optional)

try:
    # Get a single order
    api_response = api_instance.get_order(order_id, currency_pair, account=account)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID returned, or user custom ID(i.e., &#x60;text&#x60; field). Operations based on custom ID can only be checked when the order is in orderbook.  When the order is finished, it can be checked within 1 hour after the end of the order.  After that, only order ID is accepted. | 
 **currency_pair** | **str**| Currency pair | 
 **account** | **str**| Specify operation account. Default to spot and margin account if not specified. Set to &#x60;cross_margin&#x60; to operate against margin account.  Portfolio margin account must set to &#x60;cross_margin&#x60; only | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detail retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_order**
> Order cancel_order(order_id, currency_pair, account=account)

Cancel a single order

Spot and margin orders are cancelled by default. If trying to cancel cross margin orders or portfolio margin account are used, account must be set to cross_margin

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
order_id = '12345' # str | Order ID returned, or user custom ID(i.e., `text` field). Operations based on custom ID can only be checked when the order is in orderbook.  When the order is finished, it can be checked within 1 hour after the end of the order.  After that, only order ID is accepted.
currency_pair = 'BTC_USDT' # str | Currency pair
account = 'cross_margin' # str | Specify operation account. Default to spot and margin account if not specified. Set to `cross_margin` to operate against margin account.  Portfolio margin account must set to `cross_margin` only (optional)

try:
    # Cancel a single order
    api_response = api_instance.cancel_order(order_id, currency_pair, account=account)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID returned, or user custom ID(i.e., &#x60;text&#x60; field). Operations based on custom ID can only be checked when the order is in orderbook.  When the order is finished, it can be checked within 1 hour after the end of the order.  After that, only order ID is accepted. | 
 **currency_pair** | **str**| Currency pair | 
 **account** | **str**| Specify operation account. Default to spot and margin account if not specified. Set to &#x60;cross_margin&#x60; to operate against margin account.  Portfolio margin account must set to &#x60;cross_margin&#x60; only | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order cancelled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amend_order**
> Order amend_order(order_id, currency_pair, order_patch, account=account)

Amend an order

By default, the orders of spot and margin account are updated.  If you need to modify orders of the `cross-margin` account, you must specify account as `cross_margin`.  For portfolio margin account, only `cross_margin` account is supported.  Currently, only supports modification of `price` or `amount` fields.  Regarding rate limiting: modify order and create order sharing rate limiting rules. Regarding matching priority: only modifying the amount does not affect the priority. If the price is modified, the priority will be adjusted to the last of the new price. Note: If the modified amount is less than the fill amount, the order will be cancelled.

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
order_id = '12345' # str | Order ID returned, or user custom ID(i.e., `text` field). Operations based on custom ID can only be checked when the order is in orderbook.  When the order is finished, it can be checked within 1 hour after the end of the order.  After that, only order ID is accepted.
currency_pair = 'BTC_USDT' # str | Currency pair
order_patch = gate_api.OrderPatch() # OrderPatch | 
account = 'cross_margin' # str | Specify operation account. Default to spot and margin account if not specified. Set to `cross_margin` to operate against margin account.  Portfolio margin account must set to `cross_margin` only (optional)

try:
    # Amend an order
    api_response = api_instance.amend_order(order_id, currency_pair, order_patch, account=account)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->amend_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID returned, or user custom ID(i.e., &#x60;text&#x60; field). Operations based on custom ID can only be checked when the order is in orderbook.  When the order is finished, it can be checked within 1 hour after the end of the order.  After that, only order ID is accepted. | 
 **currency_pair** | **str**| Currency pair | 
 **order_patch** | [**OrderPatch**](OrderPatch.md)|  | 
 **account** | **str**| Specify operation account. Default to spot and margin account if not specified. Set to &#x60;cross_margin&#x60; to operate against margin account.  Portfolio margin account must set to &#x60;cross_margin&#x60; only | [optional] 

### Return type

[**Order**](Order.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_my_trades**
> list[Trade] list_my_trades(currency_pair=currency_pair, limit=limit, page=page, order_id=order_id, account=account, _from=_from, to=to)

List personal trading history

Spot and margin trades are queried by default. If cross margin trades are needed, `account` must be set to `cross_margin`  You can also set `from` and(or) `to` to query by time range. If you don't specify `from` and/or `to` parameters, only the last 7 days of data will be retured. The range of `from` and `to` is not alloed to exceed 30 days.  Time range parameters are handled as order finish time.

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
currency_pair = 'BTC_USDT' # str | Retrieve results with specified currency pair (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
page = 1 # int | Page number (optional) (default to 1)
order_id = '12345' # str | Filter trades with specified order ID. `currency_pair` is also required if this field is present (optional)
account = 'cross_margin' # str | Specify operation account. Default to spot and margin account if not specified. Set to `cross_margin` to operate against margin account.  Portfolio margin account must set to `cross_margin` only (optional)
_from = 1627706330 # int | Start timestamp of the query (optional)
to = 1635329650 # int | Time range ending, default to current time (optional)

try:
    # List personal trading history
    api_response = api_instance.list_my_trades(currency_pair=currency_pair, limit=limit, page=page, order_id=order_id, account=account, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->list_my_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Retrieve results with specified currency pair | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **page** | **int**| Page number | [optional] [default to 1]
 **order_id** | **str**| Filter trades with specified order ID. &#x60;currency_pair&#x60; is also required if this field is present | [optional] 
 **account** | **str**| Specify operation account. Default to spot and margin account if not specified. Set to &#x60;cross_margin&#x60; to operate against margin account.  Portfolio margin account must set to &#x60;cross_margin&#x60; only | [optional] 
 **_from** | **int**| Start timestamp of the query | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 

### Return type

[**list[Trade]**](Trade.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_time**
> SystemTime get_system_time()

Get server current time

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)

try:
    # Get server current time
    api_response = api_instance.get_system_time()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->get_system_time: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemTime**](SystemTime.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **countdown_cancel_all_spot**
> TriggerTime countdown_cancel_all_spot(countdown_cancel_all_spot_task)

Countdown cancel orders

When the timeout set by the user is reached, if there is no cancel or set a new countdown, the related pending orders will be automatically cancelled.  This endpoint can be called repeatedly to set a new countdown or cancel the countdown. For example, call this endpoint at 30s intervals, each countdown`timeout` is set to 30s. If this endpoint is not called again within 30 seconds, all pending orders on the specified `market` will be automatically cancelled, if no `market` is specified, all market pending orders will be cancelled. If the `timeout` is set to 0 within 30 seconds, the countdown timer will expire and the cacnel function will be cancelled.

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
countdown_cancel_all_spot_task = gate_api.CountdownCancelAllSpotTask() # CountdownCancelAllSpotTask | 

try:
    # Countdown cancel orders
    api_response = api_instance.countdown_cancel_all_spot(countdown_cancel_all_spot_task)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->countdown_cancel_all_spot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countdown_cancel_all_spot_task** | [**CountdownCancelAllSpotTask**](CountdownCancelAllSpotTask.md)|  | 

### Return type

[**TriggerTime**](TriggerTime.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Set countdown successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_spot_price_triggered_orders**
> list[SpotPriceTriggeredOrder] list_spot_price_triggered_orders(status, market=market, account=account, limit=limit, offset=offset)

Retrieve running auto order list

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
status = 'status_example' # str | Only list the orders with this status
market = 'BTC_USDT' # str | Currency pair (optional)
account = 'account_example' # str | Trading account type.  Portfolio margin account must set to `cross_margin` (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Retrieve running auto order list
    api_response = api_instance.list_spot_price_triggered_orders(status, market=market, account=account, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->list_spot_price_triggered_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Only list the orders with this status | 
 **market** | **str**| Currency pair | [optional] 
 **account** | **str**| Trading account type.  Portfolio margin account must set to &#x60;cross_margin&#x60; | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

### Return type

[**list[SpotPriceTriggeredOrder]**](SpotPriceTriggeredOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_spot_price_triggered_order**
> TriggerOrderResponse create_spot_price_triggered_order(spot_price_triggered_order)

Create a price-triggered order

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
spot_price_triggered_order = gate_api.SpotPriceTriggeredOrder() # SpotPriceTriggeredOrder | 

try:
    # Create a price-triggered order
    api_response = api_instance.create_spot_price_triggered_order(spot_price_triggered_order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->create_spot_price_triggered_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spot_price_triggered_order** | [**SpotPriceTriggeredOrder**](SpotPriceTriggeredOrder.md)|  | 

### Return type

[**TriggerOrderResponse**](TriggerOrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Order created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_spot_price_triggered_order_list**
> list[SpotPriceTriggeredOrder] cancel_spot_price_triggered_order_list(market=market, account=account)

Cancel all open orders

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
market = 'BTC_USDT' # str | Currency pair (optional)
account = 'account_example' # str | Trading account type.  Portfolio margin account must set to `cross_margin` (optional)

try:
    # Cancel all open orders
    api_response = api_instance.cancel_spot_price_triggered_order_list(market=market, account=account)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->cancel_spot_price_triggered_order_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **market** | **str**| Currency pair | [optional] 
 **account** | **str**| Trading account type.  Portfolio margin account must set to &#x60;cross_margin&#x60; | [optional] 

### Return type

[**list[SpotPriceTriggeredOrder]**](SpotPriceTriggeredOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch cancellation request accepted. Query order status by listing orders |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spot_price_triggered_order**
> SpotPriceTriggeredOrder get_spot_price_triggered_order(order_id)

Get a price-triggered order

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
order_id = 'order_id_example' # str | Retrieve the data of the order with the specified ID

try:
    # Get a price-triggered order
    api_response = api_instance.get_spot_price_triggered_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->get_spot_price_triggered_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Retrieve the data of the order with the specified ID | 

### Return type

[**SpotPriceTriggeredOrder**](SpotPriceTriggeredOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auto order detail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_spot_price_triggered_order**
> SpotPriceTriggeredOrder cancel_spot_price_triggered_order(order_id)

cancel a price-triggered order

### Example

* Api Key Authentication (apiv4):
```python
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization
configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = "YOU_API_KEY",
    secret = "YOUR_API_SECRET"
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.SpotApi(api_client)
order_id = 'order_id_example' # str | Retrieve the data of the order with the specified ID

try:
    # cancel a price-triggered order
    api_response = api_instance.cancel_spot_price_triggered_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->cancel_spot_price_triggered_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Retrieve the data of the order with the specified ID | 

### Return type

[**SpotPriceTriggeredOrder**](SpotPriceTriggeredOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auto order detail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

