# Position

Futures position details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** | User ID | [optional] [readonly] 
**contract** | **str** | Futures contract | [optional] [readonly] 
**size** | **int** | Position size | [optional] [readonly] 
**leverage** | **str** | Position leverage. 0 means cross margin; positive number means isolated margin | [optional] 
**risk_limit** | **str** | Position risk limit | [optional] 
**leverage_max** | **str** | Maximum leverage under current risk limit | [optional] [readonly] 
**maintenance_rate** | **str** | Maintenance rate under current risk limit | [optional] [readonly] 
**value** | **str** | Position value calculated in settlement currency | [optional] [readonly] 
**margin** | **str** | Position margin | [optional] 
**entry_price** | **str** | Entry price | [optional] [readonly] 
**liq_price** | **str** | Liquidation price | [optional] [readonly] 
**mark_price** | **str** | Current mark price | [optional] [readonly] 
**initial_margin** | **str** | The initial margin occupied by the position, applicable to the portfolio margin account | [optional] [readonly] 
**maintenance_margin** | **str** | Maintenance margin required for the position, applicable to portfolio margin account | [optional] [readonly] 
**unrealised_pnl** | **str** | Unrealized PNL | [optional] [readonly] 
**realised_pnl** | **str** | Realized PNL | [optional] [readonly] 
**history_pnl** | **str** | History realized PNL | [optional] [readonly] 
**last_close_pnl** | **str** | PNL of last position close | [optional] [readonly] 
**realised_point** | **str** | Realized POINT PNL | [optional] [readonly] 
**history_point** | **str** | History realized POINT PNL | [optional] [readonly] 
**adl_ranking** | **int** | Ranking of auto deleveraging, a total of 1-5 grades, &#x60;1&#x60; is the highest, &#x60;5&#x60; is the lowest, and &#x60;6&#x60; is the special case when there is no position held or in liquidation | [optional] [readonly] 
**pending_orders** | **int** | Current open orders | [optional] [readonly] 
**close_order** | [**PositionCloseOrder**](PositionCloseOrder.md) |  | [optional] 
**mode** | **str** | Position mode, including:  - &#x60;single&#x60;: dual mode is not enabled- &#x60;dual_long&#x60;: long position in dual mode- &#x60;dual_short&#x60;: short position in dual mode | [optional] 
**cross_leverage_limit** | **str** | Cross margin leverage(valid only when &#x60;leverage&#x60; is 0) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


