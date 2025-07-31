# FuturesTicker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | Futures contract | [optional] 
**last** | **str** | Last trading price | [optional] 
**change_percentage** | **str** | Price change percentage. Negative values indicate price decrease, e.g. -7.45 | [optional] 
**total_size** | **str** | Contract total size | [optional] 
**low_24h** | **str** | 24-hour lowest price | [optional] 
**high_24h** | **str** | 24-hour highest price | [optional] 
**volume_24h** | **str** | 24-hour trading volume | [optional] 
**volume_24h_btc** | **str** | 24-hour trading volume in BTC (deprecated, use &#x60;volume_24h_base&#x60;, &#x60;volume_24h_quote&#x60;, &#x60;volume_24h_settle&#x60; instead) | [optional] 
**volume_24h_usd** | **str** | 24-hour trading volume in USD (deprecated, use &#x60;volume_24h_base&#x60;, &#x60;volume_24h_quote&#x60;, &#x60;volume_24h_settle&#x60; instead) | [optional] 
**volume_24h_base** | **str** | 24-hour trading volume in base currency | [optional] 
**volume_24h_quote** | **str** | 24-hour trading volume in quote currency | [optional] 
**volume_24h_settle** | **str** | 24-hour trading volume in settle currency | [optional] 
**mark_price** | **str** | Recent mark price | [optional] 
**funding_rate** | **str** | Funding rate | [optional] 
**funding_rate_indicative** | **str** | Indicative Funding rate in next period. (deprecated. use &#x60;funding_rate&#x60;) | [optional] 
**index_price** | **str** | Index price | [optional] 
**quanto_base_rate** | **str** | Exchange rate of base currency and settlement currency in Quanto contract. Does not exists in contracts of other types | [optional] 
**lowest_ask** | **str** | Recent lowest ask | [optional] 
**lowest_size** | **str** | The latest seller&#39;s lowest price order quantity | [optional] 
**highest_bid** | **str** | Recent highest bid | [optional] 
**highest_size** | **str** | The latest buyer&#39;s highest price order volume | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


