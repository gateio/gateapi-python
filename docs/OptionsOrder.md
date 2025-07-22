# OptionsOrder

Options order detail.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Options order ID. | [optional] [readonly] 
**user** | **int** | User ID. | [optional] [readonly] 
**create_time** | **float** | Creation time of order. | [optional] [readonly] 
**finish_time** | **float** | Order finished time. Not returned if order is open. | [optional] [readonly] 
**finish_as** | **str** | Ending method, including:  - filled: fully completed - canceled: user canceled - liquidated: forced liquidation cancellation - ioc: Not fully filled immediately because tif is set to ioc - auto_deleveraged: automatic deleveraging cancel - reduce_only: Increased position is cancelled, or the position is closed - position_closed: Because the position was closed, the pending order was canceled - reduce_out: Only reduce the excluded pending orders that are not easy to be filled - mmp_cancelled: MMP canceled | [optional] [readonly] 
**status** | **str** | Order status  - &#x60;open&#x60;: waiting to be traded - &#x60;finished&#x60;: finished | [optional] [readonly] 
**contract** | **str** | Contract name. | 
**size** | **int** | Order size. Specify positive number to make a bid, and negative number to ask | 
**iceberg** | **int** | Display size for iceberg order. 0 for non-iceberg. Note that you will have to pay the taker fee for the hidden size | [optional] 
**price** | **str** | Order price. 0 for market order with &#x60;tif&#x60; set as &#x60;ioc&#x60; (USDT). | [optional] 
**close** | **bool** | Set as &#x60;true&#x60; to close the position, with &#x60;size&#x60; set to 0. | [optional] [default to False]
**is_close** | **bool** | Is the order to close position. | [optional] [readonly] 
**reduce_only** | **bool** | Set as &#x60;true&#x60; to be reduce-only order. | [optional] [default to False]
**is_reduce_only** | **bool** | Is the order reduce-only. | [optional] [readonly] 
**is_liq** | **bool** | Is the order for liquidation. | [optional] [readonly] 
**mmp** | **bool** | When set to true, delegate to MMP. | [optional] [default to False]
**is_mmp** | **bool** | Whether it is MMP delegation. Corresponds to &#x60;mmp&#x60; in the request. | [optional] [readonly] 
**tif** | **str** | Time in force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only - poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee | [optional] [default to 'gtc']
**left** | **int** | Size left to be traded. | [optional] [readonly] 
**fill_price** | **str** | Fill price of the order. | [optional] [readonly] 
**text** | **str** | User defined information. If not empty, must follow the rules below:  1. prefixed with &#x60;t-&#x60; 2. no longer than 28 bytes without &#x60;t-&#x60; prefix 3. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.) Besides user defined information, reserved contents are listed below, denoting how the order is created:  - web: from web - api: from API - app: from mobile phones - auto_deleveraging: from ADL - liquidation: from liquidation - insurance: from insurance  | [optional] 
**tkfr** | **str** | Taker fee. | [optional] [readonly] 
**mkfr** | **str** | Maker fee. | [optional] [readonly] 
**refu** | **int** | Reference user ID. | [optional] [readonly] 
**refr** | **str** | Referrer rebate. | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


