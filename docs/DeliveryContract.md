# DeliveryContract

Futures contract details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Futures contract | [optional] 
**underlying** | **str** | Underlying | [optional] 
**cycle** | **str** | Cycle type, e.g. WEEKLY, QUARTERLY | [optional] 
**type** | **str** | Contract type: inverse - inverse contract, direct - direct contract | [optional] 
**quanto_multiplier** | **str** | Multiplier used in converting from invoicing to settlement currency | [optional] 
**leverage_min** | **str** | Minimum leverage | [optional] 
**leverage_max** | **str** | Maximum leverage | [optional] 
**maintenance_rate** | **str** | Maintenance rate of margin | [optional] 
**mark_type** | **str** | Mark price type: internal - internal trading price, index - external index price | [optional] 
**mark_price** | **str** | Current mark price | [optional] 
**index_price** | **str** | Current index price | [optional] 
**last_price** | **str** | Last trading price | [optional] 
**maker_fee_rate** | **str** | Maker fee rate, negative values indicate rebates | [optional] 
**taker_fee_rate** | **str** | Taker fee rate | [optional] 
**order_price_round** | **str** | Minimum order price increment | [optional] 
**mark_price_round** | **str** | Minimum mark price increment | [optional] 
**basis_rate** | **str** | Fair basis rate | [optional] 
**basis_value** | **str** | Fair basis value | [optional] 
**basis_impact_value** | **str** | Funding used for calculating impact bid, ask price | [optional] 
**settle_price** | **str** | Settle price | [optional] 
**settle_price_interval** | **int** | Settle price update interval | [optional] 
**settle_price_duration** | **int** | Settle price update duration in seconds | [optional] 
**expire_time** | **int** | Contract expiry timestamp | [optional] 
**risk_limit_base** | **str** | Risk limit base | [optional] 
**risk_limit_step** | **str** | Step of adjusting risk limit | [optional] 
**risk_limit_max** | **str** | Maximum risk limit the contract allowed | [optional] 
**order_size_min** | **int** | Minimum order size allowed by the contract | [optional] 
**order_size_max** | **int** | Maximum order size allowed by the contract | [optional] 
**order_price_deviate** | **str** | Maximum allowed deviation between order price and current mark price. The order price &#x60;order_price&#x60; must satisfy the following condition:      abs(order_price - mark_price) &lt;&#x3D; mark_price * order_price_deviate | [optional] 
**ref_discount_rate** | **str** | Trading fee discount for referred users | [optional] 
**ref_rebate_rate** | **str** | Commission rate for referrers | [optional] 
**orderbook_id** | **int** | Orderbook update ID | [optional] 
**trade_id** | **int** | Current trade ID | [optional] 
**trade_size** | **int** | Historical cumulative trading volume | [optional] 
**position_size** | **int** | Current total long position size | [optional] 
**config_change_time** | **float** | Last configuration update time | [optional] 
**in_delisting** | **bool** | Contract is delisting | [optional] 
**orders_limit** | **int** | Maximum number of pending orders | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


