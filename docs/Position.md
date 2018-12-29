# Position

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | futures contract name | [optional] 
**size** | **int** | position size | [optional] 
**leverage** | **str** | position leverage | [optional] 
**leverage_max** | **str** | maximum leverage of position | [optional] 
**value** | **str** | position value calculated in settlement currency | [optional] 
**margin** | **str** | position margin | [optional] 
**entry_price** | **str** | entry price | [optional] 
**liq_price** | **str** | liquidation price | [optional] 
**unrealised_pnl** | **str** | unrealised pnl | [optional] 
**realised_pnl** | **str** | realised pnl | [optional] 
**history_pnl** | **str** | history realised pnl | [optional] 
**locked** | **bool** | is position locked. e.g. position will be locked if failed to liquidate | [optional] 
**risk_limit** | **str** | position risk limit | [optional] 
**adl_ranking** | **int** | AutoDeleverage ranking, from 1 to 5. Ranking larger than 5 is not considered | [optional] 
**close_price** | **str** | close price of position in closing. 0 if position is not in closing | [optional] 
**close_order_id** | **str** | close order id if position in closing | [optional] 
**last_close_pnl** | **str** | last closed pnl | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


