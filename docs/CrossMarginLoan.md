# CrossMarginLoan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Borrow loan ID | [optional] [readonly] 
**create_time** | **int** | Creation timestamp, in milliseconds | [optional] [readonly] 
**update_time** | **int** | Update timestamp, in milliseconds | [optional] [readonly] 
**currency** | **str** | Currency name | 
**amount** | **str** | Borrowed amount | 
**text** | **str** | User defined custom ID | [optional] 
**status** | **int** | Borrow loan status, which includes:  - 1: failed to borrow - 2: borrowed but not repaid - 3: repayment complete | [optional] [readonly] 
**repaid** | **str** | Repaid amount | [optional] [readonly] 
**repaid_interest** | **str** | Repaid interest | [optional] [readonly] 
**unpaid_interest** | **str** | Outstanding interest yet to be paid | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


