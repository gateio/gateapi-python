# FuturesBatchAmendOrderRequest

Modify contract order parameters
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **int** | Order id, order_id and text must contain at least one | [optional] 
**text** | **str** | User-defined order text, at least one of order_id and text must be passed | [optional] 
**size** | **int** | New order size, including filled size. - If less than or equal to the filled quantity, the order will be cancelled. - The new order side must be identical to the original one. - Close order size cannot be modified. - For reduce-only orders, increasing the size may cancel other reduce-only orders. - If the price is not modified, decreasing the size will not affect the depth queue, while increasing the size will place it at the end of the current price level. | [optional] 
**price** | **str** | New order price | [optional] 
**amend_text** | **str** | Custom info during order amendment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


