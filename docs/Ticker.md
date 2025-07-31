# Ticker

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_pair** | **str** | Currency pair | [optional] 
**last** | **str** | Last trading price | [optional] 
**lowest_ask** | **str** | Recent lowest ask | [optional] 
**lowest_size** | **str** | Latest seller&#39;s lowest price quantity; not available for batch queries; available for single queries, empty if no data | [optional] 
**highest_bid** | **str** | Recent highest bid | [optional] 
**highest_size** | **str** | Latest buyer&#39;s highest price quantity; not available for batch queries; available for single queries, empty if no data | [optional] 
**change_percentage** | **str** | 24h price change percentage (negative for decrease, e.g., -7.45) | [optional] 
**change_utc0** | **str** | UTC+0 timezone, 24h price change percentage, negative for decline (e.g., -7.45) | [optional] 
**change_utc8** | **str** | UTC+8 timezone, 24h price change percentage, negative for decline (e.g., -7.45) | [optional] 
**base_volume** | **str** | Base currency trading volume in the last 24h | [optional] 
**quote_volume** | **str** | Quote currency trading volume in the last 24h | [optional] 
**high_24h** | **str** | 24h High | [optional] 
**low_24h** | **str** | 24h Low | [optional] 
**etf_net_value** | **str** | ETF net value | [optional] 
**etf_pre_net_value** | **str** | ETF net value at previous rebalancing point | [optional] 
**etf_pre_timestamp** | **int** | ETF previous rebalancing time | [optional] 
**etf_leverage** | **str** | ETF current leverage | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


