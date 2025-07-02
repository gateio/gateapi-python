# UnifiedAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] 
**refresh_time** | **int** | Time of the most recent refresh | [optional] 
**locked** | **bool** | Whether the account is locked, valid in cross-currency margin/combined margin mode, false in other modes such as single-currency margin mode | [optional] 
**balances** | [**dict(str, UnifiedBalance)**](UnifiedBalance.md) |  | [optional] 
**total** | **str** | Total account assets converted to USD, i.e. the sum of &#x60;(available + freeze) * price&#x60;  in all currencies (deprecated, to be deprecated, replaced by unified_account_total) | [optional] 
**borrowed** | **str** | The total borrowed amount of the account converted into USD, i.e. the sum of &#x60;borrowed * price&#x60; of all currencies (excluding Point Cards). It is valid in cross-currency margin/combined margin mode, and is 0 in other modes such as single-currency margin mode. | [optional] 
**total_initial_margin** | **str** | Total initial margin, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**total_margin_balance** | **str** | Total margin balance, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**total_maintenance_margin** | **str** | Total maintenance margin is valid in cross-currency margin/combined margin mode, and is 0 in other modes such as single-currency margin mode | [optional] 
**total_initial_margin_rate** | **str** | Total initial margin rate, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**total_maintenance_margin_rate** | **str** | Total maintenance margin rate, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**total_available_margin** | **str** | Available margin amount, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**unified_account_total** | **str** | Unify the total account assets, valid in single currency margin/cross-currency margin/combined margin mode | [optional] 
**unified_account_total_liab** | **str** | Unify the total loan of the account, valid in the cross-currency margin/combined margin mode, and 0 in other modes such as single-currency margin mode | [optional] 
**unified_account_total_equity** | **str** | Unify the total account equity, valid in single currency margin/cross-currency margin/combined margin mode | [optional] 
**leverage** | **str** | Actual leverage, valid in cross-currency margin/combined margin mode | [optional] [readonly] 
**spot_order_loss** | **str** | Total pending order loss, in USDT, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**spot_hedge** | **bool** | Spot hedging status, true - enabled, false - not enabled. | [optional] 
**use_funding** | **bool** | Whether to use funds as margin | [optional] 
**is_all_collateral** | **bool** | 是否所有币种均作为保证金，true - 所有币种作为保证金，false - 否 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


