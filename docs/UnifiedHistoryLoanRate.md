# UnifiedHistoryLoanRate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Currency name | [optional] 
**tier** | **str** | VIP level for the floating rate to be retrieved | [optional] 
**tier_up_rate** | **str** | Floating rate corresponding to VIP level | [optional] 
**rates** | [**list[UnifiedHistoryLoanRateRates]**](UnifiedHistoryLoanRateRates.md) | Historical interest rate information, one data point per hour, array size determined by page and limit parameters from the API request, sorted by time from recent to distant | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


