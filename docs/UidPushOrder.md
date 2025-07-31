# UidPushOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Order ID | [optional] 
**push_uid** | **int** | Initiator User ID | [optional] 
**receive_uid** | **int** | Recipient User ID | [optional] 
**currency** | **str** | Currency name | [optional] 
**amount** | **str** | Transfer amount | [optional] 
**create_time** | **int** | Created time | [optional] 
**status** | **str** | Withdrawal status:  - CREATING: Creating - PENDING: Waiting for recipient (Please contact the recipient to accept the transfer on Gate official website) - CANCELLING: Cancelling - CANCELLED: Cancelled - REFUSING: Refusing - REFUSED: Refused - RECEIVING: Receiving - RECEIVED: Success | [optional] 
**message** | **str** | PENDING reason tips | [optional] 
**transaction_type** | **str** | Order Type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


