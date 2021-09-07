# gate_api.FuturesApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_futures_contracts**](FuturesApi.md#list_futures_contracts) | **GET** /futures/{settle}/contracts | List all futures contracts
[**get_futures_contract**](FuturesApi.md#get_futures_contract) | **GET** /futures/{settle}/contracts/{contract} | Get a single contract
[**list_futures_order_book**](FuturesApi.md#list_futures_order_book) | **GET** /futures/{settle}/order_book | Futures order book
[**list_futures_trades**](FuturesApi.md#list_futures_trades) | **GET** /futures/{settle}/trades | Futures trading history
[**list_futures_candlesticks**](FuturesApi.md#list_futures_candlesticks) | **GET** /futures/{settle}/candlesticks | Get futures candlesticks
[**list_futures_tickers**](FuturesApi.md#list_futures_tickers) | **GET** /futures/{settle}/tickers | List futures tickers
[**list_futures_funding_rate_history**](FuturesApi.md#list_futures_funding_rate_history) | **GET** /futures/{settle}/funding_rate | Funding rate history
[**list_futures_insurance_ledger**](FuturesApi.md#list_futures_insurance_ledger) | **GET** /futures/{settle}/insurance | Futures insurance balance history
[**list_contract_stats**](FuturesApi.md#list_contract_stats) | **GET** /futures/{settle}/contract_stats | Futures stats
[**list_liquidated_orders**](FuturesApi.md#list_liquidated_orders) | **GET** /futures/{settle}/liq_orders | Retrieve liquidation history
[**list_futures_accounts**](FuturesApi.md#list_futures_accounts) | **GET** /futures/{settle}/accounts | Query futures account
[**list_futures_account_book**](FuturesApi.md#list_futures_account_book) | **GET** /futures/{settle}/account_book | Query account book
[**list_positions**](FuturesApi.md#list_positions) | **GET** /futures/{settle}/positions | List all positions of a user
[**get_position**](FuturesApi.md#get_position) | **GET** /futures/{settle}/positions/{contract} | Get single position
[**update_position_margin**](FuturesApi.md#update_position_margin) | **POST** /futures/{settle}/positions/{contract}/margin | Update position margin
[**update_position_leverage**](FuturesApi.md#update_position_leverage) | **POST** /futures/{settle}/positions/{contract}/leverage | Update position leverage
[**update_position_risk_limit**](FuturesApi.md#update_position_risk_limit) | **POST** /futures/{settle}/positions/{contract}/risk_limit | Update position risk limit
[**set_dual_mode**](FuturesApi.md#set_dual_mode) | **POST** /futures/{settle}/dual_mode | Enable or disable dual mode
[**get_dual_mode_position**](FuturesApi.md#get_dual_mode_position) | **GET** /futures/{settle}/dual_comp/positions/{contract} | Retrieve position detail in dual mode
[**update_dual_mode_position_margin**](FuturesApi.md#update_dual_mode_position_margin) | **POST** /futures/{settle}/dual_comp/positions/{contract}/margin | Update position margin in dual mode
[**update_dual_mode_position_leverage**](FuturesApi.md#update_dual_mode_position_leverage) | **POST** /futures/{settle}/dual_comp/positions/{contract}/leverage | Update position leverage in dual mode
[**update_dual_mode_position_risk_limit**](FuturesApi.md#update_dual_mode_position_risk_limit) | **POST** /futures/{settle}/dual_comp/positions/{contract}/risk_limit | Update position risk limit in dual mode
[**list_futures_orders**](FuturesApi.md#list_futures_orders) | **GET** /futures/{settle}/orders | List futures orders
[**create_futures_order**](FuturesApi.md#create_futures_order) | **POST** /futures/{settle}/orders | Create a futures order
[**cancel_futures_orders**](FuturesApi.md#cancel_futures_orders) | **DELETE** /futures/{settle}/orders | Cancel all &#x60;open&#x60; orders matched
[**get_futures_order**](FuturesApi.md#get_futures_order) | **GET** /futures/{settle}/orders/{order_id} | Get a single order
[**cancel_futures_order**](FuturesApi.md#cancel_futures_order) | **DELETE** /futures/{settle}/orders/{order_id} | Cancel a single order
[**get_my_trades**](FuturesApi.md#get_my_trades) | **GET** /futures/{settle}/my_trades | List personal trading history
[**list_position_close**](FuturesApi.md#list_position_close) | **GET** /futures/{settle}/position_close | List position close history
[**list_liquidates**](FuturesApi.md#list_liquidates) | **GET** /futures/{settle}/liquidates | List liquidation history
[**list_price_triggered_orders**](FuturesApi.md#list_price_triggered_orders) | **GET** /futures/{settle}/price_orders | List all auto orders
[**create_price_triggered_order**](FuturesApi.md#create_price_triggered_order) | **POST** /futures/{settle}/price_orders | Create a price-triggered order
[**cancel_price_triggered_order_list**](FuturesApi.md#cancel_price_triggered_order_list) | **DELETE** /futures/{settle}/price_orders | Cancel all open orders
[**get_price_triggered_order**](FuturesApi.md#get_price_triggered_order) | **GET** /futures/{settle}/price_orders/{order_id} | Get a single order
[**cancel_price_triggered_order**](FuturesApi.md#cancel_price_triggered_order) | **DELETE** /futures/{settle}/price_orders/{order_id} | Cancel a single order


# **list_futures_contracts**
> list[Contract] list_futures_contracts(settle)

List all futures contracts

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
settle = 'usdt' # str | Settle currency

try:
    # List all futures contracts
    api_response = api_instance.list_futures_contracts(settle)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 

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
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_futures_contract**
> Contract get_futures_contract(settle, contract)

Get a single contract

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract

try:
    # Get a single contract
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
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 

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
**200** | Contract information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_order_book**
> FuturesOrderBook list_futures_order_book(settle, contract, interval=interval, limit=limit, with_id=with_id)

Futures order book

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
interval = '0' # str | Order depth. 0 means no aggregation is applied. default to 0 (optional) (default to '0')
limit = 10 # int | Maximum number of order depth data in asks or bids (optional) (default to 10)
with_id = False # bool | Whether the order book update ID will be returned. This ID increases by 1 on every order book update (optional) (default to False)

try:
    # Futures order book
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
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **interval** | **str**| Order depth. 0 means no aggregation is applied. default to 0 | [optional] [default to &#39;0&#39;]
 **limit** | **int**| Maximum number of order depth data in asks or bids | [optional] [default to 10]
 **with_id** | **bool**| Whether the order book update ID will be returned. This ID increases by 1 on every order book update | [optional] [default to False]

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
**200** | Order book retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_trades**
> list[FuturesTrade] list_futures_trades(settle, contract, limit=limit, last_id=last_id, _from=_from, to=to)

Futures trading history

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
last_id = '12345' # str | Specify the starting point for this list based on a previously retrieved id  This parameter is deprecated. Use `from` and `to` instead to limit time range (optional)
_from = 1546905600 # int | Specify starting time in Unix seconds. If not specified, `to` and `limit` will be used to limit response items. If items between `from` and `to` are more than `limit`, only `limit` number will be returned.  (optional)
to = 1546935600 # int | Specify end time in Unix seconds, default to current time (optional)

try:
    # Futures trading history
    api_response = api_instance.list_futures_trades(settle, contract, limit=limit, last_id=last_id, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **last_id** | **str**| Specify the starting point for this list based on a previously retrieved id  This parameter is deprecated. Use &#x60;from&#x60; and &#x60;to&#x60; instead to limit time range | [optional] 
 **_from** | **int**| Specify starting time in Unix seconds. If not specified, &#x60;to&#x60; and &#x60;limit&#x60; will be used to limit response items. If items between &#x60;from&#x60; and &#x60;to&#x60; are more than &#x60;limit&#x60;, only &#x60;limit&#x60; number will be returned.  | [optional] 
 **to** | **int**| Specify end time in Unix seconds, default to current time | [optional] 

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
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_candlesticks**
> list[FuturesCandlestick] list_futures_candlesticks(settle, contract, _from=_from, to=to, limit=limit, interval=interval)

Get futures candlesticks

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
_from = 1546905600 # int | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to`to - 100 * interval` if not specified (optional)
to = 1546935600 # int | End time of candlesticks, formatted in Unix timestamp in seconds. Default to current time (optional)
limit = 100 # int | Maximum recent data points to return. `limit` is conflicted with `from` and `to`. If either `from` or `to` is specified, request will be rejected. (optional) (default to 100)
interval = '5m' # str | Interval time between data points (optional) (default to '5m')

try:
    # Get futures candlesticks
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
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **_from** | **int**| Start time of candlesticks, formatted in Unix timestamp in seconds. Default to&#x60;to - 100 * interval&#x60; if not specified | [optional] 
 **to** | **int**| End time of candlesticks, formatted in Unix timestamp in seconds. Default to current time | [optional] 
 **limit** | **int**| Maximum recent data points to return. &#x60;limit&#x60; is conflicted with &#x60;from&#x60; and &#x60;to&#x60;. If either &#x60;from&#x60; or &#x60;to&#x60; is specified, request will be rejected. | [optional] [default to 100]
 **interval** | **str**| Interval time between data points | [optional] [default to &#39;5m&#39;]

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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_tickers**
> list[FuturesTicker] list_futures_tickers(settle, contract=contract)

List futures tickers

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified (optional)

try:
    # List futures tickers
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
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract, return related data only if specified | [optional] 

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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_funding_rate_history**
> list[FundingRateRecord] list_futures_funding_rate_history(settle, contract, limit=limit)

Funding rate history

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)

try:
    # Funding rate history
    api_response = api_instance.list_futures_funding_rate_history(settle, contract, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_funding_rate_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]

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
**200** | History retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_insurance_ledger**
> list[InsuranceRecord] list_futures_insurance_ledger(settle, limit=limit)

Futures insurance balance history

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
settle = 'usdt' # str | Settle currency
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)

try:
    # Futures insurance balance history
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
 **settle** | **str**| Settle currency | 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]

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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_contract_stats**
> list[ContractStat] list_contract_stats(settle, contract, _from=_from, interval=interval, limit=limit)

Futures stats

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
_from = 1604561000 # int | Start timestamp (optional)
interval = '5m' # str |  (optional) (default to '5m')
limit = 30 # int |  (optional) (default to 30)

try:
    # Futures stats
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
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **_from** | **int**| Start timestamp | [optional] 
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
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_liquidated_orders**
> list[FuturesLiquidate] list_liquidated_orders(settle, contract=contract, _from=_from, to=to, limit=limit)

Retrieve liquidation history

Interval between `from` and `to` cannot exceeds 3600. Some private fields will not be returned in public endpoints. Refer to field description for detail.

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified (optional)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)

try:
    # Retrieve liquidation history
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
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract, return related data only if specified | [optional] 
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]

### Return type

[**list[FuturesLiquidate]**](FuturesLiquidate.md)

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

# **list_futures_accounts**
> FuturesAccount list_futures_accounts(settle)

Query futures account

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
settle = 'usdt' # str | Settle currency

try:
    # Query futures account
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
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_account_book**
> list[FuturesAccountBook] list_futures_account_book(settle, limit=limit, _from=_from, to=to, type=type)

Query account book

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
settle = 'usdt' # str | Settle currency
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)
type = 'dnw' # str | Changing Type: - dnw: Deposit & Withdraw - pnl: Profit & Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding - point_dnw: POINT Deposit & Withdraw - point_fee: POINT Trading fee - point_refr: POINT Referrer rebate (optional)

try:
    # Query account book
    api_response = api_instance.list_futures_account_book(settle, limit=limit, _from=_from, to=to, type=type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_account_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 
 **type** | **str**| Changing Type: - dnw: Deposit &amp; Withdraw - pnl: Profit &amp; Loss by reducing position - fee: Trading fee - refr: Referrer rebate - fund: Funding - point_dnw: POINT Deposit &amp; Withdraw - point_fee: POINT Trading fee - point_refr: POINT Referrer rebate | [optional] 

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
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_positions**
> list[Position] list_positions(settle)

List all positions of a user

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
settle = 'usdt' # str | Settle currency

try:
    # List all positions of a user
    api_response = api_instance.list_positions(settle)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_positions: %s\n" % e)
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
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_position**
> Position get_position(settle, contract)

Get single position

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract

try:
    # Get single position
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

# **update_position_margin**
> Position update_position_margin(settle, contract, change)

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
change = '0.01' # str | Margin change. Use positive number to increase margin, negative number otherwise.

try:
    # Update position margin
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
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **change** | **str**| Margin change. Use positive number to increase margin, negative number otherwise. | 

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

# **update_position_leverage**
> Position update_position_leverage(settle, contract, leverage, cross_leverage_limit=cross_leverage_limit)

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
leverage = '10' # str | New position leverage
cross_leverage_limit = '10' # str | Cross margin leverage(valid only when `leverage` is 0) (optional)

try:
    # Update position leverage
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
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **leverage** | **str**| New position leverage | 
 **cross_leverage_limit** | **str**| Cross margin leverage(valid only when &#x60;leverage&#x60; is 0) | [optional] 

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

# **update_position_risk_limit**
> Position update_position_risk_limit(settle, contract, risk_limit)

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
risk_limit = '10' # str | New position risk limit

try:
    # Update position risk limit
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

# **set_dual_mode**
> FuturesAccount set_dual_mode(settle, dual_mode)

Enable or disable dual mode

Before setting dual mode, make sure all positions are closed and no orders are open

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
settle = 'usdt' # str | Settle currency
dual_mode = true # bool | Whether to enable dual mode

try:
    # Enable or disable dual mode
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
 **settle** | **str**| Settle currency | 
 **dual_mode** | **bool**| Whether to enable dual mode | 

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
**200** | Updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dual_mode_position**
> list[Position] get_dual_mode_position(settle, contract)

Retrieve position detail in dual mode

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract

try:
    # Retrieve position detail in dual mode
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
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 

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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dual_mode_position_margin**
> list[Position] update_dual_mode_position_margin(settle, contract, change, dual_side)

Update position margin in dual mode

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
change = '0.01' # str | Margin change. Use positive number to increase margin, negative number otherwise.
dual_side = 'dual_long' # str | Long or short position

try:
    # Update position margin in dual mode
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
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **change** | **str**| Margin change. Use positive number to increase margin, negative number otherwise. | 
 **dual_side** | **str**| Long or short position | 

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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dual_mode_position_leverage**
> list[Position] update_dual_mode_position_leverage(settle, contract, leverage)

Update position leverage in dual mode

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
leverage = '10' # str | New position leverage

try:
    # Update position leverage in dual mode
    api_response = api_instance.update_dual_mode_position_leverage(settle, contract, leverage)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->update_dual_mode_position_leverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **leverage** | **str**| New position leverage | 

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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dual_mode_position_risk_limit**
> list[Position] update_dual_mode_position_risk_limit(settle, contract, risk_limit)

Update position risk limit in dual mode

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
risk_limit = '10' # str | New position risk limit

try:
    # Update position risk limit in dual mode
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
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **risk_limit** | **str**| New position risk limit | 

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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_orders**
> list[FuturesOrder] list_futures_orders(settle, contract, status, limit=limit, offset=offset, last_id=last_id, count_total=count_total)

List futures orders

Zero-fill order cannot be retrieved for 60 seconds after cancellation

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
status = 'open' # str | Only list the orders with this status
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
last_id = '12345' # str | Specify list staring point using the `id` of last record in previous list-query results (optional)
count_total = 0 # int | Whether to return total number matched. Default to 0(no return) (optional) (default to 0)

try:
    # List futures orders
    api_response = api_instance.list_futures_orders(settle, contract, status, limit=limit, offset=offset, last_id=last_id, count_total=count_total)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **status** | **str**| Only list the orders with this status | 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **last_id** | **str**| Specify list staring point using the &#x60;id&#x60; of last record in previous list-query results | [optional] 
 **count_total** | **int**| Whether to return total number matched. Default to 0(no return) | [optional] [default to 0]

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
**200** | List retrieved |  * X-Pagination-Limit - Request limit specified <br>  * X-Pagination-Offset - Request offset specified <br>  * X-Pagination-Total - Total number matched. Only returned if &#x60;count_total&#x60; set to 1 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_futures_order**
> FuturesOrder create_futures_order(settle, futures_order)

Create a futures order

Zero-fill order cannot be retrieved for 60 seconds after cancellation

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
settle = 'usdt' # str | Settle currency
futures_order = gate_api.FuturesOrder() # FuturesOrder | 

try:
    # Create a futures order
    api_response = api_instance.create_futures_order(settle, futures_order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->create_futures_order: %s\n" % e)
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

# **cancel_futures_orders**
> list[FuturesOrder] cancel_futures_orders(settle, contract, side=side)

Cancel all `open` orders matched

Zero-fill order cannot be retrieved for 60 seconds after cancellation

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract
side = 'ask' # str | All bids or asks. Both included if not specified (optional)

try:
    # Cancel all `open` orders matched
    api_response = api_instance.cancel_futures_orders(settle, contract, side=side)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_futures_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract | 
 **side** | **str**| All bids or asks. Both included if not specified | [optional] 

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
**200** | All orders matched cancelled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_futures_order**
> FuturesOrder get_futures_order(settle, order_id)

Get a single order

Zero-fill order cannot be retrieved for 60 seconds after cancellation

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
settle = 'usdt' # str | Settle currency
order_id = '12345' # str | Order ID returned, or user custom ID(i.e., `text` field). Operations based on custom ID are accepted only in the first 30 minutes after order creation.After that, only order ID is accepted.

try:
    # Get a single order
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
 **settle** | **str**| Settle currency | 
 **order_id** | **str**| Order ID returned, or user custom ID(i.e., &#x60;text&#x60; field). Operations based on custom ID are accepted only in the first 30 minutes after order creation.After that, only order ID is accepted. | 

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

# **cancel_futures_order**
> FuturesOrder cancel_futures_order(settle, order_id)

Cancel a single order

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
settle = 'usdt' # str | Settle currency
order_id = '12345' # str | Order ID returned, or user custom ID(i.e., `text` field). Operations based on custom ID are accepted only in the first 30 minutes after order creation.After that, only order ID is accepted.

try:
    # Cancel a single order
    api_response = api_instance.cancel_futures_order(settle, order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_futures_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **order_id** | **str**| Order ID returned, or user custom ID(i.e., &#x60;text&#x60; field). Operations based on custom ID are accepted only in the first 30 minutes after order creation.After that, only order ID is accepted. | 

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

# **get_my_trades**
> list[MyFuturesTrade] get_my_trades(settle, contract=contract, order=order, limit=limit, offset=offset, last_id=last_id, count_total=count_total)

List personal trading history

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified (optional)
order = 12345 # int | Futures order ID, return related data only if specified (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
last_id = '12345' # str | Specify list staring point using the `id` of last record in previous list-query results (optional)
count_total = 0 # int | Whether to return total number matched. Default to 0(no return) (optional) (default to 0)

try:
    # List personal trading history
    api_response = api_instance.get_my_trades(settle, contract=contract, order=order, limit=limit, offset=offset, last_id=last_id, count_total=count_total)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->get_my_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract, return related data only if specified | [optional] 
 **order** | **int**| Futures order ID, return related data only if specified | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **last_id** | **str**| Specify list staring point using the &#x60;id&#x60; of last record in previous list-query results | [optional] 
 **count_total** | **int**| Whether to return total number matched. Default to 0(no return) | [optional] [default to 0]

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
**200** | List retrieved |  * X-Pagination-Limit - Request limit specified <br>  * X-Pagination-Offset - Request offset specified <br>  * X-Pagination-Total - Total number matched. Only returned if &#x60;count_total&#x60; set to 1 <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_position_close**
> list[PositionClose] list_position_close(settle, contract=contract, limit=limit, offset=offset, _from=_from, to=to)

List position close history

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)

try:
    # List position close history
    api_response = api_instance.list_position_close(settle, contract=contract, limit=limit, offset=offset, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->list_position_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract, return related data only if specified | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 

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
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_liquidates**
> list[FuturesLiquidate] list_liquidates(settle, contract=contract, limit=limit, at=at)

List liquidation history

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
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
at = 0 # int | Specify a liquidation timestamp (optional) (default to 0)

try:
    # List liquidation history
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
 **settle** | **str**| Settle currency | 
 **contract** | **str**| Futures contract, return related data only if specified | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **at** | **int**| Specify a liquidation timestamp | [optional] [default to 0]

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
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_price_triggered_orders**
> list[FuturesPriceTriggeredOrder] list_price_triggered_orders(settle, status, contract=contract, limit=limit, offset=offset)

List all auto orders

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
settle = 'usdt' # str | Settle currency
status = 'status_example' # str | Only list the orders with this status
contract = 'BTC_USDT' # str | Futures contract, return related data only if specified (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # List all auto orders
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
 **settle** | **str**| Settle currency | 
 **status** | **str**| Only list the orders with this status | 
 **contract** | **str**| Futures contract, return related data only if specified | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
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
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_price_triggered_order**
> TriggerOrderResponse create_price_triggered_order(settle, futures_price_triggered_order)

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency
futures_price_triggered_order = gate_api.FuturesPriceTriggeredOrder() # FuturesPriceTriggeredOrder | 

try:
    # Create a price-triggered order
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
**201** | Order created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_price_triggered_order_list**
> list[FuturesPriceTriggeredOrder] cancel_price_triggered_order_list(settle, contract)

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
api_instance = gate_api.FuturesApi(api_client)
settle = 'usdt' # str | Settle currency
contract = 'BTC_USDT' # str | Futures contract

try:
    # Cancel all open orders
    api_response = api_instance.cancel_price_triggered_order_list(settle, contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_price_triggered_order_list: %s\n" % e)
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
**200** | Batch cancellation request accepted. Query order status by listing orders |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_triggered_order**
> FuturesPriceTriggeredOrder get_price_triggered_order(settle, order_id)

Get a single order

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
settle = 'usdt' # str | Settle currency
order_id = 'order_id_example' # str | Retrieve the data of the order with the specified ID

try:
    # Get a single order
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
 **settle** | **str**| Settle currency | 
 **order_id** | **str**| Retrieve the data of the order with the specified ID | 

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
**200** | Auto order detail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_price_triggered_order**
> FuturesPriceTriggeredOrder cancel_price_triggered_order(settle, order_id)

Cancel a single order

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
settle = 'usdt' # str | Settle currency
order_id = 'order_id_example' # str | Retrieve the data of the order with the specified ID

try:
    # Cancel a single order
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
 **settle** | **str**| Settle currency | 
 **order_id** | **str**| Retrieve the data of the order with the specified ID | 

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
**200** | Auto order detail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

