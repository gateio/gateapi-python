# AmendOrderResult

Batch order modification results
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID | [optional] [readonly] 
**amount** | **str** | Trade amount | [optional] [readonly] 
**price** | **str** | Order price | [optional] [readonly] 
**amend_text** | **str** | The custom data that the user remarked when amending the order | [optional] [readonly] 
**succeeded** | **bool** | Update success status | [optional] [readonly] 
**label** | **str** | Error indicator for failed modifications; empty when successful | [optional] [readonly] 
**message** | **str** | Error description for failed modifications; empty when successful | [optional] [readonly] 
**account** | **str** | Account types， spot - spot account, margin - margin account, portfolio - portfolio margin account, cross_margin - cross margin account.Portfolio margin accounts can only be set to &#x60;cross_margin&#x60; | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


