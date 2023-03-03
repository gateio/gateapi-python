# FuturesAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** | total is the balance after the user&#39;s accumulated deposit, withdraw, profit and loss (including realized profit and loss, fund, fee and referral rebate), excluding unrealized profit and loss.  total &#x3D; SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund) | [optional] 
**unrealised_pnl** | **str** | Unrealized PNL | [optional] 
**position_margin** | **str** | Position margin | [optional] 
**order_margin** | **str** | Order margin of unfinished orders | [optional] 
**available** | **str** | The available balance for transferring or trading(including bonus.  Bonus can&#39;t be be withdrawn. The transfer amount needs to deduct the bonus) | [optional] 
**point** | **str** | POINT amount | [optional] 
**currency** | **str** | Settle currency | [optional] 
**in_dual_mode** | **bool** | Whether dual mode is enabled | [optional] 
**enable_credit** | **bool** | Whether portfolio margin account mode is enabled | [optional] 
**position_initial_margin** | **str** | Initial margin position, applicable to the portfolio margin account model | [optional] 
**maintenance_margin** | **str** | Maintenance margin position, applicable to the portfolio margin account model | [optional] 
**bonus** | **str** | Perpetual Contract Bonus | [optional] 
**history** | [**FuturesAccountHistory**](FuturesAccountHistory.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


