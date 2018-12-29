# FuturesOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | futures order ID | [optional] 
**create_time** | **float** | order creation time | [optional] 
**finish_time** | **float** | order finished time. Not returned if order is open | [optional] 
**finish_as** | **str** | how the order is finished.  - filled: all filled - cancelled: manually cancelled - liquidated: cancelled because of liquidation - ioc: time in force is &#x60;IOC&#x60;, finish immediately - auto_deleveraged: finished by ADL  | [optional] 
**status** | **str** | order status  - &#x60;open&#x60;: waiting to be traded - &#x60;finished&#x60;: finished  | [optional] 
**contract** | **str** | contract name | 
**size** | **int** | contract size. Specify positive number to make a bid, negative number otherwise.  Set to 0 if trying to close the position  | [optional] 
**price** | **str** | order price. Set to 0 if using market price | [optional] 
**close** | **bool** | set to true if trying to close the position | [optional] [default to False]
**is_close** | **bool** | the order is a closing position order. | [optional] 
**tif** | **str** | Time in force. If using market price, only &#x60;ioc&#x60; is supported.  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled  | [optional] [default to 'gtc']
**left** | **int** | size left to be traded | [optional] 
**fill_price** | **str** | fill price of the order | [optional] 
**text** | **str** | how order is created  - web: from web - api: from API - app: from mobile phones - auto_deleveraging: from ADL - liquidation: from liquidation - insurance: from insurance  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


