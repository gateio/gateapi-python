# CurrencyPair

Spot currency pair
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Currency pair | [optional] 
**base** | **str** | Base currency | [optional] 
**quote** | **str** | Quote currency | [optional] 
**fee** | **str** | Trading fee | [optional] 
**min_base_amount** | **str** | Minimum amount of base currency to trade, &#x60;null&#x60; means no limit | [optional] 
**min_quote_amount** | **str** | Minimum amount of quote currency to trade, &#x60;null&#x60; means no limit | [optional] 
**amount_precision** | **int** | Amount scale | [optional] 
**precision** | **int** | Price scale | [optional] 
**trade_status** | **str** | How currency pair can be traded  - untradable: cannot be bought or sold - buyable: can be bought - sellable: can be sold - tradable: can be bought or sold | [optional] 
**etf_net_value** | **str** | ETF net value | [optional] 
**etf_pre_net_value** | **str** | ETF previous net value at re-balancing time | [optional] 
**etf_pre_timestamp** | **int** | ETF previous re-balancing time | [optional] 
**etf_leverage** | **str** | ETF current leverage | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


