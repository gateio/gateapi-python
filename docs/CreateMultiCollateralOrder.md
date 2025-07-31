# CreateMultiCollateralOrder

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID | [optional] 
**order_type** | **str** | current - current rate, fixed - fixed rate, defaults to current if not specified | [optional] 
**fixed_type** | **str** | Fixed interest rate lending period: 7d - 7 days, 30d - 30 days. Required for fixed rate | [optional] 
**fixed_rate** | **str** | Fixed interest rate, required for fixed rate | [optional] 
**auto_renew** | **bool** | Fixed interest rate, auto-renewal | [optional] 
**auto_repay** | **bool** | Fixed interest rate, auto-repayment | [optional] 
**borrow_currency** | **str** | Borrowed currency | 
**borrow_amount** | **str** | Borrowed amount | 
**collateral_currencies** | [**list[CollateralCurrency]**](CollateralCurrency.md) | Collateral currency and amount | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


