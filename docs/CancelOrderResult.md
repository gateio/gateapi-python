# CancelOrderResult

Order cancellation result
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_pair** | **str** | Order currency pair | [optional] 
**id** | **str** | Order ID | [optional] 
**succeeded** | **bool** | Whether cancellation succeeded | [optional] 
**label** | **str** | Error label when failed to cancel the order; emtpy if succeeded | [optional] 
**message** | **str** | Error message when failed to cancel the order; empty if succeeded | [optional] 
**account** | **str** | Empty by default. If cancelled order is cross margin order, this field is set to &#x60;cross_margin&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


