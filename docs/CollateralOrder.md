# CollateralOrder

Collateral Order
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Order ID | [optional] 
**collateral_currency** | **str** | Collateral | [optional] 
**collateral_amount** | **str** | Collateral amount | [optional] 
**borrow_currency** | **str** | Borrowed currency | [optional] 
**borrow_amount** | **str** | Borrowing amount | [optional] 
**repaid_amount** | **str** | Repaid amount | [optional] 
**repaid_principal** | **str** | Repaid principal | [optional] 
**repaid_interest** | **str** | Repaid interest | [optional] 
**init_ltv** | **str** | The initial collateralization rate | [optional] 
**current_ltv** | **str** | The current collateralization rate | [optional] 
**liquidate_ltv** | **str** | The liquidation collateralization rate | [optional] 
**status** | **str** | Order status: - initial: Initial state after placing the order - collateral_deducted: Collateral deduction successful - collateral_returning: Loan failed - Collateral return pending - lent: Loan successful - repaying: Repayment in progress - liquidating: Liquidation in progress - finished: Order completed - closed_liquidated: Liquidation and repayment completed | [optional] 
**borrow_time** | **int** | Borrowing time, timestamp in seconds | [optional] 
**left_repay_total** | **str** | Outstanding principal and interest (outstanding principal + outstanding interest) | [optional] 
**left_repay_principal** | **str** | outstanding principal | [optional] 
**left_repay_interest** | **str** | outstanding interest | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


