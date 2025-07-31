# UnifiedLoanRecord

Borrowing Records
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] [readonly] 
**type** | **str** | Type: &#x60;borrow&#x60; - borrow, &#x60;repay&#x60; - repay | [optional] [readonly] 
**repayment_type** | **str** | Repayment type: none - No repayment type, manual_repay - Manual repayment, auto_repay - Automatic repayment, cancel_auto_repay - Automatic repayment after order cancellation, different_currencies_repayment - Cross-currency repayment | [optional] [readonly] 
**borrow_type** | **str** | Borrowing type, returned when querying loan records: manual_borrow - Manual borrowing, auto_borrow - Automatic borrowing | [optional] 
**currency_pair** | **str** | Currency pair | [optional] [readonly] 
**currency** | **str** | Currency | [optional] [readonly] 
**amount** | **str** | Borrow or repayment amount | [optional] [readonly] 
**create_time** | **int** | Created time | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


