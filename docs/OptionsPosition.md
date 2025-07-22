# OptionsPosition

Options position information.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** | User ID. | [optional] [readonly] 
**underlying** | **str** | Underlying. | [optional] [readonly] 
**underlying_price** | **str** | Underlying price (quote currency). | [optional] [readonly] 
**contract** | **str** | Options contract name. | [optional] [readonly] 
**size** | **int** | Position size (contract size). | [optional] [readonly] 
**entry_price** | **str** | Entry size (quote currency). | [optional] [readonly] 
**mark_price** | **str** | Current mark price (quote currency). | [optional] [readonly] 
**mark_iv** | **str** | Implied volatility. | [optional] [readonly] 
**realised_pnl** | **str** | Realized PNL. | [optional] [readonly] 
**unrealised_pnl** | **str** | Unrealized PNL. | [optional] [readonly] 
**pending_orders** | **int** | Current open orders. | [optional] [readonly] 
**close_order** | [**OptionsPositionCloseOrder**](OptionsPositionCloseOrder.md) |  | [optional] 
**delta** | **str** | Delta. | [optional] [readonly] 
**gamma** | **str** | Gamma. | [optional] [readonly] 
**vega** | **str** | Vega. | [optional] [readonly] 
**theta** | **str** | Theta. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


