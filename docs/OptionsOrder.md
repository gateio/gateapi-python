# OptionsOrder

Options order details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Options order ID | [optional] [readonly] 
**user** | **int** | User ID | [optional] [readonly] 
**create_time** | **float** | Creation time of order | [optional] [readonly] 
**finish_time** | **float** | Order finished time. Not returned if order is open | [optional] [readonly] 
**finish_as** | **str** | Order finish reason:  - filled: Fully filled - cancelled: User cancelled - liquidated: Cancelled due to liquidation - ioc: Not immediately fully filled due to IOC time-in-force setting - auto_deleveraged: Cancelled due to auto-deleveraging - reduce_only: Cancelled due to position increase while reduce-only is set - position_closed: Cancelled because the position was closed - reduce_out: Only reduce positions by excluding hard-to-fill orders - mmp_cancelled: Cancelled by MMP | [optional] [readonly] 
**status** | **str** | Order status  - &#x60;open&#x60;: Pending - &#x60;finished&#x60;: Completed | [optional] [readonly] 
**contract** | **str** | Options identifier | 
**size** | **int** | Required. Trading quantity. Positive for buy, negative for sell. Set to 0 for close position orders. | 
**iceberg** | **int** | Display size for iceberg orders. 0 for non-iceberg orders. Note that hidden portions are charged taker fees. | [optional] 
**price** | **str** | Order price. Price of 0 with &#x60;tif&#x60; set as &#x60;ioc&#x60; represents market order (quote currency) | [optional] 
**close** | **bool** | Set as &#x60;true&#x60; to close the position, with &#x60;size&#x60; set to 0 | [optional] [default to False]
**is_close** | **bool** | Is the order to close position | [optional] [readonly] 
**reduce_only** | **bool** | Set as &#x60;true&#x60; to be reduce-only order | [optional] [default to False]
**is_reduce_only** | **bool** | Is the order reduce-only | [optional] [readonly] 
**is_liq** | **bool** | Is the order for liquidation | [optional] [readonly] 
**mmp** | **bool** | When set to true, it is an MMP order | [optional] [default to False]
**is_mmp** | **bool** | Whether it is an MMP order. Corresponds to &#x60;mmp&#x60; in the request | [optional] [readonly] 
**tif** | **str** | Time in force strategy. Market orders currently only support IOC mode  - gtc: Good Till Cancelled - ioc: Immediate Or Cancelled, execute immediately or cancel, taker only - poc: Pending Or Cancelled, passive order, maker only | [optional] [default to 'gtc']
**left** | **int** | Unfilled quantity | [optional] [readonly] 
**fill_price** | **str** | Fill price | [optional] [readonly] 
**text** | **str** | User defined information. If not empty, must follow the rules below:  1. prefixed with &#x60;t-&#x60; 2. no longer than 28 bytes without &#x60;t-&#x60; prefix 3. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.) Besides user defined information, reserved contents are listed below, denoting how the order is created:  - web: from web - api: from API - app: from mobile phones - auto_deleveraging: from ADL - liquidation: from liquidation - insurance: from insurance  | [optional] 
**tkfr** | **str** | Taker fee | [optional] [readonly] 
**mkfr** | **str** | Maker fee | [optional] [readonly] 
**refu** | **int** | Referrer user ID | [optional] [readonly] 
**refr** | **str** | Referrer rebate | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


