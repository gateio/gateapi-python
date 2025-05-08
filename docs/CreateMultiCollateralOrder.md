# CreateMultiCollateralOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID | [optional] 
**order_type** | **str** | current - current, fixed - fixed, if not specified, default to current | [optional] 
**fixed_type** | **str** | Fixed interest rate loan period: 7d - 7 days, 30d - 30 days. Must be provided for fixed | [optional] 
**fixed_rate** | **str** | Fixed interest rate, must be specified for fixed | [optional] 
**auto_renew** | **bool** | Fixed interest rate, automatic renewal | [optional] 
**auto_repay** | **bool** | Fixed interest rate, automatic repayment | [optional] 
**borrow_currency** | **str** | Borrowed currency | 
**borrow_amount** | **str** | Borrowing amount | 
**collateral_currencies** | [**list[CollateralCurrency]**](CollateralCurrency.md) | Collateral currency and amount | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


