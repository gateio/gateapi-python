# LedgerRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Record ID | [optional] [readonly] 
**txid** | **str** | Hash record of the withdrawal | [optional] [readonly] 
**timestamp** | **str** | Record time | [optional] [readonly] 
**amount** | **str** | Trade amount | 
**currency** | **str** | Record currency | 
**address** | **str** | Withdrawal address. Required for withdrawals | [optional] 
**memo** | **str** | Extra withdrawal memo | [optional] 
**status** | **str** | Record status.  - DONE: done - CANCEL: cancelled - REQUEST: requesting - MANUAL: waiting for manual approval - BCODE: GateCode operation | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


