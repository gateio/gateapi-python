# gate_api.PortfolioApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_portfolio_accounts**](PortfolioApi.md#list_portfolio_accounts) | **GET** /portfolio/accounts | Get portfolio account information
[**list_account_portfolio_mode**](PortfolioApi.md#list_account_portfolio_mode) | **GET** /portfolio/account_mode | Retrieve the account&#39;s portfolio mode
[**get_portfolio_borrowable**](PortfolioApi.md#get_portfolio_borrowable) | **GET** /portfolio/borrowable | Retrieve the maximum borrowable amount for the account.
[**get_portfolio_transferable**](PortfolioApi.md#get_portfolio_transferable) | **GET** /portfolio/transferable | Retrieve the maximum amount that can be transferred out from the account
[**list_portfolio_uni_loan_interest_records**](PortfolioApi.md#list_portfolio_uni_loan_interest_records) | **GET** /portfolio/loans | List loans
[**create_portfolio_loan**](PortfolioApi.md#create_portfolio_loan) | **POST** /portfolio/loans | Borrow or repay
[**list_portfolio_loan_records**](PortfolioApi.md#list_portfolio_loan_records) | **GET** /portfolio/loan_records | Get load records
[**list_portfolio_loan_interest_records**](PortfolioApi.md#list_portfolio_loan_interest_records) | **GET** /portfolio/interest_records | List interest records
[**list_portfolio_orders**](PortfolioApi.md#list_portfolio_orders) | **GET** /portfolio/spot/orders | List orders
[**create_portfolio_orders**](PortfolioApi.md#create_portfolio_orders) | **POST** /portfolio/spot/orders | Create an order
[**get_portfolio_order**](PortfolioApi.md#get_portfolio_order) | **GET** /portfolio/spot/orders/{order_id} | Get order detail
[**cancel_portfolio_order**](PortfolioApi.md#cancel_portfolio_order) | **DELETE** /portfolio/spot/orders/{order_id} | Cancel a single order
[**amend_portfolio_order**](PortfolioApi.md#amend_portfolio_order) | **PATCH** /portfolio/spot/orders/{order_id} | Amend order


# **list_portfolio_accounts**
> PortfolioAccount list_portfolio_accounts(currency=currency)

Get portfolio account information

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
api_instance = gate_api.PortfolioApi(api_client)
currency = 'BTC' # str | Retrieve data of the specified currency (optional)

try:
    # Get portfolio account information
    api_response = api_instance.list_portfolio_accounts(currency=currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->list_portfolio_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | [optional] 

### Return type

[**PortfolioAccount**](PortfolioAccount.md)

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

# **list_account_portfolio_mode**
> dict(str, bool) list_account_portfolio_mode()

Retrieve the account's portfolio mode

Currently, only the Cross Margin mode is available. In the future, multiple margin modes will be supported.   - cross_margin : cross margin - usdt_futures : futures (USDT for margin) - btc_futures: futures (BTC for margin - options : option margin - delivery : delivery margin

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
api_instance = gate_api.PortfolioApi(api_client)

try:
    # Retrieve the account's portfolio mode
    api_response = api_instance.list_account_portfolio_mode()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->list_account_portfolio_mode: %s\n" % e)
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

# **get_portfolio_borrowable**
> PortfolioBorrowable get_portfolio_borrowable(currency)

Retrieve the maximum borrowable amount for the account.

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
api_instance = gate_api.PortfolioApi(api_client)
currency = 'BTC' # str | Retrieve data of the specified currency

try:
    # Retrieve the maximum borrowable amount for the account.
    api_response = api_instance.get_portfolio_borrowable(currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->get_portfolio_borrowable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | 

### Return type

[**PortfolioBorrowable**](PortfolioBorrowable.md)

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

# **get_portfolio_transferable**
> PortfolioTransferable get_portfolio_transferable(currency)

Retrieve the maximum amount that can be transferred out from the account

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
api_instance = gate_api.PortfolioApi(api_client)
currency = 'BTC' # str | Retrieve data of the specified currency

try:
    # Retrieve the maximum amount that can be transferred out from the account
    api_response = api_instance.get_portfolio_transferable(currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->get_portfolio_transferable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Retrieve data of the specified currency | 

### Return type

[**PortfolioTransferable**](PortfolioTransferable.md)

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

# **list_portfolio_uni_loan_interest_records**
> list[UniLoan] list_portfolio_uni_loan_interest_records(currency=currency, page=page, limit=limit)

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
api_instance = gate_api.PortfolioApi(api_client)
currency = 'BTC' # str | Retrieve data of the specified currency (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum response items.  Default: 100, minimum: 1, Maximum: 100 (optional) (default to 100)

try:
    # List loans
    api_response = api_instance.list_portfolio_uni_loan_interest_records(currency=currency, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->list_portfolio_uni_loan_interest_records: %s\n" % e)
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

# **create_portfolio_loan**
> create_portfolio_loan(portfolio_loan)

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
api_instance = gate_api.PortfolioApi(api_client)
portfolio_loan = gate_api.PortfolioLoan() # PortfolioLoan | 

try:
    # Borrow or repay
    api_instance.create_portfolio_loan(portfolio_loan)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->create_portfolio_loan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_loan** | [**PortfolioLoan**](PortfolioLoan.md)|  | 

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

# **list_portfolio_loan_records**
> list[PortfolioLoanRecord] list_portfolio_loan_records(type=type, currency=currency, page=page, limit=limit)

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
api_instance = gate_api.PortfolioApi(api_client)
type = 'type_example' # str | The types of lending records, borrow - indicates the action of borrowing funds, repay - indicates the action of repaying the borrowed funds (optional)
currency = 'BTC' # str | Retrieve data of the specified currency (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum response items.  Default: 100, minimum: 1, Maximum: 100 (optional) (default to 100)

try:
    # Get load records
    api_response = api_instance.list_portfolio_loan_records(type=type, currency=currency, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->list_portfolio_loan_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The types of lending records, borrow - indicates the action of borrowing funds, repay - indicates the action of repaying the borrowed funds | [optional] 
 **currency** | **str**| Retrieve data of the specified currency | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum response items.  Default: 100, minimum: 1, Maximum: 100 | [optional] [default to 100]

### Return type

[**list[PortfolioLoanRecord]**](PortfolioLoanRecord.md)

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

# **list_portfolio_loan_interest_records**
> list[UniLoanInterestRecord] list_portfolio_loan_interest_records(currency=currency, page=page, limit=limit)

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
api_instance = gate_api.PortfolioApi(api_client)
currency = 'BTC' # str | Retrieve data of the specified currency (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum response items.  Default: 100, minimum: 1, Maximum: 100 (optional) (default to 100)

try:
    # List interest records
    api_response = api_instance.list_portfolio_loan_interest_records(currency=currency, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->list_portfolio_loan_interest_records: %s\n" % e)
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

# **list_portfolio_orders**
> list[PortfolioSpotOrders] list_portfolio_orders(currency_pair, status, page=page, limit=limit, _from=_from, to=to, side=side)

List orders

When `status` is `open`, i.e., listing open orders, only pagination parameters `page` and `limit` are supported and `limit` cannot be larger than 100. Query by `side` and time range parameters `from` and `to` are not supported. When `status` is `finished`, i.e., listing finished orders, pagination parameters, time range parameters `from` and `to`, and `side` parameters are all supported. Time range parameters are handled as order finish time.

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
api_instance = gate_api.PortfolioApi(api_client)
currency_pair = 'BTC_USDT' # str | Retrieve results with specified currency pair. It is required for open orders, but optional for finished ones.
status = 'status_example' # str | List orders based on status  `open` - order is waiting to be filled `finished` - order has been filled or cancelled 
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of records to be returned. If `status` is `open`, maximum of `limit` is 100 (optional) (default to 100)
_from = 1627706330 # int | Start timestamp of the query (optional)
to = 1635329650 # int | Time range ending, default to current time (optional)
side = 'sell' # str | All bids or asks. Both included if not specified (optional)

try:
    # List orders
    api_response = api_instance.list_portfolio_orders(currency_pair, status, page=page, limit=limit, _from=_from, to=to, side=side)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->list_portfolio_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Retrieve results with specified currency pair. It is required for open orders, but optional for finished ones. | 
 **status** | **str**| List orders based on status  &#x60;open&#x60; - order is waiting to be filled &#x60;finished&#x60; - order has been filled or cancelled  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of records to be returned. If &#x60;status&#x60; is &#x60;open&#x60;, maximum of &#x60;limit&#x60; is 100 | [optional] [default to 100]
 **_from** | **int**| Start timestamp of the query | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **side** | **str**| All bids or asks. Both included if not specified | [optional] 

### Return type

[**list[PortfolioSpotOrders]**](PortfolioSpotOrders.md)

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

# **create_portfolio_orders**
> PortfolioSpotOrders create_portfolio_orders(create_portfolio_spot_order)

Create an order

Margin trading allows users to place spot orders using their spot accounts.  `auto_borrow` field can be set to `true` to enable the server to borrow the amount lacked using `POST /portfolio/loans` when your account's balance is not enough. Whether margin orders' fill will be used to repay margin loans automatically is determined by the value of `auto_repay` field in your order  Currently, it is not possible to enable both auto_borrow and auto_repay at the same time. Automatic repayment will be triggered when the order is finished, i.e., its status is either `cancelled` or `closed`.  **Order status**  An order waiting to be filled is `open`, and it stays `open` until it is filled totally. If fully filled, order is finished and its status turns to `closed`.If the order is cancelled before it is totally filled, whether or not partially filled, its status is `cancelled`.  **Iceberg order**  `iceberg` field can be used to set the amount shown. Set to `-1` to hide the order completely. Note that the hidden part's fee will be charged using taker's fee rate.  **Self Trade Prevention**  - Set `stp_act` to decide the strategy of self-trade prevention. For detailed usage, refer to the `stp_act` parameter in request body 

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
api_instance = gate_api.PortfolioApi(api_client)
create_portfolio_spot_order = gate_api.CreatePortfolioSpotOrder() # CreatePortfolioSpotOrder | 

try:
    # Create an order
    api_response = api_instance.create_portfolio_orders(create_portfolio_spot_order)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->create_portfolio_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_portfolio_spot_order** | [**CreatePortfolioSpotOrder**](CreatePortfolioSpotOrder.md)|  | 

### Return type

[**PortfolioSpotOrders**](PortfolioSpotOrders.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Order created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portfolio_order**
> PortfolioSpotOrders get_portfolio_order(order_id, currency_pair)

Get order detail

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
api_instance = gate_api.PortfolioApi(api_client)
order_id = '123456' # str | Order ID returned, or user custom ID(i.e., `text` field). Operations based on custom ID can only be checked when the order is in orderbook.  When the order is finished, it can be checked within 1 hour after the end of the order.  After that, only order ID is accepted.
currency_pair = 'BTC_USDT' # str | Currency pair

try:
    # Get order detail
    api_response = api_instance.get_portfolio_order(order_id, currency_pair)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->get_portfolio_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID returned, or user custom ID(i.e., &#x60;text&#x60; field). Operations based on custom ID can only be checked when the order is in orderbook.  When the order is finished, it can be checked within 1 hour after the end of the order.  After that, only order ID is accepted. | 
 **currency_pair** | **str**| Currency pair | 

### Return type

[**PortfolioSpotOrders**](PortfolioSpotOrders.md)

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

# **cancel_portfolio_order**
> PortfolioSpotOrders cancel_portfolio_order(order_id, currency_pair)

Cancel a single order

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
api_instance = gate_api.PortfolioApi(api_client)
order_id = '123456' # str | Order ID returned, or user custom ID(i.e., `text` field). Operations based on custom ID can only be checked when the order is in orderbook.  When the order is finished, it can be checked within 1 hour after the end of the order.  After that, only order ID is accepted.
currency_pair = 'BTC_USDT' # str | Currency pair

try:
    # Cancel a single order
    api_response = api_instance.cancel_portfolio_order(order_id, currency_pair)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->cancel_portfolio_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID returned, or user custom ID(i.e., &#x60;text&#x60; field). Operations based on custom ID can only be checked when the order is in orderbook.  When the order is finished, it can be checked within 1 hour after the end of the order.  After that, only order ID is accepted. | 
 **currency_pair** | **str**| Currency pair | 

### Return type

[**PortfolioSpotOrders**](PortfolioSpotOrders.md)

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

# **amend_portfolio_order**
> PortfolioSpotOrders amend_portfolio_order(order_id, currency_pair, order_patch)

Amend order

Regarding rate limiting: The rate limiting rules for amending orders and placing orders are shared.   Regarding matching priority: Only amending the quantity does not affect the matching priority. However, if the price is modified, the priority will be adjusted to the new price and placed at the end of the priority list.Important note: amending the quantity to a value lower than the filled quantity will trigger a cancellation of the order  

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
api_instance = gate_api.PortfolioApi(api_client)
order_id = '123456' # str | Order ID returned, or user custom ID(i.e., `text` field). Operations based on custom ID can only be checked when the order is in orderbook.  When the order is finished, it can be checked within 1 hour after the end of the order.  After that, only order ID is accepted.
currency_pair = 'BTC_USDT' # str | Currency pair
order_patch = gate_api.OrderPatch() # OrderPatch | 

try:
    # Amend order
    api_response = api_instance.amend_portfolio_order(order_id, currency_pair, order_patch)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling PortfolioApi->amend_portfolio_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Order ID returned, or user custom ID(i.e., &#x60;text&#x60; field). Operations based on custom ID can only be checked when the order is in orderbook.  When the order is finished, it can be checked within 1 hour after the end of the order.  After that, only order ID is accepted. | 
 **currency_pair** | **str**| Currency pair | 
 **order_patch** | [**OrderPatch**](OrderPatch.md)|  | 

### Return type

[**PortfolioSpotOrders**](PortfolioSpotOrders.md)

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

