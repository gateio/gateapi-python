# FuturesAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** | total is the balance after the user&#39;s accumulated deposit, withdraw, profit and loss (including realized profit and loss, fund, fee and referral rebate), excluding unrealized profit and loss.  total &#x3D; SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund) | [optional] 
**unrealised_pnl** | **str** | Unrealized PNL. | [optional] 
**position_margin** | **str** | Position margin. | [optional] 
**order_margin** | **str** | Order margin of unfinished orders. | [optional] 
**available** | **str** | The available balance for transferring or trading(including bonus. Bonus can&#39;t be withdrawn. The transfer amount needs to deduct the bonus) | [optional] 
**point** | **str** | POINT amount. | [optional] 
**currency** | **str** | Settle currency. | [optional] 
**in_dual_mode** | **bool** | Whether dual mode is enabled. | [optional] 
**enable_credit** | **bool** | Whether portfolio margin account mode is enabled. | [optional] 
**position_initial_margin** | **str** | Initial margin position, applicable to the portfolio margin account model. | [optional] 
**maintenance_margin** | **str** | The maintenance deposit occupied by the position is suitable for the new classic account margin model and unified account model | [optional] 
**bonus** | **str** | Perpetual Contract Bonus. | [optional] 
**enable_evolved_classic** | **bool** | Classic account margin mode, true-new mode, false-old mode. | [optional] 
**cross_order_margin** | **str** | Full -warehouse hanging order deposit, suitable for the new classic account margin model | [optional] 
**cross_initial_margin** | **str** | The initial security deposit of the full warehouse is suitable for the new classic account margin model | [optional] 
**cross_maintenance_margin** | **str** | Maintain deposit in full warehouse, suitable for new classic account margin models | [optional] 
**cross_unrealised_pnl** | **str** | The full warehouse does not achieve profit and loss, suitable for the new classic account margin model | [optional] 
**cross_available** | **str** | Full warehouse available amount, suitable for the new classic account margin model | [optional] 
**cross_margin_balance** | **str** | Full margin balance, suitable for the new classic account margin model. | [optional] 
**cross_mmr** | **str** | Maintain margin ratio for the full position, suitable for the new classic account margin model | [optional] 
**cross_imr** | **str** | The initial margin rate of the full position is suitable for the new classic account margin model | [optional] 
**isolated_position_margin** | **str** | Ware -position margin, suitable for the new classic account margin model. | [optional] 
**enable_new_dual_mode** | **bool** | Whether to open a new two-way position mode. | [optional] 
**margin_mode** | **int** | Margin mode, 0-classic margin mode, 1-cross-currency margin mode, 2-combined margin mode | [optional] 
**enable_tiered_mm** | **bool** | Whether to enable tiered maintenance margin calculation. | [optional] 
**history** | [**FuturesAccountHistory**](FuturesAccountHistory.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


