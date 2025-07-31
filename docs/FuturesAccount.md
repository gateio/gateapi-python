# FuturesAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** | total is the balance after the user&#39;s accumulated deposit, withdraw, profit and loss (including realized profit and loss, fund, fee and referral rebate), excluding unrealized profit and loss.  total &#x3D; SUM(history_dnw, history_pnl, history_fee, history_refr, history_fund) | [optional] 
**unrealised_pnl** | **str** | Unrealized PNL | [optional] 
**position_margin** | **str** | Position margin | [optional] 
**order_margin** | **str** | Order margin of unfinished orders | [optional] 
**available** | **str** | Available balance for transferring or trading (including bonus. Bonus cannot be withdrawn, so transfer amount needs to deduct bonus) | [optional] 
**point** | **str** | Point card amount | [optional] 
**currency** | **str** | Settlement currency | [optional] 
**in_dual_mode** | **bool** | Whether dual mode is enabled | [optional] 
**enable_credit** | **bool** | Whether portfolio margin account mode is enabled | [optional] 
**position_initial_margin** | **str** | Initial margin occupied by positions, applicable to unified account mode | [optional] 
**maintenance_margin** | **str** | Maintenance margin occupied by positions, applicable to new classic account margin mode and unified account mode | [optional] 
**bonus** | **str** | Bonus | [optional] 
**enable_evolved_classic** | **bool** | Classic account margin mode, true-new mode, false-old mode | [optional] 
**cross_order_margin** | **str** | Cross margin order margin, applicable to new classic account margin mode | [optional] 
**cross_initial_margin** | **str** | Cross margin initial margin, applicable to new classic account margin mode | [optional] 
**cross_maintenance_margin** | **str** | Cross margin maintenance margin, applicable to new classic account margin mode | [optional] 
**cross_unrealised_pnl** | **str** | Cross margin unrealized P&amp;L, applicable to new classic account margin mode | [optional] 
**cross_available** | **str** | Cross margin available balance, applicable to new classic account margin mode | [optional] 
**cross_margin_balance** | **str** | Cross margin balance, applicable to new classic account margin mode | [optional] 
**cross_mmr** | **str** | Cross margin maintenance margin rate, applicable to new classic account margin mode | [optional] 
**cross_imr** | **str** | Cross margin initial margin rate, applicable to new classic account margin mode | [optional] 
**isolated_position_margin** | **str** | Isolated position margin, applicable to new classic account margin mode | [optional] 
**enable_new_dual_mode** | **bool** | Whether to open a new two-way position mode | [optional] 
**margin_mode** | **int** | Margin mode, 0-classic margin mode, 1-cross-currency margin mode, 2-combined margin mode | [optional] 
**enable_tiered_mm** | **bool** | Whether to enable tiered maintenance margin calculation | [optional] 
**history** | [**FuturesAccountHistory**](FuturesAccountHistory.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


