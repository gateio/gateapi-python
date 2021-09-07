# LoanRecord

Margin loaned record details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Loan record ID | [optional] 
**loan_id** | **str** | Loan ID the record belongs to | [optional] 
**create_time** | **str** | Loan time | [optional] 
**expire_time** | **str** | Expiration time | [optional] 
**status** | **str** | Loan record status | [optional] 
**borrow_user_id** | **str** | Garbled user ID | [optional] 
**currency** | **str** | Loan currency | [optional] 
**rate** | **str** | Loan rate | [optional] 
**amount** | **str** | Loan amount | [optional] 
**days** | **int** | Loan days | [optional] 
**auto_renew** | **bool** | Whether the record will auto renew on expiration | [optional] [default to False]
**repaid** | **str** | Repaid amount | [optional] 
**paid_interest** | **str** | Repaid interest | [optional] [readonly] 
**unpaid_interest** | **str** | Outstanding interest yet to be paid | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


