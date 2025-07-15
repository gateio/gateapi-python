# BatchAmendItem

Order information that needs to be modified
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The order ID returned upon successful creation or the custom ID specified by the user during creation (i.e., the &#39;text&#39; field). | 
**currency_pair** | **str** | Currency pair | 
**account** | **str** | Default spot, unified account and warehouse-by-store leverage account. | [optional] 
**amount** | **str** | Trading Quantity. Only one of amountor pricecan be specified. | [optional] 
**price** | **str** | Trading Price. Only one of amountor pricecan be specified. | [optional] 
**amend_text** | **str** | Custom info during amending order | [optional] 
**action_mode** | **str** | Processing Mode: When placing an order, different fields are returned based on action_mode. This field is only valid during the request and is not included in the response result ACK: Asynchronous mode, only returns key order fields RESULT: No clearing information FULL: Full mode (default) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


