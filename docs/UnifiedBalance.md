# UnifiedBalance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **str** | Available balance, valid in single currency margin/cross-currency margin/combined margin mode, calculation varies by mode | [optional] 
**freeze** | **str** | Locked balance, valid in single currency margin/cross-currency margin/combined margin mode | [optional] 
**borrowed** | **str** | Borrowed amount, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**negative_liab** | **str** | Negative balance borrowing, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**futures_pos_liab** | **str** | Contract opening position borrowing currency (abandoned, to be offline field) | [optional] 
**equity** | **str** | Equity, valid in single currency margin/cross currency margin/combined margin mode | [optional] 
**total_freeze** | **str** | Total frozen (deprecated, to be removed) | [optional] 
**total_liab** | **str** | Total borrowed amount, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**spot_in_use** | **str** | The amount of spot hedging is valid in the combined margin mode, and is 0 in other margin modes such as single currency and cross-currency margin modes | [optional] 
**funding** | **str** | Uniloan financial management amount, effective when turned on as a unified account margin switch | [optional] 
**funding_version** | **str** | Funding version | [optional] 
**cross_balance** | **str** | Full margin balance is valid in single currency margin mode, and is 0 in other modes such as cross currency margin/combined margin mode | [optional] 
**iso_balance** | **str** | Isolated margin balance is valid in single-currency margin mode and is 0 in other modes such as cross-currency margin/combined margin mode | [optional] 
**im** | **str** | Full-position initial margin is valid in single-currency margin mode and is 0 in other modes such as cross-currency margin/combined margin mode | [optional] 
**mm** | **str** | Cross margin maintenance margin, valid in single-currency margin mode, 0 in other modes such as cross-currency margin/combined margin mode | [optional] 
**imr** | **str** | Full-position initial margin rate is valid in single-currency margin mode and is 0 in other modes such as cross-currency margin/combined margin mode | [optional] 
**mmr** | **str** | Full-position maintenance margin rate is valid in single-currency margin mode and is 0 in other modes such as cross-currency margin/combined margin mode | [optional] 
**margin_balance** | **str** | Full margin balance is valid in single currency margin mode and is 0 in other modes such as cross currency margin/combined margin mode | [optional] 
**available_margin** | **str** | Cross margin available balance, valid in single currency margin mode, 0 in other modes such as cross-currency margin/combined margin mode | [optional] 
**enabled_collateral** | **bool** | Currency enabled as margin: true - Enabled, false - Disabled | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


