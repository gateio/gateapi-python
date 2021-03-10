# gate_api.MarginApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_margin_currency_pairs**](MarginApi.md#list_margin_currency_pairs) | **GET** /margin/currency_pairs | List all supported currency pairs supported in margin trading
[**get_margin_currency_pair**](MarginApi.md#get_margin_currency_pair) | **GET** /margin/currency_pairs/{currency_pair} | Query one single margin currency pair
[**list_funding_book**](MarginApi.md#list_funding_book) | **GET** /margin/funding_book | Order book of lending loans
[**list_margin_accounts**](MarginApi.md#list_margin_accounts) | **GET** /margin/accounts | Margin account list
[**list_margin_account_book**](MarginApi.md#list_margin_account_book) | **GET** /margin/account_book | List margin account balance change history
[**list_funding_accounts**](MarginApi.md#list_funding_accounts) | **GET** /margin/funding_accounts | Funding account list
[**list_loans**](MarginApi.md#list_loans) | **GET** /margin/loans | List all loans
[**create_loan**](MarginApi.md#create_loan) | **POST** /margin/loans | Lend or borrow
[**merge_loans**](MarginApi.md#merge_loans) | **POST** /margin/merged_loans | Merge multiple lending loans
[**get_loan**](MarginApi.md#get_loan) | **GET** /margin/loans/{loan_id} | Retrieve one single loan detail
[**cancel_loan**](MarginApi.md#cancel_loan) | **DELETE** /margin/loans/{loan_id} | Cancel lending loan
[**update_loan**](MarginApi.md#update_loan) | **PATCH** /margin/loans/{loan_id} | Modify a loan
[**list_loan_repayments**](MarginApi.md#list_loan_repayments) | **GET** /margin/loans/{loan_id}/repayment | List loan repayment records
[**repay_loan**](MarginApi.md#repay_loan) | **POST** /margin/loans/{loan_id}/repayment | Repay a loan
[**list_loan_records**](MarginApi.md#list_loan_records) | **GET** /margin/loan_records | List repayment records of specified loan
[**get_loan_record**](MarginApi.md#get_loan_record) | **GET** /margin/loan_records/{loan_record_id} | Get one single loan record
[**update_loan_record**](MarginApi.md#update_loan_record) | **PATCH** /margin/loan_records/{loan_record_id} | Modify a loan record
[**get_auto_repay_status**](MarginApi.md#get_auto_repay_status) | **GET** /margin/auto_repay | Retrieve user auto repayment setting
[**set_auto_repay**](MarginApi.md#set_auto_repay) | **POST** /margin/auto_repay | Update user&#39;s auto repayment setting


# **list_margin_currency_pairs**
> list[MarginCurrencyPair] list_margin_currency_pairs()

List all supported currency pairs supported in margin trading

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
api_instance = gate_api.MarginApi(api_client)

try:
    # List all supported currency pairs supported in margin trading
    api_response = api_instance.list_margin_currency_pairs()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->list_margin_currency_pairs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[MarginCurrencyPair]**](MarginCurrencyPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_margin_currency_pair**
> MarginCurrencyPair get_margin_currency_pair(currency_pair)

Query one single margin currency pair

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
api_instance = gate_api.MarginApi(api_client)
currency_pair = 'BTC_USDT' # str | Margin currency pair

try:
    # Query one single margin currency pair
    api_response = api_instance.get_margin_currency_pair(currency_pair)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->get_margin_currency_pair: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Margin currency pair | 

### Return type

[**MarginCurrencyPair**](MarginCurrencyPair.md)

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

# **list_funding_book**
> list[FundingBookItem] list_funding_book(currency)

Order book of lending loans

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
api_instance = gate_api.MarginApi(api_client)
currency = 'BTC' # str | Retrieved specified currency related data

try:
    # Order book of lending loans
    api_response = api_instance.list_funding_book(currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->list_funding_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieved specified currency related data | 

### Return type

[**list[FundingBookItem]**](FundingBookItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order book retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_margin_accounts**
> list[MarginAccount] list_margin_accounts(currency_pair=currency_pair)

Margin account list

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
api_instance = gate_api.MarginApi(api_client)
currency_pair = 'BTC_USDT' # str | Currency pair (optional)

try:
    # Margin account list
    api_response = api_instance.list_margin_accounts(currency_pair=currency_pair)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->list_margin_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Currency pair | [optional] 

### Return type

[**list[MarginAccount]**](MarginAccount.md)

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

# **list_margin_account_book**
> list[MarginAccountBook] list_margin_account_book(currency=currency, currency_pair=currency_pair, _from=_from, to=to, page=page, limit=limit)

List margin account balance change history

Only transferring from or to margin account are provided for now. Time range allows 30 days at most

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
api_instance = gate_api.MarginApi(api_client)
currency = 'currency_example' # str | List records related to specified currency only. If specified, `currency_pair` is also required. (optional)
currency_pair = 'currency_pair_example' # str | List records related to specified currency pair. Used in combination with `currency`. Ignored if `currency` is not provided (optional)
_from = 56 # int | Time range beginning, default to 7 days before current time (optional)
to = 56 # int | Time range ending, default to current time (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records returned in one list (optional) (default to 100)

try:
    # List margin account balance change history
    api_response = api_instance.list_margin_account_book(currency=currency, currency_pair=currency_pair, _from=_from, to=to, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->list_margin_account_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| List records related to specified currency only. If specified, &#x60;currency_pair&#x60; is also required. | [optional] 
 **currency_pair** | **str**| List records related to specified currency pair. Used in combination with &#x60;currency&#x60;. Ignored if &#x60;currency&#x60; is not provided | [optional] 
 **_from** | **int**| Time range beginning, default to 7 days before current time | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records returned in one list | [optional] [default to 100]

### Return type

[**list[MarginAccountBook]**](MarginAccountBook.md)

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

# **list_funding_accounts**
> list[FundingAccount] list_funding_accounts(currency=currency)

Funding account list

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
api_instance = gate_api.MarginApi(api_client)
currency = 'BTC' # str | Retrieved specified currency related data (optional)

try:
    # Funding account list
    api_response = api_instance.list_funding_accounts(currency=currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->list_funding_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieved specified currency related data | [optional] 

### Return type

[**list[FundingAccount]**](FundingAccount.md)

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

# **list_loans**
> list[Loan] list_loans(status, side, currency=currency, currency_pair=currency_pair, sort_by=sort_by, reverse_sort=reverse_sort, page=page, limit=limit)

List all loans

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
api_instance = gate_api.MarginApi(api_client)
status = 'open' # str | Loan status
side = 'lend' # str | Lend or borrow
currency = 'BTC' # str | Retrieved specified currency related data (optional)
currency_pair = 'BTC_USDT' # str | Currency pair (optional)
sort_by = 'rate' # str | Specify which field is used to sort. `create_time` or `rate` is supported. Default to `create_time` (optional)
reverse_sort = false # bool | Whether to sort in descending order. Default to `true` (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records returned in one list (optional) (default to 100)

try:
    # List all loans
    api_response = api_instance.list_loans(status, side, currency=currency, currency_pair=currency_pair, sort_by=sort_by, reverse_sort=reverse_sort, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->list_loans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Loan status | 
 **side** | **str**| Lend or borrow | 
 **currency** | **str**| Retrieved specified currency related data | [optional] 
 **currency_pair** | **str**| Currency pair | [optional] 
 **sort_by** | **str**| Specify which field is used to sort. &#x60;create_time&#x60; or &#x60;rate&#x60; is supported. Default to &#x60;create_time&#x60; | [optional] 
 **reverse_sort** | **bool**| Whether to sort in descending order. Default to &#x60;true&#x60; | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records returned in one list | [optional] [default to 100]

### Return type

[**list[Loan]**](Loan.md)

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

# **create_loan**
> Loan create_loan(loan)

Lend or borrow

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
api_instance = gate_api.MarginApi(api_client)
loan = gate_api.Loan() # Loan | 

try:
    # Lend or borrow
    api_response = api_instance.create_loan(loan)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->create_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan** | [**Loan**](Loan.md)|  | 

### Return type

[**Loan**](Loan.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Loan created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_loans**
> Loan merge_loans(currency, ids)

Merge multiple lending loans

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
api_instance = gate_api.MarginApi(api_client)
currency = 'BTC' # str | Retrieved specified currency related data
ids = '123,234,345' # str | Lending loan ID list separated by `,`. Maximum of 20 IDs are allowed in one request

try:
    # Merge multiple lending loans
    api_response = api_instance.merge_loans(currency, ids)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->merge_loans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieved specified currency related data | 
 **ids** | **str**| Lending loan ID list separated by &#x60;,&#x60;. Maximum of 20 IDs are allowed in one request | 

### Return type

[**Loan**](Loan.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Loans merged |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan**
> Loan get_loan(loan_id, side)

Retrieve one single loan detail

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
api_instance = gate_api.MarginApi(api_client)
loan_id = '12345' # str | Loan ID
side = 'lend' # str | Lend or borrow

try:
    # Retrieve one single loan detail
    api_response = api_instance.get_loan(loan_id, side)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->get_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **str**| Loan ID | 
 **side** | **str**| Lend or borrow | 

### Return type

[**Loan**](Loan.md)

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

# **cancel_loan**
> Loan cancel_loan(loan_id, currency)

Cancel lending loan

Only lending loans can be cancelled

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
api_instance = gate_api.MarginApi(api_client)
loan_id = '12345' # str | Loan ID
currency = 'BTC' # str | Retrieved specified currency related data

try:
    # Cancel lending loan
    api_response = api_instance.cancel_loan(loan_id, currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->cancel_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **str**| Loan ID | 
 **currency** | **str**| Retrieved specified currency related data | 

### Return type

[**Loan**](Loan.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Order cancelled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan**
> Loan update_loan(loan_id, loan_patch)

Modify a loan

Only `auto_renew` modification is supported currently

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
api_instance = gate_api.MarginApi(api_client)
loan_id = '12345' # str | Loan ID
loan_patch = gate_api.LoanPatch() # LoanPatch | 

try:
    # Modify a loan
    api_response = api_instance.update_loan(loan_id, loan_patch)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->update_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **str**| Loan ID | 
 **loan_patch** | [**LoanPatch**](LoanPatch.md)|  | 

### Return type

[**Loan**](Loan.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loan_repayments**
> list[Repayment] list_loan_repayments(loan_id)

List loan repayment records

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
api_instance = gate_api.MarginApi(api_client)
loan_id = '12345' # str | Loan ID

try:
    # List loan repayment records
    api_response = api_instance.list_loan_repayments(loan_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->list_loan_repayments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **str**| Loan ID | 

### Return type

[**list[Repayment]**](Repayment.md)

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

# **repay_loan**
> Loan repay_loan(loan_id, repay_request)

Repay a loan

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
api_instance = gate_api.MarginApi(api_client)
loan_id = '12345' # str | Loan ID
repay_request = gate_api.RepayRequest() # RepayRequest | 

try:
    # Repay a loan
    api_response = api_instance.repay_loan(loan_id, repay_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->repay_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **str**| Loan ID | 
 **repay_request** | [**RepayRequest**](RepayRequest.md)|  | 

### Return type

[**Loan**](Loan.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Loan repaid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loan_records**
> list[LoanRecord] list_loan_records(loan_id, status=status, page=page, limit=limit)

List repayment records of specified loan

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
api_instance = gate_api.MarginApi(api_client)
loan_id = '12345' # str | Loan ID
status = 'loaned' # str | Loan record status (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records returned in one list (optional) (default to 100)

try:
    # List repayment records of specified loan
    api_response = api_instance.list_loan_records(loan_id, status=status, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->list_loan_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **str**| Loan ID | 
 **status** | **str**| Loan record status | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records returned in one list | [optional] [default to 100]

### Return type

[**list[LoanRecord]**](LoanRecord.md)

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

# **get_loan_record**
> LoanRecord get_loan_record(loan_record_id, loan_id)

Get one single loan record

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
api_instance = gate_api.MarginApi(api_client)
loan_record_id = '12345' # str | Loan record ID
loan_id = '12345' # str | Loan ID

try:
    # Get one single loan record
    api_response = api_instance.get_loan_record(loan_record_id, loan_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->get_loan_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_record_id** | **str**| Loan record ID | 
 **loan_id** | **str**| Loan ID | 

### Return type

[**LoanRecord**](LoanRecord.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detail retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan_record**
> LoanRecord update_loan_record(loan_record_id, loan_patch)

Modify a loan record

Only `auto_renew` modification is supported currently

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
api_instance = gate_api.MarginApi(api_client)
loan_record_id = '12345' # str | Loan record ID
loan_patch = gate_api.LoanPatch() # LoanPatch | 

try:
    # Modify a loan record
    api_response = api_instance.update_loan_record(loan_record_id, loan_patch)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->update_loan_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_record_id** | **str**| Loan record ID | 
 **loan_patch** | [**LoanPatch**](LoanPatch.md)|  | 

### Return type

[**LoanRecord**](LoanRecord.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Loan record updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auto_repay_status**
> AutoRepaySetting get_auto_repay_status()

Retrieve user auto repayment setting

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
api_instance = gate_api.MarginApi(api_client)

try:
    # Retrieve user auto repayment setting
    api_response = api_instance.get_auto_repay_status()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->get_auto_repay_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AutoRepaySetting**](AutoRepaySetting.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current auto repayment setting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_auto_repay**
> AutoRepaySetting set_auto_repay(status)

Update user's auto repayment setting

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
api_instance = gate_api.MarginApi(api_client)
status = 'true' # str | New auto repayment status. `on` - enabled, `off` - disabled

try:
    # Update user's auto repayment setting
    api_response = api_instance.set_auto_repay(status)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->set_auto_repay: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| New auto repayment status. &#x60;on&#x60; - enabled, &#x60;off&#x60; - disabled | 

### Return type

[**AutoRepaySetting**](AutoRepaySetting.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current auto repayment setting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

