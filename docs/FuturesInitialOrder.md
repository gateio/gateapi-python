# FuturesInitialOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | Futures contract | 
**size** | **int** | Represents the number of contracts that need to be closed, full closing: size&#x3D;0 Partial closing: plan-close-short-position size&gt;0  Partial closing: plan-close-long-position size&lt;0 | [optional] 
**price** | **str** | Order price. Set to 0 to use market price | 
**close** | **bool** | When all positions are closed in a single position mode, it must be set to true to perform the closing operation When partially closed positions in single-store mode/double-store mode, you can not set close, or close&#x3D;false | [optional] [default to False]
**tif** | **str** | Time in force strategy, default is gtc, market orders currently only support ioc mode  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled | [optional] [default to 'gtc']
**text** | **str** | The source of the order, including: - web: Web - api: API call - app: Mobile app | [optional] 
**reduce_only** | **bool** | When set to true, perform automatic position reduction operation. Set to true to ensure that the order will not open a new position, and is only used to close or reduce positions | [optional] [default to False]
**auto_size** | **str** | Single position mode: auto_size is not required Dual position mode full closing (size&#x3D;0): auto_size must be set, close_long for closing long positions, close_short for closing short positions Dual position mode partial closing (size≠0): auto_size is not required | [optional] 
**is_reduce_only** | **bool** | Is the order reduce-only | [optional] [readonly] 
**is_close** | **bool** | Is the order to close position | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


