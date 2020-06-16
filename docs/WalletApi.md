# gate_api.WalletApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_deposit_address**](WalletApi.md#get_deposit_address) | **GET** /wallet/deposit_address | Generate currency deposit address
[**list_deposits**](WalletApi.md#list_deposits) | **GET** /wallet/deposits | Retrieve deposit records. Time range cannot exceed 30 days
[**list_withdrawals**](WalletApi.md#list_withdrawals) | **GET** /wallet/withdrawals | Retrieve withdrawal records. Time range cannot exceed 30 days
[**transfer**](WalletApi.md#transfer) | **POST** /wallet/transfers | Transfer between accounts
[**transfer_with_sub_account**](WalletApi.md#transfer_with_sub_account) | **POST** /wallet/sub_account_transfers | Transfer between main and sub accounts


# **get_deposit_address**
> DepositAddress get_deposit_address(currency)

Generate currency deposit address

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.WalletApi(gate_api.ApiClient(configuration))
currency = 'currency_example' # str | Currency name

try:
    # Generate currency deposit address
    api_response = api_instance.get_deposit_address(currency)
    print(api_response)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_deposits**
> list[LedgerRecord] list_deposits(currency=currency, _from=_from, to=to, limit=limit, offset=offset)

Retrieve deposit records. Time range cannot exceed 30 days

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.WalletApi(gate_api.ApiClient(configuration))
currency = 'BTC' # str | Filter by currency. Return all currency records if not specified (optional)
_from = 56 # int | Time range beginning, default to 7 days before current time (optional)
to = 56 # int | Time range ending, default to current time (optional)
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Retrieve deposit records. Time range cannot exceed 30 days
    api_response = api_instance.list_deposits(currency=currency, _from=_from, to=to, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->list_deposits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Filter by currency. Return all currency records if not specified | [optional] 
 **_from** | **int**| Time range beginning, default to 7 days before current time | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

### Return type

[**list[LedgerRecord]**](LedgerRecord.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_withdrawals**
> list[LedgerRecord] list_withdrawals(currency=currency, _from=_from, to=to, limit=limit, offset=offset)

Retrieve withdrawal records. Time range cannot exceed 30 days

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.WalletApi(gate_api.ApiClient(configuration))
currency = 'BTC' # str | Filter by currency. Return all currency records if not specified (optional)
_from = 56 # int | Time range beginning, default to 7 days before current time (optional)
to = 56 # int | Time range ending, default to current time (optional)
limit = 100 # int | Maximum number of record returned in one list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # Retrieve withdrawal records. Time range cannot exceed 30 days
    api_response = api_instance.list_withdrawals(currency=currency, _from=_from, to=to, limit=limit, offset=offset)
    print(api_response)
except ApiException as e:
    print("Exception when calling WalletApi->list_withdrawals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Filter by currency. Return all currency records if not specified | [optional] 
 **_from** | **int**| Time range beginning, default to 7 days before current time | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **limit** | **int**| Maximum number of record returned in one list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

### Return type

[**list[LedgerRecord]**](LedgerRecord.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer**
> transfer(transfer)

Transfer between accounts

Transfer between different accounts. Currently support transfers between the following:  1. spot - margin 2. spot - futures

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.WalletApi(gate_api.ApiClient(configuration))
transfer = gate_api.Transfer() # Transfer | 

try:
    # Transfer between accounts
    api_instance.transfer(transfer)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_with_sub_account**
> transfer_with_sub_account(sub_account_transfer)

Transfer between main and sub accounts

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.WalletApi(gate_api.ApiClient(configuration))
sub_account_transfer = gate_api.SubAccountTransfer() # SubAccountTransfer | 

try:
    # Transfer between main and sub accounts
    api_instance.transfer_with_sub_account(sub_account_transfer)
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

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

