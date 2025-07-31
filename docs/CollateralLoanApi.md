# gate_api.CollateralLoanApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_collateral_loan_orders**](CollateralLoanApi.md#list_collateral_loan_orders) | **GET** /loan/collateral/orders | Query collateral loan order list
[**create_collateral_loan**](CollateralLoanApi.md#create_collateral_loan) | **POST** /loan/collateral/orders | Place collateral loan order
[**get_collateral_loan_order_detail**](CollateralLoanApi.md#get_collateral_loan_order_detail) | **GET** /loan/collateral/orders/{order_id} | Query single order details
[**repay_collateral_loan**](CollateralLoanApi.md#repay_collateral_loan) | **POST** /loan/collateral/repay | Collateral loan repayment
[**list_repay_records**](CollateralLoanApi.md#list_repay_records) | **GET** /loan/collateral/repay_records | Query collateral loan repayment records
[**list_collateral_records**](CollateralLoanApi.md#list_collateral_records) | **GET** /loan/collateral/collaterals | Query collateral adjustment records
[**operate_collateral**](CollateralLoanApi.md#operate_collateral) | **POST** /loan/collateral/collaterals | Increase or redeem collateral
[**get_user_total_amount**](CollateralLoanApi.md#get_user_total_amount) | **GET** /loan/collateral/total_amount | Query user&#39;s total borrowing and collateral amount
[**get_user_ltv_info**](CollateralLoanApi.md#get_user_ltv_info) | **GET** /loan/collateral/ltv | Query user&#39;s collateralization ratio and remaining borrowable currencies
[**list_collateral_currencies**](CollateralLoanApi.md#list_collateral_currencies) | **GET** /loan/collateral/currencies | Query supported borrowing and collateral currencies


# **list_collateral_loan_orders**
> list[CollateralOrder] list_collateral_loan_orders(page=page, limit=limit, collateral_currency=collateral_currency, borrow_currency=borrow_currency)

Query collateral loan order list

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
api_instance = gate_api.CollateralLoanApi(api_client)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
collateral_currency = 'BTC' # str | Collateral currency (optional)
borrow_currency = 'USDT' # str | Borrowed currency (optional)

try:
    # Query collateral loan order list
    api_response = api_instance.list_collateral_loan_orders(page=page, limit=limit, collateral_currency=collateral_currency, borrow_currency=borrow_currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CollateralLoanApi->list_collateral_loan_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **collateral_currency** | **str**| Collateral currency | [optional] 
 **borrow_currency** | **str**| Borrowed currency | [optional] 

### Return type

[**list[CollateralOrder]**](CollateralOrder.md)

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

# **create_collateral_loan**
> OrderResp create_collateral_loan(create_collateral_order)

Place collateral loan order

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
api_instance = gate_api.CollateralLoanApi(api_client)
create_collateral_order = gate_api.CreateCollateralOrder() # CreateCollateralOrder | 

try:
    # Place collateral loan order
    api_response = api_instance.create_collateral_loan(create_collateral_order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CollateralLoanApi->create_collateral_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_collateral_order** | [**CreateCollateralOrder**](CreateCollateralOrder.md)|  | 

### Return type

[**OrderResp**](OrderResp.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order placed successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collateral_loan_order_detail**
> CollateralOrder get_collateral_loan_order_detail(order_id)

Query single order details

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
api_instance = gate_api.CollateralLoanApi(api_client)
order_id = 100001 # int | Order ID returned when order is successfully created

try:
    # Query single order details
    api_response = api_instance.get_collateral_loan_order_detail(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CollateralLoanApi->get_collateral_loan_order_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **int**| Order ID returned when order is successfully created | 

### Return type

[**CollateralOrder**](CollateralOrder.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order details queried successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repay_collateral_loan**
> RepayResp repay_collateral_loan(repay_loan)

Collateral loan repayment

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
api_instance = gate_api.CollateralLoanApi(api_client)
repay_loan = gate_api.RepayLoan() # RepayLoan | 

try:
    # Collateral loan repayment
    api_response = api_instance.repay_collateral_loan(repay_loan)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CollateralLoanApi->repay_collateral_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repay_loan** | [**RepayLoan**](RepayLoan.md)|  | 

### Return type

[**RepayResp**](RepayResp.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operation successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repay_records**
> list[RepayRecord] list_repay_records(source, borrow_currency=borrow_currency, collateral_currency=collateral_currency, page=page, limit=limit, _from=_from, to=to)

Query collateral loan repayment records

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
api_instance = gate_api.CollateralLoanApi(api_client)
source = 'repay' # str | Operation type: repay - Regular repayment, liquidate - Liquidation
borrow_currency = 'USDT' # str | Borrowed currency (optional)
collateral_currency = 'BTC' # str | Collateral currency (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
_from = 1609459200 # int | Start timestamp for the query (optional)
to = 1609459200 # int | End timestamp for the query, defaults to current time if not specified (optional)

try:
    # Query collateral loan repayment records
    api_response = api_instance.list_repay_records(source, borrow_currency=borrow_currency, collateral_currency=collateral_currency, page=page, limit=limit, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CollateralLoanApi->list_repay_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**| Operation type: repay - Regular repayment, liquidate - Liquidation | 
 **borrow_currency** | **str**| Borrowed currency | [optional] 
 **collateral_currency** | **str**| Collateral currency | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **_from** | **int**| Start timestamp for the query | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 

### Return type

[**list[RepayRecord]**](RepayRecord.md)

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

# **list_collateral_records**
> list[CollateralRecord] list_collateral_records(page=page, limit=limit, _from=_from, to=to, borrow_currency=borrow_currency, collateral_currency=collateral_currency)

Query collateral adjustment records

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
api_instance = gate_api.CollateralLoanApi(api_client)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
_from = 1609459200 # int | Start timestamp for the query (optional)
to = 1609459200 # int | End timestamp for the query, defaults to current time if not specified (optional)
borrow_currency = 'USDT' # str | Borrowed currency (optional)
collateral_currency = 'BTC' # str | Collateral currency (optional)

try:
    # Query collateral adjustment records
    api_response = api_instance.list_collateral_records(page=page, limit=limit, _from=_from, to=to, borrow_currency=borrow_currency, collateral_currency=collateral_currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CollateralLoanApi->list_collateral_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **_from** | **int**| Start timestamp for the query | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 
 **borrow_currency** | **str**| Borrowed currency | [optional] 
 **collateral_currency** | **str**| Collateral currency | [optional] 

### Return type

[**list[CollateralRecord]**](CollateralRecord.md)

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

# **operate_collateral**
> operate_collateral(collateral_align)

Increase or redeem collateral

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
api_instance = gate_api.CollateralLoanApi(api_client)
collateral_align = gate_api.CollateralAlign() # CollateralAlign | 

try:
    # Increase or redeem collateral
    api_instance.operate_collateral(collateral_align)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CollateralLoanApi->operate_collateral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collateral_align** | [**CollateralAlign**](CollateralAlign.md)|  | 

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
**204** | Operation successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_total_amount**
> UserTotalAmount get_user_total_amount()

Query user's total borrowing and collateral amount

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
api_instance = gate_api.CollateralLoanApi(api_client)

try:
    # Query user's total borrowing and collateral amount
    api_response = api_instance.get_user_total_amount()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CollateralLoanApi->get_user_total_amount: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserTotalAmount**](UserTotalAmount.md)

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

# **get_user_ltv_info**
> UserLtvInfo get_user_ltv_info(collateral_currency, borrow_currency)

Query user's collateralization ratio and remaining borrowable currencies

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
api_instance = gate_api.CollateralLoanApi(api_client)
collateral_currency = 'BTC' # str | Collateral currency
borrow_currency = 'USDT' # str | Borrowed currency

try:
    # Query user's collateralization ratio and remaining borrowable currencies
    api_response = api_instance.get_user_ltv_info(collateral_currency, borrow_currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CollateralLoanApi->get_user_ltv_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collateral_currency** | **str**| Collateral currency | 
 **borrow_currency** | **str**| Borrowed currency | 

### Return type

[**UserLtvInfo**](UserLtvInfo.md)

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

# **list_collateral_currencies**
> list[CollateralLoanCurrency] list_collateral_currencies(loan_currency=loan_currency)

Query supported borrowing and collateral currencies

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
api_instance = gate_api.CollateralLoanApi(api_client)
loan_currency = 'BTC' # str | Parameter loan_currency. If omitted, returns all supported borrowing currencies; if provided, returns the array of collateral currencies supported for that borrowing currency (optional)

try:
    # Query supported borrowing and collateral currencies
    api_response = api_instance.list_collateral_currencies(loan_currency=loan_currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling CollateralLoanApi->list_collateral_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_currency** | **str**| Parameter loan_currency. If omitted, returns all supported borrowing currencies; if provided, returns the array of collateral currencies supported for that borrowing currency | [optional] 

### Return type

[**list[CollateralLoanCurrency]**](CollateralLoanCurrency.md)

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

