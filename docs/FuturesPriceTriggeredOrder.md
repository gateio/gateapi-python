# FuturesPriceTriggeredOrder

Futures order details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initial** | [**FuturesInitialOrder**](FuturesInitialOrder.md) |  | 
**trigger** | [**FuturesPriceTrigger**](FuturesPriceTrigger.md) |  | 
**id** | **int** | Auto order ID | [optional] [readonly] 
**user** | **int** | User ID | [optional] [readonly] 
**create_time** | **float** | Creation time | [optional] [readonly] 
**finish_time** | **float** | Finished time | [optional] [readonly] 
**trade_id** | **int** | ID of the newly created order on condition triggered | [optional] [readonly] 
**status** | **str** | Order status. | [optional] [readonly] 
**finish_as** | **str** | How order is finished | [optional] [readonly] 
**reason** | **str** | Additional remarks on how the order was finished | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


