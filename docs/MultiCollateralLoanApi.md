# gate_api.MultiCollateralLoanApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_multi_collateral_orders**](MultiCollateralLoanApi.md#list_multi_collateral_orders) | **GET** /loan/multi_collateral/orders | List Multi-Collateral Orders
[**create_multi_collateral**](MultiCollateralLoanApi.md#create_multi_collateral) | **POST** /loan/multi_collateral/orders | Create Multi-Collateral Order
[**get_multi_collateral_order_detail**](MultiCollateralLoanApi.md#get_multi_collateral_order_detail) | **GET** /loan/multi_collateral/orders/{order_id} | Get Multi-Collateral Order Detail
[**list_multi_repay_records**](MultiCollateralLoanApi.md#list_multi_repay_records) | **GET** /loan/multi_collateral/repay | List Multi-Collateral Repay Records
[**repay_multi_collateral_loan**](MultiCollateralLoanApi.md#repay_multi_collateral_loan) | **POST** /loan/multi_collateral/repay | Repay Multi-Collateral Loan
[**list_multi_collateral_records**](MultiCollateralLoanApi.md#list_multi_collateral_records) | **GET** /loan/multi_collateral/mortgage | Query collateral adjustment records
[**operate_multi_collateral**](MultiCollateralLoanApi.md#operate_multi_collateral) | **POST** /loan/multi_collateral/mortgage | Operate Multi-Collateral
[**list_user_currency_quota**](MultiCollateralLoanApi.md#list_user_currency_quota) | **GET** /loan/multi_collateral/currency_quota | List User Currency Quota
[**list_multi_collateral_currencies**](MultiCollateralLoanApi.md#list_multi_collateral_currencies) | **GET** /loan/multi_collateral/currencies | Query supported borrowing and collateral currencies in Multi-Collateral 
[**get_multi_collateral_ltv**](MultiCollateralLoanApi.md#get_multi_collateral_ltv) | **GET** /loan/multi_collateral/ltv | Get Multi-Collateral ratio
[**get_multi_collateral_fix_rate**](MultiCollateralLoanApi.md#get_multi_collateral_fix_rate) | **GET** /loan/multi_collateral/fixed_rate | Query fixed interest rates for the currency for 7 days and 30 days
[**get_multi_collateral_current_rate**](MultiCollateralLoanApi.md#get_multi_collateral_current_rate) | **GET** /loan/multi_collateral/current_rate | Query the current interest rate of the currency


# **list_multi_collateral_orders**
> list[MultiCollateralOrder] list_multi_collateral_orders(page=page, limit=limit, sort=sort, order_type=order_type)

List Multi-Collateral Orders

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
api_instance = gate_api.MultiCollateralLoanApi(api_client)
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Maximum number of records to be returned in a single list (optional) (default to 10)
sort = 'ltv_asc' # str | Query the current interest rate of the currency in the previous hour (optional)
order_type = 'current' # str | Order type: current - Query current orders, fixed - Query fixed orders, defaults to current orders if not specified (optional)

try:
    # List Multi-Collateral Orders
    api_response = api_instance.list_multi_collateral_orders(page=page, limit=limit, sort=sort, order_type=order_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MultiCollateralLoanApi->list_multi_collateral_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 10]
 **sort** | **str**| Query the current interest rate of the currency in the previous hour | [optional] 
 **order_type** | **str**| Order type: current - Query current orders, fixed - Query fixed orders, defaults to current orders if not specified | [optional] 

### Return type

[**list[MultiCollateralOrder]**](MultiCollateralOrder.md)

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

# **create_multi_collateral**
> OrderResp create_multi_collateral(create_multi_collateral_order)

Create Multi-Collateral Order

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
api_instance = gate_api.MultiCollateralLoanApi(api_client)
create_multi_collateral_order = gate_api.CreateMultiCollateralOrder() # CreateMultiCollateralOrder | 

try:
    # Create Multi-Collateral Order
    api_response = api_instance.create_multi_collateral(create_multi_collateral_order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MultiCollateralLoanApi->create_multi_collateral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_multi_collateral_order** | [**CreateMultiCollateralOrder**](CreateMultiCollateralOrder.md)|  | 

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

# **get_multi_collateral_order_detail**
> MultiCollateralOrder get_multi_collateral_order_detail(order_id)

Get Multi-Collateral Order Detail

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
api_instance = gate_api.MultiCollateralLoanApi(api_client)
order_id = '12345' # str | Order ID returned on successful order creation

try:
    # Get Multi-Collateral Order Detail
    api_response = api_instance.get_multi_collateral_order_detail(order_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MultiCollateralLoanApi->get_multi_collateral_order_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID returned on successful order creation | 

### Return type

[**MultiCollateralOrder**](MultiCollateralOrder.md)

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

# **list_multi_repay_records**
> list[MultiRepayRecord] list_multi_repay_records(type, borrow_currency=borrow_currency, page=page, limit=limit, _from=_from, to=to)

List Multi-Collateral Repay Records

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
api_instance = gate_api.MultiCollateralLoanApi(api_client)
type = 'repay' # str | Operation type: repay - Regular repayment, liquidate - Liquidation
borrow_currency = 'USDT' # str | Borrowed currency (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Maximum number of records to be returned in a single list (optional) (default to 10)
_from = 1609459200 # int | Start timestamp of the query (optional)
to = 1609459200 # int | Time range ending, default to current time (optional)

try:
    # List Multi-Collateral Repay Records
    api_response = api_instance.list_multi_repay_records(type, borrow_currency=borrow_currency, page=page, limit=limit, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MultiCollateralLoanApi->list_multi_repay_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Operation type: repay - Regular repayment, liquidate - Liquidation | 
 **borrow_currency** | **str**| Borrowed currency | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 10]
 **_from** | **int**| Start timestamp of the query | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 

### Return type

[**list[MultiRepayRecord]**](MultiRepayRecord.md)

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

# **repay_multi_collateral_loan**
> MultiRepayResp repay_multi_collateral_loan(repay_multi_loan)

Repay Multi-Collateral Loan

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
api_instance = gate_api.MultiCollateralLoanApi(api_client)
repay_multi_loan = gate_api.RepayMultiLoan() # RepayMultiLoan | 

try:
    # Repay Multi-Collateral Loan
    api_response = api_instance.repay_multi_collateral_loan(repay_multi_loan)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MultiCollateralLoanApi->repay_multi_collateral_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repay_multi_loan** | [**RepayMultiLoan**](RepayMultiLoan.md)|  | 

### Return type

[**MultiRepayResp**](MultiRepayResp.md)

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

# **list_multi_collateral_records**
> list[MultiCollateralRecord] list_multi_collateral_records(page=page, limit=limit, _from=_from, to=to, collateral_currency=collateral_currency)

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
api_instance = gate_api.MultiCollateralLoanApi(api_client)
page = 1 # int | Page number (optional) (default to 1)
limit = 10 # int | Maximum number of records to be returned in a single list (optional) (default to 10)
_from = 1609459200 # int | Start timestamp of the query (optional)
to = 1609459200 # int | Time range ending, default to current time (optional)
collateral_currency = 'BTC' # str | Collateral (optional)

try:
    # Query collateral adjustment records
    api_response = api_instance.list_multi_collateral_records(page=page, limit=limit, _from=_from, to=to, collateral_currency=collateral_currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MultiCollateralLoanApi->list_multi_collateral_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 10]
 **_from** | **int**| Start timestamp of the query | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **collateral_currency** | **str**| Collateral | [optional] 

### Return type

[**list[MultiCollateralRecord]**](MultiCollateralRecord.md)

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

# **operate_multi_collateral**
> CollateralAdjustRes operate_multi_collateral(collateral_adjust)

Operate Multi-Collateral

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
api_instance = gate_api.MultiCollateralLoanApi(api_client)
collateral_adjust = gate_api.CollateralAdjust() # CollateralAdjust | 

try:
    # Operate Multi-Collateral
    api_response = api_instance.operate_multi_collateral(collateral_adjust)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MultiCollateralLoanApi->operate_multi_collateral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collateral_adjust** | [**CollateralAdjust**](CollateralAdjust.md)|  | 

### Return type

[**CollateralAdjustRes**](CollateralAdjustRes.md)

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

# **list_user_currency_quota**
> list[CurrencyQuota] list_user_currency_quota(type, currency)

List User Currency Quota

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
api_instance = gate_api.MultiCollateralLoanApi(api_client)
type = 'collateral' # str | Currency type: collateral - Collateral currency, borrow - Borrowing 
currency = 'BTC' # str | When it is a collateral currency, multiple currencies can be passed separated by commas;when it is a borrowing currency, only one currenc

try:
    # List User Currency Quota
    api_response = api_instance.list_user_currency_quota(type, currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MultiCollateralLoanApi->list_user_currency_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Currency type: collateral - Collateral currency, borrow - Borrowing  | 
 **currency** | **str**| When it is a collateral currency, multiple currencies can be passed separated by commas;when it is a borrowing currency, only one currenc | 

### Return type

[**list[CurrencyQuota]**](CurrencyQuota.md)

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

# **list_multi_collateral_currencies**
> MultiCollateralCurrency list_multi_collateral_currencies()

Query supported borrowing and collateral currencies in Multi-Collateral 

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
api_instance = gate_api.MultiCollateralLoanApi(api_client)

try:
    # Query supported borrowing and collateral currencies in Multi-Collateral 
    api_response = api_instance.list_multi_collateral_currencies()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MultiCollateralLoanApi->list_multi_collateral_currencies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**MultiCollateralCurrency**](MultiCollateralCurrency.md)

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

# **get_multi_collateral_ltv**
> CollateralLtv get_multi_collateral_ltv()

Get Multi-Collateral ratio

The Multi-Collateral ratio is fixed, irrespective of the currency.

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
api_instance = gate_api.MultiCollateralLoanApi(api_client)

try:
    # Get Multi-Collateral ratio
    api_response = api_instance.get_multi_collateral_ltv()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MultiCollateralLoanApi->get_multi_collateral_ltv: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CollateralLtv**](CollateralLtv.md)

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

# **get_multi_collateral_fix_rate**
> list[CollateralFixRate] get_multi_collateral_fix_rate()

Query fixed interest rates for the currency for 7 days and 30 days

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
api_instance = gate_api.MultiCollateralLoanApi(api_client)

try:
    # Query fixed interest rates for the currency for 7 days and 30 days
    api_response = api_instance.get_multi_collateral_fix_rate()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MultiCollateralLoanApi->get_multi_collateral_fix_rate: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CollateralFixRate]**](CollateralFixRate.md)

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

# **get_multi_collateral_current_rate**
> list[CollateralCurrentRate] get_multi_collateral_current_rate(currencies, vip_level=vip_level)

Query the current interest rate of the currency

Query the current interest rate of the currency in the previous hour.

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
api_instance = gate_api.MultiCollateralLoanApi(api_client)
currencies = ['[\"BTC\",\"GT\"]'] # list[str] | Specify currency name query array, separated by commas, maximum 100items.
vip_level = '0' # str | VIP level, defaults to 0 if not transferred (optional) (default to '0')

try:
    # Query the current interest rate of the currency
    api_response = api_instance.get_multi_collateral_current_rate(currencies, vip_level=vip_level)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MultiCollateralLoanApi->get_multi_collateral_current_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencies** | [**list[str]**](str.md)| Specify currency name query array, separated by commas, maximum 100items. | 
 **vip_level** | **str**| VIP level, defaults to 0 if not transferred | [optional] [default to &#39;0&#39;]

### Return type

[**list[CollateralCurrentRate]**](CollateralCurrentRate.md)

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

