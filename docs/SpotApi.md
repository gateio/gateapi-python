# gate_api.SpotApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_currencies**](SpotApi.md#list_currencies) | **GET** /spot/currencies | Query all currency information
[**get_currency**](SpotApi.md#get_currency) | **GET** /spot/currencies/{currency} | Query single currency information
[**list_currency_pairs**](SpotApi.md#list_currency_pairs) | **GET** /spot/currency_pairs | Query all supported currency pairs
[**get_currency_pair**](SpotApi.md#get_currency_pair) | **GET** /spot/currency_pairs/{currency_pair} | Query single currency pair details
[**list_tickers**](SpotApi.md#list_tickers) | **GET** /spot/tickers | Get currency pair ticker information
[**list_order_book**](SpotApi.md#list_order_book) | **GET** /spot/order_book | Get market depth information
[**list_trades**](SpotApi.md#list_trades) | **GET** /spot/trades | Query market transaction records
[**list_candlesticks**](SpotApi.md#list_candlesticks) | **GET** /spot/candlesticks | Market K-line chart
[**get_fee**](SpotApi.md#get_fee) | **GET** /spot/fee | Query account fee rates
[**get_batch_spot_fee**](SpotApi.md#get_batch_spot_fee) | **GET** /spot/batch_fee | Batch query account fee rates
[**list_spot_accounts**](SpotApi.md#list_spot_accounts) | **GET** /spot/accounts | List spot trading accounts
[**list_spot_account_book**](SpotApi.md#list_spot_account_book) | **GET** /spot/account_book | Query spot account transaction history
[**create_batch_orders**](SpotApi.md#create_batch_orders) | **POST** /spot/batch_orders | Batch place orders
[**list_all_open_orders**](SpotApi.md#list_all_open_orders) | **GET** /spot/open_orders | List all open orders
[**create_cross_liquidate_order**](SpotApi.md#create_cross_liquidate_order) | **POST** /spot/cross_liquidate_orders | Close position when cross-currency is disabled
[**list_orders**](SpotApi.md#list_orders) | **GET** /spot/orders | List orders
[**create_order**](SpotApi.md#create_order) | **POST** /spot/orders | Create an order
[**cancel_orders**](SpotApi.md#cancel_orders) | **DELETE** /spot/orders | Cancel all &#x60;open&#x60; orders in specified currency pair
[**cancel_batch_orders**](SpotApi.md#cancel_batch_orders) | **POST** /spot/cancel_batch_orders | Cancel batch orders by specified ID list
[**get_order**](SpotApi.md#get_order) | **GET** /spot/orders/{order_id} | Query single order details
[**cancel_order**](SpotApi.md#cancel_order) | **DELETE** /spot/orders/{order_id} | Cancel single order
[**amend_order**](SpotApi.md#amend_order) | **PATCH** /spot/orders/{order_id} | Amend single order
[**list_my_trades**](SpotApi.md#list_my_trades) | **GET** /spot/my_trades | Query personal trading records
[**get_system_time**](SpotApi.md#get_system_time) | **GET** /spot/time | Get server current time
[**countdown_cancel_all_spot**](SpotApi.md#countdown_cancel_all_spot) | **POST** /spot/countdown_cancel_all | Countdown cancel orders
[**amend_batch_orders**](SpotApi.md#amend_batch_orders) | **POST** /spot/amend_batch_orders | Batch modification of orders
[**get_spot_insurance_history**](SpotApi.md#get_spot_insurance_history) | **GET** /spot/insurance_history | Query spot insurance fund historical data
[**list_spot_price_triggered_orders**](SpotApi.md#list_spot_price_triggered_orders) | **GET** /spot/price_orders | Query running auto order list
[**create_spot_price_triggered_order**](SpotApi.md#create_spot_price_triggered_order) | **POST** /spot/price_orders | Create price-triggered order
[**cancel_spot_price_triggered_order_list**](SpotApi.md#cancel_spot_price_triggered_order_list) | **DELETE** /spot/price_orders | Cancel all auto orders
[**get_spot_price_triggered_order**](SpotApi.md#get_spot_price_triggered_order) | **GET** /spot/price_orders/{order_id} | Query single auto order details
[**cancel_spot_price_triggered_order**](SpotApi.md#cancel_spot_price_triggered_order) | **DELETE** /spot/price_orders/{order_id} | Cancel single auto order


# **list_currencies**
> list[Currency] list_currencies()

Query all currency information

When a currency corresponds to multiple chains, you can query the information of multiple chains through the `chains` field, such as the charging and recharge status, identification, etc. of the chain

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
    # Query all currency information
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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency**
> Currency get_currency(currency)

Query single currency information

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
    # Query single currency information
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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_currency_pairs**
> list[CurrencyPair] list_currency_pairs()

Query all supported currency pairs

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
    # Query all supported currency pairs
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

Query single currency pair details

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
    # Query single currency pair details
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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tickers**
> list[Ticker] list_tickers(currency_pair=currency_pair, timezone=timezone)

Get currency pair ticker information

If `currency_pair` is specified, only query that currency pair; otherwise return all information

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
    # Get currency pair ticker information
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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_order_book**
> OrderBook list_order_book(currency_pair, interval=interval, limit=limit, with_id=with_id)

Get market depth information

Market depth buy orders are sorted by price from high to low, sell orders are sorted from low to high

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
interval = '0' # str | Price precision for depth aggregation, 0 means no aggregation, defaults to 0 if not specified (optional) (default to '0')
limit = 10 # int | Number of depth levels (optional) (default to 10)
with_id = False # bool | Return order book update ID (optional) (default to False)

try:
    # Get market depth information
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
 **interval** | **str**| Price precision for depth aggregation, 0 means no aggregation, defaults to 0 if not specified | [optional] [default to &#39;0&#39;]
 **limit** | **int**| Number of depth levels | [optional] [default to 10]
 **with_id** | **bool**| Return order book update ID | [optional] [default to False]

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_trades**
> list[Trade] list_trades(currency_pair, limit=limit, last_id=last_id, reverse=reverse, _from=_from, to=to, page=page)

Query market transaction records

Supports querying by time range using `from` and `to` parameters or pagination based on `last_id`. By default, queries the last 30 days.  Pagination based on `last_id` is no longer recommended. If `last_id` is specified, the time range query parameters will be ignored.  When using limit&page pagination to retrieve data, the maximum number of pages is 100,000, that is, limit * (page - 1) <= 100,000.

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
limit = 100 # int | Maximum number of items returned in list. Default: 100, minimum: 1, maximum: 1000 (optional) (default to 100)
last_id = '12345' # str | Specify the currency name to query in batches, and support up to 100 pass parameters at a time (optional)
reverse = False # bool | Whether to retrieve data less than `last_id`. Default returns records greater than `last_id`.  Set to `true` to trace back market trade records, `false` to get latest trades.  No effect when `last_id` is not set. (optional) (default to False)
_from = 1627706330 # int | Start timestamp for the query (optional)
to = 1635329650 # int | End timestamp for the query, defaults to current time if not specified (optional)
page = 1 # int | Page number (optional) (default to 1)

try:
    # Query market transaction records
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
 **limit** | **int**| Maximum number of items returned in list. Default: 100, minimum: 1, maximum: 1000 | [optional] [default to 100]
 **last_id** | **str**| Specify the currency name to query in batches, and support up to 100 pass parameters at a time | [optional] 
 **reverse** | **bool**| Whether to retrieve data less than &#x60;last_id&#x60;. Default returns records greater than &#x60;last_id&#x60;.  Set to &#x60;true&#x60; to trace back market trade records, &#x60;false&#x60; to get latest trades.  No effect when &#x60;last_id&#x60; is not set. | [optional] [default to False]
 **_from** | **int**| Start timestamp for the query | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 
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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_candlesticks**
> list[list[str]] list_candlesticks(currency_pair, limit=limit, _from=_from, to=to, interval=interval)

Market K-line chart

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
limit = 100 # int | Maximum number of recent data points to return. `limit` conflicts with `from` and `to`. If either `from` or `to` is specified, request will be rejected. (optional) (default to 100)
_from = 1546905600 # int | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to`to - 100 * interval` if not specified (optional)
to = 1546935600 # int | Specify the end time of the K-line chart, defaults to current time if not specified, note that the time format is Unix timestamp with second precision (optional)
interval = '30m' # str | Time interval between data points. Note that `30d` represents a calendar month, not aligned to 30 days (optional) (default to '30m')

try:
    # Market K-line chart
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
 **limit** | **int**| Maximum number of recent data points to return. &#x60;limit&#x60; conflicts with &#x60;from&#x60; and &#x60;to&#x60;. If either &#x60;from&#x60; or &#x60;to&#x60; is specified, request will be rejected. | [optional] [default to 100]
 **_from** | **int**| Start time of candlesticks, formatted in Unix timestamp in seconds. Default to&#x60;to - 100 * interval&#x60; if not specified | [optional] 
 **to** | **int**| Specify the end time of the K-line chart, defaults to current time if not specified, note that the time format is Unix timestamp with second precision | [optional] 
 **interval** | **str**| Time interval between data points. Note that &#x60;30d&#x60; represents a calendar month, not aligned to 30 days | [optional] [default to &#39;30m&#39;]

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fee**
> SpotFee get_fee(currency_pair=currency_pair)

Query account fee rates

This API is deprecated. The new fee query API is `/wallet/fee`

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
currency_pair = 'BTC_USDT' # str | Specify currency pair to get more accurate fee settings.  This field is optional. Usually fee settings are the same for all currency pairs. (optional)

try:
    # Query account fee rates
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
 **currency_pair** | **str**| Specify currency pair to get more accurate fee settings.  This field is optional. Usually fee settings are the same for all currency pairs. | [optional] 

### Return type

[**SpotFee**](SpotFee.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_batch_spot_fee**
> dict(str, SpotFee) get_batch_spot_fee(currency_pairs)

Batch query account fee rates

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
currency_pairs = 'BTC_USDT,ETH_USDT' # str | Maximum 50 currency pairs per request

try:
    # Batch query account fee rates
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
 **currency_pairs** | **str**| Maximum 50 currency pairs per request | 

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_spot_accounts**
> list[SpotAccount] list_spot_accounts(currency=currency)

List spot trading accounts

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
currency = 'BTC' # str | Query by specified currency name (optional)

try:
    # List spot trading accounts
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
 **currency** | **str**| Query by specified currency name | [optional] 

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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_spot_account_book**
> list[SpotAccountBook] list_spot_account_book(currency=currency, _from=_from, to=to, page=page, limit=limit, type=type, code=code)

Query spot account transaction history

Record query time range cannot exceed 30 days.  When using limit&page pagination to retrieve data, the maximum number of pages is 100,000, that is, limit * (page - 1) <= 100,000.

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
currency = 'BTC' # str | Query by specified currency name (optional)
_from = 1627706330 # int | Start timestamp for the query (optional)
to = 1635329650 # int | End timestamp for the query, defaults to current time if not specified (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
type = 'lend' # str | Query by specified account change type. If not specified, all change types will be included. (optional)
code = 'code_example' # str | Specify account change code for query. If not specified, all change types are included. This parameter has higher priority than `type` (optional)

try:
    # Query spot account transaction history
    api_response = api_instance.list_spot_account_book(currency=currency, _from=_from, to=to, page=page, limit=limit, type=type, code=code)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->list_spot_account_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Query by specified currency name | [optional] 
 **_from** | **int**| Start timestamp for the query | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **type** | **str**| Query by specified account change type. If not specified, all change types will be included. | [optional] 
 **code** | **str**| Specify account change code for query. If not specified, all change types are included. This parameter has higher priority than &#x60;type&#x60; | [optional] 

### Return type

[**list[SpotAccountBook]**](SpotAccountBook.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch_orders**
> list[BatchOrder] create_batch_orders(order, x_gate_exptime=x_gate_exptime)

Batch place orders

Batch order requirements:  1. Custom order field `text` must be specified 2. Up to 4 currency pairs per request, with up to 10 orders per currency pair 3. Spot orders and margin orders cannot be mixed; all `account` fields in the same request must be identical

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
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Batch place orders
    api_response = api_instance.create_batch_orders(order, x_gate_exptime=x_gate_exptime)
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
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

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
**200** | Request execution completed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_open_orders**
> list[OpenOrders] list_all_open_orders(page=page, limit=limit, account=account)

List all open orders

Query the current order list of all trading pairs. Please note that the paging parameter controls the number of pending orders in each trading pair. There is no paging control trading pairs. All trading pairs with pending orders will be returned.

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
account = 'spot' # str | Specify query account (optional)

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
 **account** | **str**| Specify query account | [optional] 

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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cross_liquidate_order**
> Order create_cross_liquidate_order(liquidate_order)

Close position when cross-currency is disabled

Currently, only cross-margin accounts are supported to place buy orders for disabled currencies. Maximum buy quantity = (unpaid principal and interest - currency balance - the amount of the currency in pending orders) / 0.998

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
    # Close position when cross-currency is disabled
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
**201** | Order created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> list[Order] list_orders(currency_pair, status, page=page, limit=limit, account=account, _from=_from, to=to, side=side)

List orders

Note that query results default to spot order lists for spot, unified account, and isolated margin accounts.  When `status` is set to `open` (i.e., when querying pending order lists), only `page` and `limit` pagination controls are supported. `limit` can only be set to a maximum of 100. The `side` parameter and time range query parameters `from` and `to` are not supported.  When `status` is set to `finished` (i.e., when querying historical orders), in addition to pagination queries, `from` and `to` time range queries are also supported. Additionally, the `side` parameter can be set to filter one-sided history.  Time range filter parameters are processed according to the order end time.

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
currency_pair = 'BTC_USDT' # str | Query by specified currency pair. Required for open orders, optional for filled orders
status = 'open' # str | List orders based on status  `open` - order is waiting to be filled `finished` - order has been filled or cancelled 
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records to be returned. If `status` is `open`, maximum of `limit` is 100 (optional) (default to 100)
account = 'spot' # str | Specify query account (optional)
_from = 1627706330 # int | Start timestamp for the query (optional)
to = 1635329650 # int | End timestamp for the query, defaults to current time if not specified (optional)
side = 'sell' # str | Specify all bids or all asks, both included if not specified (optional)

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
 **currency_pair** | **str**| Query by specified currency pair. Required for open orders, optional for filled orders | 
 **status** | **str**| List orders based on status  &#x60;open&#x60; - order is waiting to be filled &#x60;finished&#x60; - order has been filled or cancelled  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned. If &#x60;status&#x60; is &#x60;open&#x60;, maximum of &#x60;limit&#x60; is 100 | [optional] [default to 100]
 **account** | **str**| Specify query account | [optional] 
 **_from** | **int**| Start timestamp for the query | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 
 **side** | **str**| Specify all bids or all asks, both included if not specified | [optional] 

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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> Order create_order(order, x_gate_exptime=x_gate_exptime)

Create an order

Supports spot, margin, leverage, and cross-margin leverage orders. Use different accounts through the `account` field. Default is `spot`, which means using the spot account to place orders. If the user has a `unified` account, the default is to place orders with the unified account.  When using leveraged account trading (i.e., when `account` is set to `margin`), you can set `auto_borrow` to `true`. In case of insufficient account balance, the system will automatically execute `POST /margin/uni/loans` to borrow the insufficient amount. Whether assets obtained after leveraged order execution are automatically used to repay borrowing orders of the isolated margin account depends on the automatic repayment settings of the user's isolated margin account. Account automatic repayment settings can be queried and set through `/margin/auto_repay`.  When using unified account trading (i.e., when `account` is set to `unified`), `auto_borrow` can also be enabled to realize automatic borrowing of insufficient amounts. However, unlike the isolated margin account, whether unified account orders are automatically repaid depends on the `auto_repay` setting when placing the order. This setting only applies to the current order, meaning only assets obtained after order execution will be used to repay borrowing orders of the cross-margin account. Unified account ordering currently supports enabling both `auto_borrow` and `auto_repay` simultaneously.  Auto repayment will be triggered when the order ends, i.e., when `status` is `cancelled` or `closed`.  **Order Status**  The order status in pending orders is `open`, which remains `open` until all quantity is filled. If fully filled, the order ends and status becomes `closed`. If the order is cancelled before all transactions are completed, regardless of partial fills, the status will become `cancelled`.  **Iceberg Orders**  `iceberg` is used to set the displayed quantity of iceberg orders and does not support complete hiding. Note that hidden portions are charged according to the taker's fee rate.  **Self-Trade Prevention**  Set `stp_act` to determine the self-trade prevention strategy to use

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
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Create an order
    api_response = api_instance.create_order(order, x_gate_exptime=x_gate_exptime)
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
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

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
**201** | Order created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_orders**
> list[OrderCancel] cancel_orders(currency_pair=currency_pair, side=side, account=account, action_mode=action_mode, x_gate_exptime=x_gate_exptime)

Cancel all `open` orders in specified currency pair

When the `account` parameter is not specified, all pending orders including spot, unified account, and isolated margin will be cancelled. When `currency_pair` is not specified, all trading pair pending orders will be cancelled. You can specify a particular account to cancel all pending orders under that account

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
currency_pair = 'BTC_USDT' # str | Currency pair (optional)
side = 'sell' # str | Specify all bids or all asks, both included if not specified (optional)
account = 'spot' # str | Specify account type  Classic account: All are included if not specified Unified account: Specify `unified` (optional)
action_mode = 'ACK' # str | Processing Mode  When placing an order, different fields are returned based on the action_mode  - `ACK`: Asynchronous mode, returns only key order fields - `RESULT`: No clearing information - `FULL`: Full mode (default) (optional)
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Cancel all `open` orders in specified currency pair
    api_response = api_instance.cancel_orders(currency_pair=currency_pair, side=side, account=account, action_mode=action_mode, x_gate_exptime=x_gate_exptime)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->cancel_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | [optional] 
 **side** | **str**| Specify all bids or all asks, both included if not specified | [optional] 
 **account** | **str**| Specify account type  Classic account: All are included if not specified Unified account: Specify &#x60;unified&#x60; | [optional] 
 **action_mode** | **str**| Processing Mode  When placing an order, different fields are returned based on the action_mode  - &#x60;ACK&#x60;: Asynchronous mode, returns only key order fields - &#x60;RESULT&#x60;: No clearing information - &#x60;FULL&#x60;: Full mode (default) | [optional] 
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

### Return type

[**list[OrderCancel]**](OrderCancel.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch cancellation request accepted and processed, success determined by order list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_batch_orders**
> list[CancelOrderResult] cancel_batch_orders(cancel_batch_order, x_gate_exptime=x_gate_exptime)

Cancel batch orders by specified ID list

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
cancel_batch_order = [gate_api.CancelBatchOrder()] # list[CancelBatchOrder] | 
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Cancel batch orders by specified ID list
    api_response = api_instance.cancel_batch_orders(cancel_batch_order, x_gate_exptime=x_gate_exptime)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->cancel_batch_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancel_batch_order** | [**list[CancelBatchOrder]**](CancelBatchOrder.md)|  | 
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

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

Query single order details

By default, queries orders for spot, unified account, and isolated margin accounts.

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
order_id = '12345' # str | The order ID returned when the order was successfully created or the custom ID specified by the user's creation (i.e. the `text` field). Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel)
currency_pair = 'BTC_USDT' # str | Specify the trading pair to query. This field is required when querying pending order records. This field can be omitted when querying filled order records.
account = 'spot' # str | Specify query account (optional)

try:
    # Query single order details
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
 **order_id** | **str**| The order ID returned when the order was successfully created or the custom ID specified by the user&#39;s creation (i.e. the &#x60;text&#x60; field). Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel) | 
 **currency_pair** | **str**| Specify the trading pair to query. This field is required when querying pending order records. This field can be omitted when querying filled order records. | 
 **account** | **str**| Specify query account | [optional] 

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
> Order cancel_order(order_id, currency_pair, account=account, action_mode=action_mode, x_gate_exptime=x_gate_exptime)

Cancel single order

By default, orders for spot, unified accounts and leveraged accounts are revoked.

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
order_id = '12345' # str | The order ID returned when the order was successfully created or the custom ID specified by the user's creation (i.e. the `text` field). Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel)
currency_pair = 'BTC_USDT' # str | Currency pair
account = 'spot' # str | Specify query account (optional)
action_mode = 'ACK' # str | Processing Mode  When placing an order, different fields are returned based on the action_mode  - `ACK`: Asynchronous mode, returns only key order fields - `RESULT`: No clearing information - `FULL`: Full mode (default) (optional)
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Cancel single order
    api_response = api_instance.cancel_order(order_id, currency_pair, account=account, action_mode=action_mode, x_gate_exptime=x_gate_exptime)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order ID returned when the order was successfully created or the custom ID specified by the user&#39;s creation (i.e. the &#x60;text&#x60; field). Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel) | 
 **currency_pair** | **str**| Currency pair | 
 **account** | **str**| Specify query account | [optional] 
 **action_mode** | **str**| Processing Mode  When placing an order, different fields are returned based on the action_mode  - &#x60;ACK&#x60;: Asynchronous mode, returns only key order fields - &#x60;RESULT&#x60;: No clearing information - &#x60;FULL&#x60;: Full mode (default) | [optional] 
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

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
> Order amend_order(order_id, order_patch, currency_pair=currency_pair, account=account, x_gate_exptime=x_gate_exptime)

Amend single order

Modify orders in spot, unified account and isolated margin account by default.  Currently both request body and query support currency_pair and account parameters, but request body has higher priority.  currency_pair must be filled in one of the request body or query parameters.  About rate limit: Order modification and order creation share the same rate limit rules.  About matching priority: Only reducing the quantity does not affect the matching priority. Modifying the price or increasing the quantity will adjust the priority to the end of the new price level.  Note: Modifying the quantity to be less than the filled quantity will trigger a cancellation and isolated margin account by default.  Currently both request body and query support currency_pair and account parameters, but request body has higher priority.  currency_pair must be filled in one of the request body or query parameters.  About rate limit: Order modification and order creation share the same rate limit rules.  About matching priority: Only reducing the quantity does not affect the matching priority. Modifying the price or increasing the quantity will adjust the priority to the end of the new price level.  Note: Modifying the quantity to be less than the filled quantity will trigger a cancellation operation.

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
order_id = '12345' # str | The order ID returned when the order was successfully created or the custom ID specified by the user's creation (i.e. the `text` field). Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel)
order_patch = gate_api.OrderPatch() # OrderPatch | 
currency_pair = 'BTC_USDT' # str | Currency pair (optional)
account = 'spot' # str | Specify query account (optional)
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Amend single order
    api_response = api_instance.amend_order(order_id, order_patch, currency_pair=currency_pair, account=account, x_gate_exptime=x_gate_exptime)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->amend_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The order ID returned when the order was successfully created or the custom ID specified by the user&#39;s creation (i.e. the &#x60;text&#x60; field). Operations based on custom IDs can only be checked in pending orders. Only order ID can be used after the order is finished (transaction/cancel) | 
 **order_patch** | [**OrderPatch**](OrderPatch.md)|  | 
 **currency_pair** | **str**| Currency pair | [optional] 
 **account** | **str**| Specify query account | [optional] 
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

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
**200** | Updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_my_trades**
> list[Trade] list_my_trades(currency_pair=currency_pair, limit=limit, page=page, order_id=order_id, account=account, _from=_from, to=to)

Query personal trading records

By default query of transaction records for spot, unified account and warehouse-by-site leverage accounts.  The history within a specified time range can be queried by specifying `from` or (and) `to`.  - If no time parameters are specified, only data for the last 7 days can be obtained. - If only any parameter of `from` or `to` is specified, only 7-day data from the start (or end) of the specified time is returned. - The range not allowed to exceed 30 days.  The parameters of the time range filter are processed according to the order end time.  The maximum number of pages when searching data using limit&page paging function is 100,0, that is, limit * (page - 1) <= 100,0.

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
limit = 100 # int | Maximum number of items returned in list. Default: 100, minimum: 1, maximum: 1000 (optional) (default to 100)
page = 1 # int | Page number (optional) (default to 1)
order_id = '12345' # str | Filter trades with specified order ID. `currency_pair` is also required if this field is present (optional)
account = 'spot' # str | Specify query account (optional)
_from = 1627706330 # int | Start timestamp for the query (optional)
to = 1635329650 # int | End timestamp for the query, defaults to current time if not specified (optional)

try:
    # Query personal trading records
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
 **limit** | **int**| Maximum number of items returned in list. Default: 100, minimum: 1, maximum: 1000 | [optional] [default to 100]
 **page** | **int**| Page number | [optional] [default to 1]
 **order_id** | **str**| Filter trades with specified order ID. &#x60;currency_pair&#x60; is also required if this field is present | [optional] 
 **account** | **str**| Specify query account | [optional] 
 **_from** | **int**| Start timestamp for the query | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 

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
**200** | List retrieved successfully |  -  |

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **countdown_cancel_all_spot**
> TriggerTime countdown_cancel_all_spot(countdown_cancel_all_spot_task)

Countdown cancel orders

Spot order heartbeat detection. If there is no \"cancel existing countdown\" or \"set new countdown\" when the user-set `timeout` time is reached, the related `spot pending orders` will be automatically cancelled. This interface can be called repeatedly to set a new countdown or cancel the countdown. Usage example: Repeat this interface at 30s intervals, setting the countdown `timeout` to `30 (seconds)` each time. If this interface is not called again within 30 seconds, all pending orders on the `market` you specified will be automatically cancelled. If no `market` is specified, all market cancelled. If the `timeout` is set to 0 within 30 seconds, the countdown timer will be terminated and the automatic order cancellation function will be cancelled.

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
**200** | Countdown set successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amend_batch_orders**
> list[BatchOrder] amend_batch_orders(batch_amend_item, x_gate_exptime=x_gate_exptime)

Batch modification of orders

Modify orders in spot, unified account and isolated margin account by default. Modify uncompleted orders, up to 5 orders can be modified at a time. Request parameters should be passed in array format. If there are order modification failures during the batch modification process, the modification of the next order will continue to be executed, and the execution will return with the corresponding order failure information. The call order of batch modification orders is consistent with the order list order. The return content order of batch modification orders is consistent with the order list order.

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
batch_amend_item = [gate_api.BatchAmendItem()] # list[BatchAmendItem] | 
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Batch modification of orders
    api_response = api_instance.amend_batch_orders(batch_amend_item, x_gate_exptime=x_gate_exptime)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->amend_batch_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_amend_item** | [**list[BatchAmendItem]**](BatchAmendItem.md)|  | 
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

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
**200** | Order modification executed successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spot_insurance_history**
> list[SpotInsuranceHistory] get_spot_insurance_history(business, currency, _from, to, page=page, limit=limit)

Query spot insurance fund historical data

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
business = 'margin' # str | Leverage business, margin - position by position; unified - unified account
currency = 'BTC' # str | Currency
_from = 1547706332 # int | Start timestamp in seconds
to = 1547706332 # int | End timestamp in seconds
page = 1 # int | Page number (optional) (default to 1)
limit = 30 # int | The maximum number of items returned in the list, the default value is 30 (optional) (default to 30)

try:
    # Query spot insurance fund historical data
    api_response = api_instance.get_spot_insurance_history(business, currency, _from, to, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling SpotApi->get_spot_insurance_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business** | **str**| Leverage business, margin - position by position; unified - unified account | 
 **currency** | **str**| Currency | 
 **_from** | **int**| Start timestamp in seconds | 
 **to** | **int**| End timestamp in seconds | 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| The maximum number of items returned in the list, the default value is 30 | [optional] [default to 30]

### Return type

[**list[SpotInsuranceHistory]**](SpotInsuranceHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_spot_price_triggered_orders**
> list[SpotPriceTriggeredOrder] list_spot_price_triggered_orders(status, market=market, account=account, limit=limit, offset=offset)

Query running auto order list

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
status = 'status_example' # str | Query order list based on status
market = 'BTC_USDT' # str | Trading market (optional)
account = 'account_example' # str | Trading account type. Unified account must be set to `unified` (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Query running auto order list
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
 **status** | **str**| Query order list based on status | 
 **market** | **str**| Trading market | [optional] 
 **account** | **str**| Trading account type. Unified account must be set to &#x60;unified&#x60; | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_spot_price_triggered_order**
> TriggerOrderResponse create_spot_price_triggered_order(spot_price_triggered_order)

Create price-triggered order

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
    # Create price-triggered order
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
**201** | Order created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_spot_price_triggered_order_list**
> list[SpotPriceTriggeredOrder] cancel_spot_price_triggered_order_list(market=market, account=account)

Cancel all auto orders

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
market = 'BTC_USDT' # str | Trading market (optional)
account = 'account_example' # str | Trading account type. Unified account must be set to `unified` (optional)

try:
    # Cancel all auto orders
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
 **market** | **str**| Trading market | [optional] 
 **account** | **str**| Trading account type. Unified account must be set to &#x60;unified&#x60; | [optional] 

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
**200** | Batch cancellation request accepted and processed, success determined by order list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_spot_price_triggered_order**
> SpotPriceTriggeredOrder get_spot_price_triggered_order(order_id)

Query single auto order details

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
order_id = 'order_id_example' # str | ID returned when order is successfully created

try:
    # Query single auto order details
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
 **order_id** | **str**| ID returned when order is successfully created | 

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
**200** | Auto order details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_spot_price_triggered_order**
> SpotPriceTriggeredOrder cancel_spot_price_triggered_order(order_id)

Cancel single auto order

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
order_id = 'order_id_example' # str | ID returned when order is successfully created

try:
    # Cancel single auto order
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
 **order_id** | **str**| ID returned when order is successfully created | 

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
**200** | Auto order details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

