# OrderPatch

Spot order details.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_pair** | **str** | Currency pair. | [optional] 
**account** | **str** | Specify query account. | [optional] 
**amount** | **str** | Trading Quantity. Either amountor pricemust be specified. | [optional] 
**price** | **str** | Trading Price. Either amountor pricemust be specified. | [optional] 
**amend_text** | **str** | Custom info during amending order. | [optional] 
**action_mode** | **str** | Processing Mode: When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result ACK: Asynchronous mode, only returns key order fields RESULT: No clearing information FULL: Full mode (default) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


