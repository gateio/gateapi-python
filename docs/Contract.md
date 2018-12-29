# Contract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Futures name | [optional] 
**type** | **str** | Futures type | [optional] 
**quanto_multiplier** | **str** | Multiplier used in converting from invoicing to settlement currency in quanto futures | [optional] 
**leverage_min** | **str** | minimum leverage | [optional] 
**leverage_max** | **str** | maximum leverage | [optional] 
**mark_type** | **str** | mark price type, internal - based on internal trading, index - based on external index price | [optional] 
**mark_price** | **str** | latest mark price | [optional] 
**index_price** | **str** | latest index price | [optional] 
**maintenance_rate** | **str** | maintenance rate of margin | [optional] 
**funding_rate** | **str** | funding rate | [optional] 
**funding_interval** | **int** | funding application interval, unit in seconds | [optional] 
**funding_next_apply** | **float** | next funding time | [optional] 
**risk_limit_base** | **str** | risk limit base | [optional] 
**risk_limit_step** | **str** | step of adjusting risk limit | [optional] 
**risk_limit_max** | **str** | maximum risk limit the contract allowed | [optional] 
**order_size_min** | **int** | minimum order size the contract allowed | [optional] 
**order_size_max** | **int** | maximum order size the contract allowed | [optional] 
**order_price_deviate** | **str** | deviation between order price and current index price. If price of an order is denoted as &#x60;order_price&#x60;, it must meet the following condition:      abs(order_price - mark_price) &lt;&#x3D; mark_price * order_price_deviate  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


