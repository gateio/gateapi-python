# gate_api.RebateApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agency_transaction_history**](RebateApi.md#agency_transaction_history) | **GET** /rebate/agency/transaction_history | The broker obtains the transaction history of the recommended user
[**agency_commissions_history**](RebateApi.md#agency_commissions_history) | **GET** /rebate/agency/commission_history | The broker obtains the commission history of the recommended user


# **agency_transaction_history**
> list[AgencyTransactionHistory] agency_transaction_history(currency_pair=currency_pair, user_id=user_id, _from=_from, to=to, limit=limit, offset=offset)

The broker obtains the transaction history of the recommended user

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
api_instance = gate_api.RebateApi(api_client)
currency_pair = 'BTC_USDT' # str | Specify the currency pair, if not specified, return all currency pairs (optional)
user_id = '10003' # str | User ID. If not specified, all user records will be returned (optional)
_from = 1602120000 # int | Time range beginning, default to 7 days before current time (optional)
to = 1602123600 # int | Time range ending, default to current time (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # The broker obtains the transaction history of the recommended user
    api_response = api_instance.agency_transaction_history(currency_pair=currency_pair, user_id=user_id, _from=_from, to=to, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling RebateApi->agency_transaction_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Specify the currency pair, if not specified, return all currency pairs | [optional] 
 **user_id** | **str**| User ID. If not specified, all user records will be returned | [optional] 
 **_from** | **int**| Time range beginning, default to 7 days before current time | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

### Return type

[**list[AgencyTransactionHistory]**](AgencyTransactionHistory.md)

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

# **agency_commissions_history**
> list[AgencyCommissionHistory] agency_commissions_history(currency=currency, user_id=user_id, _from=_from, to=to, limit=limit, offset=offset)

The broker obtains the commission history of the recommended user

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
api_instance = gate_api.RebateApi(api_client)
currency = 'BTC' # str | Filter by currency. Return all currency records if not specified (optional)
user_id = '10003' # str | User ID. If not specified, all user records will be returned (optional)
_from = 1602120000 # int | Time range beginning, default to 7 days before current time (optional)
to = 1602123600 # int | Time range ending, default to current time (optional)
limit = 100 # int | Maximum number of records to be returned in a single list (optional) (default to 100)
offset = 0 # int | List offset, starting from 0 (optional) (default to 0)

try:
    # The broker obtains the commission history of the recommended user
    api_response = api_instance.agency_commissions_history(currency=currency, user_id=user_id, _from=_from, to=to, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling RebateApi->agency_commissions_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Filter by currency. Return all currency records if not specified | [optional] 
 **user_id** | **str**| User ID. If not specified, all user records will be returned | [optional] 
 **_from** | **int**| Time range beginning, default to 7 days before current time | [optional] 
 **to** | **int**| Time range ending, default to current time | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0 | [optional] [default to 0]

### Return type

[**list[AgencyCommissionHistory]**](AgencyCommissionHistory.md)

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

