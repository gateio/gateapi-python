# CrossMarginAccountBook

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Balance change record ID | [optional] 
**time** | **int** | The timestamp of the change (in milliseconds) | [optional] 
**currency** | **str** | Currency changed | [optional] 
**change** | **str** | Amount changed. Positive value means transferring in, while negative out | [optional] 
**balance** | **str** | Balance after change | [optional] 
**type** | **str** | Account change type, including:  - in: transferals into cross margin account - out: transferals out from cross margin account - repay: loan repayment - borrow: borrowed loan - interest: interest - new_order: new order locked - order_fill: order fills - referral_fee: fee refund from referrals - order_fee: order fee generated from fills - unknown: unknown type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


