# Loan

Margin loan details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Loan ID | [optional] [readonly] 
**create_time** | **str** | Creation time | [optional] [readonly] 
**expire_time** | **str** | Repay time of the loan. No value will be returned for lending loan | [optional] [readonly] 
**status** | **str** | Loan status  open - not fully loaned loaned - all loaned out for lending loan; loaned in for borrowing side finished - loan is finished, either being all repaid or cancelled by the lender auto_repaid - automatically repaid by the system | [optional] [readonly] 
**side** | **str** | Loan side | 
**currency** | **str** | Loan currency | 
**rate** | **str** | Loan rate. Only rates in [0.0001, 0.01] are supported.  Not required in lending. Market rate calculated from recent rates will be used if not set | [optional] 
**amount** | **str** | Loan amount | 
**days** | **int** | Loan days. Only 10 is supported for now | [optional] 
**auto_renew** | **bool** | Whether to auto renew the loan upon expiration | [optional] [default to False]
**currency_pair** | **str** | Currency pair. Required if borrowing | [optional] 
**left** | **str** | Amount not lent out yet | [optional] [readonly] 
**repaid** | **str** | Repaid amount | [optional] [readonly] 
**paid_interest** | **str** | Repaid interest | [optional] [readonly] 
**unpaid_interest** | **str** | Outstanding interest yet to be paid | [optional] [readonly] 
**fee_rate** | **str** | Loan fee rate | [optional] 
**orig_id** | **str** | Original loan ID of the loan if auto-renewed, otherwise equals to id | [optional] 
**text** | **str** | User defined custom ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


