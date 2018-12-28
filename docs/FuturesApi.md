# gate_client.FuturesApi

All URIs are relative to *https://fx-api.gateio.io/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](FuturesApi.md#cancel_order) | **DELETE** /futures/orders/{order_id} | Cancel a single order
[**cancel_orders**](FuturesApi.md#cancel_orders) | **DELETE** /futures/orders | Cancel all &#x60;open&#x60; orders matched
[**create_order**](FuturesApi.md#create_order) | **POST** /futures/orders | Create a futures order
[**get_my_trades**](FuturesApi.md#get_my_trades) | **GET** /futures/my_trades | List personal trading history
[**get_order**](FuturesApi.md#get_order) | **GET** /futures/orders/{order_id} | Get a single order
[**list_futures_accounts**](FuturesApi.md#list_futures_accounts) | **GET** /futures/accounts | Query futures account
[**list_futures_candlesticks**](FuturesApi.md#list_futures_candlesticks) | **GET** /futures/candlesticks | Get futures candlesticks
[**list_futures_contracts**](FuturesApi.md#list_futures_contracts) | **GET** /futures/contracts | List all futures contracts
[**list_futures_funding_rate_history**](FuturesApi.md#list_futures_funding_rate_history) | **GET** /futures/funding_rate | Funding rate history
[**list_futures_insurance_ledger**](FuturesApi.md#list_futures_insurance_ledger) | **GET** /futures/insurance | Futures insurance balance history
[**list_futures_order_book**](FuturesApi.md#list_futures_order_book) | **GET** /futures/order_book | Futures order book
[**list_futures_tickers**](FuturesApi.md#list_futures_tickers) | **GET** /futures/tickers | List futures tickers
[**list_futures_trades**](FuturesApi.md#list_futures_trades) | **GET** /futures/trades | Futures trading history
[**list_orders**](FuturesApi.md#list_orders) | **GET** /futures/orders | List futures orders
[**list_positions**](FuturesApi.md#list_positions) | **GET** /futures/positions | List all positions
[**update_position_leverage**](FuturesApi.md#update_position_leverage) | **POST** /futures/positions/{contract}/leverage | Update position leverage
[**update_position_margin**](FuturesApi.md#update_position_margin) | **POST** /futures/positions/{contract}/margin | Update position margin
[**update_position_risk_limit**](FuturesApi.md#update_position_risk_limit) | **POST** /futures/positions/{contract}/risk_limit | Update poisition risk limit


# **cancel_order**
> cancel_order(order_id)

Cancel a single order

### Example

```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.key = "YOUR_API_KEY"
configuration.secret = "YOUR_API_SECRET"

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
order_id = 'order_id_example' # str | order id

try:
    # Cancel a single order
    api_instance.cancel_order(order_id)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| order id | 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_orders**
> cancel_orders(contract, side=side)

Cancel all `open` orders matched

### Example

```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.key = "YOUR_API_KEY"
configuration.secret = "YOUR_API_SECRET"

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | futures contract
side = 'side_example' # str | All bids or asks. Both included in not specfied (optional)

try:
    # Cancel all `open` orders matched
    api_instance.cancel_orders(contract, side=side)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| futures contract | 
 **side** | **str**| All bids or asks. Both included in not specfied | [optional] 

### Return type

void (empty response body)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> FuturesOrder create_order(futures_order=futures_order)

Create a futures order

### Example

```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.key = "YOUR_API_KEY"
configuration.secret = "YOUR_API_SECRET"

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
futures_order = {"$ref":"examples/mercury/FuturesOrder.json"} # FuturesOrder |  (optional)

try:
    # Create a futures order
    api_response = api_instance.create_order(futures_order=futures_order)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **futures_order** | [**FuturesOrder**](FuturesOrder.md)|  | [optional] 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_trades**
> list[MyFuturesTrade] get_my_trades(contract=contract, limit=limit, last_id=last_id)

List personal trading history

### Example

```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.key = "YOUR_API_KEY"
configuration.secret = "YOUR_API_SECRET"

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | futures contract. If specified, return only data related to the contract (optional)
limit = 100 # int | maximum number of data returned in one request (optional) (default to 100)
last_id = 'last_id_example' # str | specify list staring record. Use the `id` in every last record of one list-query request to achieve consecutive list query (optional)

try:
    # List personal trading history
    api_response = api_instance.get_my_trades(contract=contract, limit=limit, last_id=last_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_my_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| futures contract. If specified, return only data related to the contract | [optional] 
 **limit** | **int**| maximum number of data returned in one request | [optional] [default to 100]
 **last_id** | **str**| specify list staring record. Use the &#x60;id&#x60; in every last record of one list-query request to achieve consecutive list query | [optional] 

### Return type

[**list[MyFuturesTrade]**](MyFuturesTrade.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> FuturesOrder get_order(order_id)

Get a single order

### Example

```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.key = "YOUR_API_KEY"
configuration.secret = "YOUR_API_SECRET"

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
order_id = 'order_id_example' # str | order id

try:
    # Get a single order
    api_response = api_instance.get_order(order_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| order id | 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_accounts**
> FuturesAccount list_futures_accounts()

Query futures account

### Example

```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.key = "YOUR_API_KEY"
configuration.secret = "YOUR_API_SECRET"

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))

try:
    # Query futures account
    api_response = api_instance.list_futures_accounts()
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FuturesAccount**](FuturesAccount.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_candlesticks**
> FuturesCandlestick list_futures_candlesticks(contract, _from=_from, to=to, limit=limit, interval=interval)

Get futures candlesticks

Return specified contract candlesticks. If prefix `contract` with `mark_`, the contract's mark price candlesticks are returned; if prefix with `index_`, index price candlesticks will be returned.  Maximum of 2000 points are returned in one query. Be sure not to exceed the limit when specifying `from`, `to` and `interval` 

### Example
```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# create an instance of the API class
api_instance = gate_client.FuturesApi()
contract = 'contract_example' # str | futures contract
_from = 1545696000 # float | Start time of candlesticks, formatted in Unix timestamp in seconds. Default to `to - 100 * interval` if not specified  (optional)
to = 1545955200 # float | End time of candlesticsk, formatted in Unix timestamp in seconds. Default to current time  (optional)
limit = 100 # int | Maximum recent data points returned. `limit` is conflicted with `from` and `to`. If either `from` or `to` is specified, request will be rejected.  (optional) (default to 100)
interval = '5m' # str | interval time between data points (optional) (default to '5m')

try:
    # Get futures candlesticks
    api_response = api_instance.list_futures_candlesticks(contract, _from=_from, to=to, limit=limit, interval=interval)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_candlesticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| futures contract | 
 **_from** | **float**| Start time of candlesticks, formatted in Unix timestamp in seconds. Default to &#x60;to - 100 * interval&#x60; if not specified  | [optional] 
 **to** | **float**| End time of candlesticsk, formatted in Unix timestamp in seconds. Default to current time  | [optional] 
 **limit** | **int**| Maximum recent data points returned. &#x60;limit&#x60; is conflicted with &#x60;from&#x60; and &#x60;to&#x60;. If either &#x60;from&#x60; or &#x60;to&#x60; is specified, request will be rejected.  | [optional] [default to 100]
 **interval** | **str**| interval time between data points | [optional] [default to &#39;5m&#39;]

### Return type

[**FuturesCandlestick**](FuturesCandlestick.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_contracts**
> list[Contract] list_futures_contracts()

List all futures contracts

### Example
```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# create an instance of the API class
api_instance = gate_client.FuturesApi()

try:
    # List all futures contracts
    api_response = api_instance.list_futures_contracts()
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_contracts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Contract]**](Contract.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_funding_rate_history**
> FundingRateRecord list_futures_funding_rate_history(contract, limit=limit)

Funding rate history

### Example
```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# create an instance of the API class
api_instance = gate_client.FuturesApi()
contract = 'contract_example' # str | futures contract
limit = 100 # int | maximum number of data returned in one request (optional) (default to 100)

try:
    # Funding rate history
    api_response = api_instance.list_futures_funding_rate_history(contract, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_funding_rate_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| futures contract | 
 **limit** | **int**| maximum number of data returned in one request | [optional] [default to 100]

### Return type

[**FundingRateRecord**](FundingRateRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_insurance_ledger**
> InsuranceRecord list_futures_insurance_ledger(limit=limit)

Futures insurance balance history

### Example
```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# create an instance of the API class
api_instance = gate_client.FuturesApi()
limit = 100 # int | maximum number of data returned in one request (optional) (default to 100)

try:
    # Futures insurance balance history
    api_response = api_instance.list_futures_insurance_ledger(limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_insurance_ledger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| maximum number of data returned in one request | [optional] [default to 100]

### Return type

[**InsuranceRecord**](InsuranceRecord.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_order_book**
> FuturesOrderBook list_futures_order_book(contract, interval=interval, limit=limit)

Futures order book

bids will be sorted by price from high to low, while asks sorted reversely

### Example
```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# create an instance of the API class
api_instance = gate_client.FuturesApi()
contract = 'contract_example' # str | futures contract
interval = '0' # str | order depth. 0 means no aggregation is applied. default to 0 (optional) (default to '0')
limit = 10 # int | maximum number of order depth data in asks or bids (optional) (default to 10)

try:
    # Futures order book
    api_response = api_instance.list_futures_order_book(contract, interval=interval, limit=limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_order_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| futures contract | 
 **interval** | **str**| order depth. 0 means no aggregation is applied. default to 0 | [optional] [default to &#39;0&#39;]
 **limit** | **int**| maximum number of order depth data in asks or bids | [optional] [default to 10]

### Return type

[**FuturesOrderBook**](FuturesOrderBook.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_tickers**
> list[FuturesTicker] list_futures_tickers(contract=contract)

List futures tickers

### Example
```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# create an instance of the API class
api_instance = gate_client.FuturesApi()
contract = 'contract_example' # str | futures contract. If specified, return only data related to the contract (optional)

try:
    # List futures tickers
    api_response = api_instance.list_futures_tickers(contract=contract)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| futures contract. If specified, return only data related to the contract | [optional] 

### Return type

[**list[FuturesTicker]**](FuturesTicker.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_trades**
> list[FuturesTrade] list_futures_trades(contract, limit=limit, last_id=last_id)

Futures trading history

### Example
```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# create an instance of the API class
api_instance = gate_client.FuturesApi()
contract = 'contract_example' # str | futures contract
limit = 100 # int | maximum number of data returned in one request (optional) (default to 100)
last_id = 'last_id_example' # str | specify list staring record. Use the `id` in every last record of one list-query request to achieve consecutive list query (optional)

try:
    # Futures trading history
    api_response = api_instance.list_futures_trades(contract, limit=limit, last_id=last_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| futures contract | 
 **limit** | **int**| maximum number of data returned in one request | [optional] [default to 100]
 **last_id** | **str**| specify list staring record. Use the &#x60;id&#x60; in every last record of one list-query request to achieve consecutive list query | [optional] 

### Return type

[**list[FuturesTrade]**](FuturesTrade.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> list[FuturesOrder] list_orders(contract, status, limit=limit, last_id=last_id)

List futures orders

### Example

```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.key = "YOUR_API_KEY"
configuration.secret = "YOUR_API_SECRET"

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | futures contract
status = 'status_example' # str | order status
limit = 100 # int | maximum number of data returned in one request (optional) (default to 100)
last_id = 'last_id_example' # str | specify list staring record. Use the `id` in every last record of one list-query request to achieve consecutive list query (optional)

try:
    # List futures orders
    api_response = api_instance.list_orders(contract, status, limit=limit, last_id=last_id)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| futures contract | 
 **status** | **str**| order status | 
 **limit** | **int**| maximum number of data returned in one request | [optional] [default to 100]
 **last_id** | **str**| specify list staring record. Use the &#x60;id&#x60; in every last record of one list-query request to achieve consecutive list query | [optional] 

### Return type

[**list[FuturesOrder]**](FuturesOrder.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_positions**
> list[Position] list_positions()

List all positions

### Example

```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.key = "YOUR_API_KEY"
configuration.secret = "YOUR_API_SECRET"

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))

try:
    # List all positions
    api_response = api_instance.list_positions()
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_positions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Position]**](Position.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_leverage**
> Position update_position_leverage(contract, leverage)

Update position leverage

### Example

```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.key = "YOUR_API_KEY"
configuration.secret = "YOUR_API_SECRET"

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | futures contract
leverage = 'leverage_example' # str | new leverage of position

try:
    # Update position leverage
    api_response = api_instance.update_position_leverage(contract, leverage)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_leverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| futures contract | 
 **leverage** | **str**| new leverage of position | 

### Return type

[**Position**](Position.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_margin**
> Position update_position_margin(contract, change)

Update position margin

### Example

```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.key = "YOUR_API_KEY"
configuration.secret = "YOUR_API_SECRET"

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | futures contract
change = 'change_example' # str | margin change. Use positive number to increase margin, negative number otherwise.

try:
    # Update position margin
    api_response = api_instance.update_position_margin(contract, change)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_margin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| futures contract | 
 **change** | **str**| margin change. Use positive number to increase margin, negative number otherwise. | 

### Return type

[**Position**](Position.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_risk_limit**
> Position update_position_risk_limit(contract, risk_limit)

Update poisition risk limit

### Example

```python
from __future__ import print_function
import gate_client
from gate_client.rest import ApiException

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.key = "YOUR_API_KEY"
configuration.secret = "YOUR_API_SECRET"

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | futures contract
risk_limit = 'risk_limit_example' # str | new risk limit of position

try:
    # Update poisition risk limit
    api_response = api_instance.update_position_risk_limit(contract, risk_limit)
    print(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_risk_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| futures contract | 
 **risk_limit** | **str**| new risk limit of position | 

### Return type

[**Position**](Position.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

