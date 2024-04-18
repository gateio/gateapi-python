# OrderPatch

Spot order details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | New order amount. &#x60;amount&#x60; and &#x60;price&#x60; must specify one of them | [optional] 
**price** | **str** | New order price. &#x60;amount&#x60; and &#x60;Price&#x60; must specify one of them\&quot; | [optional] 
**amend_text** | **str** | Custom info during amending order | [optional] 
**action_mode** | **str** | Processing Mode: When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result ACK: Asynchronous mode, only returns key order fields RESULT: No clearing information FULL: Full mode (default) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


