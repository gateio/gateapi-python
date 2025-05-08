# MockMarginResult

Margin result
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Position combination type &#x60;original_position&#x60; - Original position &#x60;long_delta_original_position&#x60; - Positive delta + Original position &#x60;short_delta_original_position&#x60; - Negative delta + Original position | [optional] 
**profit_loss_ranges** | [**list[ProfitLossRange]**](ProfitLossRange.md) | The results of 33 pressure scenarios for MR1 | [optional] 
**max_loss** | [**ProfitLossRange**](.md) | 最大损失 | [optional] 
**mr1** | **str** | Stress testing | [optional] 
**mr2** | **str** | Basis spread risk | [optional] 
**mr3** | **str** | Volatility spread risk | [optional] 
**mr4** | **str** | Option short risk | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


