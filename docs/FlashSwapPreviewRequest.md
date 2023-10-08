# FlashSwapPreviewRequest

Parameters of flash swap order creation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sell_currency** | **str** | 卖出的资产名称， 根据接口&#x60;查询支持闪兑的所有交易对列表 GET /flash_swap/currency_pairs&#x60;获取 | 
**sell_amount** | **str** | Amount to sell. It is required to choose one parameter between &#x60;sell_amount&#x60; and &#x60;buy_amount&#x60; | [optional] 
**buy_currency** | **str** | 买入的资产名称， 根据接口&#x60;查询支持闪兑的所有交易对列表 GET /flash_swap/currency_pairs&#x60;获取 | 
**buy_amount** | **str** | Amount to buy. It is required to choose one parameter between &#x60;sell_amount&#x60; and &#x60;buy_amount&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


