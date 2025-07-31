# gate_api.UnifiedApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_unified_accounts**](UnifiedApi.md#list_unified_accounts) | **GET** /unified/accounts | Get unified account information
[**get_unified_borrowable**](UnifiedApi.md#get_unified_borrowable) | **GET** /unified/borrowable | Query maximum borrowable amount for unified account
[**get_unified_transferable**](UnifiedApi.md#get_unified_transferable) | **GET** /unified/transferable | Query maximum transferable amount for unified account
[**get_unified_transferables**](UnifiedApi.md#get_unified_transferables) | **GET** /unified/transferables | Batch query maximum transferable amount for unified accounts. Each currency shows the maximum value. After user withdrawal, the transferable amount for all currencies will change
[**get_unified_borrowable_list**](UnifiedApi.md#get_unified_borrowable_list) | **GET** /unified/batch_borrowable | Batch query unified account maximum borrowable amount
[**list_unified_loans**](UnifiedApi.md#list_unified_loans) | **GET** /unified/loans | Query loans
[**create_unified_loan**](UnifiedApi.md#create_unified_loan) | **POST** /unified/loans | Borrow or repay
[**list_unified_loan_records**](UnifiedApi.md#list_unified_loan_records) | **GET** /unified/loan_records | Query loan records
[**list_unified_loan_interest_records**](UnifiedApi.md#list_unified_loan_interest_records) | **GET** /unified/interest_records | Query interest deduction records
[**get_unified_risk_units**](UnifiedApi.md#get_unified_risk_units) | **GET** /unified/risk_units | Get user risk unit details
[**get_unified_mode**](UnifiedApi.md#get_unified_mode) | **GET** /unified/unified_mode | Query mode of the unified account
[**set_unified_mode**](UnifiedApi.md#set_unified_mode) | **PUT** /unified/unified_mode | Set unified account mode
[**get_unified_estimate_rate**](UnifiedApi.md#get_unified_estimate_rate) | **GET** /unified/estimate_rate | Query unified account estimated interest rate
[**list_currency_discount_tiers**](UnifiedApi.md#list_currency_discount_tiers) | **GET** /unified/currency_discount_tiers | Query unified account tiered discount
[**list_loan_margin_tiers**](UnifiedApi.md#list_loan_margin_tiers) | **GET** /unified/loan_margin_tiers | Query unified account tiered loan margin
[**calculate_portfolio_margin**](UnifiedApi.md#calculate_portfolio_margin) | **POST** /unified/portfolio_calculator | Portfolio margin calculator
[**get_user_leverage_currency_config**](UnifiedApi.md#get_user_leverage_currency_config) | **GET** /unified/leverage/user_currency_config | Maximum and minimum currency leverage that can be set
[**get_user_leverage_currency_setting**](UnifiedApi.md#get_user_leverage_currency_setting) | **GET** /unified/leverage/user_currency_setting | Get user currency leverage
[**set_user_leverage_currency_setting**](UnifiedApi.md#set_user_leverage_currency_setting) | **POST** /unified/leverage/user_currency_setting | Set loan currency leverage
[**list_unified_currencies**](UnifiedApi.md#list_unified_currencies) | **GET** /unified/currencies | List of loan currencies supported by unified account
[**get_history_loan_rate**](UnifiedApi.md#get_history_loan_rate) | **GET** /unified/history_loan_rate | Get historical lending rates
[**set_unified_collateral**](UnifiedApi.md#set_unified_collateral) | **POST** /unified/collateral_currencies | Set collateral currency


# **list_unified_accounts**
> UnifiedAccount list_unified_accounts(currency=currency, sub_uid=sub_uid)

Get unified account information

The assets of each currency in the account will be adjusted according to their liquidity, defined by corresponding adjustment coefficients, and then uniformly converted to USD to calculate the total asset value and position value of the account.  For specific formulas, please refer to [Margin Formula](#margin-formula)

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
currency = 'BTC' # str | Query by specified currency name (optional)
sub_uid = '10001' # str | Sub account user ID (optional)

try:
    # Get unified account information
    api_response = api_instance.list_unified_accounts(currency=currency, sub_uid=sub_uid)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->list_unified_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Query by specified currency name | [optional] 
 **sub_uid** | **str**| Sub account user ID | [optional] 

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
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unified_borrowable**
> UnifiedBorrowable get_unified_borrowable(currency)

Query maximum borrowable amount for unified account

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
currency = 'BTC' # str | Query by specified currency name

try:
    # Query maximum borrowable amount for unified account
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
 **currency** | **str**| Query by specified currency name | 

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unified_transferable**
> UnifiedTransferable get_unified_transferable(currency)

Query maximum transferable amount for unified account

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
currency = 'BTC' # str | Query by specified currency name

try:
    # Query maximum transferable amount for unified account
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
 **currency** | **str**| Query by specified currency name | 

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unified_transferables**
> list[TransferablesResult] get_unified_transferables(currencies)

Batch query maximum transferable amount for unified accounts. Each currency shows the maximum value. After user withdrawal, the transferable amount for all currencies will change

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
currencies = 'BTC,ETH' # str | Specify the currency name to query in batches, and support up to 100 pass parameters at a time

try:
    # Batch query maximum transferable amount for unified accounts. Each currency shows the maximum value. After user withdrawal, the transferable amount for all currencies will change
    api_response = api_instance.get_unified_transferables(currencies)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->get_unified_transferables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencies** | **str**| Specify the currency name to query in batches, and support up to 100 pass parameters at a time | 

### Return type

[**list[TransferablesResult]**](TransferablesResult.md)

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

# **get_unified_borrowable_list**
> list[UnifiedBorrowable1] get_unified_borrowable_list(currencies)

Batch query unified account maximum borrowable amount

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
currencies = ['[\"BTC\",\"GT\"]'] # list[str] | Specify currency names for querying in an array, separated by commas, maximum 10 currencies

try:
    # Batch query unified account maximum borrowable amount
    api_response = api_instance.get_unified_borrowable_list(currencies)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->get_unified_borrowable_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencies** | [**list[str]**](str.md)| Specify currency names for querying in an array, separated by commas, maximum 10 currencies | 

### Return type

[**list[UnifiedBorrowable1]**](UnifiedBorrowable1.md)

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

# **list_unified_loans**
> list[UniLoan] list_unified_loans(currency=currency, page=page, limit=limit, type=type)

Query loans

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
currency = 'BTC' # str | Query by specified currency name (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100 (optional) (default to 100)
type = 'platform' # str | Loan type: platform borrowing - platform, margin borrowing - margin (optional)

try:
    # Query loans
    api_response = api_instance.list_unified_loans(currency=currency, page=page, limit=limit, type=type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->list_unified_loans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Query by specified currency name | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of items returned. Default: 100, minimum: 1, maximum: 100 | [optional] [default to 100]
 **type** | **str**| Loan type: platform borrowing - platform, margin borrowing - margin | [optional] 

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_unified_loan**
> UnifiedLoanResult create_unified_loan(unified_loan)

Borrow or repay

When borrowing, ensure the borrowed amount is not below the minimum borrowing threshold for the specific cryptocurrency and does not exceed the maximum borrowing limit set by the platform and user.  Loan interest will be automatically deducted from the account at regular intervals. Users are responsible for managing repayment of borrowed amounts.  For repayment, use `repaid_all=true` to repay all available amounts

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
    api_response = api_instance.create_unified_loan(unified_loan)
    print(api_response)
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

[**UnifiedLoanResult**](UnifiedLoanResult.md)

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

# **list_unified_loan_records**
> list[UnifiedLoanRecord] list_unified_loan_records(type=type, currency=currency, page=page, limit=limit)

Query loan records

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
type = 'type_example' # str | Loan record type: borrow - borrowing, repay - repayment (optional)
currency = 'BTC' # str | Query by specified currency name (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100 (optional) (default to 100)

try:
    # Query loan records
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
 **type** | **str**| Loan record type: borrow - borrowing, repay - repayment | [optional] 
 **currency** | **str**| Query by specified currency name | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of items returned. Default: 100, minimum: 1, maximum: 100 | [optional] [default to 100]

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_unified_loan_interest_records**
> list[UniLoanInterestRecord] list_unified_loan_interest_records(currency=currency, page=page, limit=limit, _from=_from, to=to, type=type)

Query interest deduction records

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
currency = 'BTC' # str | Query by specified currency name (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100 (optional) (default to 100)
_from = 1627706330 # int | Start timestamp for the query (optional)
to = 1635329650 # int | End timestamp for the query, defaults to current time if not specified (optional)
type = 'platform' # str | Loan type: platform borrowing - platform, margin borrowing - margin. Defaults to margin if not specified (optional)

try:
    # Query interest deduction records
    api_response = api_instance.list_unified_loan_interest_records(currency=currency, page=page, limit=limit, _from=_from, to=to, type=type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->list_unified_loan_interest_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Query by specified currency name | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of items returned. Default: 100, minimum: 1, maximum: 100 | [optional] [default to 100]
 **_from** | **int**| Start timestamp for the query | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 
 **type** | **str**| Loan type: platform borrowing - platform, margin borrowing - margin. Defaults to margin if not specified | [optional] 

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
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unified_risk_units**
> UnifiedRiskUnits get_unified_risk_units()

Get user risk unit details

Get user risk unit details, only valid in portfolio margin mode

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
    # Get user risk unit details
    api_response = api_instance.get_unified_risk_units()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->get_unified_risk_units: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnifiedRiskUnits**](UnifiedRiskUnits.md)

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

# **get_unified_mode**
> UnifiedModeSet get_unified_mode()

Query mode of the unified account

Unified account mode: - `classic`: Classic account mode - `multi_currency`: Cross-currency margin mode - `portfolio`: Portfolio margin mode - `single_currency`: Single-currency margin mode

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
    api_response = api_instance.get_unified_mode()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->get_unified_mode: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UnifiedModeSet**](UnifiedModeSet.md)

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

# **set_unified_mode**
> set_unified_mode(unified_mode_set)

Set unified account mode

Each account mode switch only requires passing the corresponding account mode parameter, and also supports turning on or off the configuration switches under the corresponding account mode during the switch. - When enabling the classic account mode, mode=classic ```  PUT /unified/unified_mode  {  \"mode\": \"classic\"  } ``` - When enabling the cross-currency margin \"multi_currency\",  \"settings\": {  \"usdt_futures\": true  }  } ``` - When enabling the portfolio margin mode, mode=portfolio ```  PUT /unified/unified_mode  {  \"mode\": \"portfolio\",  \"settings\": {  \"spot_hedge\": true  }  } ``` - When enabling the single-currency margin mode, mode=single_currency ```  PUT /unified/unified_mode  {  \"mode\": \"single_currency\"  } ```

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
unified_mode_set = gate_api.UnifiedModeSet() # UnifiedModeSet | 

try:
    # Set unified account mode
    api_instance.set_unified_mode(unified_mode_set)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->set_unified_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unified_mode_set** | [**UnifiedModeSet**](UnifiedModeSet.md)|  | 

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
**204** | Set successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unified_estimate_rate**
> dict(str, str) get_unified_estimate_rate(currencies)

Query unified account estimated interest rate

Interest rates fluctuate hourly based on lending depth, so exact rates cannot be provided. When a currency is not supported, the interest rate returned will be an empty string

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
currencies = ['[\"BTC\",\"GT\"]'] # list[str] | Specify currency names for querying in an array, separated by commas, maximum 10 currencies

try:
    # Query unified account estimated interest rate
    api_response = api_instance.get_unified_estimate_rate(currencies)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->get_unified_estimate_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currencies** | [**list[str]**](str.md)| Specify currency names for querying in an array, separated by commas, maximum 10 currencies | 

### Return type

**dict(str, str)**

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

# **list_currency_discount_tiers**
> list[UnifiedDiscount] list_currency_discount_tiers()

Query unified account tiered discount

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
api_instance = gate_api.UnifiedApi(api_client)

try:
    # Query unified account tiered discount
    api_response = api_instance.list_currency_discount_tiers()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->list_currency_discount_tiers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UnifiedDiscount]**](UnifiedDiscount.md)

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

# **list_loan_margin_tiers**
> list[UnifiedMarginTiers] list_loan_margin_tiers()

Query unified account tiered loan margin

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
api_instance = gate_api.UnifiedApi(api_client)

try:
    # Query unified account tiered loan margin
    api_response = api_instance.list_loan_margin_tiers()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->list_loan_margin_tiers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[UnifiedMarginTiers]**](UnifiedMarginTiers.md)

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

# **calculate_portfolio_margin**
> UnifiedPortfolioOutput calculate_portfolio_margin(unified_portfolio_input)

Portfolio margin calculator

Portfolio Margin Calculator  When inputting simulated position portfolios, each position includes the position name and quantity held, supporting markets within the range of BTC and ETH perpetual contracts, options, and spot markets. When inputting simulated orders, each order includes the market identifier, order price, and order quantity, supporting markets within the range of BTC and ETH perpetual contracts, options, and spot markets. Market orders are not included.

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
api_instance = gate_api.UnifiedApi(api_client)
unified_portfolio_input = gate_api.UnifiedPortfolioInput() # UnifiedPortfolioInput | 

try:
    # Portfolio margin calculator
    api_response = api_instance.calculate_portfolio_margin(unified_portfolio_input)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->calculate_portfolio_margin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unified_portfolio_input** | [**UnifiedPortfolioInput**](UnifiedPortfolioInput.md)|  | 

### Return type

[**UnifiedPortfolioOutput**](UnifiedPortfolioOutput.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_leverage_currency_config**
> UnifiedLeverageConfig get_user_leverage_currency_config(currency)

Maximum and minimum currency leverage that can be set

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
currency = 'BTC' # str | Currency

try:
    # Maximum and minimum currency leverage that can be set
    api_response = api_instance.get_user_leverage_currency_config(currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->get_user_leverage_currency_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency | 

### Return type

[**UnifiedLeverageConfig**](UnifiedLeverageConfig.md)

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

# **get_user_leverage_currency_setting**
> list[UnifiedLeverageSetting] get_user_leverage_currency_setting(currency=currency)

Get user currency leverage

Get user currency leverage. If currency is not specified, query all currencies

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
currency = 'BTC' # str | Currency (optional)

try:
    # Get user currency leverage
    api_response = api_instance.get_user_leverage_currency_setting(currency=currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->get_user_leverage_currency_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency | [optional] 

### Return type

[**list[UnifiedLeverageSetting]**](UnifiedLeverageSetting.md)

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

# **set_user_leverage_currency_setting**
> set_user_leverage_currency_setting(unified_leverage_setting)

Set loan currency leverage

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
unified_leverage_setting = gate_api.UnifiedLeverageSetting() # UnifiedLeverageSetting | 

try:
    # Set loan currency leverage
    api_instance.set_user_leverage_currency_setting(unified_leverage_setting)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->set_user_leverage_currency_setting: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unified_leverage_setting** | [**UnifiedLeverageSetting**](UnifiedLeverageSetting.md)|  | 

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
**204** | Set successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_unified_currencies**
> list[UnifiedCurrency] list_unified_currencies(currency=currency)

List of loan currencies supported by unified account

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
api_instance = gate_api.UnifiedApi(api_client)
currency = 'BTC' # str | Currency (optional)

try:
    # List of loan currencies supported by unified account
    api_response = api_instance.list_unified_currencies(currency=currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->list_unified_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency | [optional] 

### Return type

[**list[UnifiedCurrency]**](UnifiedCurrency.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_loan_rate**
> UnifiedHistoryLoanRate get_history_loan_rate(currency, tier=tier, page=page, limit=limit)

Get historical lending rates

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
api_instance = gate_api.UnifiedApi(api_client)
currency = 'USDT' # str | Currency
tier = '1' # str | VIP level for the floating rate to be queried (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100 (optional) (default to 100)

try:
    # Get historical lending rates
    api_response = api_instance.get_history_loan_rate(currency, tier=tier, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->get_history_loan_rate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency | 
 **tier** | **str**| VIP level for the floating rate to be queried | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of items returned. Default: 100, minimum: 1, maximum: 100 | [optional] [default to 100]

### Return type

[**UnifiedHistoryLoanRate**](UnifiedHistoryLoanRate.md)

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

# **set_unified_collateral**
> UnifiedCollateralRes set_unified_collateral(unified_collateral_req)

Set collateral currency

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
unified_collateral_req = gate_api.UnifiedCollateralReq() # UnifiedCollateralReq | 

try:
    # Set collateral currency
    api_response = api_instance.set_unified_collateral(unified_collateral_req)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling UnifiedApi->set_unified_collateral: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unified_collateral_req** | [**UnifiedCollateralReq**](UnifiedCollateralReq.md)|  | 

### Return type

[**UnifiedCollateralRes**](UnifiedCollateralRes.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

