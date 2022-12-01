# gate_api.OptionsApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_options_underlyings**](OptionsApi.md#list_options_underlyings) | **GET** /options/underlyings | List all underlyings
[**list_options_expirations**](OptionsApi.md#list_options_expirations) | **GET** /options/expirations | List all expiration times
[**list_options_contracts**](OptionsApi.md#list_options_contracts) | **GET** /options/contracts | List all the contracts with specified underlying and expiration time
[**get_options_contract**](OptionsApi.md#get_options_contract) | **GET** /options/contracts/{contract} | Query specified contract detail
[**list_options_settlements**](OptionsApi.md#list_options_settlements) | **GET** /options/settlements | List settlement history
[**get_options_settlement**](OptionsApi.md#get_options_settlement) | **GET** /options/settlements/{contract} | Get specified contract&#39;s settlement
[**list_my_options_settlements**](OptionsApi.md#list_my_options_settlements) | **GET** /options/my_settlements | List my options settlements
[**list_options_order_book**](OptionsApi.md#list_options_order_book) | **GET** /options/order_book | Options order book
[**list_options_tickers**](OptionsApi.md#list_options_tickers) | **GET** /options/tickers | List tickers of options contracts
[**list_options_underlying_tickers**](OptionsApi.md#list_options_underlying_tickers) | **GET** /options/underlying/tickers/{underlying} | Get underlying ticker
[**list_options_candlesticks**](OptionsApi.md#list_options_candlesticks) | **GET** /options/candlesticks | Get options candlesticks
[**list_options_underlying_candlesticks**](OptionsApi.md#list_options_underlying_candlesticks) | **GET** /options/underlying/candlesticks | Mark price candlesticks of an underlying
[**list_options_trades**](OptionsApi.md#list_options_trades) | **GET** /options/trades | Options trade history
[**list_options_account**](OptionsApi.md#list_options_account) | **GET** /options/accounts | List options account
[**list_options_account_book**](OptionsApi.md#list_options_account_book) | **GET** /options/account_book | List account changing history
[**list_options_positions**](OptionsApi.md#list_options_positions) | **GET** /options/positions | List user&#39;s positions of specified underlying
[**get_options_position**](OptionsApi.md#get_options_position) | **GET** /options/positions/{contract} | Get specified contract position
[**list_options_position_close**](OptionsApi.md#list_options_position_close) | **GET** /options/position_close | List user&#39;s liquidation history of specified underlying
[**list_options_orders**](OptionsApi.md#list_options_orders) | **GET** /options/orders | List options orders
[**create_options_order**](OptionsApi.md#create_options_order) | **POST** /options/orders | Create an options order
[**cancel_options_orders**](OptionsApi.md#cancel_options_orders) | **DELETE** /options/orders | Cancel all &#x60;open&#x60; orders matched
[**get_options_order**](OptionsApi.md#get_options_order) | **GET** /options/orders/{order_id} | Get a single order
[**cancel_options_order**](OptionsApi.md#cancel_options_order) | **DELETE** /options/orders/{order_id} | Cancel a single order
[**list_my_options_trades**](OptionsApi.md#list_my_options_trades) | **GET** /options/my_trades | List personal trading history


# **list_options_underlyings**
> list[OptionsUnderlying] list_options_underlyings()

List all underlyings

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
api_instance = gate_api.OptionsApi(api_client)

try:
    # List all underlyings
    api_response = api_instance.list_options_underlyings()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_underlyings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[OptionsUnderlying]**](OptionsUnderlying.md)

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

# **list_options_expirations**
> list[int] list_options_expirations(underlying)

List all expiration times

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
api_instance = gate_api.OptionsApi(api_client)
underlying = 'BTC_USDT' # str | Underlying (Obtained by listing underlying endpoint)

try:
    # List all expiration times
    api_response = api_instance.list_options_expirations(underlying)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_expirations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying (Obtained by listing underlying endpoint) | 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List expiration times of specified underlying |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_options_contracts**
> list[OptionsContract] list_options_contracts(underlying, expiration=expiration)

List all the contracts with specified underlying and expiration time

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
api_instance = gate_api.OptionsApi(api_client)
underlying = 'BTC_USDT' # str | Underlying (Obtained by listing underlying endpoint)
expiration = 1636588800 # int | Unix timestamp of the expiration time (optional)

try:
    # List all the contracts with specified underlying and expiration time
    api_response = api_instance.list_options_contracts(underlying, expiration=expiration)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_contracts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying (Obtained by listing underlying endpoint) | 
 **expiration** | **int**| Unix timestamp of the expiration time | [optional] 

### Return type

[**list[OptionsContract]**](OptionsContract.md)

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

# **get_options_contract**
> OptionsContract get_options_contract(contract)

Query specified contract detail

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
api_instance = gate_api.OptionsApi(api_client)
contract = 'BTC_USDT-20211130-65000-C' # str | 

try:
    # Query specified contract detail
    api_response = api_instance.get_options_contract(contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->get_options_contract: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 

### Return type

[**OptionsContract**](OptionsContract.md)

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

# **list_options_settlements**
> list[OptionsSettlement] list_options_settlements(underlying, limit=limit, offset=offset, _from=_from, to=to)

List settlement history

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
api_instance = gate_api.OptionsApi(api_client)
underlying = 'BTC_USDT' # str | Underlying (Obtained by listing underlying endpoint)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)

try:
    # List settlement history
    api_response = api_instance.list_options_settlements(underlying, limit=limit, offset=offset, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_settlements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying (Obtained by listing underlying endpoint) | 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 

### Return type

[**list[OptionsSettlement]**](OptionsSettlement.md)

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

# **get_options_settlement**
> OptionsSettlement get_options_settlement(contract, underlying, at)

Get specified contract's settlement

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
api_instance = gate_api.OptionsApi(api_client)
contract = 'BTC_USDT-20211130-65000-C' # str | 
underlying = 'BTC_USDT' # str | Underlying (Obtained by listing underlying endpoint)
at = 56 # int | 

try:
    # Get specified contract's settlement
    api_response = api_instance.get_options_settlement(contract, underlying, at)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->get_options_settlement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 
 **underlying** | **str**| Underlying (Obtained by listing underlying endpoint) | 
 **at** | **int**|  | 

### Return type

[**OptionsSettlement**](OptionsSettlement.md)

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

# **list_my_options_settlements**
> list[OptionsMySettlements] list_my_options_settlements(underlying, contract=contract, limit=limit, offset=offset, _from=_from, to=to)

List my options settlements

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
api_instance = gate_api.OptionsApi(api_client)
underlying = 'BTC_USDT' # str | Underlying (Obtained by listing underlying endpoint)
contract = 'BTC_USDT-20210916-5000-C' # str | Options contract name (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)

try:
    # List my options settlements
    api_response = api_instance.list_my_options_settlements(underlying, contract=contract, limit=limit, offset=offset, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_my_options_settlements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying (Obtained by listing underlying endpoint) | 
 **contract** | **str**| Options contract name | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 

### Return type

[**list[OptionsMySettlements]**](OptionsMySettlements.md)

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

# **list_options_order_book**
> FuturesOrderBook list_options_order_book(contract, interval=interval, limit=limit, with_id=with_id)

Options order book

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
api_instance = gate_api.OptionsApi(api_client)
contract = 'BTC_USDT-20210916-5000-C' # str | Options contract name
interval = '0' # str | Order depth. 0 means no aggregation is applied. default to 0 (optional) (default to '0')
limit = 10 # int | Maximum number of order depth data in asks or bids (optional) (default to 10)
with_id = False # bool | Whether the order book update ID will be returned. This ID increases by 1 on every order book update (optional) (default to False)

try:
    # Options order book
    api_response = api_instance.list_options_order_book(contract, interval=interval, limit=limit, with_id=with_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_order_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Options contract name | 
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

# **list_options_tickers**
> list[OptionsTicker] list_options_tickers(underlying)

List tickers of options contracts

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
api_instance = gate_api.OptionsApi(api_client)
underlying = 'BTC_USDT' # str | Underlying (Obtained by listing underlying endpoint)

try:
    # List tickers of options contracts
    api_response = api_instance.list_options_tickers(underlying)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying (Obtained by listing underlying endpoint) | 

### Return type

[**list[OptionsTicker]**](OptionsTicker.md)

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

# **list_options_underlying_tickers**
> OptionsUnderlyingTicker list_options_underlying_tickers(underlying)

Get underlying ticker

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
api_instance = gate_api.OptionsApi(api_client)
underlying = 'BTC_USDT' # str | Underlying

try:
    # Get underlying ticker
    api_response = api_instance.list_options_underlying_tickers(underlying)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_underlying_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying | 

### Return type

[**OptionsUnderlyingTicker**](OptionsUnderlyingTicker.md)

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

# **list_options_candlesticks**
> list[OptionsCandlestick] list_options_candlesticks(contract, limit=limit, _from=_from, to=to, interval=interval)

Get options candlesticks

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
api_instance = gate_api.OptionsApi(api_client)
contract = 'BTC_USDT-20210916-5000-C' # str | Options contract name
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)
interval = '5m' # str | Interval time between data points (optional) (default to '5m')

try:
    # Get options candlesticks
    api_response = api_instance.list_options_candlesticks(contract, limit=limit, _from=_from, to=to, interval=interval)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_candlesticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Options contract name | 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 
 **interval** | **str**| Interval time between data points | [optional] [default to &#39;5m&#39;]

### Return type

[**list[OptionsCandlestick]**](OptionsCandlestick.md)

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

# **list_options_underlying_candlesticks**
> list[FuturesCandlestick] list_options_underlying_candlesticks(underlying, limit=limit, _from=_from, to=to, interval=interval)

Mark price candlesticks of an underlying

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
api_instance = gate_api.OptionsApi(api_client)
underlying = 'BTC_USDT' # str | Underlying (Obtained by listing underlying endpoint)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)
interval = '5m' # str | Interval time between data points (optional) (default to '5m')

try:
    # Mark price candlesticks of an underlying
    api_response = api_instance.list_options_underlying_candlesticks(underlying, limit=limit, _from=_from, to=to, interval=interval)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_underlying_candlesticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying (Obtained by listing underlying endpoint) | 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 
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

# **list_options_trades**
> list[FuturesTrade] list_options_trades(contract=contract, type=type, limit=limit, offset=offset, _from=_from, to=to)

Options trade history

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
api_instance = gate_api.OptionsApi(api_client)
contract = 'BTC_USDT-20210916-5000-C' # str | Options contract name (optional)
type = '1546935600' # str | `C` is call, while `P` is put (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)

try:
    # Options trade history
    api_response = api_instance.list_options_trades(contract=contract, type=type, limit=limit, offset=offset, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Options contract name | [optional] 
 **type** | **str**| &#x60;C&#x60; is call, while &#x60;P&#x60; is put | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 

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

# **list_options_account**
> OptionsAccount list_options_account()

List options account

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
api_instance = gate_api.OptionsApi(api_client)

try:
    # List options account
    api_response = api_instance.list_options_account()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OptionsAccount**](OptionsAccount.md)

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

# **list_options_account_book**
> list[OptionsAccountBook] list_options_account_book(limit=limit, offset=offset, _from=_from, to=to, type=type)

List account changing history

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
api_instance = gate_api.OptionsApi(api_client)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)
type = 'dnw' # str | Changing Type: - dnw: Deposit & Withdraw - prem: Trading premium - fee: Trading fee - refr: Referrer rebate - set: settlement PNL  (optional)

try:
    # List account changing history
    api_response = api_instance.list_options_account_book(limit=limit, offset=offset, _from=_from, to=to, type=type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_account_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 
 **type** | **str**| Changing Type: - dnw: Deposit &amp; Withdraw - prem: Trading premium - fee: Trading fee - refr: Referrer rebate - set: settlement PNL  | [optional] 

### Return type

[**list[OptionsAccountBook]**](OptionsAccountBook.md)

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

# **list_options_positions**
> list[OptionsPosition] list_options_positions(underlying=underlying)

List user's positions of specified underlying

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
api_instance = gate_api.OptionsApi(api_client)
underlying = 'BTC_USDT' # str | Underlying (optional)

try:
    # List user's positions of specified underlying
    api_response = api_instance.list_options_positions(underlying=underlying)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_positions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying | [optional] 

### Return type

[**list[OptionsPosition]**](OptionsPosition.md)

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

# **get_options_position**
> OptionsPosition get_options_position(contract)

Get specified contract position

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
api_instance = gate_api.OptionsApi(api_client)
contract = 'BTC_USDT-20211130-65000-C' # str | 

try:
    # Get specified contract position
    api_response = api_instance.get_options_position(contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->get_options_position: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**|  | 

### Return type

[**OptionsPosition**](OptionsPosition.md)

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

# **list_options_position_close**
> list[OptionsPositionClose] list_options_position_close(underlying, contract=contract)

List user's liquidation history of specified underlying

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
api_instance = gate_api.OptionsApi(api_client)
underlying = 'BTC_USDT' # str | Underlying (Obtained by listing underlying endpoint)
contract = 'BTC_USDT-20210916-5000-C' # str | Options contract name (optional)

try:
    # List user's liquidation history of specified underlying
    api_response = api_instance.list_options_position_close(underlying, contract=contract)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_position_close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying (Obtained by listing underlying endpoint) | 
 **contract** | **str**| Options contract name | [optional] 

### Return type

[**list[OptionsPositionClose]**](OptionsPositionClose.md)

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

# **list_options_orders**
> list[OptionsOrder] list_options_orders(status, contract=contract, underlying=underlying, limit=limit, offset=offset, _from=_from, to=to)

List options orders

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
api_instance = gate_api.OptionsApi(api_client)
status = 'open' # str | Only list the orders with this status
contract = 'BTC_USDT-20210916-5000-C' # str | Options contract name (optional)
underlying = 'BTC_USDT' # str | Underlying (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)

try:
    # List options orders
    api_response = api_instance.list_options_orders(status, contract=contract, underlying=underlying, limit=limit, offset=offset, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_options_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Only list the orders with this status | 
 **contract** | **str**| Options contract name | [optional] 
 **underlying** | **str**| Underlying | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 

### Return type

[**list[OptionsOrder]**](OptionsOrder.md)

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

# **create_options_order**
> OptionsOrder create_options_order(options_order)

Create an options order

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
api_instance = gate_api.OptionsApi(api_client)
options_order = gate_api.OptionsOrder() # OptionsOrder | 

try:
    # Create an options order
    api_response = api_instance.create_options_order(options_order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->create_options_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **options_order** | [**OptionsOrder**](OptionsOrder.md)|  | 

### Return type

[**OptionsOrder**](OptionsOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Order detail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_options_orders**
> list[OptionsOrder] cancel_options_orders(contract=contract, underlying=underlying, side=side)

Cancel all `open` orders matched

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
api_instance = gate_api.OptionsApi(api_client)
contract = 'BTC_USDT-20210916-5000-C' # str | Options contract name (optional)
underlying = 'BTC_USDT' # str | Underlying (optional)
side = 'ask' # str | All bids or asks. Both included if not specified (optional)

try:
    # Cancel all `open` orders matched
    api_response = api_instance.cancel_options_orders(contract=contract, underlying=underlying, side=side)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->cancel_options_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| Options contract name | [optional] 
 **underlying** | **str**| Underlying | [optional] 
 **side** | **str**| All bids or asks. Both included if not specified | [optional] 

### Return type

[**list[OptionsOrder]**](OptionsOrder.md)

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

# **get_options_order**
> OptionsOrder get_options_order(order_id)

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
api_instance = gate_api.OptionsApi(api_client)
order_id = 12345 # int | Order ID returned on successful order creation

try:
    # Get a single order
    api_response = api_instance.get_options_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->get_options_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID returned on successful order creation | 

### Return type

[**OptionsOrder**](OptionsOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order detail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_options_order**
> OptionsOrder cancel_options_order(order_id)

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
api_instance = gate_api.OptionsApi(api_client)
order_id = 12345 # int | Order ID returned on successful order creation

try:
    # Cancel a single order
    api_response = api_instance.cancel_options_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->cancel_options_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID returned on successful order creation | 

### Return type

[**OptionsOrder**](OptionsOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order detail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_my_options_trades**
> list[OptionsMyTrade] list_my_options_trades(underlying, contract=contract, limit=limit, offset=offset, _from=_from, to=to)

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
api_instance = gate_api.OptionsApi(api_client)
underlying = 'BTC_USDT' # str | Underlying (Obtained by listing underlying endpoint)
contract = 'BTC_USDT-20210916-5000-C' # str | Options contract name (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)

try:
    # List personal trading history
    api_response = api_instance.list_my_options_trades(underlying, contract=contract, limit=limit, offset=offset, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling OptionsApi->list_my_options_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **underlying** | **str**| Underlying (Obtained by listing underlying endpoint) | 
 **contract** | **str**| Options contract name | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 

### Return type

[**list[OptionsMyTrade]**](OptionsMyTrade.md)

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

