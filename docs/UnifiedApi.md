# gate_api.UnifiedApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_unified_accounts**](UnifiedApi.md#list_unified_accounts) | **GET** /unified/accounts | Get unified account information
[**get_unified_borrowable**](UnifiedApi.md#get_unified_borrowable) | **GET** /unified/borrowable | Query about the maximum borrowing for the unified account
[**get_unified_transferable**](UnifiedApi.md#get_unified_transferable) | **GET** /unified/transferable | Query about the maximum transferable for the unified account
[**get_unified_transferables**](UnifiedApi.md#get_unified_transferables) | **GET** /unified/transferables | Batch query can be transferred out at most for unified accounts; each currency is the maximum value. After the user withdraws the currency, the amount of transferable currency will be changed.
[**list_unified_loans**](UnifiedApi.md#list_unified_loans) | **GET** /unified/loans | List loans
[**create_unified_loan**](UnifiedApi.md#create_unified_loan) | **POST** /unified/loans | Borrow or repay
[**list_unified_loan_records**](UnifiedApi.md#list_unified_loan_records) | **GET** /unified/loan_records | Get load records
[**list_unified_loan_interest_records**](UnifiedApi.md#list_unified_loan_interest_records) | **GET** /unified/interest_records | List interest records
[**get_unified_risk_units**](UnifiedApi.md#get_unified_risk_units) | **GET** /unified/risk_units | Get user risk unit details
[**get_unified_mode**](UnifiedApi.md#get_unified_mode) | **GET** /unified/unified_mode | Query mode of the unified account
[**set_unified_mode**](UnifiedApi.md#set_unified_mode) | **PUT** /unified/unified_mode | Set mode of the unified account
[**get_unified_estimate_rate**](UnifiedApi.md#get_unified_estimate_rate) | **GET** /unified/estimate_rate | Get unified estimate rate
[**list_currency_discount_tiers**](UnifiedApi.md#list_currency_discount_tiers) | **GET** /unified/currency_discount_tiers | List currency discount tiers
[**list_loan_margin_tiers**](UnifiedApi.md#list_loan_margin_tiers) | **GET** /unified/loan_margin_tiers | List loan margin tiers
[**calculate_portfolio_margin**](UnifiedApi.md#calculate_portfolio_margin) | **POST** /unified/portfolio_calculator | Portfolio margin calculator
[**get_user_leverage_currency_config**](UnifiedApi.md#get_user_leverage_currency_config) | **GET** /unified/leverage/user_currency_config | Minimum currency leverage that can be set
[**get_user_leverage_currency_setting**](UnifiedApi.md#get_user_leverage_currency_setting) | **GET** /unified/leverage/user_currency_setting | Get the leverage multiple of the user currency
[**set_user_leverage_currency_setting**](UnifiedApi.md#set_user_leverage_currency_setting) | **POST** /unified/leverage/user_currency_setting | Set the loan currency leverage
[**list_unified_currencies**](UnifiedApi.md#list_unified_currencies) | **GET** /unified/currencies | List of loan currencies supported by unified account
[**get_history_loan_rate**](UnifiedApi.md#get_history_loan_rate) | **GET** /unified/history_loan_rate | get historical lending rates


# **list_unified_accounts**
> UnifiedAccount list_unified_accounts(currency=currency, sub_uid=sub_uid)

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
 **currency** | **str**| Retrieve data of the specified currency | [optional] 
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
**200** | List retrieved |  -  |

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

# **get_unified_transferables**
> list[TransferablesResult] get_unified_transferables(currencies)

Batch query can be transferred out at most for unified accounts; each currency is the maximum value. After the user withdraws the currency, the amount of transferable currency will be changed.

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
currencies = 'BTC,ETH' # str | Specify the currency name to query in batches, and support up to 100 pass parameters at a time.

try:
    # Batch query can be transferred out at most for unified accounts; each currency is the maximum value. After the user withdraws the currency, the amount of transferable currency will be changed.
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
 **currencies** | **str**| Specify the currency name to query in batches, and support up to 100 pass parameters at a time. | 

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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_unified_loans**
> list[UniLoan] list_unified_loans(currency=currency, page=page, limit=limit, type=type)

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
type = 'platform' # str | Loan type, platform - platform, margin - margin (optional)

try:
    # List loans
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
 **currency** | **str**| Retrieve data of the specified currency | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum response items.  Default: 100, minimum: 1, Maximum: 100 | [optional] [default to 100]
 **type** | **str**| Loan type, platform - platform, margin - margin | [optional] 

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
> UnifiedLoanResult create_unified_loan(unified_loan)

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
**200** | Operated successfully |  -  |

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
> list[UniLoanInterestRecord] list_unified_loan_interest_records(currency=currency, page=page, limit=limit, _from=_from, to=to, type=type)

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
_from = 1627706330 # int | Start timestamp of the query (optional)
to = 1635329650 # int | Time range ending, default to current time (optional)
type = 'platform' # str | Loan type, platform loan - platform, leverage loan - margin, if not passed, defaults to margin (optional)

try:
    # List interest records
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
 **currency** | **str**| Retrieve data of the specified currency | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum response items.  Default: 100, minimum: 1, Maximum: 100 | [optional] [default to 100]
 **_from** | **int**| Start timestamp of the query | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **type** | **str**| Loan type, platform loan - platform, leverage loan - margin, if not passed, defaults to margin | [optional] 

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

# **get_unified_risk_units**
> UnifiedRiskUnits get_unified_risk_units()

Get user risk unit details

Retrieve user risk unit details, only valid in portfolio margin mode

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
**200** | Successfully retrieved |  -  |

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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_unified_mode**
> set_unified_mode(unified_mode_set)

Set mode of the unified account

Switching each account mode only requires passing the parameters of the corresponding account mode, and supports turning on or off the configuration switch in the corresponding account mode when switching the account mode  - When opening the classic account mode, mode=classic ```  PUT /unified/unified_mode  {  \"mode\": \"classic\"  } ``` - Open the cross-currency margin mode, mode=multi_currency ```  PUT /unified/unified_mode  {  \"mode\": \"multi_currency\",  \"settings\": {  \"usdt_futures\": true  }  } ``` - When the portfolio margin mode is enabled, mode=portfolio ```  PUT /unified/unified_mode  {  \"mode\": \"portfolio\",  \"settings\": {  \"spot_hedge\": true  }  } ``` - When opening a single currency margin mode, mode=single_currency ```  PUT /unified/unified_mode  {  \"mode\": \"single_currency\"  } ```

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
    # Set mode of the unified account
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
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unified_estimate_rate**
> dict(str, str) get_unified_estimate_rate(currencies)

Get unified estimate rate

Due to fluctuations in lending depth, hourly interest rates may vary, and thus, I cannot provide exact rates. When a currency is not supported, the interest rate returned will be an empty string.

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
currencies = ['[\"BTC\",\"GT\"]'] # list[str] | Specify the currency names for querying in an array, separated by commas, with a maximum of 10 currencies.

try:
    # Get unified estimate rate
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
 **currencies** | [**list[str]**](str.md)| Specify the currency names for querying in an array, separated by commas, with a maximum of 10 currencies. | 

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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_currency_discount_tiers**
> list[UnifiedDiscount] list_currency_discount_tiers()

List currency discount tiers

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
    # List currency discount tiers
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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_loan_margin_tiers**
> list[UnifiedMarginTiers] list_loan_margin_tiers()

List loan margin tiers

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
    # List loan margin tiers
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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **calculate_portfolio_margin**
> UnifiedPortfolioOutput calculate_portfolio_margin(unified_portfolio_input)

Portfolio margin calculator

Portfolio Margin Calculator When inputting a simulated position portfolio, each position includes the position name and quantity held, supporting markets within the range of BTC and ETH perpetual contracts, options, and spot markets. When inputting simulated orders, each order includes the market identifier, order price, and order quantity,  supporting markets within the range of BTC and ETH perpetual contracts, options, and spot markets. Market orders are not included.

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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_leverage_currency_config**
> UnifiedLeverageConfig get_user_leverage_currency_config(currency)

Minimum currency leverage that can be set

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
    # Minimum currency leverage that can be set
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
**200** | Successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_leverage_currency_setting**
> UnifiedLeverageSetting get_user_leverage_currency_setting(currency=currency)

Get the leverage multiple of the user currency

Get the user's currency leverage. If currency is not passed, query all currencies.

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
    # Get the leverage multiple of the user currency
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

[**UnifiedLeverageSetting**](UnifiedLeverageSetting.md)

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

# **set_user_leverage_currency_setting**
> set_user_leverage_currency_setting(unified_leverage_setting)

Set the loan currency leverage

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
    # Set the loan currency leverage
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
**204** | Success |  -  |

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
**200** | List retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_history_loan_rate**
> UnifiedHistoryLoanRate get_history_loan_rate(currency, tier=tier, page=page, limit=limit)

get historical lending rates

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
currency = 'USDT' # str | Currency
tier = '1' # str | The VIP level of the floating rate that needs to be queried (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum response items.  Default: 100, minimum: 1, Maximum: 100 (optional) (default to 100)

try:
    # get historical lending rates
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
 **tier** | **str**| The VIP level of the floating rate that needs to be queried | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum response items.  Default: 100, minimum: 1, Maximum: 100 | [optional] [default to 100]

### Return type

[**UnifiedHistoryLoanRate**](UnifiedHistoryLoanRate.md)

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

