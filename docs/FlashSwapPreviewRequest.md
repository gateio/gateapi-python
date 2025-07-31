# FlashSwapPreviewRequest

Parameters of flash swap order creation
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sell_currency** | **str** | The name of the asset being sold, as obtained from the \&quot;GET /flash_swap/currency_pairs\&quot; API, which retrieves a list of supported flash swap currency pairs | 
**sell_amount** | **str** | Amount to sell. It is required to choose one parameter between &#x60;sell_amount&#x60; and &#x60;buy_amount&#x60; | [optional] 
**buy_currency** | **str** | The name of the asset being purchased, as obtained from the \&quot;GET /flash_swap/currency_pairs\&quot; API, which provides a list of supported flash swap currency pairs | 
**buy_amount** | **str** | Amount to buy. It is required to choose one parameter between &#x60;sell_amount&#x60; and &#x60;buy_amount&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


