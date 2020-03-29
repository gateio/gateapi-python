# BatchOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | User defined information. If not empty, must follow the rules below:  1. prefixed with &#x60;t-&#x60; 2. no longer than 16 bytes without &#x60;t-&#x60; prefix 3. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  | [optional] 
**succeeded** | **bool** | Whether order succeeds | [optional] 
**label** | **str** | Error label, empty string if order succeeds | [optional] 
**message** | **str** | Detailed error message, empty string if order succeeds | [optional] 
**id** | **str** | Order ID | [optional] 
**create_time** | **str** | Order creation time | [optional] 
**update_time** | **str** | Order last modification time | [optional] 
**status** | **str** | Order status  - &#x60;open&#x60;: to be filled - &#x60;closed&#x60;: filled - &#x60;cancelled&#x60;: cancelled | [optional] 
**currency_pair** | **str** | Currency pair | [optional] 
**type** | **str** | Order type. limit - limit order | [optional] [default to 'limit']
**account** | **str** | Account type. spot - use spot account; margin - use margin account | [optional] [default to 'spot']
**side** | **str** | Order side | [optional] 
**amount** | **str** | Trade amount | [optional] 
**price** | **str** | Order price | [optional] 
**time_in_force** | **str** | Time in force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only - poc: PendingOrCancelled, reduce only | [optional] [default to 'gtc']
**auto_borrow** | **bool** | Used in margin trading(i.e. &#x60;account&#x60; is &#x60;margin&#x60;) to allow automatic loan of insufficient part if balance is not enough. | [optional] 
**left** | **str** | Amount left to fill | [optional] 
**fill_price** | **str** | Total filled in quote currency. Deprecated in favor of &#x60;filled_total&#x60; | [optional] 
**filled_total** | **str** | Total filled in quote currency | [optional] 
**fee** | **str** | Fee deducted | [optional] 
**fee_currency** | **str** | Fee currency unit | [optional] 
**point_fee** | **str** | Point used to deduct fee | [optional] 
**gt_fee** | **str** | GT used to deduct fee | [optional] 
**gt_discount** | **bool** | Whether GT fee discount is used | [optional] 
**rebated_fee** | **str** | Rebated fee | [optional] 
**rebated_fee_currency** | **str** | Rebated fee currency unit | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


