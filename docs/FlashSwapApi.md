# gate_api.FlashSwapApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_flash_swap_currencies**](FlashSwapApi.md#list_flash_swap_currencies) | **GET** /flash_swap/currencies | List all supported currencies in flash swap
[**list_flash_swap_orders**](FlashSwapApi.md#list_flash_swap_orders) | **GET** /flash_swap/orders | List all flash swap orders
[**create_flash_swap_order**](FlashSwapApi.md#create_flash_swap_order) | **POST** /flash_swap/orders | Create a flash swap order
[**get_flash_swap_order**](FlashSwapApi.md#get_flash_swap_order) | **GET** /flash_swap/orders/{order_id} | Get a single flash swap order&#39;s detail
[**preview_flash_swap_order**](FlashSwapApi.md#preview_flash_swap_order) | **POST** /flash_swap/orders/preview | Initiate a flash swap order preview


# **list_flash_swap_currencies**
> list[FlashSwapCurrency] list_flash_swap_currencies()

List all supported currencies in flash swap

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

try:
    # List all supported currencies in flash swap
    api_response = api_instance.list_flash_swap_currencies()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FlashSwapApi->list_flash_swap_currencies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[FlashSwapCurrency]**](FlashSwapCurrency.md)

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

# **list_flash_swap_orders**
> list[FlashSwapOrder] list_flash_swap_orders(status=status, sell_currency=sell_currency, buy_currency=buy_currency, reverse=reverse, limit=limit, page=page)

List all flash swap orders

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
status = 1 # int | Flash swap order status  `1` - success `2` - failure (optional)
sell_currency = 'BTC' # str | Currency to sell which can be retrieved from supported currency list API `GET /flash_swap/currencies` (optional)
buy_currency = 'BTC' # str | Currency to buy which can be retrieved from supported currency list API `GET /flash_swap/currencies` (optional)
reverse = true # bool | If results are sorted by id in reverse order. Default to `true`  - `true`: sort by id in descending order(recent first) - `false`: sort by id in ascending order(oldest first) (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
page = 1 # int | Page number (optional) (default to 1)

try:
    # List all flash swap orders
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
 **status** | **int**| Flash swap order status  &#x60;1&#x60; - success &#x60;2&#x60; - failure | [optional] 
 **sell_currency** | **str**| Currency to sell which can be retrieved from supported currency list API &#x60;GET /flash_swap/currencies&#x60; | [optional] 
 **buy_currency** | **str**| Currency to buy which can be retrieved from supported currency list API &#x60;GET /flash_swap/currencies&#x60; | [optional] 
 **reverse** | **bool**| If results are sorted by id in reverse order. Default to &#x60;true&#x60;  - &#x60;true&#x60;: sort by id in descending order(recent first) - &#x60;false&#x60;: sort by id in ascending order(oldest first) | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
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
**200** | List retrieved |  -  |

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
**201** | The flash swap order is created successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_flash_swap_order**
> FlashSwapOrder get_flash_swap_order(order_id)

Get a single flash swap order's detail

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
    # Get a single flash swap order's detail
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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_flash_swap_order**
> FlashSwapOrderPreview preview_flash_swap_order(flash_swap_order_request)

Initiate a flash swap order preview

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
    # Initiate a flash swap order preview
    api_response = api_instance.preview_flash_swap_order(flash_swap_order_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling FlashSwapApi->preview_flash_swap_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flash_swap_order_request** | [**FlashSwapOrderRequest**](FlashSwapOrderRequest.md)|  | 

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
**200** | The flash swap order successfully previewed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

