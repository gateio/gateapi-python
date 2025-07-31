# FuturesTrade

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Fill ID | [optional] 
**create_time** | **float** | Fill Time | [optional] 
**create_time_ms** | **float** | Trade time, with millisecond precision to 3 decimal places | [optional] 
**contract** | **str** | Futures contract | [optional] 
**size** | **int** | Trading size | [optional] 
**price** | **str** | Trade price (quote currency) | [optional] 
**is_internal** | **bool** | Whether it is an internal trade. Internal trade refers to the takeover of liquidation orders by the insurance fund and ADL users. Since it is not a normal matching on the market depth, the trade price may deviate from the market, and it will not be recorded in the K-line. If it is not an internal trade, this field will not be returned | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


