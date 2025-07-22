# MultiRepayRecord

Mult Repay Record.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Order ID. | [optional] 
**record_id** | **int** | Repayment record ID. | [optional] 
**init_ltv** | **str** | The initial collateralization rate. | [optional] 
**before_ltv** | **str** | Ltv before the operation. | [optional] 
**after_ltv** | **str** | Ltv after the operation. | [optional] 
**borrow_time** | **int** | Borrowing time, timestamp in seconds. | [optional] 
**repay_time** | **int** | Repayment time, timestamp in seconds. | [optional] 
**borrow_currencies** | [**list[RepayRecordCurrency]**](RepayRecordCurrency.md) | List of borrowing information. | [optional] 
**collateral_currencies** | [**list[RepayRecordCurrency]**](RepayRecordCurrency.md) | List of collateral information. | [optional] 
**repaid_currencies** | [**list[RepayRecordRepaidCurrency]**](RepayRecordRepaidCurrency.md) | Repay Currency List. | [optional] 
**total_interest_list** | [**list[RepayRecordTotalInterest]**](RepayRecordTotalInterest.md) | Total Interest List. | [optional] 
**left_repay_interest_list** | [**list[RepayRecordLeftInterest]**](RepayRecordLeftInterest.md) | List of left repay interest. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


