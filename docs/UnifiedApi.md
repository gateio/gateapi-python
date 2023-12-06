# gate_api.UnifiedApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_unified_accounts**](UnifiedApi.md#list_unified_accounts) | **GET** /unified/accounts | Get unified account information
[**list_unified_account_mode**](UnifiedApi.md#list_unified_account_mode) | **GET** /unified/account_mode | Query mode of the unified account
[**set_unified_account_mode**](UnifiedApi.md#set_unified_account_mode) | **POST** /unified/account_mode | Set mode of the unified account
[**get_unified_borrowable**](UnifiedApi.md#get_unified_borrowable) | **GET** /unified/borrowable | Query about the maximum borrowing for the unified account
[**get_unified_transferable**](UnifiedApi.md#get_unified_transferable) | **GET** /unified/transferable | Query about the maximum transferable for the unified account
[**list_unified_loans**](UnifiedApi.md#list_unified_loans) | **GET** /unified/loans | List loans
[**create_unified_loan**](UnifiedApi.md#create_unified_loan) | **POST** /unified/loans | Borrow or repay
[**list_unified_loan_records**](UnifiedApi.md#list_unified_loan_records) | **GET** /unified/loan_records | Get load records
[**list_unified_loan_interest_records**](UnifiedApi.md#list_unified_loan_interest_records) | **GET** /unified/interest_records | List interest records


# **list_unified_accounts**
> UnifiedAccount list_unified_accounts(currency=currency)

Get unified account information

The assets of each currency in the account will be adjusted according to their liquidity, defined by corresponding adjustment coefficients, and then uniformly converted to USD to calculate the total asset value and position value of the account.  You can refer to the [Formula](#portfolio-account) in the documentation

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
api_instance = gate_api.UnifiedApi(api_client)
currency = 'BTC' # str | Retrieve data of the specified currency (optional)

try:
    # Get unified account information
    api_response = api_instance.list_unified_accounts(currency=currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->list_unified_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | [optional] 

### Return type

[**UnifiedAccount**](UnifiedAccount.md)

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

# **list_unified_account_mode**
> dict(str, bool) list_unified_account_mode()

Query mode of the unified account

cross_margin - cross margin, usdt_futures - usdt futures

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
api_instance = gate_api.UnifiedApi(api_client)

try:
    # Query mode of the unified account
    api_response = api_instance.list_unified_account_mode()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->list_unified_account_mode: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**dict(str, bool)**

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

# **set_unified_account_mode**
> dict(str, bool) set_unified_account_mode(unified_mode)

Set mode of the unified account

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
api_instance = gate_api.UnifiedApi(api_client)
unified_mode = gate_api.UnifiedMode() # UnifiedMode | 

try:
    # Set mode of the unified account
    api_response = api_instance.set_unified_account_mode(unified_mode)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->set_unified_account_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unified_mode** | [**UnifiedMode**](UnifiedMode.md)|  | 

### Return type

**dict(str, bool)**

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

# **get_unified_borrowable**
> UnifiedBorrowable get_unified_borrowable(currency)

Query about the maximum borrowing for the unified account

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
api_instance = gate_api.UnifiedApi(api_client)
currency = 'BTC' # str | Retrieve data of the specified currency

try:
    # Query about the maximum borrowing for the unified account
    api_response = api_instance.get_unified_borrowable(currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->get_unified_borrowable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | 

### Return type

[**UnifiedBorrowable**](UnifiedBorrowable.md)

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

# **get_unified_transferable**
> UnifiedTransferable get_unified_transferable(currency)

Query about the maximum transferable for the unified account

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
api_instance = gate_api.UnifiedApi(api_client)
currency = 'BTC' # str | Retrieve data of the specified currency

try:
    # Query about the maximum transferable for the unified account
    api_response = api_instance.get_unified_transferable(currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->get_unified_transferable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | 

### Return type

[**UnifiedTransferable**](UnifiedTransferable.md)

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

# **list_unified_loans**
> list[UniLoan] list_unified_loans(currency=currency, page=page, limit=limit)

List loans

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
api_instance = gate_api.UnifiedApi(api_client)
currency = 'BTC' # str | Retrieve data of the specified currency (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum response items.  Default: 100, minimum: 1, Maximum: 100 (optional) (default to 100)

try:
    # List loans
    api_response = api_instance.list_unified_loans(currency=currency, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->list_unified_loans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum response items.  Default: 100, minimum: 1, Maximum: 100 | [optional] [default to 100]

### Return type

[**list[UniLoan]**](UniLoan.md)

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

# **create_unified_loan**
> create_unified_loan(unified_loan)

Borrow or repay

When borrowing, it is essential to ensure that the borrowed amount is not below the minimum borrowing threshold for the specific cryptocurrency and does not exceed the maximum borrowing limit set by the platform and the user.  The interest on the loan will be automatically deducted from the account at regular intervals. It is the user's responsibility to manage the repayment of the borrowed amount.  For repayment, the option to repay the entire borrowed amount is available by setting the parameter `repaid_all=true`

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
api_instance = gate_api.UnifiedApi(api_client)
unified_loan = gate_api.UnifiedLoan() # UnifiedLoan | 

try:
    # Borrow or repay
    api_instance.create_unified_loan(unified_loan)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->create_unified_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unified_loan** | [**UnifiedLoan**](UnifiedLoan.md)|  | 

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

# **list_unified_loan_records**
> list[UnifiedLoanRecord] list_unified_loan_records(type=type, currency=currency, page=page, limit=limit)

Get load records

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
api_instance = gate_api.UnifiedApi(api_client)
type = 'type_example' # str | The types of lending records, borrow - indicates the action of borrowing funds, repay - indicates the action of repaying the borrowed funds (optional)
currency = 'BTC' # str | Retrieve data of the specified currency (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum response items.  Default: 100, minimum: 1, Maximum: 100 (optional) (default to 100)

try:
    # Get load records
    api_response = api_instance.list_unified_loan_records(type=type, currency=currency, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->list_unified_loan_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The types of lending records, borrow - indicates the action of borrowing funds, repay - indicates the action of repaying the borrowed funds | [optional] 
 **currency** | **str**| Retrieve data of the specified currency | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum response items.  Default: 100, minimum: 1, Maximum: 100 | [optional] [default to 100]

### Return type

[**list[UnifiedLoanRecord]**](UnifiedLoanRecord.md)

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

# **list_unified_loan_interest_records**
> list[UniLoanInterestRecord] list_unified_loan_interest_records(currency=currency, page=page, limit=limit)

List interest records

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
api_instance = gate_api.UnifiedApi(api_client)
currency = 'BTC' # str | Retrieve data of the specified currency (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum response items.  Default: 100, minimum: 1, Maximum: 100 (optional) (default to 100)

try:
    # List interest records
    api_response = api_instance.list_unified_loan_interest_records(currency=currency, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->list_unified_loan_interest_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum response items.  Default: 100, minimum: 1, Maximum: 100 | [optional] [default to 100]

### Return type

[**list[UniLoanInterestRecord]**](UniLoanInterestRecord.md)

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

