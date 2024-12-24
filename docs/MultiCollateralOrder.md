# MultiCollateralOrder

Multi-Collateral Order
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID | [optional] 
**order_type** | **str** | current - current, fixed - fixed | [optional] 
**fixed_type** | **str** | Fixed interest rate loan periods: 7d - 7 days, 30d - 30 days. | [optional] 
**fixed_rate** | **str** | Fixed interest rate | [optional] 
**expire_time** | **int** | Expiration time, timestamp, unit in seconds. | [optional] 
**auto_renew** | **bool** | Fixed interest rate, automatic renewal | [optional] 
**auto_repay** | **bool** | Fixed interest rate, automatic repayment | [optional] 
**current_ltv** | **str** | The current collateralization rate | [optional] 
**status** | **str** | Order status: - initial: Initial state after placing the order - collateral_deducted: Collateral deduction successful - collateral_returning: Loan failed - Collateral return pending - lent: Loan successful - repaying: Repayment in progress - liquidating: Liquidation in progress - finished: Order completed - closed_liquidated: Liquidation and repayment completed | [optional] 
**borrow_time** | **int** | Borrowing time, timestamp in seconds | [optional] 
**total_left_repay_usdt** | **str** | Value of Left repay amount converted in USDT | [optional] 
**total_left_collateral_usdt** | **str** | Value of Collateral amount in USDT | [optional] 
**borrow_currencies** | [**list[BorrowCurrencyInfo]**](BorrowCurrencyInfo.md) | Borrowing Currency List | [optional] 
**collateral_currencies** | [**list[CollateralCurrencyInfo]**](CollateralCurrencyInfo.md) | Collateral Currency List | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


