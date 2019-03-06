# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Order ID | [optional] 
**create_time** | **str** | Order creation time | [optional] 
**status** | **str** | Order status  - &#x60;open&#x60;: to be filled- &#x60;closed&#x60;: filled- &#x60;cancelled&#x60;: cancelled | [optional] 
**currency_pair** | **str** | Currency pair | 
**type** | **str** | Order type. limit - limit order | [optional] [default to 'limit']
**account** | **str** | Account type. spot - use spot account; margin - use margin account | [optional] [default to 'spot']
**side** | **str** | Order side | 
**amount** | **str** | Trade amount | 
**price** | **str** | Order price | 
**time_in_force** | **str** | Time in force | [optional] [default to 'gtc']
**left** | **str** | Amount left to fill | [optional] 
**fill_price** | **str** | Fill price of the order | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


