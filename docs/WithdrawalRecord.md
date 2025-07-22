# WithdrawalRecord

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Record ID. | [optional] [readonly] 
**txid** | **str** | Hash record of the withdrawal. | [optional] [readonly] 
**block_number** | **str** | Block Number. | [optional] [readonly] 
**withdraw_order_id** | **str** | Client order id, up to 32 length and can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  | [optional] 
**timestamp** | **str** | Operation time. | [optional] [readonly] 
**amount** | **str** | Currency amount. | 
**fee** | **str** | fee. | [optional] [readonly] 
**currency** | **str** | Currency name. | 
**address** | **str** | Withdrawal address. | [optional] 
**fail_reason** | **str** | The reason for withdrawal failure is that there is a value when status &#x3D; CANCEL, and the rest of the state is empty | [optional] 
**timestamp2** | **str** | The withdrawal end time, i.e.: withdrawal cancel time or withdrawal success time When status &#x3D; CANCEL, the corresponding cancel time When status &#x3D; DONE and block_number &gt; 0, it is the | [optional] 
**memo** | **str** | Additional remarks with regards to the withdrawal. | [optional] 
**status** | **str** | Transaction status  - DONE: Completed (block_number &gt; 0 is considered to be truly completed) - CANCEL: Canceled - REQUEST: Requesting - MANUAL: Pending manual review - BCODE: Recharge code operation - EXTPEND: Sent awaiting confirmation - FAIL: Failure on the chain awaiting confirmation - INVALID: Invalid order - VERIFY: Verifying - PROCES: Processing - PEND: Processing - DMOVE: pending manual review - REVIEW: Under review | [optional] [readonly] 
**chain** | **str** | Name of the chain used in withdrawals. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


