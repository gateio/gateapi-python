# gate_api.MarginApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_loan**](MarginApi.md#cancel_loan) | **DELETE** /margin/loans/{loan_id} | Cancel lending loan
[**create_loan**](MarginApi.md#create_loan) | **POST** /margin/loans | Lend or borrow
[**get_loan**](MarginApi.md#get_loan) | **GET** /margin/loans/{loan_id} | Retrieve one single loan detail
[**get_loan_record**](MarginApi.md#get_loan_record) | **GET** /margin/loan_records/{loan_record_id} | Get one single loan record
[**list_funding_accounts**](MarginApi.md#list_funding_accounts) | **GET** /margin/funding_accounts | Funding account list
[**list_funding_book**](MarginApi.md#list_funding_book) | **GET** /margin/funding_book | Order book of lending loans
[**list_loan_records**](MarginApi.md#list_loan_records) | **GET** /margin/loan_records | List repayment records of specified loan
[**list_loan_repayments**](MarginApi.md#list_loan_repayments) | **GET** /margin/loans/{loan_id}/repayment | List loan repayment records
[**list_loans**](MarginApi.md#list_loans) | **GET** /margin/loans | List all loans
[**list_margin_accounts**](MarginApi.md#list_margin_accounts) | **GET** /margin/accounts | Margin account list
[**list_margin_currency_pairs**](MarginApi.md#list_margin_currency_pairs) | **GET** /margin/currency_pairs | List all supported currency pairs supported in margin trading
[**merge_loans**](MarginApi.md#merge_loans) | **POST** /margin/merged_loans | Merge multiple lending loans
[**repay_loan**](MarginApi.md#repay_loan) | **POST** /margin/loans/{loan_id}/repayment | Repay a loan
[**update_loan**](MarginApi.md#update_loan) | **PATCH** /margin/loans/{loan_id} | Modify a loan
[**update_loan_record**](MarginApi.md#update_loan_record) | **PATCH** /margin/loan_records/{loan_record_id} | Modify a loan record


# **cancel_loan**
> Loan cancel_loan(loan_id, currency)

Cancel lending loan

Only lending loans can be cancelled

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
loan_id = '12345' # str | Loan ID
currency = 'BTC' # str | Retrieved specified currency related data

try:
    # Cancel lending loan
    api_response = api_instance.cancel_loan(loan_id, currency)
    print(api_response)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_loan**
> Loan create_loan(loan)

Lend or borrow

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
loan = gate_api.Loan() # Loan | 

try:
    # Lend or borrow
    api_response = api_instance.create_loan(loan)
    print(api_response)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan**
> Loan get_loan(loan_id, side)

Retrieve one single loan detail

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
loan_id = '12345' # str | Loan ID
side = 'lend' # str | Lend or borrow

try:
    # Retrieve one single loan detail
    api_response = api_instance.get_loan(loan_id, side)
    print(api_response)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loan_record**
> LoanRecord get_loan_record(loan_record_id, loan_id)

Get one single loan record

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
loan_record_id = '12345' # str | Loan record ID
loan_id = '12345' # str | Loan ID

try:
    # Get one single loan record
    api_response = api_instance.get_loan_record(loan_record_id, loan_id)
    print(api_response)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_funding_accounts**
> list[FundingAccount] list_funding_accounts(currency=currency)

Funding account list

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
currency = 'BTC' # str | Retrieved specified currency related data (optional)

try:
    # Funding account list
    api_response = api_instance.list_funding_accounts(currency=currency)
    print(api_response)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_funding_book**
> list[FundingBookItem] list_funding_book(currency)

Order book of lending loans

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.MarginApi()
currency = 'BTC' # str | Retrieved specified currency related data

try:
    # Order book of lending loans
    api_response = api_instance.list_funding_book(currency)
    print(api_response)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loan_records**
> list[LoanRecord] list_loan_records(loan_id, status=status, page=page, limit=limit)

List repayment records of specified loan

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
loan_id = '12345' # str | Loan ID
status = 'loaned' # str | Loan record status (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)

try:
    # List repayment records of specified loan
    api_response = api_instance.list_loan_records(loan_id, status=status, page=page, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->list_loan_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_id** | **str**| Loan ID | 
 **status** | **str**| Loan record status | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]

### Return type

[**list[LoanRecord]**](LoanRecord.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loan_repayments**
> list[Repayment] list_loan_repayments(loan_id)

List loan repayment records

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
loan_id = '12345' # str | Loan ID

try:
    # List loan repayment records
    api_response = api_instance.list_loan_repayments(loan_id)
    print(api_response)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loans**
> list[Loan] list_loans(status, side, currency=currency, page=page, limit=limit)

List all loans

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
status = 'open' # str | Loan status
side = 'lend' # str | Lend or borrow
currency = 'BTC' # str | Retrieved specified currency related data (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)

try:
    # List all loans
    api_response = api_instance.list_loans(status, side, currency=currency, page=page, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling MarginApi->list_loans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Loan status | 
 **side** | **str**| Lend or borrow | 
 **currency** | **str**| Retrieved specified currency related data | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]

### Return type

[**list[Loan]**](Loan.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_margin_accounts**
> list[MarginAccount] list_margin_accounts(currency_pair=currency_pair)

Margin account list

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
currency_pair = 'BTC_USDT' # str | Currency pair (optional)

try:
    # Margin account list
    api_response = api_instance.list_margin_accounts(currency_pair=currency_pair)
    print(api_response)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_margin_currency_pairs**
> list[MarginCurrencyPair] list_margin_currency_pairs()

List all supported currency pairs supported in margin trading

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

# create an instance of the API class
api_instance = gate_api.MarginApi()

try:
    # List all supported currency pairs supported in margin trading
    api_response = api_instance.list_margin_currency_pairs()
    print(api_response)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_loans**
> Loan merge_loans(currency, ids)

Merge multiple lending loans

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
currency = 'BTC' # str | Retrieved specified currency related data
ids = '123,234,345' # str | Lending loan ID list separated by `,`. Maximum of 20 IDs are allowed in one request

try:
    # Merge multiple lending loans
    api_response = api_instance.merge_loans(currency, ids)
    print(api_response)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **repay_loan**
> Loan repay_loan(loan_id, repay_request)

Repay a loan

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
loan_id = '12345' # str | Loan ID
repay_request = gate_api.RepayRequest() # RepayRequest | 

try:
    # Repay a loan
    api_response = api_instance.repay_loan(loan_id, repay_request)
    print(api_response)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan**
> Loan update_loan(loan_id, loan_patch)

Modify a loan

Only `auto_renew` modification is supported currently

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
loan_id = '12345' # str | Loan ID
loan_patch = gate_api.LoanPatch() # LoanPatch | 

try:
    # Modify a loan
    api_response = api_instance.update_loan(loan_id, loan_patch)
    print(api_response)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_loan_record**
> LoanRecord update_loan_record(loan_record_id, loan_patch)

Modify a loan record

Only `auto_renew` modification is supported currently

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.MarginApi(gate_api.ApiClient(configuration))
loan_record_id = '12345' # str | Loan record ID
loan_patch = gate_api.LoanPatch() # LoanPatch | 

try:
    # Modify a loan record
    api_response = api_instance.update_loan_record(loan_record_id, loan_patch)
    print(api_response)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

