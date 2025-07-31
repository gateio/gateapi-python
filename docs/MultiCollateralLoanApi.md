# gate_api.MultiCollateralLoanApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_multi_collateral_orders**](MultiCollateralLoanApi.md#list_multi_collateral_orders) | **GET** /loan/multi_collateral/orders | Query multi-currency collateral order list
[**create_multi_collateral**](MultiCollateralLoanApi.md#create_multi_collateral) | **POST** /loan/multi_collateral/orders | Place multi-currency collateral order
[**get_multi_collateral_order_detail**](MultiCollateralLoanApi.md#get_multi_collateral_order_detail) | **GET** /loan/multi_collateral/orders/{order_id} | Query order details
[**list_multi_repay_records**](MultiCollateralLoanApi.md#list_multi_repay_records) | **GET** /loan/multi_collateral/repay | Query multi-currency collateral repayment records
[**repay_multi_collateral_loan**](MultiCollateralLoanApi.md#repay_multi_collateral_loan) | **POST** /loan/multi_collateral/repay | Multi-currency collateral repayment
[**list_multi_collateral_records**](MultiCollateralLoanApi.md#list_multi_collateral_records) | **GET** /loan/multi_collateral/mortgage | Query collateral adjustment records
[**operate_multi_collateral**](MultiCollateralLoanApi.md#operate_multi_collateral) | **POST** /loan/multi_collateral/mortgage | Add or withdraw collateral
[**list_user_currency_quota**](MultiCollateralLoanApi.md#list_user_currency_quota) | **GET** /loan/multi_collateral/currency_quota | Query user&#39;s collateral and borrowing currency quota information
[**list_multi_collateral_currencies**](MultiCollateralLoanApi.md#list_multi_collateral_currencies) | **GET** /loan/multi_collateral/currencies | Query supported borrowing and collateral currencies for multi-currency collateral
[**get_multi_collateral_ltv**](MultiCollateralLoanApi.md#get_multi_collateral_ltv) | **GET** /loan/multi_collateral/ltv | Query collateralization ratio information
[**get_multi_collateral_fix_rate**](MultiCollateralLoanApi.md#get_multi_collateral_fix_rate) | **GET** /loan/multi_collateral/fixed_rate | Query currency&#39;s 7-day and 30-day fixed interest rates
[**get_multi_collateral_current_rate**](MultiCollateralLoanApi.md#get_multi_collateral_current_rate) | **GET** /loan/multi_collateral/current_rate | Query currency&#39;s current interest rate


# **list_multi_collateral_orders**
> list[MultiCollateralOrder] list_multi_collateral_orders(page=page, limit=limit, sort=sort, order_type=order_type)

Query multi-currency collateral order list

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
limit = 10 # int | Maximum number of records returned in a single list (optional) (default to 10)
sort = 'ltv_asc' # str | Sort type: `time_desc` - Created time descending (default), `ltv_asc` - Collateral ratio ascending, `ltv_desc` - Collateral ratio descending. (optional)
order_type = 'current' # str | Order type: current - Query current orders, fixed - Query fixed orders, defaults to current orders if not specifiedOrder type: current - Query current orders, fixed - Query fixed orders, defaults to current orders if not specified (optional)

try:
    # Query multi-currency collateral order list
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
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 10]
 **sort** | **str**| Sort type: &#x60;time_desc&#x60; - Created time descending (default), &#x60;ltv_asc&#x60; - Collateral ratio ascending, &#x60;ltv_desc&#x60; - Collateral ratio descending. | [optional] 
 **order_type** | **str**| Order type: current - Query current orders, fixed - Query fixed orders, defaults to current orders if not specifiedOrder type: current - Query current orders, fixed - Query fixed orders, defaults to current orders if not specified | [optional] 

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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multi_collateral**
> OrderResp create_multi_collateral(create_multi_collateral_order)

Place multi-currency collateral order

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
    # Place multi-currency collateral order
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
**200** | Order placed successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multi_collateral_order_detail**
> MultiCollateralOrder get_multi_collateral_order_detail(order_id)

Query order details

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
order_id = '12345' # str | Order ID returned when order is successfully created

try:
    # Query order details
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
 **order_id** | **str**| Order ID returned when order is successfully created | 

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
**200** | Order details queried successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_multi_repay_records**
> list[MultiRepayRecord] list_multi_repay_records(type, borrow_currency=borrow_currency, page=page, limit=limit, _from=_from, to=to)

Query multi-currency collateral repayment records

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
limit = 10 # int | Maximum number of records returned in a single list (optional) (default to 10)
_from = 1609459200 # int | Start timestamp for the query (optional)
to = 1609459200 # int | End timestamp for the query, defaults to current time if not specified (optional)

try:
    # Query multi-currency collateral repayment records
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
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 10]
 **_from** | **int**| Start timestamp for the query | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repay_multi_collateral_loan**
> MultiRepayResp repay_multi_collateral_loan(repay_multi_loan)

Multi-currency collateral repayment

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
    # Multi-currency collateral repayment
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
**200** | Operation successful |  -  |

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
limit = 10 # int | Maximum number of records returned in a single list (optional) (default to 10)
_from = 1609459200 # int | Start timestamp for the query (optional)
to = 1609459200 # int | End timestamp for the query, defaults to current time if not specified (optional)
collateral_currency = 'BTC' # str | Collateral currency (optional)

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
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 10]
 **_from** | **int**| Start timestamp for the query | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 
 **collateral_currency** | **str**| Collateral currency | [optional] 

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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **operate_multi_collateral**
> CollateralAdjustRes operate_multi_collateral(collateral_adjust)

Add or withdraw collateral

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
    # Add or withdraw collateral
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
**200** | Operation successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_user_currency_quota**
> list[CurrencyQuota] list_user_currency_quota(type, currency)

Query user's collateral and borrowing currency quota information

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
type = 'collateral' # str | Currency type: collateral - Collateral currency, borrow - Borrowing currency
currency = 'BTC' # str | When it is a collateral currency, multiple currencies can be provided separated by commas; when it is a borrowing currency, only one currency can be provided.

try:
    # Query user's collateral and borrowing currency quota information
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
 **type** | **str**| Currency type: collateral - Collateral currency, borrow - Borrowing currency | 
 **currency** | **str**| When it is a collateral currency, multiple currencies can be provided separated by commas; when it is a borrowing currency, only one currency can be provided. | 

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_multi_collateral_currencies**
> MultiCollateralCurrency list_multi_collateral_currencies()

Query supported borrowing and collateral currencies for multi-currency collateral

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
    # Query supported borrowing and collateral currencies for multi-currency collateral
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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multi_collateral_ltv**
> CollateralLtv get_multi_collateral_ltv()

Query collateralization ratio information

Multi-currency collateral ratio is fixed, independent of currency

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
    # Query collateralization ratio information
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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multi_collateral_fix_rate**
> list[CollateralFixRate] get_multi_collateral_fix_rate()

Query currency's 7-day and 30-day fixed interest rates

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
    # Query currency's 7-day and 30-day fixed interest rates
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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multi_collateral_current_rate**
> list[CollateralCurrentRate] get_multi_collateral_current_rate(currencies, vip_level=vip_level)

Query currency's current interest rate

Query currency's current interest rate for the previous hour, current interest rate updates hourly

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
currencies = ['[\"BTC\",\"GT\"]'] # list[str] | Specify currency name query array, separated by commas, maximum 100 items
vip_level = '0' # str | VIP level, defaults to 0 if not specified (optional) (default to '0')

try:
    # Query currency's current interest rate
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
 **currencies** | [**list[str]**](str.md)| Specify currency name query array, separated by commas, maximum 100 items | 
 **vip_level** | **str**| VIP level, defaults to 0 if not specified | [optional] [default to &#39;0&#39;]

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

