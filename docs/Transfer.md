# Transfer

Accounts available to transfer:  - `spot`: spot account - `margin`: margin account - `futures`: perpetual futures account - `delivery`: delivery futures account
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Transfer ID | [optional] [readonly] 
**created_at** | **str** | Timestamp when the transfer occurred | [optional] [readonly] 
**currency** | **str** | Transfer currency. For futures account, &#x60;currency&#x60; can be set to &#x60;POINT&#x60; or settle currency | 
**_from** | **str** | Account transferred from | 
**to** | **str** | Account transferred to | 
**amount** | **str** | Transfer amount | 
**currency_pair** | **str** | Margin currency pair. Required if transfer from or to margin account | [optional] 
**settle** | **str** | Futures settle currency. Required if &#x60;currency&#x60; is &#x60;POINT&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


