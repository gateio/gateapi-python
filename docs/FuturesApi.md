# gate_client.FuturesApi

All URIs are relative to *https://fx-api.gateio.io/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](FuturesApi.md#cancel_order) | **DELETE** /futures/orders/{order_id} | 撤销单个订单
[**cancel_orders**](FuturesApi.md#cancel_orders) | **DELETE** /futures/orders | 批量取消状态为 open 的订单
[**create_order**](FuturesApi.md#create_order) | **POST** /futures/orders | 期货交易下单
[**get_my_trades**](FuturesApi.md#get_my_trades) | **GET** /futures/my_trades | 查询个人成交记录
[**get_order**](FuturesApi.md#get_order) | **GET** /futures/orders/{order_id} | 查询单个订单详情
[**list_futures_accounts**](FuturesApi.md#list_futures_accounts) | **GET** /futures/accounts | 获取期货账号
[**list_futures_candlesticks**](FuturesApi.md#list_futures_candlesticks) | **GET** /futures/candlesticks | 期货市场 K 线图
[**list_futures_contracts**](FuturesApi.md#list_futures_contracts) | **GET** /futures/contracts | 查询所有的期货信息
[**list_futures_funding_rate_history**](FuturesApi.md#list_futures_funding_rate_history) | **GET** /futures/funding_rate | 期货市场历史资金费率
[**list_futures_insurance_ledger**](FuturesApi.md#list_futures_insurance_ledger) | **GET** /futures/insurance | 期货市场保险基金历史
[**list_futures_order_book**](FuturesApi.md#list_futures_order_book) | **GET** /futures/order_book | 查询期货市场深度信息
[**list_futures_tickers**](FuturesApi.md#list_futures_tickers) | **GET** /futures/tickers | 获取所有期货交易行情统计
[**list_futures_trades**](FuturesApi.md#list_futures_trades) | **GET** /futures/trades | 期货市场成交记录
[**list_orders**](FuturesApi.md#list_orders) | **GET** /futures/orders | 查询订单列表
[**list_positions**](FuturesApi.md#list_positions) | **GET** /futures/positions | 获取用户头寸列表
[**update_position_leverage**](FuturesApi.md#update_position_leverage) | **POST** /futures/positions/{contract}/leverage | 更新头寸杠杆
[**update_position_margin**](FuturesApi.md#update_position_margin) | **POST** /futures/positions/{contract}/margin | 更新头寸保证金
[**update_position_risk_limit**](FuturesApi.md#update_position_risk_limit) | **POST** /futures/positions/{contract}/risk_limit | 更新头寸风险限额


# **cancel_order**
> cancel_order(order_id)

撤销单个订单

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.api_key['KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
order_id = 'order_id_example' # str | 成功创建订单时返回的 ID

try:
    # 撤销单个订单
    api_instance.cancel_order(order_id)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_order: %s\n" % e)
```


* Api Key Authentication (api_sign): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_sign
configuration = gate_client.Configuration()
configuration.api_key['SIGN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SIGN'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
order_id = 'order_id_example' # str | 成功创建订单时返回的 ID

try:
    # 撤销单个订单
    api_instance.cancel_order(order_id)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_order: %s\n" % e)
```


* Api Key Authentication (api_timestamp): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_timestamp
configuration = gate_client.Configuration()
configuration.api_key['Timestamp'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Timestamp'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
order_id = 'order_id_example' # str | 成功创建订单时返回的 ID

try:
    # 撤销单个订单
    api_instance.cancel_order(order_id)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| 成功创建订单时返回的 ID | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_sign](../README.md#api_sign), [api_timestamp](../README.md#api_timestamp)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_orders**
> cancel_orders(contract, side=side)

批量取消状态为 open 的订单

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.api_key['KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
side = 'side_example' # str | 指定全部买单或全部卖单，不指定则两者都包括 (optional)

try:
    # 批量取消状态为 open 的订单
    api_instance.cancel_orders(contract, side=side)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_orders: %s\n" % e)
```


* Api Key Authentication (api_sign): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_sign
configuration = gate_client.Configuration()
configuration.api_key['SIGN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SIGN'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
side = 'side_example' # str | 指定全部买单或全部卖单，不指定则两者都包括 (optional)

try:
    # 批量取消状态为 open 的订单
    api_instance.cancel_orders(contract, side=side)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_orders: %s\n" % e)
```


* Api Key Authentication (api_timestamp): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_timestamp
configuration = gate_client.Configuration()
configuration.api_key['Timestamp'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Timestamp'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
side = 'side_example' # str | 指定全部买单或全部卖单，不指定则两者都包括 (optional)

try:
    # 批量取消状态为 open 的订单
    api_instance.cancel_orders(contract, side=side)
except ApiException as e:
    print("Exception when calling FuturesApi->cancel_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| 期货合约标识 | 
 **side** | **str**| 指定全部买单或全部卖单，不指定则两者都包括 | [optional] 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_sign](../README.md#api_sign), [api_timestamp](../README.md#api_timestamp)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> FuturesOrder create_order(futures_order=futures_order)

期货交易下单

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.api_key['KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
futures_order = {"$ref":"examples/mercury/FuturesOrder.json"} # FuturesOrder |  (optional)

try:
    # 期货交易下单
    api_response = api_instance.create_order(futures_order=futures_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->create_order: %s\n" % e)
```


* Api Key Authentication (api_sign): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_sign
configuration = gate_client.Configuration()
configuration.api_key['SIGN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SIGN'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
futures_order = {"$ref":"examples/mercury/FuturesOrder.json"} # FuturesOrder |  (optional)

try:
    # 期货交易下单
    api_response = api_instance.create_order(futures_order=futures_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->create_order: %s\n" % e)
```


* Api Key Authentication (api_timestamp): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_timestamp
configuration = gate_client.Configuration()
configuration.api_key['Timestamp'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Timestamp'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
futures_order = {"$ref":"examples/mercury/FuturesOrder.json"} # FuturesOrder |  (optional)

try:
    # 期货交易下单
    api_response = api_instance.create_order(futures_order=futures_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **futures_order** | [**FuturesOrder**](FuturesOrder.md)|  | [optional] 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### Authorization

[api_key](../README.md#api_key), [api_sign](../README.md#api_sign), [api_timestamp](../README.md#api_timestamp)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_trades**
> list[MyFuturesTrade] get_my_trades(contract=contract, limit=limit, last_id=last_id)

查询个人成交记录

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.api_key['KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识，如果指定则只返回该合约相关数据 (optional)
limit = 100 # int | 列表返回的最大数量 (optional) (default to 100)
last_id = 'last_id_example' # str | 以上个列表的最后一条记录的 ID 作为下个列表的起点 (optional)

try:
    # 查询个人成交记录
    api_response = api_instance.get_my_trades(contract=contract, limit=limit, last_id=last_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_my_trades: %s\n" % e)
```


* Api Key Authentication (api_sign): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_sign
configuration = gate_client.Configuration()
configuration.api_key['SIGN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SIGN'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识，如果指定则只返回该合约相关数据 (optional)
limit = 100 # int | 列表返回的最大数量 (optional) (default to 100)
last_id = 'last_id_example' # str | 以上个列表的最后一条记录的 ID 作为下个列表的起点 (optional)

try:
    # 查询个人成交记录
    api_response = api_instance.get_my_trades(contract=contract, limit=limit, last_id=last_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_my_trades: %s\n" % e)
```


* Api Key Authentication (api_timestamp): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_timestamp
configuration = gate_client.Configuration()
configuration.api_key['Timestamp'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Timestamp'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识，如果指定则只返回该合约相关数据 (optional)
limit = 100 # int | 列表返回的最大数量 (optional) (default to 100)
last_id = 'last_id_example' # str | 以上个列表的最后一条记录的 ID 作为下个列表的起点 (optional)

try:
    # 查询个人成交记录
    api_response = api_instance.get_my_trades(contract=contract, limit=limit, last_id=last_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_my_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| 期货合约标识，如果指定则只返回该合约相关数据 | [optional] 
 **limit** | **int**| 列表返回的最大数量 | [optional] [default to 100]
 **last_id** | **str**| 以上个列表的最后一条记录的 ID 作为下个列表的起点 | [optional] 

### Return type

[**list[MyFuturesTrade]**](MyFuturesTrade.md)

### Authorization

[api_key](../README.md#api_key), [api_sign](../README.md#api_sign), [api_timestamp](../README.md#api_timestamp)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> FuturesOrder get_order(order_id)

查询单个订单详情

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.api_key['KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
order_id = 'order_id_example' # str | 成功创建订单时返回的 ID

try:
    # 查询单个订单详情
    api_response = api_instance.get_order(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_order: %s\n" % e)
```


* Api Key Authentication (api_sign): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_sign
configuration = gate_client.Configuration()
configuration.api_key['SIGN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SIGN'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
order_id = 'order_id_example' # str | 成功创建订单时返回的 ID

try:
    # 查询单个订单详情
    api_response = api_instance.get_order(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_order: %s\n" % e)
```


* Api Key Authentication (api_timestamp): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_timestamp
configuration = gate_client.Configuration()
configuration.api_key['Timestamp'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Timestamp'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
order_id = 'order_id_example' # str | 成功创建订单时返回的 ID

try:
    # 查询单个订单详情
    api_response = api_instance.get_order(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->get_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| 成功创建订单时返回的 ID | 

### Return type

[**FuturesOrder**](FuturesOrder.md)

### Authorization

[api_key](../README.md#api_key), [api_sign](../README.md#api_sign), [api_timestamp](../README.md#api_timestamp)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_accounts**
> FuturesAccount list_futures_accounts()

获取期货账号

期货交易目前只按照 BTC 结算，所以账号只会有一个，但是为了保持 API 格式一致， 同样使用列表返回 

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.api_key['KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))

try:
    # 获取期货账号
    api_response = api_instance.list_futures_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_accounts: %s\n" % e)
```


* Api Key Authentication (api_sign): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_sign
configuration = gate_client.Configuration()
configuration.api_key['SIGN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SIGN'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))

try:
    # 获取期货账号
    api_response = api_instance.list_futures_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_accounts: %s\n" % e)
```


* Api Key Authentication (api_timestamp): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_timestamp
configuration = gate_client.Configuration()
configuration.api_key['Timestamp'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Timestamp'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))

try:
    # 获取期货账号
    api_response = api_instance.list_futures_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FuturesAccount**](FuturesAccount.md)

### Authorization

[api_key](../README.md#api_key), [api_sign](../README.md#api_sign), [api_timestamp](../README.md#api_timestamp)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_candlesticks**
> FuturesCandlesticks list_futures_candlesticks(contract, _from=_from, to=to, limit=limit, interval=interval)

期货市场 K 线图

如果 `contract` 字段在合约标识前增加了 `mark_` 前缀则返回标记价格数据(如mark_BTC_USD)， 如果增加了 `index_` 则返回指数价格的数据(如index_BTC_USD)  K 线图数据单次请求最大返回 2000 个点，指定 from, to 和 interval 的时候注意点数不能过多。 

### Example
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gate_client.FuturesApi()
contract = 'contract_example' # str | 期货合约标识
_from = 3.4 # float | 指定 K 线图的起始时间，注意时间格式为秒(s)精度的 Unix 时间戳， 不指定则默认为 to - 100 * interval，即向前最多 100 个点的时间  (optional)
to = 3.4 # float | 指定 K 线图的结束时间，不指定则默认当前时间，注意时间格式为秒(s)精度的 Unix 时间戳  (optional)
limit = 100 # int | 指定数据点的数量，适用于取最近 `limit` 数量的数据，该字段与 `from`, `to` 互斥，如果指定了 `from`, `to` 中的任意字段，该字段会被拒绝  (optional) (default to 100)
interval = '5m' # str | 数据点的时间间隔 (optional) (default to '5m')

try:
    # 期货市场 K 线图
    api_response = api_instance.list_futures_candlesticks(contract, _from=_from, to=to, limit=limit, interval=interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_candlesticks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| 期货合约标识 | 
 **_from** | **float**| 指定 K 线图的起始时间，注意时间格式为秒(s)精度的 Unix 时间戳， 不指定则默认为 to - 100 * interval，即向前最多 100 个点的时间  | [optional] 
 **to** | **float**| 指定 K 线图的结束时间，不指定则默认当前时间，注意时间格式为秒(s)精度的 Unix 时间戳  | [optional] 
 **limit** | **int**| 指定数据点的数量，适用于取最近 &#x60;limit&#x60; 数量的数据，该字段与 &#x60;from&#x60;, &#x60;to&#x60; 互斥，如果指定了 &#x60;from&#x60;, &#x60;to&#x60; 中的任意字段，该字段会被拒绝  | [optional] [default to 100]
 **interval** | **str**| 数据点的时间间隔 | [optional] [default to &#39;5m&#39;]

### Return type

[**FuturesCandlesticks**](FuturesCandlesticks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_contracts**
> list[Contract] list_futures_contracts()

查询所有的期货信息

### Example
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gate_client.FuturesApi()

try:
    # 查询所有的期货信息
    api_response = api_instance.list_futures_contracts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_contracts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Contract]**](Contract.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_funding_rate_history**
> FundingRateHistory list_futures_funding_rate_history(contract, limit=limit)

期货市场历史资金费率

### Example
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gate_client.FuturesApi()
contract = 'contract_example' # str | 期货合约标识
limit = 100 # int | 列表返回的最大数量 (optional) (default to 100)

try:
    # 期货市场历史资金费率
    api_response = api_instance.list_futures_funding_rate_history(contract, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_funding_rate_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| 期货合约标识 | 
 **limit** | **int**| 列表返回的最大数量 | [optional] [default to 100]

### Return type

[**FundingRateHistory**](FundingRateHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_insurance_ledger**
> InsuranceRecord list_futures_insurance_ledger(limit=limit)

期货市场保险基金历史

### Example
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gate_client.FuturesApi()
limit = 100 # int | 列表返回的最大数量 (optional) (default to 100)

try:
    # 期货市场保险基金历史
    api_response = api_instance.list_futures_insurance_ledger(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_insurance_ledger: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 列表返回的最大数量 | [optional] [default to 100]

### Return type

[**InsuranceRecord**](InsuranceRecord.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_order_book**
> FuturesOrderBook list_futures_order_book(contract, interval=interval, limit=limit)

查询期货市场深度信息

买单会按照价格从高到低排序，卖单反之

### Example
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gate_client.FuturesApi()
contract = 'contract_example' # str | 期货合约标识
interval = '0' # str | 合并深度指定的价格精度，0 为不合并，不指定则默认为 0 (optional) (default to '0')
limit = 10 # int | 深度档位数量 (optional) (default to 10)

try:
    # 查询期货市场深度信息
    api_response = api_instance.list_futures_order_book(contract, interval=interval, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_order_book: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| 期货合约标识 | 
 **interval** | **str**| 合并深度指定的价格精度，0 为不合并，不指定则默认为 0 | [optional] [default to &#39;0&#39;]
 **limit** | **int**| 深度档位数量 | [optional] [default to 10]

### Return type

[**FuturesOrderBook**](FuturesOrderBook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_tickers**
> list[FuturesTicker] list_futures_tickers(contract=contract)

获取所有期货交易行情统计

### Example
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gate_client.FuturesApi()
contract = 'contract_example' # str | 期货合约标识，如果指定则只返回该合约相关数据 (optional)

try:
    # 获取所有期货交易行情统计
    api_response = api_instance.list_futures_tickers(contract=contract)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_tickers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| 期货合约标识，如果指定则只返回该合约相关数据 | [optional] 

### Return type

[**list[FuturesTicker]**](FuturesTicker.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_futures_trades**
> list[FuturesTrade] list_futures_trades(contract, limit=limit, last_id=last_id)

期货市场成交记录

### Example
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = gate_client.FuturesApi()
contract = 'contract_example' # str | 期货合约标识
limit = 100 # int | 列表返回的最大数量 (optional) (default to 100)
last_id = 'last_id_example' # str | 以上个列表的最后一条记录的 ID 作为下个列表的起点 (optional)

try:
    # 期货市场成交记录
    api_response = api_instance.list_futures_trades(contract, limit=limit, last_id=last_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_futures_trades: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| 期货合约标识 | 
 **limit** | **int**| 列表返回的最大数量 | [optional] [default to 100]
 **last_id** | **str**| 以上个列表的最后一条记录的 ID 作为下个列表的起点 | [optional] 

### Return type

[**list[FuturesTrade]**](FuturesTrade.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_orders**
> list[FuturesOrder] list_orders(contract, status, limit=limit, last_id=last_id)

查询订单列表

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.api_key['KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
status = 'status_example' # str | 基于状态查询订单列表
limit = 100 # int | 列表返回的最大数量 (optional) (default to 100)
last_id = 'last_id_example' # str | 以上个列表的最后一条记录的 ID 作为下个列表的起点 (optional)

try:
    # 查询订单列表
    api_response = api_instance.list_orders(contract, status, limit=limit, last_id=last_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_orders: %s\n" % e)
```


* Api Key Authentication (api_sign): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_sign
configuration = gate_client.Configuration()
configuration.api_key['SIGN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SIGN'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
status = 'status_example' # str | 基于状态查询订单列表
limit = 100 # int | 列表返回的最大数量 (optional) (default to 100)
last_id = 'last_id_example' # str | 以上个列表的最后一条记录的 ID 作为下个列表的起点 (optional)

try:
    # 查询订单列表
    api_response = api_instance.list_orders(contract, status, limit=limit, last_id=last_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_orders: %s\n" % e)
```


* Api Key Authentication (api_timestamp): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_timestamp
configuration = gate_client.Configuration()
configuration.api_key['Timestamp'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Timestamp'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
status = 'status_example' # str | 基于状态查询订单列表
limit = 100 # int | 列表返回的最大数量 (optional) (default to 100)
last_id = 'last_id_example' # str | 以上个列表的最后一条记录的 ID 作为下个列表的起点 (optional)

try:
    # 查询订单列表
    api_response = api_instance.list_orders(contract, status, limit=limit, last_id=last_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| 期货合约标识 | 
 **status** | **str**| 基于状态查询订单列表 | 
 **limit** | **int**| 列表返回的最大数量 | [optional] [default to 100]
 **last_id** | **str**| 以上个列表的最后一条记录的 ID 作为下个列表的起点 | [optional] 

### Return type

[**list[FuturesOrder]**](FuturesOrder.md)

### Authorization

[api_key](../README.md#api_key), [api_sign](../README.md#api_sign), [api_timestamp](../README.md#api_timestamp)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_positions**
> list[Position] list_positions()

获取用户头寸列表

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.api_key['KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))

try:
    # 获取用户头寸列表
    api_response = api_instance.list_positions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_positions: %s\n" % e)
```


* Api Key Authentication (api_sign): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_sign
configuration = gate_client.Configuration()
configuration.api_key['SIGN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SIGN'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))

try:
    # 获取用户头寸列表
    api_response = api_instance.list_positions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_positions: %s\n" % e)
```


* Api Key Authentication (api_timestamp): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_timestamp
configuration = gate_client.Configuration()
configuration.api_key['Timestamp'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Timestamp'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))

try:
    # 获取用户头寸列表
    api_response = api_instance.list_positions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->list_positions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Position]**](Position.md)

### Authorization

[api_key](../README.md#api_key), [api_sign](../README.md#api_sign), [api_timestamp](../README.md#api_timestamp)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_leverage**
> Position update_position_leverage(contract, leverage)

更新头寸杠杆

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.api_key['KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
leverage = 'leverage_example' # str | 新的杠杆倍数

try:
    # 更新头寸杠杆
    api_response = api_instance.update_position_leverage(contract, leverage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_leverage: %s\n" % e)
```


* Api Key Authentication (api_sign): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_sign
configuration = gate_client.Configuration()
configuration.api_key['SIGN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SIGN'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
leverage = 'leverage_example' # str | 新的杠杆倍数

try:
    # 更新头寸杠杆
    api_response = api_instance.update_position_leverage(contract, leverage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_leverage: %s\n" % e)
```


* Api Key Authentication (api_timestamp): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_timestamp
configuration = gate_client.Configuration()
configuration.api_key['Timestamp'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Timestamp'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
leverage = 'leverage_example' # str | 新的杠杆倍数

try:
    # 更新头寸杠杆
    api_response = api_instance.update_position_leverage(contract, leverage)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_leverage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| 期货合约标识 | 
 **leverage** | **str**| 新的杠杆倍数 | 

### Return type

[**Position**](Position.md)

### Authorization

[api_key](../README.md#api_key), [api_sign](../README.md#api_sign), [api_timestamp](../README.md#api_timestamp)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_margin**
> Position update_position_margin(contract, change)

更新头寸保证金

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.api_key['KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
change = 'change_example' # str | 保证金变化数额，正数增加，负数减少

try:
    # 更新头寸保证金
    api_response = api_instance.update_position_margin(contract, change)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_margin: %s\n" % e)
```


* Api Key Authentication (api_sign): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_sign
configuration = gate_client.Configuration()
configuration.api_key['SIGN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SIGN'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
change = 'change_example' # str | 保证金变化数额，正数增加，负数减少

try:
    # 更新头寸保证金
    api_response = api_instance.update_position_margin(contract, change)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_margin: %s\n" % e)
```


* Api Key Authentication (api_timestamp): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_timestamp
configuration = gate_client.Configuration()
configuration.api_key['Timestamp'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Timestamp'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
change = 'change_example' # str | 保证金变化数额，正数增加，负数减少

try:
    # 更新头寸保证金
    api_response = api_instance.update_position_margin(contract, change)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_margin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| 期货合约标识 | 
 **change** | **str**| 保证金变化数额，正数增加，负数减少 | 

### Return type

[**Position**](Position.md)

### Authorization

[api_key](../README.md#api_key), [api_sign](../README.md#api_sign), [api_timestamp](../README.md#api_timestamp)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_position_risk_limit**
> Position update_position_risk_limit(contract, risk_limit)

更新头寸风险限额

### Example

* Api Key Authentication (api_key): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = gate_client.Configuration()
configuration.api_key['KEY'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['KEY'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
risk_limit = 'risk_limit_example' # str | 新的风险限额

try:
    # 更新头寸风险限额
    api_response = api_instance.update_position_risk_limit(contract, risk_limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_risk_limit: %s\n" % e)
```


* Api Key Authentication (api_sign): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_sign
configuration = gate_client.Configuration()
configuration.api_key['SIGN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['SIGN'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
risk_limit = 'risk_limit_example' # str | 新的风险限额

try:
    # 更新头寸风险限额
    api_response = api_instance.update_position_risk_limit(contract, risk_limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_risk_limit: %s\n" % e)
```


* Api Key Authentication (api_timestamp): 
```python
from __future__ import print_function
import time
import gate_client
from gate_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_timestamp
configuration = gate_client.Configuration()
configuration.api_key['Timestamp'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Timestamp'] = 'Bearer'

# create an instance of the API class
api_instance = gate_client.FuturesApi(gate_client.ApiClient(configuration))
contract = 'contract_example' # str | 期货合约标识
risk_limit = 'risk_limit_example' # str | 新的风险限额

try:
    # 更新头寸风险限额
    api_response = api_instance.update_position_risk_limit(contract, risk_limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FuturesApi->update_position_risk_limit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract** | **str**| 期货合约标识 | 
 **risk_limit** | **str**| 新的风险限额 | 

### Return type

[**Position**](Position.md)

### Authorization

[api_key](../README.md#api_key), [api_sign](../README.md#api_sign), [api_timestamp](../README.md#api_timestamp)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

