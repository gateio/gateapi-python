# LedgerRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Record ID | [optional] [readonly] 
**txid** | **str** | Hash record of the withdrawal | [optional] [readonly] 
**withdraw_order_id** | **str** | User-defined order number for withdrawal. Default is empty. When not empty, the specified user-defined order number record will be queried | [optional] 
**timestamp** | **str** | Operation time | [optional] [readonly] 
**amount** | **str** | Token amount | 
**currency** | **str** | Currency name | 
**address** | **str** | Withdrawal address. Required for withdrawals | [optional] 
**memo** | **str** | Additional remarks with regards to the withdrawal | [optional] 
**withdraw_id** | **str** | Withdrawal record ID starts with &#39;w&#39;, such as: w1879219868. When withdraw_id is not empty, only this specific withdrawal record will be queried, and time-based querying will be disabled | [optional] 
**asset_class** | **str** | Withdrawal record currency type, empty by default. Supports users to query withdrawal records in main area and innovation area on demand. Valid values: SPOT, PILOT  SPOT: Main area PILOT: Innovation area | [optional] 
**status** | **str** | Transaction status  - DONE: Completed - CANCEL: Cancelled - REQUEST: Requesting - MANUAL: Pending manual review - BCODE: GateCode operation - EXTPEND: Sent, waiting for confirmation - FAIL: Failed on chain, waiting for confirmation - INVALID: Invalid order - VERIFY: Verifying - PROCES: Processing - PEND: Processing - DMOVE: Pending manual review - REVIEW: Under review | [optional] [readonly] 
**chain** | **str** | Name of the chain used in withdrawals | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


