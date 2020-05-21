# gate_api.WithdrawalApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**withdraw**](WithdrawalApi.md#withdraw) | **POST** /withdrawals | Withdraw


# **withdraw**
> LedgerRecord withdraw(ledger_record)

Withdraw

### Example

```python
from __future__ import print_function
import gate_api
from gate_api.rest import ApiException

configuration = gate_api.Configuration()
configuration.key = 'YOUR_API_KEY'
configuration.secret = 'YOUR_API_SECRET'

# create an instance of the API class
api_instance = gate_api.WithdrawalApi(gate_api.ApiClient(configuration))
ledger_record = gate_api.LedgerRecord() # LedgerRecord | 

try:
    # Withdraw
    api_response = api_instance.withdraw(ledger_record)
    print(api_response)
except ApiException as e:
    print("Exception when calling WithdrawalApi->withdraw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ledger_record** | [**LedgerRecord**](LedgerRecord.md)|  | 

### Return type

[**LedgerRecord**](LedgerRecord.md)

### Authorization

Authentication with API key and secret is required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

