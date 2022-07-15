# SpotPricePutOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Order type, default to &#x60;limit&#x60; | [optional] [default to 'limit']
**side** | **str** | Order side  - buy: buy side - sell: sell side | 
**price** | **str** | Order price | 
**amount** | **str** | Order amount | 
**account** | **str** | Trading account type.  Portfolio margin account must set to &#x60;cross_margin&#x60;  - normal: spot trading - margin: margin trading - cross_margin: cross_margin trading  | [default to 'normal']
**time_in_force** | **str** | time_in_force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only  | [optional] [default to 'gtc']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


