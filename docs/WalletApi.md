# gate_api.WalletApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deposit_address**](WalletApi.md#get_deposit_address) | **GET** /wallet/deposit_address | Generate currency deposit address
[**list_withdrawals**](WalletApi.md#list_withdrawals) | **GET** /wallet/withdrawals | Retrieve withdrawal records
[**list_deposits**](WalletApi.md#list_deposits) | **GET** /wallet/deposits | Retrieve deposit records
[**transfer**](WalletApi.md#transfer) | **POST** /wallet/transfers | Transfer between trading accounts
[**list_sub_account_transfers**](WalletApi.md#list_sub_account_transfers) | **GET** /wallet/sub_account_transfers | Transfer records between main and sub accounts
[**transfer_with_sub_account**](WalletApi.md#transfer_with_sub_account) | **POST** /wallet/sub_account_transfers | Transfer between main and sub accounts


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
currency = 'currency_example' # str | Currency name

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
> list[LedgerRecord] list_withdrawals(currency=currency, _from=_from, to=to, limit=limit, offset=offset)

Retrieve withdrawal records

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
api_instance = gate_api.WalletApi(api_client)
currency = 'BTC' # str | Filter by currency. Return all currency records if not specified (optional)
_from = 56 # int | Time range beginning, default to 7 days before current time (optional)
to = 56 # int | Time range ending, default to current time (optional)
limit = 100 # int | Maximum number of records returned in one list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Retrieve withdrawal records
    api_response = api_instance.list_withdrawals(currency=currency, _from=_from, to=to, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->list_withdrawals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Filter by currency. Return all currency records if not specified | [optional] 
 **_from** | **int**| Time range beginning, default to 7 days before current time | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **limit** | **int**| Maximum number of records returned in one list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

### Return type

[**list[LedgerRecord]**](LedgerRecord.md)

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

# **list_deposits**
> list[LedgerRecord] list_deposits(currency=currency, _from=_from, to=to, limit=limit, offset=offset)

Retrieve deposit records

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
api_instance = gate_api.WalletApi(api_client)
currency = 'BTC' # str | Filter by currency. Return all currency records if not specified (optional)
_from = 56 # int | Time range beginning, default to 7 days before current time (optional)
to = 56 # int | Time range ending, default to current time (optional)
limit = 100 # int | Maximum number of records returned in one list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Retrieve deposit records
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
 **currency** | **str**| Filter by currency. Return all currency records if not specified | [optional] 
 **_from** | **int**| Time range beginning, default to 7 days before current time | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **limit** | **int**| Maximum number of records returned in one list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

### Return type

[**list[LedgerRecord]**](LedgerRecord.md)

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

# **transfer**
> transfer(transfer)

Transfer between trading accounts

Transfer between different accounts. Currently support transfers between the following:  1. spot - margin 2. spot - futures(perpetual) 3. spot - delivery

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
    api_instance.transfer(transfer)
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

void (empty response body)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Balance transferred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sub_account_transfers**
> list[SubAccountTransfer] list_sub_account_transfers(sub_uid=sub_uid, _from=_from, to=to, limit=limit, offset=offset)

Transfer records between main and sub accounts

Record time range cannot exceed 30 days  > Note: only records after 2020-04-10 can be retrieved

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
sub_uid = '10003' # str | Sub account user ID. Return records related to all sub accounts if not specified (optional)
_from = 56 # int | Time range beginning, default to 7 days before current time (optional)
to = 56 # int | Time range ending, default to current time (optional)
limit = 100 # int | Maximum number of records returned in one list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Transfer records between main and sub accounts
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
 **sub_uid** | **str**| Sub account user ID. Return records related to all sub accounts if not specified | [optional] 
 **_from** | **int**| Time range beginning, default to 7 days before current time | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **limit** | **int**| Maximum number of records returned in one list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

### Return type

[**list[SubAccountTransfer]**](SubAccountTransfer.md)

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

# **transfer_with_sub_account**
> transfer_with_sub_account(sub_account_transfer)

Transfer between main and sub accounts

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
    api_instance.transfer_with_sub_account(sub_account_transfer)
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

void (empty response body)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Balance transferred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

