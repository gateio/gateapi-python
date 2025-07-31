# SpotPriceTriggeredOrder

Spot price order details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger** | [**SpotPriceTrigger**](SpotPriceTrigger.md) |  | 
**put** | [**SpotPricePutOrder**](SpotPricePutOrder.md) |  | 
**id** | **int** | Auto order ID | [optional] [readonly] 
**user** | **int** | User ID | [optional] [readonly] 
**market** | **str** | Market | 
**ctime** | **int** | Created time | [optional] [readonly] 
**ftime** | **int** | End time | [optional] [readonly] 
**fired_order_id** | **int** | ID of the order created after trigger | [optional] [readonly] 
**status** | **str** | Status  - open: Running - cancelled: Manually cancelled - finish: Successfully completed - failed: Failed to execute - expired: Expired | [optional] [readonly] 
**reason** | **str** | Additional description of how the order was completed | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


