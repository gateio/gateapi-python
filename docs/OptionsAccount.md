# OptionsAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **int** | User ID | [optional] 
**total** | **str** | 账户余额 | [optional] 
**position_value** | **str** | 仓位价值，做多仓位价值为正，做空仓位价值为负 | [optional] 
**equity** | **str** | 账户权益，账户余额与仓位价值的和 | [optional] 
**short_enabled** | **bool** | If the account is allowed to short | [optional] 
**mmp_enabled** | **bool** | 是否启用MMP | [optional] 
**liq_triggered** | **bool** | 是否触发仓位强平 | [optional] 
**margin_mode** | **int** | ｜ 保证金模式： - 0：经典现货保证金模式 - 1：跨币种保证金模式 - 2：组合保证金模式 | [optional] 
**unrealised_pnl** | **str** | Unrealized PNL | [optional] 
**init_margin** | **str** | Initial position margin | [optional] 
**maint_margin** | **str** | Position maintenance margin | [optional] 
**order_margin** | **str** | Order margin of unfinished orders | [optional] 
**ask_order_margin** | **str** | 未完成卖单的保证金 | [optional] 
**bid_order_margin** | **str** | 未完成买单的保证金 | [optional] 
**available** | **str** | Available balance to transfer out or trade | [optional] 
**point** | **str** | POINT amount | [optional] 
**currency** | **str** | Settle currency | [optional] 
**orders_limit** | **int** | 未完成订单数量上限 | [optional] 
**position_notional_limit** | **int** | 名义价值上限，包含仓位以及未完成订单的名义价值 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


