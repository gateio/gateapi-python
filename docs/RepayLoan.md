# RepayLoan

Repay
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Order ID | 
**repay_amount** | **str** | Repayment amount, it is mandatory when making partial repayments | 
**repaid_all** | **bool** | Repayment method, set to &#x60;true&#x60; for full repayment, and &#x60;false&#x60; for partial repayment; When set to false for partial repayment, the repay_amount parameter cannot be greater than the remaining amount to be repaid by the user.  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


