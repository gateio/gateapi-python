# FuturesOrder

Futures order details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Futures order ID | [optional] [readonly] 
**user** | **int** | User ID | [optional] [readonly] 
**create_time** | **float** | Creation time of order | [optional] [readonly] 
**finish_time** | **float** | Order finished time. Not returned if order is open | [optional] [readonly] 
**finish_as** | **str** | How the order was finished.  - filled: all filled - cancelled: manually cancelled - liquidated: cancelled because of liquidation - ioc: time in force is &#x60;IOC&#x60;, finish immediately - auto_deleveraged: finished by ADL - reduce_only: cancelled because of increasing position while &#x60;reduce-only&#x60; set- position_closed: cancelled because of position close - position_closed: canceled because the position was closed - reduce_out: only reduce positions by excluding hard-to-fill orders - stp: cancelled because self trade prevention  | [optional] [readonly] 
**status** | **str** | Order status  - &#x60;open&#x60;: waiting to be traded - &#x60;finished&#x60;: finished | [optional] [readonly] 
**contract** | **str** | Futures contract | 
**size** | **int** | Order size. Specify positive number to make a bid, and negative number to ask | 
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
**text** | **str** | Order custom information, users can use this field to set a custom ID, and the user-defined field must meet the following conditions:  1. Must start with &#x60;t-&#x60; 2. If &#x60;t-&#x60; is not calculated, the length cannot exceed 28 bytes 3. The input content can only contain numbers, letters, underscores (_), midscores (-) or dots (.)  In addition to user-defined information, the following are internal reserved fields that identifies the source of the order:  - web: web page - api: API call - app: mobile terminal - auto_deleveraging: Automatic position reduction - liquidation: ⽼Classic mode position forced closing - liq-xxx: a. The new classic model of forced closing positions, including position-by-position, one-way full position, and two-way full position non-held position. b. The unified account single currency margin model of forced closing positions by position - hedge-liq-xxx: New classic model two-way full position hedging part of forced closing, that is, close long and short positions at the same time - pm_liquidate: Unified account cross-currency margin model for forced closing positions - cob_margin_liquidate: Unified account combination margin model for forced closing position - scm_liquidate: Unified account single currency margin mode position forced closing - insurance: insurance | [optional] 
**tkfr** | **str** | Taker fee | [optional] [readonly] 
**mkfr** | **str** | Maker fee | [optional] [readonly] 
**refu** | **int** | Reference user ID | [optional] [readonly] 
**auto_size** | **str** | Set side to close dual-mode position. &#x60;close_long&#x60; closes the long side; while &#x60;close_short&#x60; the short one. Note &#x60;size&#x60; also needs to be set to 0 | [optional] 
**stp_id** | **int** | Orders between users in the same &#x60;stp_id&#x60; group are not allowed to be self-traded  1. If the &#x60;stp_id&#x60; of two orders being matched is non-zero and equal, they will not be executed. Instead, the corresponding strategy will be executed based on the &#x60;stp_act&#x60; of the taker. 2. &#x60;stp_id&#x60; returns &#x60;0&#x60; by default for orders that have not been set for &#x60;STP group&#x60; | [optional] [readonly] 
**stp_act** | **str** | Self-Trading Prevention Action. Users can use this field to set self-trade prevetion strategies  1. After users join the &#x60;STP Group&#x60;, he can pass &#x60;stp_act&#x60; to limit the user&#39;s self-trade prevetion strategy. If &#x60;stp_act&#x60; is not passed, the default is &#x60;cn&#x60; strategy。 2. When the user does not join the &#x60;STP group&#x60;, an error will be returned when passing the &#x60;stp_act&#x60; parameter。 3. If the user did not use &#39;stp_act&#39; when placing the order, &#39;stp_act&#39; will return &#39;-&#39;  - cn: Cancel newest, Cancel new orders and keep old ones - co: Cancel oldest, Cancel old orders and keep new ones - cb: Cancel both, Both old and new orders will be cancelled | [optional] 
**amend_text** | **str** | The custom data that the user remarked when amending the order | [optional] [readonly] 
**biz_info** | **str** | Additional information | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


