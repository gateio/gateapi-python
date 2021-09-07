# FuturesOrderBook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Order Book ID. Increases by 1 on every order book change. Set &#x60;with_id&#x3D;true&#x60; to include this field in response | [optional] 
**current** | **float** | Response data generation timestamp | [optional] 
**update** | **float** | Order book changed timestamp | [optional] 
**asks** | [**list[FuturesOrderBookItem]**](FuturesOrderBookItem.md) | Asks order depth | 
**bids** | [**list[FuturesOrderBookItem]**](FuturesOrderBookItem.md) | Bids order depth | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


