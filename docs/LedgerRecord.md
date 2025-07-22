# LedgerRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Record ID. | [optional] [readonly] 
**txid** | **str** | Hash record of the withdrawal. | [optional] [readonly] 
**withdraw_order_id** | **str** | User-defined order number when withdrawing. Default is empty. When not empty, the specified user-defined order number record will be queried | [optional] 
**timestamp** | **str** | Operation time. | [optional] [readonly] 
**amount** | **str** | Currency amount. | 
**currency** | **str** | Currency name. | 
**address** | **str** | Withdrawal address. Required for withdrawals. | [optional] 
**memo** | **str** | Additional remarks with regards to the withdrawal. | [optional] 
**withdraw_id** | **str** | The withdrawal record id starts with w, such as: w1879219868. When withdraw_id is not empty, the value querys this withdrawal record and no longer querys according to time | [optional] 
**asset_class** | **str** | The currency type of withdrawal record is empty by default. It supports users to query the withdrawal records in the main and innovation areas on demand. Value range: SPOT, PILOT  SPOT: Main Zone  PILOT: Innovation Zone | [optional] 
**status** | **str** | Record status.  - DONE: done - CANCEL: cancelled - REQUEST: requesting - MANUAL: pending manual approval - BCODE: GateCode operation - EXTPEND: pending confirm after sending - FAIL: pending confirm when fail - INVALID: invalid order - VERIFY: verifying - PROCES: processing - PEND: pending - DMOVE: required manual approval - REVIEW: Under review | [optional] [readonly] 
**chain** | **str** | Name of the chain used in withdrawals. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


