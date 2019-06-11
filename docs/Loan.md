# Loan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Loan ID | [optional] 
**create_time** | **str** | Creation time | [optional] 
**expire_time** | **str** | Repay time of the loan. No value will be returned for lending loan | [optional] 
**status** | **str** | Loan status  open - not fully loaned loaned - all loaned out for lending loan; loaned in for borrowing side finished - loan is finished, either being all repaid or cancelled by the lender auto_repaid - automatically repaid by the system | [optional] 
**side** | **str** | Loan side | 
**currency** | **str** | Loan currency | 
**rate** | **str** | Loan rate. Only rates in [0.0002, 0.002] are supported.  Not required in lending. Market rate calculated from recent rates will be used if not set | [optional] 
**amount** | **str** | Loan amount | 
**days** | **int** | Loan days | 
**auto_renew** | **bool** | Auto renew the loan on expiration | [optional] [default to False]
**currency_pair** | **str** | Currency pair. Required for borrowing side | [optional] 
**left** | **str** | Amount not lending out | [optional] 
**repaid** | **str** | Repaid amount | [optional] 
**paid_interest** | **str** | Repaid interest | [optional] 
**unpaid_interest** | **str** | Interest not repaid | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


