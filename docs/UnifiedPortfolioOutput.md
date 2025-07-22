# UnifiedPortfolioOutput

The output of the portfolio margin calculator.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maintain_margin_total** | **str** | Total maintenance margin, including only the portfolio margin calculation results for positions in the risk unit,  excluding borrowed margin. If borrowing exists, conventional borrowing margin requirements will still apply. | [optional] 
**initial_margin_total** | **str** | Total initial margin, calculated as the maximum of the following three combinations: position,  position + positive delta orders, orders. | [optional] 
**calculate_time** | **int** | Calculate time. | [optional] 
**risk_unit** | [**list[MockRiskUnit]**](MockRiskUnit.md) | Risk unit. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


