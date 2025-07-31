# Transfer

Accounts available to transfer:  - `spot`: spot account - `margin`: margin account - `futures`: perpetual futures account - `delivery`: delivery futures account - `options`: options account
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Transfer currency name. For contract accounts, &#x60;currency&#x60; can be set to &#x60;POINT&#x60; (points) or supported settlement currencies (e.g., &#x60;BTC&#x60;, &#x60;USDT&#x60;) | 
**_from** | **str** | Account to transfer from | 
**to** | **str** | Account to transfer to | 
**amount** | **str** | Transfer amount | 
**currency_pair** | **str** | Margin trading pair. Required when transferring to or from margin account | [optional] 
**settle** | **str** | Contract settlement currency. Required when transferring to or from contract account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


