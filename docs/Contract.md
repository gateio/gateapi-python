# Contract

Futures contract details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Futures contract | [optional] 
**type** | **str** | Futures contract type | [optional] 
**quanto_multiplier** | **str** | Multiplier used in converting from invoicing to settlement currency | [optional] 
**leverage_min** | **str** | Minimum leverage | [optional] 
**leverage_max** | **str** | Maximum leverage | [optional] 
**maintenance_rate** | **str** | Maintenance rate of margin | [optional] 
**mark_type** | **str** | Mark price type, internal - based on internal trading, index - based on external index price | [optional] 
**mark_price** | **str** | Current mark price | [optional] 
**index_price** | **str** | Current index price | [optional] 
**last_price** | **str** | Last trading price | [optional] 
**maker_fee_rate** | **str** | Maker fee rate, where negative means rebate | [optional] 
**taker_fee_rate** | **str** | Taker fee rate | [optional] 
**order_price_round** | **str** | Minimum order price increment | [optional] 
**mark_price_round** | **str** | Minimum mark price increment | [optional] 
**funding_rate** | **str** | Current funding rate | [optional] 
**funding_interval** | **int** | Funding application interval, unit in seconds | [optional] 
**funding_next_apply** | **float** | Next funding time | [optional] 
**risk_limit_base** | **str** | Risk limit base | [optional] 
**risk_limit_step** | **str** | Step of adjusting risk limit | [optional] 
**risk_limit_max** | **str** | Maximum risk limit the contract allowed | [optional] 
**order_size_min** | **int** | Minimum order size the contract allowed | [optional] 
**order_size_max** | **int** | Maximum order size the contract allowed | [optional] 
**order_price_deviate** | **str** | deviation between order price and current index price. If price of an order is denoted as order_price, it must meet the following condition:      abs(order_price - mark_price) &lt;&#x3D; mark_price * order_price_deviate | [optional] 
**ref_discount_rate** | **str** | Referral fee rate discount | [optional] 
**ref_rebate_rate** | **str** | Referrer commission rate | [optional] 
**orderbook_id** | **int** | Current orderbook ID | [optional] 
**trade_id** | **int** | Current trade ID | [optional] 
**trade_size** | **int** | Historical accumulated trade size | [optional] 
**position_size** | **int** | Current total long position size | [optional] 
**config_change_time** | **float** | Last changed time of configuration | [optional] 
**in_delisting** | **bool** | Contract is delisting | [optional] 
**orders_limit** | **int** | Maximum number of open orders | [optional] 
**enable_bonus** | **bool** | Whether bouns is enabled | [optional] 
**enable_credit** | **bool** | Whether portfolio margin account is enabled | [optional] 
**create_time** | **float** | Created time of the contract | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


