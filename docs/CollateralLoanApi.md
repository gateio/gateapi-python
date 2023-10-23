# gate_api.CollateralLoanApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_collateral_loan_orders**](CollateralLoanApi.md#list_collateral_loan_orders) | **GET** /loan/collateral/orders | List Orders
[**create_collateral_loan**](CollateralLoanApi.md#create_collateral_loan) | **POST** /loan/collateral/orders | Place order
[**get_collateral_loan_order_detail**](CollateralLoanApi.md#get_collateral_loan_order_detail) | **GET** /loan/collateral/orders/{order_id} | Get a single order
[**repay_collateral_loan**](CollateralLoanApi.md#repay_collateral_loan) | **POST** /loan/collateral/repay | Repayment
[**list_repay_records**](CollateralLoanApi.md#list_repay_records) | **GET** /loan/collateral/repay_records | Repayment history
[**list_collateral_records**](CollateralLoanApi.md#list_collateral_records) | **GET** /loan/collateral/collaterals | Query collateral adjustment records
[**operate_collateral**](CollateralLoanApi.md#operate_collateral) | **POST** /loan/collateral/collaterals | Increase or redeem collateral
[**get_user_total_amount**](CollateralLoanApi.md#get_user_total_amount) | **GET** /loan/collateral/total_amount | Query the total borrowing and collateral amount for the user
[**get_user_ltv_info**](CollateralLoanApi.md#get_user_ltv_info) | **GET** /loan/collateral/ltv | Query user&#39;s collateralization ratio
[**list_collateral_currencies**](CollateralLoanApi.md#list_collateral_currencies) | **GET** /loan/collateral/currencies | Query supported borrowing and collateral currencies


# **list_collateral_loan_orders**
> list[CollateralOrder] list_collateral_loan_orders(page=page, limit=limit, collateral_currency=collateral_currency, borrow_currency=borrow_currency)

List Orders

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
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
collateral_currency = 'BTC' # str | Collateral (optional)
borrow_currency = 'USDT' # str | Borrowed currency (optional)

try:
    # List Orders
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
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **collateral_currency** | **str**| Collateral | [optional] 
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
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_collateral_loan**
> OrderResp create_collateral_loan(create_collateral_order)

Place order

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
    # Place order
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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collateral_loan_order_detail**
> CollateralOrder get_collateral_loan_order_detail(order_id)

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
api_instance = gate_api.CollateralLoanApi(api_client)
order_id = 100001 # int | Order ID returned on successful order creation

try:
    # Get a single order
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
 **order_id** | **int**| Order ID returned on successful order creation | 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repay_collateral_loan**
> RepayResp repay_collateral_loan(repay_loan)

Repayment

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
    # Repayment
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
**200** | Operated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repay_records**
> list[RepayRecord] list_repay_records(source, borrow_currency=borrow_currency, collateral_currency=collateral_currency, page=page, limit=limit, _from=_from, to=to)

Repayment history

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
collateral_currency = 'BTC' # str | Collateral (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
_from = 1609459200 # int | Start timestamp of the query (optional)
to = 1609459200 # int | Time range ending, default to current time (optional)

try:
    # Repayment history
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
 **collateral_currency** | **str**| Collateral | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **_from** | **int**| Start timestamp of the query | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 

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
**200** | Successfully retrieved |  -  |

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
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
_from = 1609459200 # int | Start timestamp of the query (optional)
to = 1609459200 # int | Time range ending, default to current time (optional)
borrow_currency = 'USDT' # str | Borrowed currency (optional)
collateral_currency = 'BTC' # str | Collateral (optional)

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
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **_from** | **int**| Start timestamp of the query | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **borrow_currency** | **str**| Borrowed currency | [optional] 
 **collateral_currency** | **str**| Collateral | [optional] 

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
**200** | Successfully retrieved |  -  |

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
**204** | Operated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_total_amount**
> UserTotalAmount get_user_total_amount()

Query the total borrowing and collateral amount for the user

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
    # Query the total borrowing and collateral amount for the user
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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_ltv_info**
> UserLtvInfo get_user_ltv_info(collateral_currency, borrow_currency)

Query user's collateralization ratio

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
collateral_currency = 'BTC' # str | Collateral
borrow_currency = 'USDT' # str | Borrowed currency

try:
    # Query user's collateralization ratio
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
 **collateral_currency** | **str**| Collateral | 
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
**200** | Successfully retrieved |  -  |

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
loan_currency = 'BTC' # str | The parameter loan_currency is used to specify the borrowing currency. If loan_currency is not provided, the API will return all supported borrowing currencies. If loan_currency is provided, the API will return an array of collateral currencies supported for the specified borrowing currency. (optional)

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
 **loan_currency** | **str**| The parameter loan_currency is used to specify the borrowing currency. If loan_currency is not provided, the API will return all supported borrowing currencies. If loan_currency is provided, the API will return an array of collateral currencies supported for the specified borrowing currency. | [optional] 

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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

