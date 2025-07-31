# gate_api.WalletApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_currency_chains**](WalletApi.md#list_currency_chains) | **GET** /wallet/currency_chains | Query chains supported for specified currency
[**get_deposit_address**](WalletApi.md#get_deposit_address) | **GET** /wallet/deposit_address | Generate currency deposit address
[**list_withdrawals**](WalletApi.md#list_withdrawals) | **GET** /wallet/withdrawals | Get withdrawal records
[**list_deposits**](WalletApi.md#list_deposits) | **GET** /wallet/deposits | Get deposit records
[**transfer**](WalletApi.md#transfer) | **POST** /wallet/transfers | Transfer between trading accounts
[**list_sub_account_transfers**](WalletApi.md#list_sub_account_transfers) | **GET** /wallet/sub_account_transfers | Get transfer records between main and sub accounts
[**transfer_with_sub_account**](WalletApi.md#transfer_with_sub_account) | **POST** /wallet/sub_account_transfers | Transfer between main and sub accounts
[**sub_account_to_sub_account**](WalletApi.md#sub_account_to_sub_account) | **POST** /wallet/sub_account_to_sub_account | Transfer between sub-accounts
[**get_transfer_order_status**](WalletApi.md#get_transfer_order_status) | **GET** /wallet/order_status | Transfer status query
[**list_withdraw_status**](WalletApi.md#list_withdraw_status) | **GET** /wallet/withdraw_status | Query withdrawal status
[**list_sub_account_balances**](WalletApi.md#list_sub_account_balances) | **GET** /wallet/sub_account_balances | Query sub-account balance information
[**list_sub_account_margin_balances**](WalletApi.md#list_sub_account_margin_balances) | **GET** /wallet/sub_account_margin_balances | Query sub-account isolated margin account balance information
[**list_sub_account_futures_balances**](WalletApi.md#list_sub_account_futures_balances) | **GET** /wallet/sub_account_futures_balances | Query sub-account perpetual futures account balance information
[**list_sub_account_cross_margin_balances**](WalletApi.md#list_sub_account_cross_margin_balances) | **GET** /wallet/sub_account_cross_margin_balances | Query sub-account cross margin account balance information
[**list_saved_address**](WalletApi.md#list_saved_address) | **GET** /wallet/saved_address | Query withdrawal address whitelist
[**get_trade_fee**](WalletApi.md#get_trade_fee) | **GET** /wallet/fee | Query personal trading fees
[**get_total_balance**](WalletApi.md#get_total_balance) | **GET** /wallet/total_balance | Query personal account totals
[**list_small_balance**](WalletApi.md#list_small_balance) | **GET** /wallet/small_balance | Get list of convertible small balance currencies
[**convert_small_balance**](WalletApi.md#convert_small_balance) | **POST** /wallet/small_balance | Convert small balance currency
[**list_small_balance_history**](WalletApi.md#list_small_balance_history) | **GET** /wallet/small_balance_history | Get convertible small balance currency history
[**list_push_orders**](WalletApi.md#list_push_orders) | **GET** /wallet/push | Get UID transfer history


# **list_currency_chains**
> list[CurrencyChain] list_currency_chains(currency)

Query chains supported for specified currency

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
api_instance = gate_api.WalletApi(api_client)
currency = 'GT' # str | Currency name

try:
    # Query chains supported for specified currency
    api_response = api_instance.list_currency_chains(currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_currency_chains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency name | 

### Return type

[**list[CurrencyChain]**](CurrencyChain.md)

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

# **get_deposit_address**
> DepositAddress get_deposit_address(currency)

Generate currency deposit address

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
api_instance = gate_api.WalletApi(api_client)
currency = 'USDT' # str | Currency name

try:
    # Generate currency deposit address
    api_response = api_instance.get_deposit_address(currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->get_deposit_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency name | 

### Return type

[**DepositAddress**](DepositAddress.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Address successfully generated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_withdrawals**
> list[WithdrawalRecord] list_withdrawals(currency=currency, withdraw_id=withdraw_id, asset_class=asset_class, withdraw_order_id=withdraw_order_id, _from=_from, to=to, limit=limit, offset=offset)

Get withdrawal records

Record query time range cannot exceed 30 days

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
api_instance = gate_api.WalletApi(api_client)
currency = 'BTC' # str | Specify the currency. If not specified, returns all currencies (optional)
withdraw_id = 'withdraw_id_example' # str | Withdrawal record ID starts with 'w', such as: w1879219868. When withdraw_id is not empty, only this specific withdrawal record will be queried, and time-based querying will be disabled (optional)
asset_class = 'asset_class_example' # str | Currency type of withdrawal record, empty by default. Supports querying withdrawal records in main zone and innovation zone on demand. Value range: SPOT, PILOT  SPOT: Main Zone PILOT: Innovation Zone (optional)
withdraw_order_id = 'withdraw_order_id_example' # str | User-defined order number for withdrawal. Default is empty. When not empty, the specified user-defined order number record will be queried (optional)
_from = 1602120000 # int | Start time for querying records, defaults to 7 days before current time if not specified (optional)
to = 1602123600 # int | End timestamp for the query, defaults to current time if not specified (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Get withdrawal records
    api_response = api_instance.list_withdrawals(currency=currency, withdraw_id=withdraw_id, asset_class=asset_class, withdraw_order_id=withdraw_order_id, _from=_from, to=to, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_withdrawals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Specify the currency. If not specified, returns all currencies | [optional] 
 **withdraw_id** | **str**| Withdrawal record ID starts with &#39;w&#39;, such as: w1879219868. When withdraw_id is not empty, only this specific withdrawal record will be queried, and time-based querying will be disabled | [optional] 
 **asset_class** | **str**| Currency type of withdrawal record, empty by default. Supports querying withdrawal records in main zone and innovation zone on demand. Value range: SPOT, PILOT  SPOT: Main Zone PILOT: Innovation Zone | [optional] 
 **withdraw_order_id** | **str**| User-defined order number for withdrawal. Default is empty. When not empty, the specified user-defined order number record will be queried | [optional] 
 **_from** | **int**| Start time for querying records, defaults to 7 days before current time if not specified | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

### Return type

[**list[WithdrawalRecord]**](WithdrawalRecord.md)

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

# **list_deposits**
> list[DepositRecord] list_deposits(currency=currency, _from=_from, to=to, limit=limit, offset=offset)

Get deposit records

Record query time range cannot exceed 30 days

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
api_instance = gate_api.WalletApi(api_client)
currency = 'BTC' # str | Specify the currency. If not specified, returns all currencies (optional)
_from = 1602120000 # int | Start time for querying records, defaults to 7 days before current time if not specified (optional)
to = 1602123600 # int | End timestamp for the query, defaults to current time if not specified (optional)
limit = 100 # int | Maximum number of entries returned in the list, limited to 500 transactions (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Get deposit records
    api_response = api_instance.list_deposits(currency=currency, _from=_from, to=to, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_deposits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Specify the currency. If not specified, returns all currencies | [optional] 
 **_from** | **int**| Start time for querying records, defaults to 7 days before current time if not specified | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 
 **limit** | **int**| Maximum number of entries returned in the list, limited to 500 transactions | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

### Return type

[**list[DepositRecord]**](DepositRecord.md)

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

# **transfer**
> TransactionID transfer(transfer)

Transfer between trading accounts

Balance transfers between personal trading accounts. Currently supports the following transfer operations:  1. Spot account - Margin account 2. Spot account - Perpetual futures account 3. Spot account - Delivery futures account 4. Spot account - Options account

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
api_instance = gate_api.WalletApi(api_client)
transfer = gate_api.Transfer() # Transfer | 

try:
    # Transfer between trading accounts
    api_response = api_instance.transfer(transfer)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer** | [**Transfer**](Transfer.md)|  | 

### Return type

[**TransactionID**](TransactionID.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer operation successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sub_account_transfers**
> list[SubAccountTransferRecordItem] list_sub_account_transfers(sub_uid=sub_uid, _from=_from, to=to, limit=limit, offset=offset)

Get transfer records between main and sub accounts

Record query time range cannot exceed 30 days  > Note: Only records after 2020-04-10 can be retrieved

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
api_instance = gate_api.WalletApi(api_client)
sub_uid = '10003' # str | Sub-account user ID, you can query multiple records separated by `,`. If not specified, it will return records of all sub-accounts (optional)
_from = 1602120000 # int | Start time for querying records, defaults to 7 days before current time if not specified (optional)
to = 1602123600 # int | End timestamp for the query, defaults to current time if not specified (optional)
limit = 100 # int | Maximum number of records returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Get transfer records between main and sub accounts
    api_response = api_instance.list_sub_account_transfers(sub_uid=sub_uid, _from=_from, to=to, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_sub_account_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_uid** | **str**| Sub-account user ID, you can query multiple records separated by &#x60;,&#x60;. If not specified, it will return records of all sub-accounts | [optional] 
 **_from** | **int**| Start time for querying records, defaults to 7 days before current time if not specified | [optional] 
 **to** | **int**| End timestamp for the query, defaults to current time if not specified | [optional] 
 **limit** | **int**| Maximum number of records returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

### Return type

[**list[SubAccountTransferRecordItem]**](SubAccountTransferRecordItem.md)

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

# **transfer_with_sub_account**
> TransactionID transfer_with_sub_account(sub_account_transfer)

Transfer between main and sub accounts

Supports transfers to/from sub-account's spot or futures accounts. Note that regardless of which sub-account is operated, only the main account's spot account is used

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
api_instance = gate_api.WalletApi(api_client)
sub_account_transfer = gate_api.SubAccountTransfer() # SubAccountTransfer | 

try:
    # Transfer between main and sub accounts
    api_response = api_instance.transfer_with_sub_account(sub_account_transfer)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->transfer_with_sub_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_transfer** | [**SubAccountTransfer**](SubAccountTransfer.md)|  | 

### Return type

[**TransactionID**](TransactionID.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer operation successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_account_to_sub_account**
> TransactionID sub_account_to_sub_account(sub_account_to_sub_account)

Transfer between sub-accounts

Supports balance transfers between two sub-accounts under the same main account. You can use either the main account's API Key or the source sub-account's API Key to perform the operation

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
api_instance = gate_api.WalletApi(api_client)
sub_account_to_sub_account = gate_api.SubAccountToSubAccount() # SubAccountToSubAccount | 

try:
    # Transfer between sub-accounts
    api_response = api_instance.sub_account_to_sub_account(sub_account_to_sub_account)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->sub_account_to_sub_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_account_to_sub_account** | [**SubAccountToSubAccount**](SubAccountToSubAccount.md)|  | 

### Return type

[**TransactionID**](TransactionID.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer operation successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfer_order_status**
> TransferOrderStatus get_transfer_order_status(client_order_id=client_order_id, tx_id=tx_id)

Transfer status query

Supports querying transfer status based on user-defined client_order_id or tx_id returned by the transfer interface

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
api_instance = gate_api.WalletApi(api_client)
client_order_id = 'da3ce7a088c8b0372b741419c7829033' # str | Customer-defined ID to prevent duplicate transfers. Can be a combination of letters (case-sensitive), numbers, hyphens '-', and underscores '_'. Can be pure letters or pure numbers with length between 1-64 characters (optional)
tx_id = '59636381286' # str | Transfer operation number, cannot be empty at the same time as client_order_id (optional)

try:
    # Transfer status query
    api_response = api_instance.get_transfer_order_status(client_order_id=client_order_id, tx_id=tx_id)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->get_transfer_order_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_order_id** | **str**| Customer-defined ID to prevent duplicate transfers. Can be a combination of letters (case-sensitive), numbers, hyphens &#39;-&#39;, and underscores &#39;_&#39;. Can be pure letters or pure numbers with length between 1-64 characters | [optional] 
 **tx_id** | **str**| Transfer operation number, cannot be empty at the same time as client_order_id | [optional] 

### Return type

[**TransferOrderStatus**](TransferOrderStatus.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transfer status retrieved successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_withdraw_status**
> list[WithdrawStatus] list_withdraw_status(currency=currency)

Query withdrawal status

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
api_instance = gate_api.WalletApi(api_client)
currency = 'BTC' # str | Query by specified currency name (optional)

try:
    # Query withdrawal status
    api_response = api_instance.list_withdraw_status(currency=currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_withdraw_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Query by specified currency name | [optional] 

### Return type

[**list[WithdrawStatus]**](WithdrawStatus.md)

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

# **list_sub_account_balances**
> list[SubAccountBalance] list_sub_account_balances(sub_uid=sub_uid)

Query sub-account balance information

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
api_instance = gate_api.WalletApi(api_client)
sub_uid = '10003' # str | Sub-account user ID, you can query multiple records separated by `,`. If not specified, it will return records of all sub-accounts (optional)

try:
    # Query sub-account balance information
    api_response = api_instance.list_sub_account_balances(sub_uid=sub_uid)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_sub_account_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_uid** | **str**| Sub-account user ID, you can query multiple records separated by &#x60;,&#x60;. If not specified, it will return records of all sub-accounts | [optional] 

### Return type

[**list[SubAccountBalance]**](SubAccountBalance.md)

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

# **list_sub_account_margin_balances**
> list[SubAccountMarginBalance] list_sub_account_margin_balances(sub_uid=sub_uid)

Query sub-account isolated margin account balance information

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
api_instance = gate_api.WalletApi(api_client)
sub_uid = '10003' # str | Sub-account user ID, you can query multiple records separated by `,`. If not specified, it will return records of all sub-accounts (optional)

try:
    # Query sub-account isolated margin account balance information
    api_response = api_instance.list_sub_account_margin_balances(sub_uid=sub_uid)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_sub_account_margin_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_uid** | **str**| Sub-account user ID, you can query multiple records separated by &#x60;,&#x60;. If not specified, it will return records of all sub-accounts | [optional] 

### Return type

[**list[SubAccountMarginBalance]**](SubAccountMarginBalance.md)

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

# **list_sub_account_futures_balances**
> list[SubAccountFuturesBalance] list_sub_account_futures_balances(sub_uid=sub_uid, settle=settle)

Query sub-account perpetual futures account balance information

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
api_instance = gate_api.WalletApi(api_client)
sub_uid = '10003' # str | Sub-account user ID, you can query multiple records separated by `,`. If not specified, it will return records of all sub-accounts (optional)
settle = 'usdt' # str | Query balance of specified settlement currency (optional)

try:
    # Query sub-account perpetual futures account balance information
    api_response = api_instance.list_sub_account_futures_balances(sub_uid=sub_uid, settle=settle)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_sub_account_futures_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_uid** | **str**| Sub-account user ID, you can query multiple records separated by &#x60;,&#x60;. If not specified, it will return records of all sub-accounts | [optional] 
 **settle** | **str**| Query balance of specified settlement currency | [optional] 

### Return type

[**list[SubAccountFuturesBalance]**](SubAccountFuturesBalance.md)

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

# **list_sub_account_cross_margin_balances**
> list[SubAccountCrossMarginBalance] list_sub_account_cross_margin_balances(sub_uid=sub_uid)

Query sub-account cross margin account balance information

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
api_instance = gate_api.WalletApi(api_client)
sub_uid = '10003' # str | Sub-account user ID, you can query multiple records separated by `,`. If not specified, it will return records of all sub-accounts (optional)

try:
    # Query sub-account cross margin account balance information
    api_response = api_instance.list_sub_account_cross_margin_balances(sub_uid=sub_uid)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_sub_account_cross_margin_balances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_uid** | **str**| Sub-account user ID, you can query multiple records separated by &#x60;,&#x60;. If not specified, it will return records of all sub-accounts | [optional] 

### Return type

[**list[SubAccountCrossMarginBalance]**](SubAccountCrossMarginBalance.md)

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

# **list_saved_address**
> list[SavedAddress] list_saved_address(currency, chain=chain, limit=limit, page=page)

Query withdrawal address whitelist

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
api_instance = gate_api.WalletApi(api_client)
currency = 'USDT' # str | Currency
chain = '' # str | Chain name (optional) (default to '')
limit = '50' # str | Maximum number returned, up to 100 (optional) (default to '50')
page = 1 # int | Page number (optional) (default to 1)

try:
    # Query withdrawal address whitelist
    api_response = api_instance.list_saved_address(currency, chain=chain, limit=limit, page=page)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_saved_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency | 
 **chain** | **str**| Chain name | [optional] [default to &#39;&#39;]
 **limit** | **str**| Maximum number returned, up to 100 | [optional] [default to &#39;50&#39;]
 **page** | **int**| Page number | [optional] [default to 1]

### Return type

[**list[SavedAddress]**](SavedAddress.md)

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

# **get_trade_fee**
> TradeFee get_trade_fee(currency_pair=currency_pair, settle=settle)

Query personal trading fees

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
api_instance = gate_api.WalletApi(api_client)
currency_pair = 'BTC_USDT' # str | Specify currency pair to get more accurate fee settings.  This field is optional. Usually fee settings are the same for all currency pairs. (optional)
settle = 'BTC' # str | Specify the settlement currency of the contract to get more accurate fee settings.  This field is optional. Generally, the fee settings for all settlement currencies are the same. (optional)

try:
    # Query personal trading fees
    api_response = api_instance.get_trade_fee(currency_pair=currency_pair, settle=settle)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->get_trade_fee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Specify currency pair to get more accurate fee settings.  This field is optional. Usually fee settings are the same for all currency pairs. | [optional] 
 **settle** | **str**| Specify the settlement currency of the contract to get more accurate fee settings.  This field is optional. Generally, the fee settings for all settlement currencies are the same. | [optional] 

### Return type

[**TradeFee**](TradeFee.md)

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

# **get_total_balance**
> TotalBalance get_total_balance(currency=currency)

Query personal account totals

This query endpoint returns the total *estimated value* of all currencies in each account converted to the input currency. Exchange rates and related account balance information may be cached for up to 1 minute. It is not recommended to use this interface data for real-time calculations.  For real-time calculations, query the corresponding balance interface based on account type, such as:  - `GET /spot/accounts` to query spot account - `GET /margin/accounts` to query margin account - `GET /futures/{settle}/accounts` to query futures account

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
api_instance = gate_api.WalletApi(api_client)
currency = 'USDT' # str | Target currency type for statistical conversion. Accepts BTC, CNY, USD, and USDT. USDT is the default value (optional) (default to 'USDT')

try:
    # Query personal account totals
    api_response = api_instance.get_total_balance(currency=currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->get_total_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Target currency type for statistical conversion. Accepts BTC, CNY, USD, and USDT. USDT is the default value | [optional] [default to &#39;USDT&#39;]

### Return type

[**TotalBalance**](TotalBalance.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request is valid and successfully returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_small_balance**
> list[SmallBalance] list_small_balance()

Get list of convertible small balance currencies

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
api_instance = gate_api.WalletApi(api_client)

try:
    # Get list of convertible small balance currencies
    api_response = api_instance.list_small_balance()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_small_balance: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SmallBalance]**](SmallBalance.md)

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

# **convert_small_balance**
> convert_small_balance(convert_small_balance)

Convert small balance currency

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
api_instance = gate_api.WalletApi(api_client)
convert_small_balance = gate_api.ConvertSmallBalance() # ConvertSmallBalance | 

try:
    # Convert small balance currency
    api_instance.convert_small_balance(convert_small_balance)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->convert_small_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert_small_balance** | [**ConvertSmallBalance**](ConvertSmallBalance.md)|  | 

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_small_balance_history**
> list[SmallBalanceHistory] list_small_balance_history(currency=currency, page=page, limit=limit)

Get convertible small balance currency history

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
api_instance = gate_api.WalletApi(api_client)
currency = 'currency_example' # str | Currency to convert (optional)
page = 1 # int | Page number (optional) (default to 1)
limit = 100 # int | Maximum number of items returned. Default: 100, minimum: 1, maximum: 100 (optional) (default to 100)

try:
    # Get convertible small balance currency history
    api_response = api_instance.list_small_balance_history(currency=currency, page=page, limit=limit)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_small_balance_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Currency to convert | [optional] 
 **page** | **int**| Page number | [optional] [default to 1]
 **limit** | **int**| Maximum number of items returned. Default: 100, minimum: 1, maximum: 100 | [optional] [default to 100]

### Return type

[**list[SmallBalanceHistory]**](SmallBalanceHistory.md)

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

# **list_push_orders**
> list[UidPushOrder] list_push_orders(id=id, _from=_from, to=to, limit=limit, offset=offset, transaction_type=transaction_type)

Get UID transfer history

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
api_instance = gate_api.WalletApi(api_client)
id = 56 # int | Order ID (optional)
_from = 56 # int | Start time for querying records. If not specified, defaults to 7 days before the current time. Unix timestamp in seconds (optional)
to = 56 # int | End time for querying records. If not specified, defaults to the current time. Unix timestamp in seconds (optional)
limit = 100 # int | Maximum number of items returned in the list, default value is 100 (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)
transaction_type = 'withdraw' # str | Order type returned in the list: `withdraw`, `deposit`. Default is `withdraw`. (optional) (default to 'withdraw')

try:
    # Get UID transfer history
    api_response = api_instance.list_push_orders(id=id, _from=_from, to=to, limit=limit, offset=offset, transaction_type=transaction_type)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_push_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Order ID | [optional] 
 **_from** | **int**| Start time for querying records. If not specified, defaults to 7 days before the current time. Unix timestamp in seconds | [optional] 
 **to** | **int**| End time for querying records. If not specified, defaults to the current time. Unix timestamp in seconds | [optional] 
 **limit** | **int**| Maximum number of items returned in the list, default value is 100 | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]
 **transaction_type** | **str**| Order type returned in the list: &#x60;withdraw&#x60;, &#x60;deposit&#x60;. Default is &#x60;withdraw&#x60;. | [optional] [default to &#39;withdraw&#39;]

### Return type

[**list[UidPushOrder]**](UidPushOrder.md)

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

