# CollateralOrder

抵押借币订单
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | 订单id | [optional] 
**collateral_currency** | **str** | 质押币种 | [optional] 
**collateral_amount** | **str** | 质押数量 | [optional] 
**borrow_currency** | **str** | 借款币种 | [optional] 
**borrow_amount** | **str** | 借款数量 | [optional] 
**repaid_amount** | **str** | 已还款数量 | [optional] 
**repaid_principal** | **str** | 已还本金 | [optional] 
**repaid_interest** | **str** | 已还利息 | [optional] 
**init_ltv** | **str** | 初始质押率 | [optional] 
**current_ltv** | **str** | 当前质押率 | [optional] 
**liquidate_ltv** | **str** | 平仓质押率 | [optional] 
**status** | **str** | 订单状态: - initial: 下单初始状态 - collateral_deducted: 扣除质押物成功 - collateral_returning: 放款失败-待退回质押物 - lent: 放款成功 - repaying: 还款中 - liquidating: 平仓中 - finished: 已完成 - closed_liquidated: 已结束-平仓还款结束 | [optional] 
**borrow_time** | **int** | 借款时间，时间戳，单位秒 | [optional] 
**left_repay_total** | **str** | 待还本息（待还本金+待还利息） | [optional] 
**left_repay_principal** | **str** | 待还本金 | [optional] 
**left_repay_interest** | **str** | 待还利息 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


