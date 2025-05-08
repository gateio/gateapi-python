# FuturesAutoDeleverage

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **int** | Automatic deleveraging time | [optional] [readonly] 
**user** | **int** | User ID | [optional] [readonly] 
**order_id** | **int** | Order ID. Order IDs before 2023-02-20 are null | [optional] [readonly] 
**contract** | **str** | Futures contract | [optional] [readonly] 
**leverage** | **str** | Position leverage | [optional] [readonly] 
**cross_leverage_limit** | **str** | Cross margin leverage(valid only when &#x60;leverage&#x60; is 0) | [optional] [readonly] 
**entry_price** | **str** | Average entry price | [optional] [readonly] 
**fill_price** | **str** | Average fill price | [optional] [readonly] 
**trade_size** | **int** | Trading size | [optional] [readonly] 
**position_size** | **int** | Positions after auto-deleveraging | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


