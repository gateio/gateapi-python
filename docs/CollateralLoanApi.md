# gate_api.CollateralLoanApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_collateral_loan_orders**](CollateralLoanApi.md#list_collateral_loan_orders) | **GET** /loan/collateral/orders | 查询抵押借币订单列表
[**create_collateral_loan**](CollateralLoanApi.md#create_collateral_loan) | **POST** /loan/collateral/orders | 抵押借币借贷下单
[**get_collateral_loan_order_detail**](CollateralLoanApi.md#get_collateral_loan_order_detail) | **GET** /loan/collateral/orders/{order_id} | Get a single order
[**repay_collateral_loan**](CollateralLoanApi.md#repay_collateral_loan) | **POST** /loan/collateral/repay | 抵押借币还款
[**list_repay_records**](CollateralLoanApi.md#list_repay_records) | **GET** /loan/collateral/repay_records | 查询抵押借币还款记录
[**list_collateral_records**](CollateralLoanApi.md#list_collateral_records) | **GET** /loan/collateral/collaterals | 查询质押物调整记录
[**operate_collateral**](CollateralLoanApi.md#operate_collateral) | **POST** /loan/collateral/collaterals | 增加或赎回质押物
[**get_user_total_amount**](CollateralLoanApi.md#get_user_total_amount) | **GET** /loan/collateral/total_amount | 查询用户总借贷与质押数量
[**get_user_ltv_info**](CollateralLoanApi.md#get_user_ltv_info) | **GET** /loan/collateral/ltv | 查询用户质押率和可借剩余币种
[**list_collateral_currencies**](CollateralLoanApi.md#list_collateral_currencies) | **GET** /loan/collateral/currencies | 查询支持的借款币种和抵押币种


# **list_collateral_loan_orders**
> list[CollateralOrder] list_collateral_loan_orders(page=page, limit=limit, collateral_currency=collateral_currency, borrow_currency=borrow_currency)

查询抵押借币订单列表

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
collateral_currency = 'BTC' # str | 质押币种 (optional)
borrow_currency = 'USDT' # str | 借款币种 (optional)

try:
    # 查询抵押借币订单列表
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
 **collateral_currency** | **str**| 质押币种 | [optional] 
 **borrow_currency** | **str**| 借款币种 | [optional] 

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

抵押借币借贷下单

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
    # 抵押借币借贷下单
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
**200** | 下单成功 |  -  |

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
**200** | 订单详情查询成功 |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repay_collateral_loan**
> RepayResp repay_collateral_loan(repay_loan)

抵押借币还款

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
    # 抵押借币还款
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

查询抵押借币还款记录

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
source = 'repay' # str | 操作类型 ;  repay - 普通还款, liquidate - 平仓
borrow_currency = 'USDT' # str | 借款币种 (optional)
collateral_currency = 'BTC' # str | 质押币种 (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
_from = 1609459200 # int | Start timestamp of the query (optional)
to = 1609459200 # int | Time range ending, default to current time (optional)

try:
    # 查询抵押借币还款记录
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
 **source** | **str**| 操作类型 ;  repay - 普通还款, liquidate - 平仓 | 
 **borrow_currency** | **str**| 借款币种 | [optional] 
 **collateral_currency** | **str**| 质押币种 | [optional] 
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

查询质押物调整记录

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
borrow_currency = 'USDT' # str | 借款币种 (optional)
collateral_currency = 'BTC' # str | 质押币种 (optional)

try:
    # 查询质押物调整记录
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
 **borrow_currency** | **str**| 借款币种 | [optional] 
 **collateral_currency** | **str**| 质押币种 | [optional] 

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

增加或赎回质押物

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
    # 增加或赎回质押物
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

查询用户总借贷与质押数量

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
    # 查询用户总借贷与质押数量
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

查询用户质押率和可借剩余币种

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
collateral_currency = 'BTC' # str | 质押币种
borrow_currency = 'USDT' # str | 借款币种

try:
    # 查询用户质押率和可借剩余币种
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
 **collateral_currency** | **str**| 质押币种 | 
 **borrow_currency** | **str**| 借款币种 | 

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

查询支持的借款币种和抵押币种

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
loan_currency = 'BTC' # str | 借款币种参数,当loan_currency没传时会返回支持的所有借款币种,当传loan_currency时会查询该借款币种支持的抵押币种数组 (optional)

try:
    # 查询支持的借款币种和抵押币种
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
 **loan_currency** | **str**| 借款币种参数,当loan_currency没传时会返回支持的所有借款币种,当传loan_currency时会查询该借款币种支持的抵押币种数组 | [optional] 

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

