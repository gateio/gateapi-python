# gate_api.DeliveryApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_delivery_contracts**](DeliveryApi.md#list_delivery_contracts) | **GET** /delivery/{settle}/contracts | Query all futures contracts
[**get_delivery_contract**](DeliveryApi.md#get_delivery_contract) | **GET** /delivery/{settle}/contracts/{contract} | Query single contract information
[**list_delivery_order_book**](DeliveryApi.md#list_delivery_order_book) | **GET** /delivery/{settle}/order_book | Query futures market depth information
[**list_delivery_trades**](DeliveryApi.md#list_delivery_trades) | **GET** /delivery/{settle}/trades | Futures market transaction records
[**list_delivery_candlesticks**](DeliveryApi.md#list_delivery_candlesticks) | **GET** /delivery/{settle}/candlesticks | Futures market K-line chart
[**list_delivery_tickers**](DeliveryApi.md#list_delivery_tickers) | **GET** /delivery/{settle}/tickers | Get all futures trading statistics
[**list_delivery_insurance_ledger**](DeliveryApi.md#list_delivery_insurance_ledger) | **GET** /delivery/{settle}/insurance | Futures market insurance fund history
[**list_delivery_accounts**](DeliveryApi.md#list_delivery_accounts) | **GET** /delivery/{settle}/accounts | Get futures account
[**list_delivery_account_book**](DeliveryApi.md#list_delivery_account_book) | **GET** /delivery/{settle}/account_book | Query futures account change history
[**list_delivery_positions**](DeliveryApi.md#list_delivery_positions) | **GET** /delivery/{settle}/positions | Get user position list
[**get_delivery_position**](DeliveryApi.md#get_delivery_position) | **GET** /delivery/{settle}/positions/{contract} | Get single position information
[**update_delivery_position_margin**](DeliveryApi.md#update_delivery_position_margin) | **POST** /delivery/{settle}/positions/{contract}/margin | Update position margin
[**update_delivery_position_leverage**](DeliveryApi.md#update_delivery_position_leverage) | **POST** /delivery/{settle}/positions/{contract}/leverage | Update position leverage
[**update_delivery_position_risk_limit**](DeliveryApi.md#update_delivery_position_risk_limit) | **POST** /delivery/{settle}/positions/{contract}/risk_limit | Update position risk limit
[**list_delivery_orders**](DeliveryApi.md#list_delivery_orders) | **GET** /delivery/{settle}/orders | Query futures order list
[**create_delivery_order**](DeliveryApi.md#create_delivery_order) | **POST** /delivery/{settle}/orders | Place futures order
[**cancel_delivery_orders**](DeliveryApi.md#cancel_delivery_orders) | **DELETE** /delivery/{settle}/orders | Cancel all orders with &#39;open&#39; status
[**get_delivery_order**](DeliveryApi.md#get_delivery_order) | **GET** /delivery/{settle}/orders/{order_id} | Query single order details
[**cancel_delivery_order**](DeliveryApi.md#cancel_delivery_order) | **DELETE** /delivery/{settle}/orders/{order_id} | Cancel single order
[**get_my_delivery_trades**](DeliveryApi.md#get_my_delivery_trades) | **GET** /delivery/{settle}/my_trades | Query personal trading records
[**list_delivery_position_close**](DeliveryApi.md#list_delivery_position_close) | **GET** /delivery/{settle}/position_close | Query position close history
[**list_delivery_liquidates**](DeliveryApi.md#list_delivery_liquidates) | **GET** /delivery/{settle}/liquidates | Query liquidation history
[**list_delivery_settlements**](DeliveryApi.md#list_delivery_settlements) | **GET** /delivery/{settle}/settlements | Query settlement records
[**list_delivery_risk_limit_tiers**](DeliveryApi.md#list_delivery_risk_limit_tiers) | **GET** /delivery/{settle}/risk_limit_tiers | Query risk limit tiers
[**list_price_triggered_delivery_orders**](DeliveryApi.md#list_price_triggered_delivery_orders) | **GET** /delivery/{settle}/price_orders | Query auto order list
[**create_price_triggered_delivery_order**](DeliveryApi.md#create_price_triggered_delivery_order) | **POST** /delivery/{settle}/price_orders | Create price-triggered order
[**cancel_price_triggered_delivery_order_list**](DeliveryApi.md#cancel_price_triggered_delivery_order_list) | **DELETE** /delivery/{settle}/price_orders | Cancel all auto orders
[**get_price_triggered_delivery_order**](DeliveryApi.md#get_price_triggered_delivery_order) | **GET** /delivery/{settle}/price_orders/{order_id} | Query single auto order details
[**cancel_price_triggered_delivery_order**](DeliveryApi.md#cancel_price_triggered_delivery_order) | **DELETE** /delivery/{settle}/price_orders/{order_id} | Cancel single auto order


# **list_delivery_contracts**
> list[DeliveryContract] list_delivery_contracts(settle)

Query all futures contracts

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency

try:
    # Query all futures contracts
    api_response = api_instance.list_delivery_contracts(settle)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 

### Return type

[**list[DeliveryContract]**](DeliveryContract.md)

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

# **get_delivery_contract**
> DeliveryContract get_delivery_contract(settle, contract)

Query single contract information

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract

try:
    # Query single contract information
    api_response = api_instance.get_delivery_contract(settle, contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->get_delivery_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 

### Return type

[**DeliveryContract**](DeliveryContract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Contract information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_order_book**
> FuturesOrderBook list_delivery_order_book(settle, contract, interval=interval, limit=limit, with_id=with_id)

Query futures market depth information

Bids will be sorted by price from high to low, while asks sorted reversely

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract
interval = '0' # str | Price precision for depth aggregation, 0 means no aggregation, defaults to 0 if not specified (optional) (default to '0')
limit = 10 # int | Number of depth levels (optional) (default to 10)
with_id = False # bool | Whether to return depth update ID. This ID increments by 1 each time depth changes (optional) (default to False)

try:
    # Query futures market depth information
    api_response = api_instance.list_delivery_order_book(settle, contract, interval=interval, limit=limit, with_id=with_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_order_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **interval** | **str**| Price precision for depth aggregation, 0 means no aggregation, defaults to 0 if not specified | [optional] [default to &#39;0&#39;]
 **limit** | **int**| Number of depth levels | [optional] [default to 10]
 **with_id** | **bool**| Whether to return depth update ID. This ID increments by 1 each time depth changes | [optional] [default to False]

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
**200** | Depth query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_trades**
> list[FuturesTrade] list_delivery_trades(settle, contract, limit=limit, last_id=last_id, _from=_from, to=to)

Futures market transaction records

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
last_id = '12345' # str | 以上个列表的最后一条记录的 ID 作为下个列表的起点。 该字段不再继续支持，新的请求请使用 `from` 和 `to` 字段来限定时间范围 (optional)
_from = 1546905600 # int | Specify starting time in Unix seconds. If not specified, `to` and `limit` will be used to limit response items. If items between `from` and `to` are more than `limit`, only `limit` number will be returned.  (optional)
to = 1546935600 # int | Specify end time in Unix seconds, default to current time. (optional)

try:
    # Futures market transaction records
    api_response = api_instance.list_delivery_trades(settle, contract, limit=limit, last_id=last_id, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **last_id** | **str**| 以上个列表的最后一条记录的 ID 作为下个列表的起点。 该字段不再继续支持，新的请求请使用 &#x60;from&#x60; 和 &#x60;to&#x60; 字段来限定时间范围 | [optional] 
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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_candlesticks**
> list[DeliveryCandlestick] list_delivery_candlesticks(settle, contract, _from=_from, to=to, limit=limit, interval=interval)

Futures market K-line chart

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract
_from = 1546905600 # int | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to`to - 100 * interval` if not specified (optional)
to = 1546935600 # int | Specify the end time of the K-line chart, defaults to current time if not specified, note that the time format is Unix timestamp with second precision (optional)
limit = 100 # int | Maximum number of recent data points to return. `limit` conflicts with `from` and `to`. If either `from` or `to` is specified, request will be rejected. (optional) (default to 100)
interval = '5m' # str | Time interval between data points, note that 1w represents a natural week, 7d time is aligned with Unix initial timeTime interval between data points, note that 1w represents a natural week, 7d time is aligned with Unix initial timeweek, 7d time is aligned with Unix initial time (optional) (default to '5m')

try:
    # Futures market K-line chart
    api_response = api_instance.list_delivery_candlesticks(settle, contract, _from=_from, to=to, limit=limit, interval=interval)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_candlesticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **_from** | **int**| Start time of candlesticks, formatted in Unix timestamp in seconds. Default to&#x60;to - 100 * interval&#x60; if not specified | [optional] 
 **to** | **int**| Specify the end time of the K-line chart, defaults to current time if not specified, note that the time format is Unix timestamp with second precision | [optional] 
 **limit** | **int**| Maximum number of recent data points to return. &#x60;limit&#x60; conflicts with &#x60;from&#x60; and &#x60;to&#x60;. If either &#x60;from&#x60; or &#x60;to&#x60; is specified, request will be rejected. | [optional] [default to 100]
 **interval** | **str**| Time interval between data points, note that 1w represents a natural week, 7d time is aligned with Unix initial timeTime interval between data points, note that 1w represents a natural week, 7d time is aligned with Unix initial timeweek, 7d time is aligned with Unix initial time | [optional] [default to &#39;5m&#39;]

### Return type

[**list[DeliveryCandlestick]**](DeliveryCandlestick.md)

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

# **list_delivery_tickers**
> list[DeliveryTicker] list_delivery_tickers(settle, contract=contract)

Get all futures trading statistics

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract (optional)

try:
    # Get all futures trading statistics
    api_response = api_instance.list_delivery_tickers(settle, contract=contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | [optional] 

### Return type

[**list[DeliveryTicker]**](DeliveryTicker.md)

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

# **list_delivery_insurance_ledger**
> list[InsuranceRecord] list_delivery_insurance_ledger(settle, limit=limit)

Futures market insurance fund history

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)

try:
    # Futures market insurance fund history
    api_response = api_instance.list_delivery_insurance_ledger(settle, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_insurance_ledger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_accounts**
> FuturesAccount list_delivery_accounts(settle)

Get futures account

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency

try:
    # Get futures account
    api_response = api_instance.list_delivery_accounts(settle)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 

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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_account_book**
> list[FuturesAccountBook] list_delivery_account_book(settle, limit=limit, _from=_from, to=to, type=type)

Query futures account change history

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
_from = 1547706332 # int | Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) (optional)
to = 1547706332 # int | Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp (optional)
type = 'dnw' # str | Changing Type: - dnw: Deposit & Withdraw - pnl: Profit & Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding - point_dnw: point_fee: POINT Trading fee - point_refr: POINT Referrer rebate (optional)

try:
    # Query futures account change history
    api_response = api_instance.list_delivery_account_book(settle, limit=limit, _from=_from, to=to, type=type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_account_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **_from** | **int**| Start timestamp  Specify start time, time format is Unix timestamp. If not specified, it defaults to (the data start time of the time range actually returned by to and limit) | [optional] 
 **to** | **int**| Termination Timestamp  Specify the end time. If not specified, it defaults to the current time, and the time format is a Unix timestamp | [optional] 
 **type** | **str**| Changing Type: - dnw: Deposit &amp; Withdraw - pnl: Profit &amp; Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding - point_dnw: point_fee: POINT Trading fee - point_refr: POINT Referrer rebate | [optional] 

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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_positions**
> list[Position] list_delivery_positions(settle)

Get user position list

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency

try:
    # Get user position list
    api_response = api_instance.list_delivery_positions(settle)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 

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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delivery_position**
> Position get_delivery_position(settle, contract)

Get single position information

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract

try:
    # Get single position information
    api_response = api_instance.get_delivery_position(settle, contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->get_delivery_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 

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
**200** | Position information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_delivery_position_margin**
> Position update_delivery_position_margin(settle, contract, change)

Update position margin

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract
change = '0.01' # str | Margin change amount, positive number increases, negative number decreases

try:
    # Update position margin
    api_response = api_instance.update_delivery_position_margin(settle, contract, change)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->update_delivery_position_margin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **change** | **str**| Margin change amount, positive number increases, negative number decreases | 

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
**200** | Position information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_delivery_position_leverage**
> Position update_delivery_position_leverage(settle, contract, leverage)

Update position leverage

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract
leverage = '10' # str | New position leverage

try:
    # Update position leverage
    api_response = api_instance.update_delivery_position_leverage(settle, contract, leverage)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->update_delivery_position_leverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **leverage** | **str**| New position leverage | 

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
**200** | Position information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_delivery_position_risk_limit**
> Position update_delivery_position_risk_limit(settle, contract, risk_limit)

Update position risk limit

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract
risk_limit = '10' # str | New position risk limit

try:
    # Update position risk limit
    api_response = api_instance.update_delivery_position_risk_limit(settle, contract, risk_limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->update_delivery_position_risk_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **risk_limit** | **str**| New position risk limit | 

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
**200** | Position information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_orders**
> list[FuturesOrder] list_delivery_orders(settle, status, contract=contract, limit=limit, offset=offset, last_id=last_id, count_total=count_total)

Query futures order list

Zero-fill orders cannot be retrieved 10 minutes after order cancellation

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
status = 'open' # str | Query order list based on status
contract = 'BTC_USDT_20200814' # str | Futures contract (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
last_id = '12345' # str | Specify the currency name to query in batches, and support up to 100 pass parameters at a time (optional)
count_total = 0 # int | Whether to return total number matched, defaults to 0 (no return) (optional) (default to 0)

try:
    # Query futures order list
    api_response = api_instance.list_delivery_orders(settle, status, contract=contract, limit=limit, offset=offset, last_id=last_id, count_total=count_total)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **status** | **str**| Query order list based on status | 
 **contract** | **str**| Futures contract | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **last_id** | **str**| Specify the currency name to query in batches, and support up to 100 pass parameters at a time | [optional] 
 **count_total** | **int**| Whether to return total number matched, defaults to 0 (no return) | [optional] [default to 0]

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
**200** | List retrieved successfully |  * X-Pagination-Limit - Limit specified for pagination <br>  * X-Pagination-Offset - Offset specified for pagination <br>  * X-Pagination-Total - Total number matched, only returned if &#x60;count_total&#x60; is set to 1 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_delivery_order**
> FuturesOrder create_delivery_order(settle, futures_order)

Place futures order

Zero-fill orders cannot be retrieved 10 minutes after order cancellation

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
futures_order = gate_api.FuturesOrder() # FuturesOrder | 

try:
    # Place futures order
    api_response = api_instance.create_delivery_order(settle, futures_order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->create_delivery_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **futures_order** | [**FuturesOrder**](FuturesOrder.md)|  | 

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
**201** | Order details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_delivery_orders**
> list[FuturesOrder] cancel_delivery_orders(settle, contract, side=side)

Cancel all orders with 'open' status

Zero-fill orders cannot be retrieved 10 minutes after order cancellation

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract
side = 'ask' # str | Specify all bids or all asks, both included if not specified (optional)

try:
    # Cancel all orders with 'open' status
    api_response = api_instance.cancel_delivery_orders(settle, contract, side=side)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->cancel_delivery_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **side** | **str**| Specify all bids or all asks, both included if not specified | [optional] 

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
**200** | Batch cancellation successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delivery_order**
> FuturesOrder get_delivery_order(settle, order_id)

Query single order details

Zero-fill orders cannot be retrieved 10 minutes after order cancellation

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
order_id = '12345' # str | ID returned when order is successfully created

try:
    # Query single order details
    api_response = api_instance.get_delivery_order(settle, order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->get_delivery_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **order_id** | **str**| ID returned when order is successfully created | 

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
**200** | Order details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_delivery_order**
> FuturesOrder cancel_delivery_order(settle, order_id)

Cancel single order

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
order_id = '12345' # str | ID returned when order is successfully created

try:
    # Cancel single order
    api_response = api_instance.cancel_delivery_order(settle, order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->cancel_delivery_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **order_id** | **str**| ID returned when order is successfully created | 

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
**200** | Order details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_delivery_trades**
> list[MyFuturesTrade] get_my_delivery_trades(settle, contract=contract, order=order, limit=limit, offset=offset, last_id=last_id, count_total=count_total)

Query personal trading records

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract (optional)
order = 12345 # int | Futures order ID, return related data only if specified (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
last_id = '12345' # str | Specify the currency name to query in batches, and support up to 100 pass parameters at a time (optional)
count_total = 0 # int | Whether to return total number matched, defaults to 0 (no return) (optional) (default to 0)

try:
    # Query personal trading records
    api_response = api_instance.get_my_delivery_trades(settle, contract=contract, order=order, limit=limit, offset=offset, last_id=last_id, count_total=count_total)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->get_my_delivery_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | [optional] 
 **order** | **int**| Futures order ID, return related data only if specified | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **last_id** | **str**| Specify the currency name to query in batches, and support up to 100 pass parameters at a time | [optional] 
 **count_total** | **int**| Whether to return total number matched, defaults to 0 (no return) | [optional] [default to 0]

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
**200** | List retrieved successfully |  * X-Pagination-Limit - Limit specified for pagination <br>  * X-Pagination-Offset - Offset specified for pagination <br>  * X-Pagination-Total - Total number matched, only returned if &#x60;count_total&#x60; is set to 1 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_position_close**
> list[PositionClose] list_delivery_position_close(settle, contract=contract, limit=limit)

Query position close history

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)

try:
    # Query position close history
    api_response = api_instance.list_delivery_position_close(settle, contract=contract, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_position_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]

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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_liquidates**
> list[FuturesLiquidate] list_delivery_liquidates(settle, contract=contract, limit=limit, at=at)

Query liquidation history

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
at = 0 # int | Specify liquidation timestamp (optional) (default to 0)

try:
    # Query liquidation history
    api_response = api_instance.list_delivery_liquidates(settle, contract=contract, limit=limit, at=at)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_liquidates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **at** | **int**| Specify liquidation timestamp | [optional] [default to 0]

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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_delivery_settlements**
> list[DeliverySettlement] list_delivery_settlements(settle, contract=contract, limit=limit, at=at)

Query settlement records

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
at = 0 # int | Specify settlement timestamp (optional) (default to 0)

try:
    # Query settlement records
    api_response = api_instance.list_delivery_settlements(settle, contract=contract, limit=limit, at=at)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_settlements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **at** | **int**| Specify settlement timestamp | [optional] [default to 0]

### Return type

[**list[DeliverySettlement]**](DeliverySettlement.md)

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

# **list_delivery_risk_limit_tiers**
> list[FuturesLimitRiskTiers] list_delivery_risk_limit_tiers(settle, contract=contract, limit=limit, offset=offset)

Query risk limit tiers

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT_20200814' # str | Futures contract (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Query risk limit tiers
    api_response = api_instance.list_delivery_risk_limit_tiers(settle, contract=contract, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_delivery_risk_limit_tiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_price_triggered_delivery_orders**
> list[FuturesPriceTriggeredOrder] list_price_triggered_delivery_orders(settle, status, contract=contract, limit=limit, offset=offset)

Query auto order list

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
status = 'status_example' # str | Query order list based on status
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Query auto order list
    api_response = api_instance.list_price_triggered_delivery_orders(settle, status, contract=contract, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->list_price_triggered_delivery_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **status** | **str**| Query order list based on status | 
 **contract** | **str**| Futures contract, return related data only if specified | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_price_triggered_delivery_order**
> TriggerOrderResponse create_price_triggered_delivery_order(settle, futures_price_triggered_order)

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
futures_price_triggered_order = gate_api.FuturesPriceTriggeredOrder() # FuturesPriceTriggeredOrder | 

try:
    # Create price-triggered order
    api_response = api_instance.create_price_triggered_delivery_order(settle, futures_price_triggered_order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->create_price_triggered_delivery_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
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
**201** | Order created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_price_triggered_delivery_order_list**
> list[FuturesPriceTriggeredOrder] cancel_price_triggered_delivery_order_list(settle, contract)

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract

try:
    # Cancel all auto orders
    api_response = api_instance.cancel_price_triggered_delivery_order_list(settle, contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->cancel_price_triggered_delivery_order_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 

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
**200** | Batch cancellation request accepted and processed, success determined by order list |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_triggered_delivery_order**
> FuturesPriceTriggeredOrder get_price_triggered_delivery_order(settle, order_id)

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
order_id = 'order_id_example' # str | ID returned when order is successfully created

try:
    # Query single auto order details
    api_response = api_instance.get_price_triggered_delivery_order(settle, order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->get_price_triggered_delivery_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **order_id** | **str**| ID returned when order is successfully created | 

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
**200** | Auto order details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_price_triggered_delivery_order**
> FuturesPriceTriggeredOrder cancel_price_triggered_delivery_order(settle, order_id)

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
api_instance = gate_api.DeliveryApi(api_client)
settle = 'usdt' # str | Settle currency
order_id = 'order_id_example' # str | ID returned when order is successfully created

try:
    # Cancel single auto order
    api_response = api_instance.cancel_price_triggered_delivery_order(settle, order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling DeliveryApi->cancel_price_triggered_delivery_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **order_id** | **str**| ID returned when order is successfully created | 

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
**200** | Auto order details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

