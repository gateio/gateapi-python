# gate_api.RebateApi

All URIs are relative to *https://api.gateio.ws/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agency_transaction_history**](RebateApi.md#agency_transaction_history) | **GET** /rebate/agency/transaction_history | The agency obtains the transaction history of the recommended user.
[**agency_commissions_history**](RebateApi.md#agency_commissions_history) | **GET** /rebate/agency/commission_history | The agency obtains the commission history of the recommended user.
[**partner_transaction_history**](RebateApi.md#partner_transaction_history) | **GET** /rebate/partner/transaction_history | Partner obtains transaction records of recommended users.
[**partner_commissions_history**](RebateApi.md#partner_commissions_history) | **GET** /rebate/partner/commission_history | Partner obtains commission records of recommended users.
[**partner_sub_list**](RebateApi.md#partner_sub_list) | **GET** /rebate/partner/sub_list | Partner subordinate list.
[**rebate_broker_commission_history**](RebateApi.md#rebate_broker_commission_history) | **GET** /rebate/broker/commission_history | The broker obtains the user&#39;s commission rebate records.
[**rebate_broker_transaction_history**](RebateApi.md#rebate_broker_transaction_history) | **GET** /rebate/broker/transaction_history | The broker obtains the user&#39;s trading history.
[**rebate_user_info**](RebateApi.md#rebate_user_info) | **GET** /rebate/user/info | User retrieves rebate information.
[**user_sub_relation**](RebateApi.md#user_sub_relation) | **GET** /rebate/user/sub_relation | User-subordinate relationship.


# **agency_transaction_history**
> list[AgencyTransactionHistory] agency_transaction_history(currency_pair=currency_pair, user_id=user_id, _from=_from, to=to, limit=limit, offset=offset)

The agency obtains the transaction history of the recommended user.

Record time range cannot exceed 30 days.

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
currency_pair = 'BTC_USDT' # str | Specify the currency pair, if not specified, return all currency pairs. (optional)
user_id = 10003 # int | User ID. If not specified, all user records will be returned. (optional)
_from = 1602120000 # int | Time range beginning, default to 7 days before current time. (optional)
to = 1602123600 # int | Time range ending, default to current time. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)

try:
    # The agency obtains the transaction history of the recommended user.
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
 **currency_pair** | **str**| Specify the currency pair, if not specified, return all currency pairs. | [optional] 
 **user_id** | **int**| User ID. If not specified, all user records will be returned. | [optional] 
 **_from** | **int**| Time range beginning, default to 7 days before current time. | [optional] 
 **to** | **int**| Time range ending, default to current time. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]

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
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **agency_commissions_history**
> list[AgencyCommissionHistory] agency_commissions_history(currency=currency, user_id=user_id, _from=_from, to=to, limit=limit, offset=offset)

The agency obtains the commission history of the recommended user.

Record time range cannot exceed 30 days.

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
currency = 'BTC' # str | Filter by currency. Return all currency records if not specified. (optional)
user_id = 10003 # int | User ID. If not specified, all user records will be returned. (optional)
_from = 1602120000 # int | Time range beginning, default to 7 days before current time. (optional)
to = 1602123600 # int | Time range ending, default to current time. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)

try:
    # The agency obtains the commission history of the recommended user.
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
 **currency** | **str**| Filter by currency. Return all currency records if not specified. | [optional] 
 **user_id** | **int**| User ID. If not specified, all user records will be returned. | [optional] 
 **_from** | **int**| Time range beginning, default to 7 days before current time. | [optional] 
 **to** | **int**| Time range ending, default to current time. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]

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
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_transaction_history**
> PartnerTransactionHistory partner_transaction_history(currency_pair=currency_pair, user_id=user_id, _from=_from, to=to, limit=limit, offset=offset)

Partner obtains transaction records of recommended users.

Record time range cannot exceed 30 days.

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
currency_pair = 'BTC_USDT' # str | Specify the currency pair, if not specified, return all currency pairs. (optional)
user_id = 10003 # int | User ID. If not specified, all user records will be returned. (optional)
_from = 1602120000 # int | Time range beginning, default to 7 days before current time. (optional)
to = 1602123600 # int | Time range ending, default to current time. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)

try:
    # Partner obtains transaction records of recommended users.
    api_response = api_instance.partner_transaction_history(currency_pair=currency_pair, user_id=user_id, _from=_from, to=to, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling RebateApi->partner_transaction_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency_pair** | **str**| Specify the currency pair, if not specified, return all currency pairs. | [optional] 
 **user_id** | **int**| User ID. If not specified, all user records will be returned. | [optional] 
 **_from** | **int**| Time range beginning, default to 7 days before current time. | [optional] 
 **to** | **int**| Time range ending, default to current time. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]

### Return type

[**PartnerTransactionHistory**](PartnerTransactionHistory.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_commissions_history**
> PartnerCommissionHistory partner_commissions_history(currency=currency, user_id=user_id, _from=_from, to=to, limit=limit, offset=offset)

Partner obtains commission records of recommended users.

Record time range cannot exceed 30 days.

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
currency = 'BTC' # str | Filter by currency. Return all currency records if not specified. (optional)
user_id = 10003 # int | User ID. If not specified, all user records will be returned. (optional)
_from = 1602120000 # int | Time range beginning, default to 7 days before current time. (optional)
to = 1602123600 # int | Time range ending, default to current time. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)

try:
    # Partner obtains commission records of recommended users.
    api_response = api_instance.partner_commissions_history(currency=currency, user_id=user_id, _from=_from, to=to, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling RebateApi->partner_commissions_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currency** | **str**| Filter by currency. Return all currency records if not specified. | [optional] 
 **user_id** | **int**| User ID. If not specified, all user records will be returned. | [optional] 
 **_from** | **int**| Time range beginning, default to 7 days before current time. | [optional] 
 **to** | **int**| Time range ending, default to current time. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]

### Return type

[**PartnerCommissionHistory**](PartnerCommissionHistory.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partner_sub_list**
> PartnerSubList partner_sub_list(user_id=user_id, limit=limit, offset=offset)

Partner subordinate list.

Including sub-agents, direct customers, indirect customers.

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
user_id = 10003 # int | User ID. If not specified, all user records will be returned. (optional)
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)

try:
    # Partner subordinate list.
    api_response = api_instance.partner_sub_list(user_id=user_id, limit=limit, offset=offset)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling RebateApi->partner_sub_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| User ID. If not specified, all user records will be returned. | [optional] 
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]

### Return type

[**PartnerSubList**](PartnerSubList.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebate_broker_commission_history**
> list[BrokerCommission] rebate_broker_commission_history(limit=limit, offset=offset, user_id=user_id, _from=_from, to=to)

The broker obtains the user's commission rebate records.

Record time range cannot exceed 30 days.

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
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)
user_id = 10003 # int | User ID. If not specified, all user records will be returned. (optional)
_from = 1711929600 # int | The start time of the query record. If not specified, the default is to push forward 30 days from the current time. (optional)
to = 1714521600 # int | Time range ending, default to current time. (optional)

try:
    # The broker obtains the user's commission rebate records.
    api_response = api_instance.rebate_broker_commission_history(limit=limit, offset=offset, user_id=user_id, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling RebateApi->rebate_broker_commission_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]
 **user_id** | **int**| User ID. If not specified, all user records will be returned. | [optional] 
 **_from** | **int**| The start time of the query record. If not specified, the default is to push forward 30 days from the current time. | [optional] 
 **to** | **int**| Time range ending, default to current time. | [optional] 

### Return type

[**list[BrokerCommission]**](BrokerCommission.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebate_broker_transaction_history**
> list[BrokerTransaction] rebate_broker_transaction_history(limit=limit, offset=offset, user_id=user_id, _from=_from, to=to)

The broker obtains the user's trading history.

Record time range cannot exceed 30 days.

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
limit = 100 # int | Maximum number of records to be returned in a single list. (optional) (default to 100)
offset = 0 # int | List offset, starting from 0. (optional) (default to 0)
user_id = 10003 # int | User ID. If not specified, all user records will be returned. (optional)
_from = 1711929600 # int | The start time of the query record. If not specified, the default is to push forward 30 days from the current time. (optional)
to = 1714521600 # int | Time range ending, default to current time. (optional)

try:
    # The broker obtains the user's trading history.
    api_response = api_instance.rebate_broker_transaction_history(limit=limit, offset=offset, user_id=user_id, _from=_from, to=to)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling RebateApi->rebate_broker_transaction_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of records to be returned in a single list. | [optional] [default to 100]
 **offset** | **int**| List offset, starting from 0. | [optional] [default to 0]
 **user_id** | **int**| User ID. If not specified, all user records will be returned. | [optional] 
 **_from** | **int**| The start time of the query record. If not specified, the default is to push forward 30 days from the current time. | [optional] 
 **to** | **int**| Time range ending, default to current time. | [optional] 

### Return type

[**list[BrokerTransaction]**](BrokerTransaction.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebate_user_info**
> list[RebateUserInfo] rebate_user_info()

User retrieves rebate information.

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

try:
    # User retrieves rebate information.
    api_response = api_instance.rebate_user_info()
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling RebateApi->rebate_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[RebateUserInfo]**](RebateUserInfo.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_sub_relation**
> UserSubRelation user_sub_relation(user_id_list)

User-subordinate relationship.

Query whether the specified user is in the system.

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
user_id_list = '1, 2, 3' # str | Query the user's ID list, split by,, if there are more than 100, take 100.

try:
    # User-subordinate relationship.
    api_response = api_instance.user_sub_relation(user_id_list)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling RebateApi->user_sub_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id_list** | **str**| Query the user&#39;s ID list, split by,, if there are more than 100, take 100. | 

### Return type

[**UserSubRelation**](UserSubRelation.md)

### Authorization

[apiv4](../README.md#apiv4)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List retrieved. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

