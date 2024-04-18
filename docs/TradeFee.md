# TradeFee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] 
**taker_fee** | **str** | taker fee rate | [optional] 
**maker_fee** | **str** | maker fee rate | [optional] 
**gt_discount** | **bool** | If GT deduction is enabled | [optional] 
**gt_taker_fee** | **str** | Taker fee rate if using GT deduction. It will be 0 if GT deduction is disabled | [optional] 
**gt_maker_fee** | **str** | Maker fee rate if using GT deduction. It will be 0 if GT deduction is disabled | [optional] 
**loan_fee** | **str** | Loan fee rate of margin lending | [optional] 
**point_type** | **str** | Point type. 0 - Initial version. 1 - new version since 202009 | [optional] 
**futures_taker_fee** | **str** | Futures trading taker fee | [optional] 
**futures_maker_fee** | **str** | Future trading maker fee | [optional] 
**delivery_taker_fee** | **str** | Delivery trading taker fee | [optional] 
**delivery_maker_fee** | **str** | Delivery trading maker fee | [optional] 
**debit_fee** | **int** | Deduction types for rates, 1 - GT deduction, 2 - Point card deduction, 3 - VIP rates | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


