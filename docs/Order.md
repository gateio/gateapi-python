# Order

Spot order details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order ID | [optional] [readonly] 
**text** | **str** | User defined information. If not empty, must follow the rules below:  1. prefixed with &#x60;t-&#x60; 2. no longer than 28 bytes without &#x60;t-&#x60; prefix 3. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  | [optional] 
**create_time** | **str** | Order creation time | [optional] [readonly] 
**update_time** | **str** | Order last modification time | [optional] [readonly] 
**status** | **str** | Order status  - &#x60;open&#x60;: to be filled - &#x60;closed&#x60;: filled - &#x60;cancelled&#x60;: cancelled | [optional] [readonly] 
**currency_pair** | **str** | Currency pair | 
**type** | **str** | Order type. limit - limit order | [optional] [default to 'limit']
**account** | **str** | Account type. spot - use spot account; margin - use margin account | [optional] [default to 'spot']
**side** | **str** | Order side | 
**amount** | **str** | Trade amount | 
**price** | **str** | Order price | 
**time_in_force** | **str** | Time in force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only - poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee | [optional] [default to 'gtc']
**iceberg** | **str** | Amount to display for the iceberg order. Null or 0 for normal orders. Set to -1 to hide the amount totally | [optional] 
**auto_borrow** | **bool** | Used in margin trading(i.e. &#x60;account&#x60; is &#x60;margin&#x60;) to allow automatic loan of insufficient part if balance is not enough. | [optional] 
**left** | **str** | Amount left to fill | [optional] [readonly] 
**fill_price** | **str** | Total filled in quote currency. Deprecated in favor of &#x60;filled_total&#x60; | [optional] [readonly] 
**filled_total** | **str** | Total filled in quote currency | [optional] [readonly] 
**fee** | **str** | Fee deducted | [optional] [readonly] 
**fee_currency** | **str** | Fee currency unit | [optional] [readonly] 
**point_fee** | **str** | Point used to deduct fee | [optional] [readonly] 
**gt_fee** | **str** | GT used to deduct fee | [optional] [readonly] 
**gt_discount** | **bool** | Whether GT fee discount is used | [optional] [readonly] 
**rebated_fee** | **str** | Rebated fee | [optional] [readonly] 
**rebated_fee_currency** | **str** | Rebated fee currency unit | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


