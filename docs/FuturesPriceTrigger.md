# FuturesPriceTrigger

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy_type** | **int** | How the order will be triggered   - &#x60;0&#x60;: by price, which means the order will be triggered if price condition is satisfied  - &#x60;1&#x60;: by price gap, which means the order will be triggered if gap of recent two prices of specified &#x60;price_type&#x60; are satisfied.  Only &#x60;0&#x60; is supported currently | [optional] 
**price_type** | **int** | Price type. 0 - latest deal price, 1 - mark price, 2 - index price | [optional] 
**price** | **str** | Value of price on price triggered, or price gap on price gap triggered | [optional] 
**rule** | **int** | Trigger condition type  - &#x60;1&#x60;: calculated price based on &#x60;strategy_type&#x60; and &#x60;price_type&#x60; &gt;&#x3D; &#x60;price&#x60; - &#x60;2&#x60;: calculated price based on &#x60;strategy_type&#x60; and &#x60;price_type&#x60; &lt;&#x3D; &#x60;price&#x60; | [optional] 
**expiration** | **int** | How long (in seconds) to wait for the condition to be triggered before cancelling the order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


