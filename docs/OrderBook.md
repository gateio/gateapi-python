# OrderBook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Order book ID, which is updated whenever the order book is changed. Valid only when &#x60;with_id&#x60; is set to &#x60;true&#x60; | [optional] 
**current** | **int** | The timestamp of the response data being generated (in milliseconds) | [optional] 
**update** | **int** | The timestamp of when the orderbook last changed (in milliseconds) | [optional] 
**asks** | **list[list[str]]** | Ask Depth | 
**bids** | **list[list[str]]** | Bid Depth | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


