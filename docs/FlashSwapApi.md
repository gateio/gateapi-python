# gate_api.FlashSwapApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_flash_swap_currency_pair**](FlashSwapApi.md#list_flash_swap_currency_pair) | **GET** /flash_swap/currency_pairs | List All Supported Currency Pairs In Flash Swap
[**list_flash_swap_orders**](FlashSwapApi.md#list_flash_swap_orders) | **GET** /flash_swap/orders | Query flash swap order list
[**create_flash_swap_order**](FlashSwapApi.md#create_flash_swap_order) | **POST** /flash_swap/orders | Create a flash swap order
[**get_flash_swap_order**](FlashSwapApi.md#get_flash_swap_order) | **GET** /flash_swap/orders/{order_id} | Query single flash swap order
[**preview_flash_swap_order**](FlashSwapApi.md#preview_flash_swap_order) | **POST** /flash_swap/orders/preview | Flash swap order preview


# **list_flash_swap_currency_pair**
> list[FlashSwapCurrencyPair] list_flash_swap_currency_pair(currency=currency, page=page, limit=limit)

List All Supported Currency Pairs In Flash Swap

`BTC_GT` represents selling BTC and buying GT. The limits for each currency may vary across different currency pairs.  It is not necessary that two currencies that can be swapped instantaneously can be exchanged with each other. For example, it is possible to sell BTC and buy GT, but it does not necessarily mean that GT can be sold to buy BTC.

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
api_instance = gate_api.FlashSwapApi(api_client)
currency = 'BTC' # str | Query by specified currency name (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 1000 # int | Maximum number of items returned. Default: 1000, minimum: 1, maximum: 1000 (optional) (default to 1000)

try:
    # List All Supported Currency Pairs In Flash Swap
    api_response = api_instance.list_flash_swap_currency_pair(currency=currency, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FlashSwapApi->list_flash_swap_currency_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Query by specified currency name | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of items returned. Default: 1000, minimum: 1, maximum: 1000 | [optional] [default to 1000]

### Return type

[**list[FlashSwapCurrencyPair]**](FlashSwapCurrencyPair.md)

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

# **list_flash_swap_orders**
> list[FlashSwapOrder] list_flash_swap_orders(status=status, sell_currency=sell_currency, buy_currency=buy_currency, reverse=reverse, limit=limit, page=page)

Query flash swap order list

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
api_instance = gate_api.FlashSwapApi(api_client)
status = 1 # int | Flash swap order status  `1` - success `2` - failed (optional)
sell_currency = 'BTC' # str | Asset name to sell - Retrieved from API `GET /flash_swap/currencies` for supported flash swap currencies (optional)
buy_currency = 'BTC' # str | Asset name to buy - Retrieved from API `GET /flash_swap/currencies` for supported flash swap currencies (optional)
reverse = true # bool | Sort by ID in ascending or descending order, default `true` - `true`: ID descending order (most recent data first) - `false`: ID ascending order (oldest data first) (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
page = 1 # int | Page number (optional) (default to 1)

try:
    # Query flash swap order list
    api_response = api_instance.list_flash_swap_orders(status=status, sell_currency=sell_currency, buy_currency=buy_currency, reverse=reverse, limit=limit, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FlashSwapApi->list_flash_swap_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **int**| Flash swap order status  &#x60;1&#x60; - success &#x60;2&#x60; - failed | [optional] 
 **sell_currency** | **str**| Asset name to sell - Retrieved from API &#x60;GET /flash_swap/currencies&#x60; for supported flash swap currencies | [optional] 
 **buy_currency** | **str**| Asset name to buy - Retrieved from API &#x60;GET /flash_swap/currencies&#x60; for supported flash swap currencies | [optional] 
 **reverse** | **bool**| Sort by ID in ascending or descending order, default &#x60;true&#x60; - &#x60;true&#x60;: ID descending order (most recent data first) - &#x60;false&#x60;: ID ascending order (oldest data first) | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[FlashSwapOrder]**](FlashSwapOrder.md)

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

# **create_flash_swap_order**
> FlashSwapOrder create_flash_swap_order(flash_swap_order_request)

Create a flash swap order

Initiate a flash swap preview in advance because order creation requires a preview result

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
api_instance = gate_api.FlashSwapApi(api_client)
flash_swap_order_request = gate_api.FlashSwapOrderRequest() # FlashSwapOrderRequest | 

try:
    # Create a flash swap order
    api_response = api_instance.create_flash_swap_order(flash_swap_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FlashSwapApi->create_flash_swap_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flash_swap_order_request** | [**FlashSwapOrderRequest**](FlashSwapOrderRequest.md)|  | 

### Return type

[**FlashSwapOrder**](FlashSwapOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Flash swap order created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flash_swap_order**
> FlashSwapOrder get_flash_swap_order(order_id)

Query single flash swap order

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
api_instance = gate_api.FlashSwapApi(api_client)
order_id = 1 # int | Flash swap order ID

try:
    # Query single flash swap order
    api_response = api_instance.get_flash_swap_order(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FlashSwapApi->get_flash_swap_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Flash swap order ID | 

### Return type

[**FlashSwapOrder**](FlashSwapOrder.md)

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

# **preview_flash_swap_order**
> FlashSwapOrderPreview preview_flash_swap_order(flash_swap_preview_request)

Flash swap order preview

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
api_instance = gate_api.FlashSwapApi(api_client)
flash_swap_preview_request = gate_api.FlashSwapPreviewRequest() # FlashSwapPreviewRequest | 

try:
    # Flash swap order preview
    api_response = api_instance.preview_flash_swap_order(flash_swap_preview_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FlashSwapApi->preview_flash_swap_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flash_swap_preview_request** | [**FlashSwapPreviewRequest**](FlashSwapPreviewRequest.md)|  | 

### Return type

[**FlashSwapOrderPreview**](FlashSwapOrderPreview.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Flash swap order preview successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

