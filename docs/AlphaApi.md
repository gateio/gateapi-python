# gate_api.AlphaApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_alpha_accounts**](AlphaApi.md#list_alpha_accounts) | **GET** /alpha/accounts | API for Alpha Accounts
[**list_alpha_account_book**](AlphaApi.md#list_alpha_account_book) | **GET** /alpha/account_book | Alpha Asset Transaction API
[**quote_alpha_order**](AlphaApi.md#quote_alpha_order) | **POST** /alpha/quote | Alpha Quotation API
[**list_alpha_order**](AlphaApi.md#list_alpha_order) | **GET** /alpha/orders | Alpha 查询订单列表接口
[**place_alpha_order**](AlphaApi.md#place_alpha_order) | **POST** /alpha/orders | Alpha Order Placement API
[**get_alpha_order**](AlphaApi.md#get_alpha_order) | **GET** /alpha/order | Alpha 查询单个订单接口
[**list_alpha_currencies**](AlphaApi.md#list_alpha_currencies) | **GET** /alpha/currencies | 查询币种信息
[**list_alpha_tickers**](AlphaApi.md#list_alpha_tickers) | **GET** /alpha/tickers | 查询币种ticker


# **list_alpha_accounts**
> list[AccountsResponse] list_alpha_accounts()

API for Alpha Accounts

Query Position Assets

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
api_instance = gate_api.AlphaApi(api_client)

try:
    # API for Alpha Accounts
    api_response = api_instance.list_alpha_accounts()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->list_alpha_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AccountsResponse]**](AccountsResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 查询持仓成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alpha_account_book**
> list[AccountBookResponse] list_alpha_account_book(_from, to=to, page=page, limit=limit)

Alpha Asset Transaction API

Query Asset Transactions

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
api_instance = gate_api.AlphaApi(api_client)
_from = 56 # int | Start timestamp of the query
to = 56 # int | Time range ending, default to current time (optional)
page = 56 # int | Page number (optional)
limit = 56 # int | The maximum number of items per page is 100 (optional)

try:
    # Alpha Asset Transaction API
    api_response = api_instance.list_alpha_account_book(_from, to=to, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->list_alpha_account_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Start timestamp of the query | 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **page** | **int**| Page number | [optional] 
 **limit** | **int**| The maximum number of items per page is 100 | [optional] 

### Return type

[**list[AccountBookResponse]**](AccountBookResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 查询流水成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quote_alpha_order**
> QuoteResponse quote_alpha_order(quote_request)

Alpha Quotation API

The quote_id returned by the quotation API is valid for one minute.You must place the order within this time window;otherwise, the quote will expire and a new quotation request is required

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
api_instance = gate_api.AlphaApi(api_client)
quote_request = gate_api.QuoteRequest() # QuoteRequest | 

try:
    # Alpha Quotation API
    api_response = api_instance.quote_alpha_order(quote_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->quote_alpha_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quote_request** | [**QuoteRequest**](QuoteRequest.md)|  | 

### Return type

[**QuoteResponse**](QuoteResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 询价成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alpha_order**
> list[OrderResponse] list_alpha_order(currency, side, status, _from=_from, to=to, limit=limit, page=page)

Alpha 查询订单列表接口

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
api_instance = gate_api.AlphaApi(api_client)
currency = 'memeboxsst' # str | Trading Symbol
side = 'buy' # str | 买单或者卖单 - buy - sell
status = 2 # int | Order Status - `0` : All - `1` : Processing - `2` : Successful - `3` : Failed - `4` : Canceled - `5` : Buy order placed but transfer not completed - `6` : Cancelled order with transfer not complete
_from = 1627706330 # int | 查询订单的起始时间 (optional)
to = 1635329650 # int | 查询订单的结束时间，不指定则默认为当前时间 (optional)
limit = 100 # int | Maximum response items.  Default: 100, minimum: 1, Maximum: 100 (optional) (default to 100)
page = 1 # int | Page number (optional) (default to 1)

try:
    # Alpha 查询订单列表接口
    api_response = api_instance.list_alpha_order(currency, side, status, _from=_from, to=to, limit=limit, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->list_alpha_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Trading Symbol | 
 **side** | **str**| 买单或者卖单 - buy - sell | 
 **status** | **int**| Order Status - &#x60;0&#x60; : All - &#x60;1&#x60; : Processing - &#x60;2&#x60; : Successful - &#x60;3&#x60; : Failed - &#x60;4&#x60; : Canceled - &#x60;5&#x60; : Buy order placed but transfer not completed - &#x60;6&#x60; : Cancelled order with transfer not complete | 
 **_from** | **int**| 查询订单的起始时间 | [optional] 
 **to** | **int**| 查询订单的结束时间，不指定则默认为当前时间 | [optional] 
 **limit** | **int**| Maximum response items.  Default: 100, minimum: 1, Maximum: 100 | [optional] [default to 100]
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[OrderResponse]**](OrderResponse.md)

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

# **place_alpha_order**
> PlaceOrderResponse place_alpha_order(place_order_request)

Alpha Order Placement API

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
api_instance = gate_api.AlphaApi(api_client)
place_order_request = gate_api.PlaceOrderRequest() # PlaceOrderRequest | 

try:
    # Alpha Order Placement API
    api_response = api_instance.place_alpha_order(place_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->place_alpha_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_order_request** | [**PlaceOrderRequest**](PlaceOrderRequest.md)|  | 

### Return type

[**PlaceOrderResponse**](PlaceOrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alpha_order**
> OrderResponse get_alpha_order(order_id)

Alpha 查询单个订单接口

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
api_instance = gate_api.AlphaApi(api_client)
order_id = 'fdaf12321' # str | Order ID

try:
    # Alpha 查询单个订单接口
    api_response = api_instance.get_alpha_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->get_alpha_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID | 

### Return type

[**OrderResponse**](OrderResponse.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 订单查询成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_alpha_currencies**
> list[Currency2] list_alpha_currencies(currency=currency, limit=limit, page=page)

查询币种信息

When the currency parameter is provided, query and return information for the specified currency. When the currency parameter is not provided, return a paginated list of currencies.

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
api_instance = gate_api.AlphaApi(api_client)
currency = 'memeboxtrump' # str | 根据币种符号查询币种信息 (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
page = 1 # int | Page number (optional) (default to 1)

try:
    # 查询币种信息
    api_response = api_instance.list_alpha_currencies(currency=currency, limit=limit, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->list_alpha_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| 根据币种符号查询币种信息 | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[Currency2]**](Currency2.md)

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

# **list_alpha_tickers**
> list[Ticker2] list_alpha_tickers(currency=currency, limit=limit, page=page)

查询币种ticker

When the currency parameter is provided, query and return information for the specified ticker, When the currency parameter is not provided, return a paginated list of tickers.

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
api_instance = gate_api.AlphaApi(api_client)
currency = 'memeboxtrump' # str | Retrieve data of the specified currency (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
page = 1 # int | Page number (optional) (default to 1)

try:
    # 查询币种ticker
    api_response = api_instance.list_alpha_tickers(currency=currency, limit=limit, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling AlphaApi->list_alpha_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[Ticker2]**](Ticker2.md)

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

