# gate_api.EarnApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**swap_eth2**](EarnApi.md#swap_eth2) | **POST** /earn/staking/eth2/swap | ETH2 swap
[**rate_list_eth2**](EarnApi.md#rate_list_eth2) | **GET** /earn/staking/eth2/rate_records | ETH2 historical rate of return query
[**list_dual_investment_plans**](EarnApi.md#list_dual_investment_plans) | **GET** /earn/dual/investment_plan | Dual Investment product list
[**list_dual_orders**](EarnApi.md#list_dual_orders) | **GET** /earn/dual/orders | Dual Investment order list
[**place_dual_order**](EarnApi.md#place_dual_order) | **POST** /earn/dual/orders | Place Dual Investment order
[**list_structured_products**](EarnApi.md#list_structured_products) | **GET** /earn/structured/products | Structured Product List
[**list_structured_orders**](EarnApi.md#list_structured_orders) | **GET** /earn/structured/orders | Structured Product Order List
[**place_structured_order**](EarnApi.md#place_structured_order) | **POST** /earn/structured/orders | Place Structured Product Order


# **swap_eth2**
> swap_eth2(eth2_swap)

ETH2 swap

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
api_instance = gate_api.EarnApi(api_client)
eth2_swap = gate_api.Eth2Swap() # Eth2Swap | 

try:
    # ETH2 swap
    api_instance.swap_eth2(eth2_swap)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->swap_eth2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eth2_swap** | [**Eth2Swap**](Eth2Swap.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | swap success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rate_list_eth2**
> list[Eth2RateList] rate_list_eth2()

ETH2 historical rate of return query

Check the ETH earnings rate record for the last 31 days

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
api_instance = gate_api.EarnApi(api_client)

try:
    # ETH2 historical rate of return query
    api_response = api_instance.rate_list_eth2()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->rate_list_eth2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Eth2RateList]**](Eth2RateList.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dual_investment_plans**
> list[DualGetPlans] list_dual_investment_plans(plan_id=plan_id)

Dual Investment product list

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
api_instance = gate_api.EarnApi(api_client)
plan_id = 1 # int | Financial project id (optional)

try:
    # Dual Investment product list
    api_response = api_instance.list_dual_investment_plans(plan_id=plan_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_dual_investment_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_id** | **int**| Financial project id | [optional] 

### Return type

[**list[DualGetPlans]**](DualGetPlans.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dual_orders**
> list[DualGetOrders] list_dual_orders(_from=_from, to=to, page=page, limit=limit)

Dual Investment order list

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
api_instance = gate_api.EarnApi(api_client)
_from = 1740727000 # int | Start checkout time (optional)
to = 1740729000 # int | End settlement time (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)

try:
    # Dual Investment order list
    api_response = api_instance.list_dual_orders(_from=_from, to=to, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_dual_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Start checkout time | [optional] 
 **to** | **int**| End settlement time | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]

### Return type

[**list[DualGetOrders]**](DualGetOrders.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_dual_order**
> place_dual_order(place_dual_investment_order)

Place Dual Investment order

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
api_instance = gate_api.EarnApi(api_client)
place_dual_investment_order = gate_api.PlaceDualInvestmentOrder() # PlaceDualInvestmentOrder | 

try:
    # Place Dual Investment order
    api_instance.place_dual_order(place_dual_investment_order)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->place_dual_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **place_dual_investment_order** | [**PlaceDualInvestmentOrder**](PlaceDualInvestmentOrder.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_structured_products**
> list[StructuredGetProjectList] list_structured_products(status, type=type, page=page, limit=limit)

Structured Product List

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
api_instance = gate_api.EarnApi(api_client)
status = 'in_process' # str | Status (default: all)  `in_process`-processing  `will_begin`-unstarted  `wait_settlement`-unsettled  `done`-finish
type = 'BullishSharkFin' # str | Product Type (default all)  `SharkFin2.0`-SharkFin  `BullishSharkFin`-BullishSharkFin  `BearishSharkFin`-BearishSharkFin `DoubleNoTouch`-DoubleNoTouch `RangeAccrual`-RangeAccrual `SnowBall`-SnowBall (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)

try:
    # Structured Product List
    api_response = api_instance.list_structured_products(status, type=type, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_structured_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Status (default: all)  &#x60;in_process&#x60;-processing  &#x60;will_begin&#x60;-unstarted  &#x60;wait_settlement&#x60;-unsettled  &#x60;done&#x60;-finish | 
 **type** | **str**| Product Type (default all)  &#x60;SharkFin2.0&#x60;-SharkFin  &#x60;BullishSharkFin&#x60;-BullishSharkFin  &#x60;BearishSharkFin&#x60;-BearishSharkFin &#x60;DoubleNoTouch&#x60;-DoubleNoTouch &#x60;RangeAccrual&#x60;-RangeAccrual &#x60;SnowBall&#x60;-SnowBall | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]

### Return type

[**list[StructuredGetProjectList]**](StructuredGetProjectList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_structured_orders**
> list[StructuredOrderList] list_structured_orders(_from=_from, to=to, page=page, limit=limit)

Structured Product Order List

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
api_instance = gate_api.EarnApi(api_client)
_from = 1547706332 # int | Start timestamp (optional)
to = 1547706332 # int | End timestamp (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)

try:
    # Structured Product Order List
    api_response = api_instance.list_structured_orders(_from=_from, to=to, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->list_structured_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| Start timestamp | [optional] 
 **to** | **int**| End timestamp | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]

### Return type

[**list[StructuredOrderList]**](StructuredOrderList.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_structured_order**
> place_structured_order(structured_buy)

Place Structured Product Order

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
api_instance = gate_api.EarnApi(api_client)
structured_buy = gate_api.StructuredBuy() # StructuredBuy | 

try:
    # Place Structured Product Order
    api_instance.place_structured_order(structured_buy)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling EarnApi->place_structured_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **structured_buy** | [**StructuredBuy**](StructuredBuy.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

