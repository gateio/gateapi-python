# FuturesOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Futures order ID | [optional] 
**create_time** | **float** | Order creation time | [optional] 
**finish_time** | **float** | Order finished time. Not returned if order is open | [optional] 
**finish_as** | **str** | how the order is finished.  - filled: all filled - cancelled: manually cancelled - liquidated: cancelled because of liquidation - ioc: time in force is &#x60;IOC&#x60;, finish immediately - auto_deleveraged: finished by ADL - reduce_only: cancelled because of increasing position while &#x60;reduce-only&#x60; set | [optional] 
**status** | **str** | Order status  - &#x60;open&#x60;: waiting to be traded - &#x60;finished&#x60;: finished | [optional] 
**contract** | **str** | Futures contract | 
**size** | **int** | Order size. Specify positive number to make a bid, and negative number to ask | [optional] 
**iceberg** | **int** | Display size for iceberg order. 0 for non-iceberg. Note that you would pay the taker fee for the hidden size | [optional] 
**price** | **str** | Order price. 0 for market order with &#x60;tif&#x60; set as &#x60;ioc&#x60; | [optional] 
**close** | **bool** | Set as &#x60;true&#x60; to close the position, with &#x60;size&#x60; set to 0 | [optional] [default to False]
**is_close** | **bool** | Is the order to close position | [optional] 
**reduce_only** | **bool** | Set as &#x60;true&#x60; to be post-only order | [optional] [default to False]
**is_reduce_only** | **bool** | Is the order post-only | [optional] 
**is_liq** | **bool** | Is the order for liquidation | [optional] 
**tif** | **str** | Time in force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only - poc: PendingOrCancelled, post-only | [optional] [default to 'gtc']
**left** | **int** | Size left to be traded | [optional] 
**fill_price** | **str** | Fill price of the order | [optional] 
**text** | **str** | How order is created  - web: from web - api: from API - app: from mobile phones - auto_deleveraging: from ADL - liquidation: from liquidation - insurance: from insurance  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


