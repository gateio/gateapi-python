# gate_api.FuturesApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_futures_contracts**](FuturesApi.md#list_futures_contracts) | **GET** /futures/{settle}/contracts | List all futures contracts.
[**get_futures_contract**](FuturesApi.md#get_futures_contract) | **GET** /futures/{settle}/contracts/{contract} | Get a single contract.
[**list_futures_order_book**](FuturesApi.md#list_futures_order_book) | **GET** /futures/{settle}/order_book | Futures order book.
[**list_futures_trades**](FuturesApi.md#list_futures_trades) | **GET** /futures/{settle}/trades | Futures trading history.
[**list_futures_candlesticks**](FuturesApi.md#list_futures_candlesticks) | **GET** /futures/{settle}/candlesticks | Get futures candlesticks.
[**list_futures_premium_index**](FuturesApi.md#list_futures_premium_index) | **GET** /futures/{settle}/premium_index | Premium Index K-Line.
[**list_futures_tickers**](FuturesApi.md#list_futures_tickers) | **GET** /futures/{settle}/tickers | List futures tickers.
[**list_futures_funding_rate_history**](FuturesApi.md#list_futures_funding_rate_history) | **GET** /futures/{settle}/funding_rate | Funding rate history.
[**list_futures_insurance_ledger**](FuturesApi.md#list_futures_insurance_ledger) | **GET** /futures/{settle}/insurance | Futures insurance balance history.
[**list_contract_stats**](FuturesApi.md#list_contract_stats) | **GET** /futures/{settle}/contract_stats | Futures stats.
[**get_index_constituents**](FuturesApi.md#get_index_constituents) | **GET** /futures/{settle}/index_constituents/{index} | Get index constituents.
[**list_liquidated_orders**](FuturesApi.md#list_liquidated_orders) | **GET** /futures/{settle}/liq_orders | Retrieve liquidation history.
[**list_futures_risk_limit_tiers**](FuturesApi.md#list_futures_risk_limit_tiers) | **GET** /futures/{settle}/risk_limit_tiers | List risk limit tiers.
[**list_futures_accounts**](FuturesApi.md#list_futures_accounts) | **GET** /futures/{settle}/accounts | Query futures account.
[**list_futures_account_book**](FuturesApi.md#list_futures_account_book) | **GET** /futures/{settle}/account_book | Query account book.
[**list_positions**](FuturesApi.md#list_positions) | **GET** /futures/{settle}/positions | List all positions of a user.
[**get_position**](FuturesApi.md#get_position) | **GET** /futures/{settle}/positions/{contract} | Get single position.
[**update_position_margin**](FuturesApi.md#update_position_margin) | **POST** /futures/{settle}/positions/{contract}/margin | Update position margin.
[**update_position_leverage**](FuturesApi.md#update_position_leverage) | **POST** /futures/{settle}/positions/{contract}/leverage | Update position leverage.
[**update_position_cross_mode**](FuturesApi.md#update_position_cross_mode) | **POST** /futures/{settle}/positions/cross_mode | Switch to the full position-by-store mode.
[**update_position_risk_limit**](FuturesApi.md#update_position_risk_limit) | **POST** /futures/{settle}/positions/{contract}/risk_limit | Update position risk limit.
[**set_dual_mode**](FuturesApi.md#set_dual_mode) | **POST** /futures/{settle}/dual_mode | Enable or disable dual mode.
[**get_dual_mode_position**](FuturesApi.md#get_dual_mode_position) | **GET** /futures/{settle}/dual_comp/positions/{contract} | Retrieve position detail in dual mode.
[**update_dual_mode_position_margin**](FuturesApi.md#update_dual_mode_position_margin) | **POST** /futures/{settle}/dual_comp/positions/{contract}/margin | Update position margin in dual mode.
[**update_dual_mode_position_leverage**](FuturesApi.md#update_dual_mode_position_leverage) | **POST** /futures/{settle}/dual_comp/positions/{contract}/leverage | Update position leverage in dual mode.
[**update_dual_mode_position_risk_limit**](FuturesApi.md#update_dual_mode_position_risk_limit) | **POST** /futures/{settle}/dual_comp/positions/{contract}/risk_limit | Update position risk limit in dual mode.
[**list_futures_orders**](FuturesApi.md#list_futures_orders) | **GET** /futures/{settle}/orders | List futures orders.
[**create_futures_order**](FuturesApi.md#create_futures_order) | **POST** /futures/{settle}/orders | Create a futures order.
[**cancel_futures_orders**](FuturesApi.md#cancel_futures_orders) | **DELETE** /futures/{settle}/orders | Cancel all &#x60;open&#x60; orders matched.
[**get_orders_with_time_range**](FuturesApi.md#get_orders_with_time_range) | **GET** /futures/{settle}/orders_timerange | List Futures Orders By Time Range.
[**create_batch_futures_order**](FuturesApi.md#create_batch_futures_order) | **POST** /futures/{settle}/batch_orders | Create a batch of futures orders.
[**get_futures_order**](FuturesApi.md#get_futures_order) | **GET** /futures/{settle}/orders/{order_id} | Get a single order.
[**amend_futures_order**](FuturesApi.md#amend_futures_order) | **PUT** /futures/{settle}/orders/{order_id} | Amend an order.
[**cancel_futures_order**](FuturesApi.md#cancel_futures_order) | **DELETE** /futures/{settle}/orders/{order_id} | Cancel a single order.
[**get_my_trades**](FuturesApi.md#get_my_trades) | **GET** /futures/{settle}/my_trades | List personal trading history.
[**get_my_trades_with_time_range**](FuturesApi.md#get_my_trades_with_time_range) | **GET** /futures/{settle}/my_trades_timerange | List personal trading history by time range.
[**list_position_close**](FuturesApi.md#list_position_close) | **GET** /futures/{settle}/position_close | List position close history.
[**list_liquidates**](FuturesApi.md#list_liquidates) | **GET** /futures/{settle}/liquidates | List liquidation history.
[**list_auto_deleverages**](FuturesApi.md#list_auto_deleverages) | **GET** /futures/{settle}/auto_deleverages | List Auto-Deleveraging History.
[**countdown_cancel_all_futures**](FuturesApi.md#countdown_cancel_all_futures) | **POST** /futures/{settle}/countdown_cancel_all | Countdown cancel orders.
[**get_futures_fee**](FuturesApi.md#get_futures_fee) | **GET** /futures/{settle}/fee | Query user trading fee rates.
[**cancel_batch_future_orders**](FuturesApi.md#cancel_batch_future_orders) | **POST** /futures/{settle}/batch_cancel_orders | Cancel a batch of orders with an ID list.
[**amend_batch_future_orders**](FuturesApi.md#amend_batch_future_orders) | **POST** /futures/{settle}/batch_amend_orders | Batch modify orders with specified IDs.
[**get_futures_risk_limit_table**](FuturesApi.md#get_futures_risk_limit_table) | **GET** /futures/{settle}/risk_limit_table | Query risk limit table by table_id.
[**list_price_triggered_orders**](FuturesApi.md#list_price_triggered_orders) | **GET** /futures/{settle}/price_orders | List All Price-triggered Orders.
[**create_price_triggered_order**](FuturesApi.md#create_price_triggered_order) | **POST** /futures/{settle}/price_orders | Create a price-triggered order.
[**cancel_price_triggered_order_list**](FuturesApi.md#cancel_price_triggered_order_list) | **DELETE** /futures/{settle}/price_orders | Cancel All Price-triggered Orders.
[**get_price_triggered_order**](FuturesApi.md#get_price_triggered_order) | **GET** /futures/{settle}/price_orders/{order_id} | Get a price-triggered order.
[**cancel_price_triggered_order**](FuturesApi.md#cancel_price_triggered_order) | **DELETE** /futures/{settle}/price_orders/{order_id} | cancel a price-triggered order.


# **list_futures_contracts**
> list[Contract] list_futures_contracts(settle, limit=limit, offset=offset)

List all futures contracts.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)

try:
    # List all futures contracts.
    api_response = api_instance.list_futures_contracts(settle, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]

### Return type

[**list[Contract]**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_futures_contract**
> Contract get_futures_contract(settle, contract)

Get a single contract.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.

try:
    # Get a single contract.
    api_response = api_instance.get_futures_contract(settle, contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->get_futures_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 

### Return type

[**Contract**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_order_book**
> FuturesOrderBook list_futures_order_book(settle, contract, interval=interval, limit=limit, with_id=with_id)

Futures order book.

Bids will be sorted by price from high to low, while asks sorted reversely.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
interval = '0' # str | Order depth. 0 means no aggregation is applied. default to 0. (optional) (default to '0')
limit = 10 # int | Maximum number of order depth data in asks or bids. (optional) (default to 10)
with_id = False # bool | Whether to return depth update ID. This ID increments by 1 each time. (optional) (default to False)

try:
    # Futures order book.
    api_response = api_instance.list_futures_order_book(settle, contract, interval=interval, limit=limit, with_id=with_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_order_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **interval** | **str**| Order depth. 0 means no aggregation is applied. default to 0. | [optional] [default to &#39;0&#39;]
 **limit** | **int**| Maximum number of order depth data in asks or bids. | [optional] [default to 10]
 **with_id** | **bool**| Whether to return depth update ID. This ID increments by 1 each time. | [optional] [default to False]

### Return type

[**FuturesOrderBook**](FuturesOrderBook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Depth query successful. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_trades**
> list[FuturesTrade] list_futures_trades(settle, contract, limit=limit, offset=offset, last_id=last_id, _from=_from, to=to)

Futures trading history.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)
last_id = '12345' # str | Specify the starting point for this list based on a previously retrieved id  This parameter is deprecated. Use `from` and `to` instead to limit time range (optional)
_from = 1546905600 # int | Specify starting time in Unix seconds. If not specified, `to` and `limit` will be used to limit response items. If items between `from` and `to` are more than `limit`, only `limit` number will be returned.  (optional)
to = 1546935600 # int | Specify end time in Unix seconds, default to current time. (optional)

try:
    # Futures trading history.
    api_response = api_instance.list_futures_trades(settle, contract, limit=limit, offset=offset, last_id=last_id, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]
 **last_id** | **str**| Specify the starting point for this list based on a previously retrieved id  This parameter is deprecated. Use &#x60;from&#x60; and &#x60;to&#x60; instead to limit time range | [optional] 
 **_from** | **int**| Specify starting time in Unix seconds. If not specified, &#x60;to&#x60; and &#x60;limit&#x60; will be used to limit response items. If items between &#x60;from&#x60; and &#x60;to&#x60; are more than &#x60;limit&#x60;, only &#x60;limit&#x60; number will be returned.  | [optional] 
 **to** | **int**| Specify end time in Unix seconds, default to current time. | [optional] 

### Return type

[**list[FuturesTrade]**](FuturesTrade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_candlesticks**
> list[FuturesCandlestick] list_futures_candlesticks(settle, contract, _from=_from, to=to, limit=limit, interval=interval)

Get futures candlesticks.

Return specified contract candlesticks. If prefix `contract` with `mark_`, the contract's mark price candlesticks are returned; if prefix with `index_`, index price candlesticks will be returned.  Maximum of 2000 points are returned in one query. Be sure not to exceed the limit when specifying `from`, `to` and `interval`

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
_from = 1546905600 # int | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to`to - 100 * interval` if not specified (optional)
to = 1546935600 # int | Specify the end time of the K-line chart, defaults to current time if not specified, note that the time format is Unix timestamp with second precision specified (optional)
limit = 100 # int | Maximum recent data points to return. `limit` is conflicted with `from` and `to`. If either `from` or `to` is specified, request will be rejected. (optional) (default to 100)
interval = '5m' # str | Interval time between data points. Note that `1w` means natual week(Mon-Sun), while `7d` means every 7d since unix 0. 1 natual month, not 30 days (optional) (default to '5m')

try:
    # Get futures candlesticks.
    api_response = api_instance.list_futures_candlesticks(settle, contract, _from=_from, to=to, limit=limit, interval=interval)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_candlesticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **_from** | **int**| Start time of candlesticks, formatted in Unix timestamp in seconds. Default to&#x60;to - 100 * interval&#x60; if not specified | [optional] 
 **to** | **int**| Specify the end time of the K-line chart, defaults to current time if not specified, note that the time format is Unix timestamp with second precision specified | [optional] 
 **limit** | **int**| Maximum recent data points to return. &#x60;limit&#x60; is conflicted with &#x60;from&#x60; and &#x60;to&#x60;. If either &#x60;from&#x60; or &#x60;to&#x60; is specified, request will be rejected. | [optional] [default to 100]
 **interval** | **str**| Interval time between data points. Note that &#x60;1w&#x60; means natual week(Mon-Sun), while &#x60;7d&#x60; means every 7d since unix 0. 1 natual month, not 30 days | [optional] [default to &#39;5m&#39;]

### Return type

[**list[FuturesCandlestick]**](FuturesCandlestick.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_premium_index**
> list[FuturesPremiumIndex] list_futures_premium_index(settle, contract, _from=_from, to=to, limit=limit, interval=interval)

Premium Index K-Line.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
_from = 1546905600 # int | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to`to - 100 * interval` if not specified (optional)
to = 1546935600 # int | Specify the end time of the K-line chart, defaults to current time if not specified, note that the time format is Unix timestamp with second precision specified (optional)
limit = 100 # int | Maximum recent data points to return. `limit` is conflicted with `from` and `to`. If either `from` or `to` is specified, request will be rejected. (optional) (default to 100)
interval = '5m' # str | Interval time between data points. (optional) (default to '5m')

try:
    # Premium Index K-Line.
    api_response = api_instance.list_futures_premium_index(settle, contract, _from=_from, to=to, limit=limit, interval=interval)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_premium_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **_from** | **int**| Start time of candlesticks, formatted in Unix timestamp in seconds. Default to&#x60;to - 100 * interval&#x60; if not specified | [optional] 
 **to** | **int**| Specify the end time of the K-line chart, defaults to current time if not specified, note that the time format is Unix timestamp with second precision specified | [optional] 
 **limit** | **int**| Maximum recent data points to return. &#x60;limit&#x60; is conflicted with &#x60;from&#x60; and &#x60;to&#x60;. If either &#x60;from&#x60; or &#x60;to&#x60; is specified, request will be rejected. | [optional] [default to 100]
 **interval** | **str**| Interval time between data points. | [optional] [default to &#39;5m&#39;]

### Return type

[**list[FuturesPremiumIndex]**](FuturesPremiumIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_tickers**
> list[FuturesTicker] list_futures_tickers(settle, contract=contract)

List futures tickers.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)

try:
    # List futures tickers.
    api_response = api_instance.list_futures_tickers(settle, contract=contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 

### Return type

[**list[FuturesTicker]**](FuturesTicker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_funding_rate_history**
> list[FundingRateRecord] list_futures_funding_rate_history(settle, contract, limit=limit, _from=_from, to=to)

Funding rate history.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
_from = 1547706332 # int | Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) (optional)
to = 1547706332 # int | Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp (optional)

try:
    # Funding rate history.
    api_response = api_instance.list_futures_funding_rate_history(settle, contract, limit=limit, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_funding_rate_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **_from** | **int**| Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) | [optional] 
 **to** | **int**| Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp | [optional] 

### Return type

[**list[FundingRateRecord]**](FundingRateRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | History retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_insurance_ledger**
> list[InsuranceRecord] list_futures_insurance_ledger(settle, limit=limit)

Futures insurance balance history.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)

try:
    # Futures insurance balance history.
    api_response = api_instance.list_futures_insurance_ledger(settle, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_insurance_ledger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]

### Return type

[**list[InsuranceRecord]**](InsuranceRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contract_stats**
> list[ContractStat] list_contract_stats(settle, contract, _from=_from, interval=interval, limit=limit)

Futures stats.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
_from = 1604561000 # int | Start timestamp. (optional)
interval = '5m' # str |  (optional) (default to '5m')
limit = 30 # int |  (optional) (default to 30)

try:
    # Futures stats.
    api_response = api_instance.list_contract_stats(settle, contract, _from=_from, interval=interval, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_contract_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **_from** | **int**| Start timestamp. | [optional] 
 **interval** | **str**|  | [optional] [default to &#39;5m&#39;]
 **limit** | **int**|  | [optional] [default to 30]

### Return type

[**list[ContractStat]**](ContractStat.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_index_constituents**
> FuturesIndexConstituents get_index_constituents(settle, index)

Get index constituents.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
index = 'BTC_USDT' # str | Index name.

try:
    # Get index constituents.
    api_response = api_instance.get_index_constituents(settle, index)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->get_index_constituents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **index** | **str**| Index name. | 

### Return type

[**FuturesIndexConstituents**](FuturesIndexConstituents.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_liquidated_orders**
> list[FuturesLiqOrder] list_liquidated_orders(settle, contract=contract, _from=_from, to=to, limit=limit)

Retrieve liquidation history.

The time interval between from and to is maximum 3600. Some private fields are not returned by public interfaces, refer to field descriptions for interfaces, refer to field descriptions for details

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)
_from = 1547706332 # int | Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) (optional)
to = 1547706332 # int | Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)

try:
    # Retrieve liquidation history.
    api_response = api_instance.list_liquidated_orders(settle, contract=contract, _from=_from, to=to, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_liquidated_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 
 **_from** | **int**| Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) | [optional] 
 **to** | **int**| Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]

### Return type

[**list[FuturesLiqOrder]**](FuturesLiqOrder.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_risk_limit_tiers**
> list[FuturesLimitRiskTiers] list_futures_risk_limit_tiers(settle, contract=contract, limit=limit, offset=offset)

List risk limit tiers.

When the 'contract' parameter is not passed, the default is to query the risk limits for the top 100 markets.'Limit' and 'offset' correspond to pagination queries at the market level, not to the length of the returned array. This only takes effect empty.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)

try:
    # List risk limit tiers.
    api_response = api_instance.list_futures_risk_limit_tiers(settle, contract=contract, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_risk_limit_tiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]

### Return type

[**list[FuturesLimitRiskTiers]**](FuturesLimitRiskTiers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_accounts**
> FuturesAccount list_futures_accounts(settle)

Query futures account.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.

try:
    # Query futures account.
    api_response = api_instance.list_futures_accounts(settle)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 

### Return type

[**FuturesAccount**](FuturesAccount.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_account_book**
> list[FuturesAccountBook] list_futures_account_book(settle, contract=contract, limit=limit, offset=offset, _from=_from, to=to, type=type)

Query account book.

If the contract field is passed, only records containing this field after 2023-10-30 can be filtered。 2023-10-30 can be filtered.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)
_from = 1547706332 # int | Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) (optional)
to = 1547706332 # int | Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp (optional)
type = 'dnw' # str | Changing Type：  - dnw: Deposit & Withdraw - pnl: Profit & Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding - point_dnw: point_fee: POINT Trading fee - point_refr: POINT Referrer rebate - bonus_offset: bouns deduction (optional)

try:
    # Query account book.
    api_response = api_instance.list_futures_account_book(settle, contract=contract, limit=limit, offset=offset, _from=_from, to=to, type=type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_account_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]
 **_from** | **int**| Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) | [optional] 
 **to** | **int**| Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp | [optional] 
 **type** | **str**| Changing Type：  - dnw: Deposit &amp; Withdraw - pnl: Profit &amp; Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding - point_dnw: point_fee: POINT Trading fee - point_refr: POINT Referrer rebate - bonus_offset: bouns deduction | [optional] 

### Return type

[**list[FuturesAccountBook]**](FuturesAccountBook.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_positions**
> list[Position] list_positions(settle, holding=holding, limit=limit, offset=offset)

List all positions of a user.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
holding = true # bool | Return only real positions - true, return all - false. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)

try:
    # List all positions of a user.
    api_response = api_instance.list_positions(settle, holding=holding, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **holding** | **bool**| Return only real positions - true, return all - false. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]

### Return type

[**list[Position]**](Position.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_position**
> Position get_position(settle, contract)

Get single position.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.

try:
    # Get single position.
    api_response = api_instance.get_position(settle, contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->get_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 

### Return type

[**Position**](Position.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Position information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_margin**
> Position update_position_margin(settle, contract, change)

Update position margin.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
change = '0.01' # str | Margin change amount, positive number increases, negative number.

try:
    # Update position margin.
    api_response = api_instance.update_position_margin(settle, contract, change)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_margin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **change** | **str**| Margin change amount, positive number increases, negative number. | 

### Return type

[**Position**](Position.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Position information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_leverage**
> Position update_position_leverage(settle, contract, leverage, cross_leverage_limit=cross_leverage_limit)

Update position leverage.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
leverage = '10' # str | New position leverage.
cross_leverage_limit = '10' # str | Cross margin leverage(valid only when `leverage` is 0). (optional)

try:
    # Update position leverage.
    api_response = api_instance.update_position_leverage(settle, contract, leverage, cross_leverage_limit=cross_leverage_limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_leverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **leverage** | **str**| New position leverage. | 
 **cross_leverage_limit** | **str**| Cross margin leverage(valid only when &#x60;leverage&#x60; is 0). | [optional] 

### Return type

[**Position**](Position.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Position information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_cross_mode**
> Position update_position_cross_mode(settle, futures_position_cross_mode)

Switch to the full position-by-store mode.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
futures_position_cross_mode = gate_api.FuturesPositionCrossMode() # FuturesPositionCrossMode | 

try:
    # Switch to the full position-by-store mode.
    api_response = api_instance.update_position_cross_mode(settle, futures_position_cross_mode)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_cross_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **futures_position_cross_mode** | [**FuturesPositionCrossMode**](FuturesPositionCrossMode.md)|  | 

### Return type

[**Position**](Position.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Position information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_risk_limit**
> Position update_position_risk_limit(settle, contract, risk_limit)

Update position risk limit.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
risk_limit = '1000000' # str | New Risk Limit Value.

try:
    # Update position risk limit.
    api_response = api_instance.update_position_risk_limit(settle, contract, risk_limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_risk_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **risk_limit** | **str**| New Risk Limit Value. | 

### Return type

[**Position**](Position.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Position information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_dual_mode**
> FuturesAccount set_dual_mode(settle, dual_mode)

Enable or disable dual mode.

The prerequisite for changing mode is that all positions have no holdings.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
dual_mode = true # bool | Whether to enable dual mode.

try:
    # Enable or disable dual mode.
    api_response = api_instance.set_dual_mode(settle, dual_mode)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->set_dual_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **dual_mode** | **bool**| Whether to enable dual mode. | 

### Return type

[**FuturesAccount**](FuturesAccount.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dual_mode_position**
> list[Position] get_dual_mode_position(settle, contract)

Retrieve position detail in dual mode.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.

try:
    # Retrieve position detail in dual mode.
    api_response = api_instance.get_dual_mode_position(settle, contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->get_dual_mode_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 

### Return type

[**list[Position]**](Position.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dual_mode_position_margin**
> list[Position] update_dual_mode_position_margin(settle, contract, change, dual_side)

Update position margin in dual mode.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
change = '0.01' # str | Margin change amount, positive number increases, negative number.
dual_side = 'dual_long' # str | Long or short position.

try:
    # Update position margin in dual mode.
    api_response = api_instance.update_dual_mode_position_margin(settle, contract, change, dual_side)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->update_dual_mode_position_margin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **change** | **str**| Margin change amount, positive number increases, negative number. | 
 **dual_side** | **str**| Long or short position. | 

### Return type

[**list[Position]**](Position.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dual_mode_position_leverage**
> list[Position] update_dual_mode_position_leverage(settle, contract, leverage, cross_leverage_limit=cross_leverage_limit)

Update position leverage in dual mode.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
leverage = '10' # str | New position leverage.
cross_leverage_limit = '10' # str | Cross margin leverage(valid only when `leverage` is 0). (optional)

try:
    # Update position leverage in dual mode.
    api_response = api_instance.update_dual_mode_position_leverage(settle, contract, leverage, cross_leverage_limit=cross_leverage_limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->update_dual_mode_position_leverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **leverage** | **str**| New position leverage. | 
 **cross_leverage_limit** | **str**| Cross margin leverage(valid only when &#x60;leverage&#x60; is 0). | [optional] 

### Return type

[**list[Position]**](Position.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dual_mode_position_risk_limit**
> list[Position] update_dual_mode_position_risk_limit(settle, contract, risk_limit)

Update position risk limit in dual mode.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
risk_limit = '1000000' # str | New Risk Limit Value.

try:
    # Update position risk limit in dual mode.
    api_response = api_instance.update_dual_mode_position_risk_limit(settle, contract, risk_limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->update_dual_mode_position_risk_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **risk_limit** | **str**| New Risk Limit Value. | 

### Return type

[**list[Position]**](Position.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_orders**
> list[FuturesOrder] list_futures_orders(settle, status, contract=contract, limit=limit, offset=offset, last_id=last_id)

List futures orders.

- Zero-fill order cannot be retrieved for 10 minutes after cancellation - Historical orders, by default, only data within the past 6 months is supported.  If you need to query data for a longer period, please use `GET /futures/{settle}/orders_timerange`.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
status = 'open' # str | Only list the orders with this status.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)
last_id = '12345' # str | Specify the currency name to query in batches, and support up to 100 pass parameters at a time. (optional)

try:
    # List futures orders.
    api_response = api_instance.list_futures_orders(settle, status, contract=contract, limit=limit, offset=offset, last_id=last_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **status** | **str**| Only list the orders with this status. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]
 **last_id** | **str**| Specify the currency name to query in batches, and support up to 100 pass parameters at a time. | [optional] 

### Return type

[**list[FuturesOrder]**](FuturesOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  * X-Pagination-Limit - Request limit specified. <br>  * X-Pagination-Offset - Request offset specified. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_futures_order**
> FuturesOrder create_futures_order(settle, futures_order, x_gate_exptime=x_gate_exptime)

Create a futures order.

- When placing an order, the number of contracts is specified `size`, not the number of coins. The number of coins corresponding to each contract is returned in the contract details interface `quanto_multiplier` - 0 The order that was completed cannot be obtained after 10 minutes of withdrawal, and the order will be mentioned that the order does not exist - Setting `reduce_only` to `true` can prevent the position from being penetrated when reducing the position - In single-position mode, if you need to close the position, you need to set `size` to 0 and `close` to `true` - In dual warehouse mode,   - Reduce position: reduce_only=true, size is a positive number that indicates short position, negative number that indicates long position  - Add number that indicates adding long positions, and negative numbers indicate adding short positions  - Close position: size=0, set the direction of closing position according to auto_size, and set `reduce_only` to true  at the same time - reduce_only: Make sure to only perform position reduction operations to prevent increased positions - Set `stp_act` to determine the use of a strategy that restricts user transactions. For detailed usage, refer to the body parameter `stp_act`

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
futures_order = gate_api.FuturesOrder() # FuturesOrder | 
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Create a futures order.
    api_response = api_instance.create_futures_order(settle, futures_order, x_gate_exptime=x_gate_exptime)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->create_futures_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **futures_order** | [**FuturesOrder**](FuturesOrder.md)|  | 
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Order details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_futures_orders**
> list[FuturesOrder] cancel_futures_orders(settle, contract, x_gate_exptime=x_gate_exptime, side=side)

Cancel all `open` orders matched.

Zero-filled order cannot be retrieved 10 minutes after order cancellation.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract.
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)
side = 'ask' # str | Specify all buy orders or all sell orders, both are included if not specified. Set to bid, set to ask to cancel all sell ordersspecified. Set to bid, set to ask to cancel all sell ordersspecified. Set to bid, set to ask to cancel all sell orders (optional)

try:
    # Cancel all `open` orders matched.
    api_response = api_instance.cancel_futures_orders(settle, contract, x_gate_exptime=x_gate_exptime, side=side)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_futures_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract. | 
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 
 **side** | **str**| Specify all buy orders or all sell orders, both are included if not specified. Set to bid, set to ask to cancel all sell ordersspecified. Set to bid, set to ask to cancel all sell ordersspecified. Set to bid, set to ask to cancel all sell orders | [optional] 

### Return type

[**list[FuturesOrder]**](FuturesOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | All orders matched cancelled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_orders_with_time_range**
> list[FuturesOrder] get_orders_with_time_range(settle, contract=contract, _from=_from, to=to, limit=limit, offset=offset)

List Futures Orders By Time Range.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)
_from = 1547706332 # int | Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) (optional)
to = 1547706332 # int | Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)

try:
    # List Futures Orders By Time Range.
    api_response = api_instance.get_orders_with_time_range(settle, contract=contract, _from=_from, to=to, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->get_orders_with_time_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 
 **_from** | **int**| Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) | [optional] 
 **to** | **int**| Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]

### Return type

[**list[FuturesOrder]**](FuturesOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  * X-Pagination-Limit - Request limit specified. <br>  * X-Pagination-Offset - Request offset specified. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_batch_futures_order**
> list[BatchFuturesOrder] create_batch_futures_order(settle, futures_order, x_gate_exptime=x_gate_exptime)

Create a batch of futures orders.

- Up to 10 orders per request - If any of the order's parameters are missing or in the wrong format, all of them will not be executed, and a http status 400 error will be returned directly - If the parameters are checked and passed, all are executed. Even if there is a business logic error in the middle (such as insufficient funds), it will not affect other execution orders - The returned result is in array format, and the order corresponds to the orders in the request body - In the returned result, the `succeeded` field of type bool indicates whether the execution was successful or not - If the execution is successful, the normal order content is included; if the execution fails, the `label` field is included to indicate the cause of the error - In the rate limiting, each order is counted individually

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
futures_order = [gate_api.FuturesOrder()] # list[FuturesOrder] | 
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Create a batch of futures orders.
    api_response = api_instance.create_batch_futures_order(settle, futures_order, x_gate_exptime=x_gate_exptime)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->create_batch_futures_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **futures_order** | [**list[FuturesOrder]**](FuturesOrder.md)|  | 
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

### Return type

[**list[BatchFuturesOrder]**](BatchFuturesOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request is completed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_futures_order**
> FuturesOrder get_futures_order(settle, order_id)

Get a single order.

- Zero-fill order cannot be retrieved for 10 minutes after cancellation - Historical orders, by default, only data within the past 6 months is supported.  

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
order_id = '12345' # str | Order ID returned, or user custom ID(i.e., `text` field). Operations based on custom ID can only be checked when the order is in orderbook. finished, it can be checked within 60 seconds after the end of the order. After that, only order ID is accepted.

try:
    # Get a single order.
    api_response = api_instance.get_futures_order(settle, order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->get_futures_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **order_id** | **str**| Order ID returned, or user custom ID(i.e., &#x60;text&#x60; field). Operations based on custom ID can only be checked when the order is in orderbook. finished, it can be checked within 60 seconds after the end of the order. After that, only order ID is accepted. | 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amend_futures_order**
> FuturesOrder amend_futures_order(settle, order_id, futures_order_amendment, x_gate_exptime=x_gate_exptime)

Amend an order.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
order_id = '12345' # str | Order ID returned, or user custom ID(i.e., `text` field). Operations based on custom ID can only be checked when the order is in orderbook. finished, it can be checked within 60 seconds after the end of the order. After that, only order ID is accepted.
futures_order_amendment = gate_api.FuturesOrderAmendment() # FuturesOrderAmendment | 
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Amend an order.
    api_response = api_instance.amend_futures_order(settle, order_id, futures_order_amendment, x_gate_exptime=x_gate_exptime)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->amend_futures_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **order_id** | **str**| Order ID returned, or user custom ID(i.e., &#x60;text&#x60; field). Operations based on custom ID can only be checked when the order is in orderbook. finished, it can be checked within 60 seconds after the end of the order. After that, only order ID is accepted. | 
 **futures_order_amendment** | [**FuturesOrderAmendment**](FuturesOrderAmendment.md)|  | 
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_futures_order**
> FuturesOrder cancel_futures_order(settle, order_id, x_gate_exptime=x_gate_exptime)

Cancel a single order.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
order_id = '12345' # str | Order ID returned, or user custom ID(i.e., `text` field). Operations based on custom ID can only be checked when the order is in orderbook. finished, it can be checked within 60 seconds after the end of the order. After that, only order ID is accepted.
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Cancel a single order.
    api_response = api_instance.cancel_futures_order(settle, order_id, x_gate_exptime=x_gate_exptime)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_futures_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **order_id** | **str**| Order ID returned, or user custom ID(i.e., &#x60;text&#x60; field). Operations based on custom ID can only be checked when the order is in orderbook. finished, it can be checked within 60 seconds after the end of the order. After that, only order ID is accepted. | 
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order details. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_trades**
> list[MyFuturesTrade] get_my_trades(settle, contract=contract, order=order, limit=limit, offset=offset, last_id=last_id)

List personal trading history.

By default, only data within the past 6 months is supported.  If you need to query data for a longer period, please use `GET /futures/{settle}/my_trades_timerange`.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)
order = 12345 # int | Futures order ID, return related data only if specified. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)
last_id = '12345' # str | Specify the starting point for this list based on a previously retrieved id  This parameter is deprecated. If you need to iterate through and retrieve more records, we recommend using 'GET /futures/{settle}/my_trades_timerange'. (optional)

try:
    # List personal trading history.
    api_response = api_instance.get_my_trades(settle, contract=contract, order=order, limit=limit, offset=offset, last_id=last_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->get_my_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 
 **order** | **int**| Futures order ID, return related data only if specified. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]
 **last_id** | **str**| Specify the starting point for this list based on a previously retrieved id  This parameter is deprecated. If you need to iterate through and retrieve more records, we recommend using &#39;GET /futures/{settle}/my_trades_timerange&#39;. | [optional] 

### Return type

[**list[MyFuturesTrade]**](MyFuturesTrade.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  * X-Pagination-Limit - Request limit specified. <br>  * X-Pagination-Offset - Request offset specified. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_trades_with_time_range**
> list[MyFuturesTradeTimeRange] get_my_trades_with_time_range(settle, contract=contract, _from=_from, to=to, limit=limit, offset=offset, role=role)

List personal trading history by time range.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)
_from = 1547706332 # int | Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) (optional)
to = 1547706332 # int | Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)
role = 'maker' # str | Query role, maker or taker. (optional)

try:
    # List personal trading history by time range.
    api_response = api_instance.get_my_trades_with_time_range(settle, contract=contract, _from=_from, to=to, limit=limit, offset=offset, role=role)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->get_my_trades_with_time_range: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 
 **_from** | **int**| Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) | [optional] 
 **to** | **int**| Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]
 **role** | **str**| Query role, maker or taker. | [optional] 

### Return type

[**list[MyFuturesTradeTimeRange]**](MyFuturesTradeTimeRange.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  * X-Pagination-Limit - Request limit specified. <br>  * X-Pagination-Offset - Request offset specified. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_position_close**
> list[PositionClose] list_position_close(settle, contract=contract, limit=limit, offset=offset, _from=_from, to=to, side=side, pnl=pnl)

List position close history.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)
_from = 1547706332 # int | Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) (optional)
to = 1547706332 # int | Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp (optional)
side = 'short' # str | Query side. long or shot. (optional)
pnl = 'profit' # str | Query profit or loss. (optional)

try:
    # List position close history.
    api_response = api_instance.list_position_close(settle, contract=contract, limit=limit, offset=offset, _from=_from, to=to, side=side, pnl=pnl)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_position_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]
 **_from** | **int**| Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) | [optional] 
 **to** | **int**| Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp | [optional] 
 **side** | **str**| Query side. long or shot. | [optional] 
 **pnl** | **str**| Query profit or loss. | [optional] 

### Return type

[**list[PositionClose]**](PositionClose.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_liquidates**
> list[FuturesLiquidate] list_liquidates(settle, contract=contract, limit=limit, at=at)

List liquidation history.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
at = 0 # int | Specify a liquidation timestamp. (optional) (default to 0)

try:
    # List liquidation history.
    api_response = api_instance.list_liquidates(settle, contract=contract, limit=limit, at=at)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_liquidates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **at** | **int**| Specify a liquidation timestamp. | [optional] [default to 0]

### Return type

[**list[FuturesLiquidate]**](FuturesLiquidate.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_auto_deleverages**
> list[FuturesAutoDeleverage] list_auto_deleverages(settle, contract=contract, limit=limit, at=at)

List Auto-Deleveraging History.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
at = 0 # int | Specify an auto-deleveraging timestamp. (optional) (default to 0)

try:
    # List Auto-Deleveraging History.
    api_response = api_instance.list_auto_deleverages(settle, contract=contract, limit=limit, at=at)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_auto_deleverages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **at** | **int**| Specify an auto-deleveraging timestamp. | [optional] [default to 0]

### Return type

[**list[FuturesAutoDeleverage]**](FuturesAutoDeleverage.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **countdown_cancel_all_futures**
> TriggerTime countdown_cancel_all_futures(settle, countdown_cancel_all_futures_task)

Countdown cancel orders.

Heartbeat detection for contract orders: When the user-set `timeout` time is reached, if neither the existing countdown is canceled nor a new countdown is set, the relevant contract orders will be automatically canceled. This API can be called repeatedly to or cancel the countdown. Usage example: Repeatedly call this API at 30-second intervals, setting the `timeout` to 30 (seconds) each time. If this API is not called again within 30 seconds, all open orders on your specified `market` will be automatically canceled. If the `timeout` is set to 0 within 30 seconds, the countdown timer will terminate, and the automatic order cancellation function will be disabled.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
countdown_cancel_all_futures_task = gate_api.CountdownCancelAllFuturesTask() # CountdownCancelAllFuturesTask | 

try:
    # Countdown cancel orders.
    api_response = api_instance.countdown_cancel_all_futures(settle, countdown_cancel_all_futures_task)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->countdown_cancel_all_futures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **countdown_cancel_all_futures_task** | [**CountdownCancelAllFuturesTask**](CountdownCancelAllFuturesTask.md)|  | 

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
**200** | Set countdown successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_futures_fee**
> dict(str, FuturesFee) get_futures_fee(settle, contract=contract)

Query user trading fee rates.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)

try:
    # Query user trading fee rates.
    api_response = api_instance.get_futures_fee(settle, contract=contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->get_futures_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 

### Return type

[**dict(str, FuturesFee)**](FuturesFee.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_batch_future_orders**
> list[FutureCancelOrderResult] cancel_batch_future_orders(settle, request_body, x_gate_exptime=x_gate_exptime)

Cancel a batch of orders with an ID list.

Multiple different order IDs can be specified. A maximum of 20 records.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
request_body = ['request_body_example'] # list[str] | 
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Cancel a batch of orders with an ID list.
    api_response = api_instance.cancel_batch_future_orders(settle, request_body, x_gate_exptime=x_gate_exptime)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_batch_future_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **request_body** | [**list[str]**](str.md)|  | 
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

### Return type

[**list[FutureCancelOrderResult]**](FutureCancelOrderResult.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order cancellation operation completed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **amend_batch_future_orders**
> list[BatchFuturesOrder] amend_batch_future_orders(settle, batch_amend_order_req, x_gate_exptime=x_gate_exptime)

Batch modify orders with specified IDs.

Multiple different order IDs can be specified. A maximum of 10 orders can.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
batch_amend_order_req = [gate_api.BatchAmendOrderReq()] # list[BatchAmendOrderReq] | 
x_gate_exptime = '1689560679123' # str | Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected (optional)

try:
    # Batch modify orders with specified IDs.
    api_response = api_instance.amend_batch_future_orders(settle, batch_amend_order_req, x_gate_exptime=x_gate_exptime)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->amend_batch_future_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **batch_amend_order_req** | [**list[BatchAmendOrderReq]**](BatchAmendOrderReq.md)|  | 
 **x_gate_exptime** | **str**| Specify the expiration time (milliseconds); if the GATE receives the request time greater than the expiration time, the request will be rejected | [optional] 

### Return type

[**list[BatchFuturesOrder]**](BatchFuturesOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request is completed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_futures_risk_limit_table**
> list[FuturesRiskLimitTier] get_futures_risk_limit_table(settle, table_id)

Query risk limit table by table_id.

Just pass table_id.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
table_id = 'CYBER_USDT_20241122' # str | Risk limit table ID.

try:
    # Query risk limit table by table_id.
    api_response = api_instance.get_futures_risk_limit_table(settle, table_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->get_futures_risk_limit_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **table_id** | **str**| Risk limit table ID. | 

### Return type

[**list[FuturesRiskLimitTier]**](FuturesRiskLimitTier.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_price_triggered_orders**
> list[FuturesPriceTriggeredOrder] list_price_triggered_orders(settle, status, contract=contract, limit=limit, offset=offset)

List All Price-triggered Orders.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
status = 'status_example' # str | Only list the orders with this status.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)

try:
    # List All Price-triggered Orders.
    api_response = api_instance.list_price_triggered_orders(settle, status, contract=contract, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_price_triggered_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **status** | **str**| Only list the orders with this status. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]

### Return type

[**list[FuturesPriceTriggeredOrder]**](FuturesPriceTriggeredOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_price_triggered_order**
> TriggerOrderResponse create_price_triggered_order(settle, futures_price_triggered_order)

Create a price-triggered order.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
futures_price_triggered_order = gate_api.FuturesPriceTriggeredOrder() # FuturesPriceTriggeredOrder | 

try:
    # Create a price-triggered order.
    api_response = api_instance.create_price_triggered_order(settle, futures_price_triggered_order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->create_price_triggered_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **futures_price_triggered_order** | [**FuturesPriceTriggeredOrder**](FuturesPriceTriggeredOrder.md)|  | 

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
**201** | Order created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_price_triggered_order_list**
> list[FuturesPriceTriggeredOrder] cancel_price_triggered_order_list(settle, contract=contract)

Cancel All Price-triggered Orders.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified. (optional)

try:
    # Cancel All Price-triggered Orders.
    api_response = api_instance.cancel_price_triggered_order_list(settle, contract=contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_price_triggered_order_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **contract** | **str**| Futures contract, return related data only if specified. | [optional] 

### Return type

[**list[FuturesPriceTriggeredOrder]**](FuturesPriceTriggeredOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Batch cancellation request accepted. Query order status by listing orders. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_triggered_order**
> FuturesPriceTriggeredOrder get_price_triggered_order(settle, order_id)

Get a price-triggered order.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
order_id = 'order_id_example' # str | Retrieve the data of the order with the specified ID.

try:
    # Get a price-triggered order.
    api_response = api_instance.get_price_triggered_order(settle, order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->get_price_triggered_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **order_id** | **str**| Retrieve the data of the order with the specified ID. | 

### Return type

[**FuturesPriceTriggeredOrder**](FuturesPriceTriggeredOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auto order detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_price_triggered_order**
> FuturesPriceTriggeredOrder cancel_price_triggered_order(settle, order_id)

cancel a price-triggered order.

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency.
order_id = 'order_id_example' # str | Retrieve the data of the order with the specified ID.

try:
    # cancel a price-triggered order.
    api_response = api_instance.cancel_price_triggered_order(settle, order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_price_triggered_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency. | 
 **order_id** | **str**| Retrieve the data of the order with the specified ID. | 

### Return type

[**FuturesPriceTriggeredOrder**](FuturesPriceTriggeredOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Auto order detail. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

