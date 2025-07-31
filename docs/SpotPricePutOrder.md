# SpotPricePutOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Order type，default to &#x60;limit&#x60;  - limit : Limit Order - market : Market Order | [optional] [default to 'limit']
**side** | **str** | Order side  - buy: buy side - sell: sell side | 
**price** | **str** | Order price | 
**amount** | **str** | Trading quantity When &#x60;type&#x60; is &#x60;limit&#x60;, it refers to the base currency (the currency being traded), such as &#x60;BTC&#x60; in &#x60;BTC_USDT&#x60; When &#x60;type&#x60; is &#x60;market&#x60;, it refers to different currencies based on the side: - &#x60;side&#x60;: &#x60;buy&#x60; refers to quote currency, &#x60;BTC_USDT&#x60; means &#x60;USDT&#x60; - &#x60;side&#x60;: &#x60;sell&#x60; refers to base currency, &#x60;BTC_USDT&#x60; means &#x60;BTC&#x60; | 
**account** | **str** | Trading account type. Unified account must be set to &#x60;unified&#x60;  - normal: spot trading - margin: margin trading - unified: unified account  | [default to 'normal']
**time_in_force** | **str** | time_in_force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only  | [optional] [default to 'gtc']
**auto_borrow** | **bool** | Whether to borrow coins automatically | [optional] [default to False]
**auto_repay** | **bool** | Whether to repay the loan automatically | [optional] [default to False]
**text** | **str** | The source of the order, including: - web: Web - api: API call - app: Mobile app | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


