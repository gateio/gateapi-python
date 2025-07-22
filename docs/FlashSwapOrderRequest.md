# FlashSwapOrderRequest

Parameters of flash swap order creation.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_id** | **str** | Preview result ID. | 
**sell_currency** | **str** | Name of the asset to be sold, obtained from the interface GET /flash_swap/currency_pairs: Query the list of all trading pairs supporting flash swap | 
**sell_amount** | **str** | Amount to sell (based on the preview result). | 
**buy_currency** | **str** | Name of the asset to be bought, obtained from the interface GET /flash_swap/currency_pairs: Query the list of all trading pairs supporting flash swap | 
**buy_amount** | **str** | Amount to buy (based on the preview result). | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


