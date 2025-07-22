# UnifiedLoanRecord

Loan records.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID. | [optional] [readonly] 
**type** | **str** | type: borrow - borrow, repay - repay. | [optional] [readonly] 
**repayment_type** | **str** | Repayment type, none - No repayment type, manual_repay - Manual repayment, auto_repay - Automatic repayment after withdrawal, different_currencies_repayment - Different currency repayment | [optional] [readonly] 
**borrow_type** | **str** | Loan type, returned when querying loan records. manual_borrow - Manual repayment , auto_borrow - Automatic repayment | [optional] 
**currency_pair** | **str** | Currency pair. | [optional] [readonly] 
**currency** | **str** | Currency. | [optional] [readonly] 
**amount** | **str** | The amount of lending or repaying. | [optional] [readonly] 
**create_time** | **int** | Created time. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


