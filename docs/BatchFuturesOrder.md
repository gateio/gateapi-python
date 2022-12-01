# BatchFuturesOrder

Futures order details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**succeeded** | **bool** | Whether the batch of orders succeeded | [optional] 
**label** | **str** | Error label, only exists if execution fails | [optional] 
**detail** | **str** | Error detail, only present if execution failed and details need to be given | [optional] 
**id** | **int** | Futures order ID | [optional] [readonly] 
**user** | **int** | User ID | [optional] [readonly] 
**create_time** | **float** | Creation time of order | [optional] [readonly] 
**finish_time** | **float** | Order finished time. Not returned if order is open | [optional] [readonly] 
**finish_as** | **str** | How the order was finished.  - filled: all filled - cancelled: manually cancelled - liquidated: cancelled because of liquidation - ioc: time in force is &#x60;IOC&#x60;, finish immediately - auto_deleveraged: finished by ADL - reduce_only: cancelled because of increasing position while &#x60;reduce-only&#x60; set- position_closed: cancelled because of position close  | [optional] [readonly] 
**status** | **str** | Order status  - &#x60;open&#x60;: waiting to be traded - &#x60;finished&#x60;: finished | [optional] [readonly] 
**contract** | **str** | Futures contract | [optional] 
**size** | **int** | Order size. Specify positive number to make a bid, and negative number to ask | [optional] 
**iceberg** | **int** | Display size for iceberg order. 0 for non-iceberg. Note that you will have to pay the taker fee for the hidden size | [optional] 
**price** | **str** | Order price. 0 for market order with &#x60;tif&#x60; set as &#x60;ioc&#x60; | [optional] 
**close** | **bool** | Set as &#x60;true&#x60; to close the position, with &#x60;size&#x60; set to 0 | [optional] [default to False]
**is_close** | **bool** | Is the order to close position | [optional] [readonly] 
**reduce_only** | **bool** | Set as &#x60;true&#x60; to be reduce-only order | [optional] [default to False]
**is_reduce_only** | **bool** | Is the order reduce-only | [optional] [readonly] 
**is_liq** | **bool** | Is the order for liquidation | [optional] [readonly] 
**tif** | **str** | Time in force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only - poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee - fok: FillOrKill, fill either completely or none | [optional] [default to 'gtc']
**left** | **int** | Size left to be traded | [optional] [readonly] 
**fill_price** | **str** | Fill price of the order | [optional] [readonly] 
**text** | **str** | User defined information. If not empty, must follow the rules below:  1. prefixed with &#x60;t-&#x60; 2. no longer than 28 bytes without &#x60;t-&#x60; prefix 3. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.) Besides user defined information, reserved contents are listed below, denoting how the order is created:  - web: from web - api: from API - app: from mobile phones - auto_deleveraging: from ADL - liquidation: from liquidation - insurance: from insurance  | [optional] 
**tkfr** | **str** | Taker fee | [optional] [readonly] 
**mkfr** | **str** | Maker fee | [optional] [readonly] 
**refu** | **int** | Reference user ID | [optional] [readonly] 
**auto_size** | **str** | Set side to close dual-mode position. &#x60;close_long&#x60; closes the long side; while &#x60;close_short&#x60; the short one. Note &#x60;size&#x60; also needs to be set to 0 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


