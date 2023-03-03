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
[**list_loan_records**](MarginApi.md#list_loan_records) | **GET** /margin/loan_records | List repayment records of a specific loan
[**get_loan_record**](MarginApi.md#get_loan_record) | **GET** /margin/loan_records/{loan_record_id} | Get one single loan record
[**update_loan_record**](MarginApi.md#update_loan_record) | **PATCH** /margin/loan_records/{loan_record_id} | Modify a loan record
[**get_auto_repay_status**](MarginApi.md#get_auto_repay_status) | **GET** /margin/auto_repay | Retrieve user auto repayment setting
[**set_auto_repay**](MarginApi.md#set_auto_repay) | **POST** /margin/auto_repay | Update user&#39;s auto repayment setting
[**get_margin_transferable**](MarginApi.md#get_margin_transferable) | **GET** /margin/transferable | Get the max transferable amount for a specific margin currency
[**get_margin_borrowable**](MarginApi.md#get_margin_borrowable) | **GET** /margin/borrowable | Get the max borrowable amount for a specific margin currency
[**list_cross_margin_currencies**](MarginApi.md#list_cross_margin_currencies) | **GET** /margin/cross/currencies | Currencies supported by cross margin.
[**get_cross_margin_currency**](MarginApi.md#get_cross_margin_currency) | **GET** /margin/cross/currencies/{currency} | Retrieve detail of one single currency supported by cross margin
[**get_cross_margin_account**](MarginApi.md#get_cross_margin_account) | **GET** /margin/cross/accounts | Retrieve cross margin account
[**list_cross_margin_account_book**](MarginApi.md#list_cross_margin_account_book) | **GET** /margin/cross/account_book | Retrieve cross margin account change history
[**list_cross_margin_loans**](MarginApi.md#list_cross_margin_loans) | **GET** /margin/cross/loans | List cross margin borrow history
[**create_cross_margin_loan**](MarginApi.md#create_cross_margin_loan) | **POST** /margin/cross/loans | Create a cross margin borrow loan
[**get_cross_margin_loan**](MarginApi.md#get_cross_margin_loan) | **GET** /margin/cross/loans/{loan_id} | Retrieve single borrow loan detail
[**list_cross_margin_repayments**](MarginApi.md#list_cross_margin_repayments) | **GET** /margin/cross/repayments | Retrieve cross margin repayments
[**repay_cross_margin_loan**](MarginApi.md#repay_cross_margin_loan) | **POST** /margin/cross/repayments | Cross margin repayments
[**get_cross_margin_transferable**](MarginApi.md#get_cross_margin_transferable) | **GET** /margin/cross/transferable | Get the max transferable amount for a specific cross margin currency
[**get_cross_margin_borrowable**](MarginApi.md#get_cross_margin_borrowable) | **GET** /margin/cross/borrowable | Get the max borrowable amount for a specific cross margin currency


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
currency = 'BTC' # str | Retrieve data of the specified currency

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
 **currency** | **str**| Retrieve data of the specified currency | 

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

Only transferals from and to margin account are provided for now. Time range allows 30 days at most

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
_from = 1627706330 # int | Start timestamp of the query (optional)
to = 1635329650 # int | Time range ending, default to current time (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)

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
 **_from** | **int**| Start timestamp of the query | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]

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
currency = 'BTC' # str | Retrieve data of the specified currency (optional)

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
 **currency** | **str**| Retrieve data of the specified currency | [optional] 

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
currency = 'BTC' # str | Retrieve data of the specified currency (optional)
currency_pair = 'BTC_USDT' # str | Currency pair (optional)
sort_by = 'rate' # str | Specify which field is used to sort. `create_time` or `rate` is supported. Default to `create_time` (optional)
reverse_sort = false # bool | Whether to sort in descending order. Default to `true` (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)

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
 **currency** | **str**| Retrieve data of the specified currency | [optional] 
 **currency_pair** | **str**| Currency pair | [optional] 
 **sort_by** | **str**| Specify which field is used to sort. &#x60;create_time&#x60; or &#x60;rate&#x60; is supported. Default to &#x60;create_time&#x60; | [optional] 
 **reverse_sort** | **bool**| Whether to sort in descending order. Default to &#x60;true&#x60; | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]

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
currency = 'BTC' # str | Retrieve data of the specified currency
ids = '123,234,345' # str | A comma-separated (,) list of IDs of the loans lent. Maximum of 20 IDs are allowed in a request

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
 **currency** | **str**| Retrieve data of the specified currency | 
 **ids** | **str**| A comma-separated (,) list of IDs of the loans lent. Maximum of 20 IDs are allowed in a request | 

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

Only lent loans can be cancelled

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
currency = 'BTC' # str | Retrieve data of the specified currency

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
 **currency** | **str**| Retrieve data of the specified currency | 

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

List repayment records of a specific loan

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
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)

try:
    # List repayment records of a specific loan
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
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]

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
status = 'on' # str | New auto repayment status. `on` - enabled, `off` - disabled

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

# **get_margin_transferable**
> MarginTransferable get_margin_transferable(currency, currency_pair=currency_pair)

Get the max transferable amount for a specific margin currency

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
currency = 'BTC' # str | Retrieve data of the specified currency
currency_pair = 'BTC_USDT' # str | Currency pair (optional)

try:
    # Get the max transferable amount for a specific margin currency
    api_response = api_instance.get_margin_transferable(currency, currency_pair=currency_pair)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->get_margin_transferable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | 
 **currency_pair** | **str**| Currency pair | [optional] 

### Return type

[**MarginTransferable**](MarginTransferable.md)

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

# **get_margin_borrowable**
> MarginBorrowable get_margin_borrowable(currency, currency_pair=currency_pair)

Get the max borrowable amount for a specific margin currency

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
currency = 'BTC' # str | Retrieve data of the specified currency
currency_pair = 'BTC_USDT' # str | Currency pair (optional)

try:
    # Get the max borrowable amount for a specific margin currency
    api_response = api_instance.get_margin_borrowable(currency, currency_pair=currency_pair)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->get_margin_borrowable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | 
 **currency_pair** | **str**| Currency pair | [optional] 

### Return type

[**MarginBorrowable**](MarginBorrowable.md)

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

# **list_cross_margin_currencies**
> list[CrossMarginCurrency] list_cross_margin_currencies()

Currencies supported by cross margin.

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
    # Currencies supported by cross margin.
    api_response = api_instance.list_cross_margin_currencies()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->list_cross_margin_currencies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CrossMarginCurrency]**](CrossMarginCurrency.md)

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

# **get_cross_margin_currency**
> CrossMarginCurrency get_cross_margin_currency(currency)

Retrieve detail of one single currency supported by cross margin

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
currency = 'BTC' # str | Currency name

try:
    # Retrieve detail of one single currency supported by cross margin
    api_response = api_instance.get_cross_margin_currency(currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->get_cross_margin_currency: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency name | 

### Return type

[**CrossMarginCurrency**](CrossMarginCurrency.md)

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

# **get_cross_margin_account**
> CrossMarginAccount get_cross_margin_account()

Retrieve cross margin account

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
    # Retrieve cross margin account
    api_response = api_instance.get_cross_margin_account()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->get_cross_margin_account: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CrossMarginAccount**](CrossMarginAccount.md)

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

# **list_cross_margin_account_book**
> list[CrossMarginAccountBook] list_cross_margin_account_book(currency=currency, _from=_from, to=to, page=page, limit=limit, type=type)

Retrieve cross margin account change history

Record time range cannot exceed 30 days

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
currency = 'currency_example' # str | Filter by currency (optional)
_from = 1627706330 # int | Start timestamp of the query (optional)
to = 1635329650 # int | Time range ending, default to current time (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
type = 'borrow' # str | Only retrieve changes of the specified type. All types will be returned if not specified. (optional)

try:
    # Retrieve cross margin account change history
    api_response = api_instance.list_cross_margin_account_book(currency=currency, _from=_from, to=to, page=page, limit=limit, type=type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->list_cross_margin_account_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Filter by currency | [optional] 
 **_from** | **int**| Start timestamp of the query | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **type** | **str**| Only retrieve changes of the specified type. All types will be returned if not specified. | [optional] 

### Return type

[**list[CrossMarginAccountBook]**](CrossMarginAccountBook.md)

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

# **list_cross_margin_loans**
> list[CrossMarginLoan] list_cross_margin_loans(status, currency=currency, limit=limit, offset=offset, reverse=reverse)

List cross margin borrow history

Sort by creation time in descending order by default. Set `reverse=false` to return ascending results.

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
status = 56 # int | Filter by status. Supported values are 2 and 3.
currency = 'currency_example' # str | Filter by currency (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
reverse = True # bool | Whether to sort in descending order, which is the default. Set `reverse=false` to return ascending results (optional) (default to True)

try:
    # List cross margin borrow history
    api_response = api_instance.list_cross_margin_loans(status, currency=currency, limit=limit, offset=offset, reverse=reverse)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->list_cross_margin_loans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **int**| Filter by status. Supported values are 2 and 3. | 
 **currency** | **str**| Filter by currency | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **reverse** | **bool**| Whether to sort in descending order, which is the default. Set &#x60;reverse&#x3D;false&#x60; to return ascending results | [optional] [default to True]

### Return type

[**list[CrossMarginLoan]**](CrossMarginLoan.md)

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

# **create_cross_margin_loan**
> CrossMarginLoan create_cross_margin_loan(cross_margin_loan)

Create a cross margin borrow loan

Borrow amount cannot be less than currency minimum borrow amount

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
cross_margin_loan = gate_api.CrossMarginLoan() # CrossMarginLoan | 

try:
    # Create a cross margin borrow loan
    api_response = api_instance.create_cross_margin_loan(cross_margin_loan)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->create_cross_margin_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_margin_loan** | [**CrossMarginLoan**](CrossMarginLoan.md)|  | 

### Return type

[**CrossMarginLoan**](CrossMarginLoan.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully borrowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cross_margin_loan**
> CrossMarginLoan get_cross_margin_loan(loan_id)

Retrieve single borrow loan detail

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
loan_id = '12345' # str | Borrow loan ID

try:
    # Retrieve single borrow loan detail
    api_response = api_instance.get_cross_margin_loan(loan_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->get_cross_margin_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **str**| Borrow loan ID | 

### Return type

[**CrossMarginLoan**](CrossMarginLoan.md)

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

# **list_cross_margin_repayments**
> list[CrossMarginRepayment] list_cross_margin_repayments(currency=currency, loan_id=loan_id, limit=limit, offset=offset, reverse=reverse)

Retrieve cross margin repayments

Sort by creation time in descending order by default. Set `reverse=false` to return ascending results.

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
currency = 'BTC' # str |  (optional)
loan_id = '12345' # str |  (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
reverse = True # bool | Whether to sort in descending order, which is the default. Set `reverse=false` to return ascending results (optional) (default to True)

try:
    # Retrieve cross margin repayments
    api_response = api_instance.list_cross_margin_repayments(currency=currency, loan_id=loan_id, limit=limit, offset=offset, reverse=reverse)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->list_cross_margin_repayments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**|  | [optional] 
 **loan_id** | **str**|  | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **reverse** | **bool**| Whether to sort in descending order, which is the default. Set &#x60;reverse&#x3D;false&#x60; to return ascending results | [optional] [default to True]

### Return type

[**list[CrossMarginRepayment]**](CrossMarginRepayment.md)

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

# **repay_cross_margin_loan**
> list[CrossMarginLoan] repay_cross_margin_loan(cross_margin_repay_request)

Cross margin repayments

When the liquidity of the currency is insufficient and the transaction risk is high, the currency will be disabled, and funds cannot be transferred.When the available balance of cross-margin is insufficient, the balance of the spot account can be used for repayment. Please ensure that the balance of the spot account is sufficient, and system uses cross-margin account for repayment first

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
cross_margin_repay_request = gate_api.CrossMarginRepayRequest() # CrossMarginRepayRequest | 

try:
    # Cross margin repayments
    api_response = api_instance.repay_cross_margin_loan(cross_margin_repay_request)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->repay_cross_margin_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cross_margin_repay_request** | [**CrossMarginRepayRequest**](CrossMarginRepayRequest.md)|  | 

### Return type

[**list[CrossMarginLoan]**](CrossMarginLoan.md)

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

# **get_cross_margin_transferable**
> CrossMarginTransferable get_cross_margin_transferable(currency)

Get the max transferable amount for a specific cross margin currency

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
currency = 'BTC' # str | Retrieve data of the specified currency

try:
    # Get the max transferable amount for a specific cross margin currency
    api_response = api_instance.get_cross_margin_transferable(currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->get_cross_margin_transferable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | 

### Return type

[**CrossMarginTransferable**](CrossMarginTransferable.md)

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

# **get_cross_margin_borrowable**
> CrossMarginBorrowable get_cross_margin_borrowable(currency)

Get the max borrowable amount for a specific cross margin currency

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
currency = 'BTC' # str | Retrieve data of the specified currency

try:
    # Get the max borrowable amount for a specific cross margin currency
    api_response = api_instance.get_cross_margin_borrowable(currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling MarginApi->get_cross_margin_borrowable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | 

### Return type

[**CrossMarginBorrowable**](CrossMarginBorrowable.md)

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

