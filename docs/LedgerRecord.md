# LedgerRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Record ID | [optional] [readonly] 
**txid** | **str** | Hash record of the withdrawal | [optional] [readonly] 
**timestamp** | **str** | Operation time | [optional] [readonly] 
**amount** | **str** | Currency amount | 
**currency** | **str** | Currency name | 
**address** | **str** | Withdrawal address. Required for withdrawals | [optional] 
**memo** | **str** | Additional remarks with regards to the withdrawal | [optional] 
**status** | **str** | Record status.  - DONE: done - CANCEL: cancelled - REQUEST: requesting - MANUAL: pending manual approval - BCODE: GateCode operation - EXTPEND: pending confirm after sending - FAIL: pending confirm when fail - INVALID: invalid order - VERIFY: verifying - PROCES: processing - PEND: pending | [optional] [readonly] 
**chain** | **str** | Name of the chain used in withdrawals | [optional] 
**fee** | **str** | Fee | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


