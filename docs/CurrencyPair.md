# CurrencyPair

Spot currency pair
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Currency pair | [optional] 
**base** | **str** | Base currency | [optional] 
**base_name** | **str** | Transaction currency name | [optional] 
**quote** | **str** | Quote currency | [optional] 
**quote_name** | **str** | Name of the denominated currency | [optional] 
**fee** | **str** | Trading fee | [optional] 
**min_base_amount** | **str** | Minimum amount of base currency to trade, &#x60;null&#x60; means no limit | [optional] 
**min_quote_amount** | **str** | Minimum amount of quote currency to trade, &#x60;null&#x60; means no limit | [optional] 
**max_base_amount** | **str** | Maximum amount of base currency to trade, &#x60;null&#x60; means no limit | [optional] 
**max_quote_amount** | **str** | Maximum amount of quote currency to trade, &#x60;null&#x60; means no limit | [optional] 
**amount_precision** | **int** | Amount scale | [optional] 
**precision** | **int** | Price scale | [optional] 
**trade_status** | **str** | How currency pair can be traded  - untradable: cannot be bought or sold - buyable: can be bought - sellable: can be sold - tradable: can be bought or sold | [optional] 
**sell_start** | **int** | Sell start unix timestamp in seconds | [optional] 
**buy_start** | **int** | Buy start unix timestamp in seconds | [optional] 
**delisting_time** | **int** | Expected time to remove the shelves, Unix timestamp in seconds | [optional] 
**type** | **str** | Trading pair type, normal: normal, premarket: pre-market | [optional] 
**trade_url** | **str** | Transaction link | [optional] 
**st_tag** | **bool** | Whether the trading pair is in ST risk assessment, false - No, true - Yes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


