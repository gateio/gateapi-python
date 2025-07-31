# UnifiedAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] 
**refresh_time** | **int** | Last refresh time | [optional] 
**locked** | **bool** | Whether the account is locked, valid in cross-currency margin/combined margin mode, false in other modes such as single-currency margin mode | [optional] 
**balances** | [**dict(str, UnifiedBalance)**](UnifiedBalance.md) |  | [optional] 
**total** | **str** | Total account assets converted to USD, i.e. the sum of &#x60;(available + freeze) * price&#x60; in all currencies (deprecated, to be removed, replaced by unified_account_total) | [optional] 
**borrowed** | **str** | Total borrowed amount converted to USD, i.e. the sum of &#x60;borrowed * price&#x60; of all currencies (excluding point cards), valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**total_initial_margin** | **str** | Total initial margin, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**total_margin_balance** | **str** | Total margin balance, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**total_maintenance_margin** | **str** | Total maintenance margin is valid in cross-currency margin/combined margin mode, and is 0 in other modes such as single-currency margin mode | [optional] 
**total_initial_margin_rate** | **str** | Total initial margin rate, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**total_maintenance_margin_rate** | **str** | Total maintenance margin rate, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**total_available_margin** | **str** | Available margin amount, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**unified_account_total** | **str** | Total unified account assets, valid in single currency margin/cross-currency margin/combined margin mode | [optional] 
**unified_account_total_liab** | **str** | Total unified account borrowed amount, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**unified_account_total_equity** | **str** | Total unified account equity, valid in single currency margin/cross-currency margin/combined margin mode | [optional] 
**leverage** | **str** | Actual leverage ratio, valid in cross-currency margin/combined margin mode | [optional] [readonly] 
**spot_order_loss** | **str** | Total pending order loss, in USDT, valid in cross-currency margin/combined margin mode, 0 in other modes such as single-currency margin mode | [optional] 
**spot_hedge** | **bool** | Spot hedging status: true - enabled, false - disabled | [optional] 
**use_funding** | **bool** | Whether to use Earn funds as margin | [optional] 
**is_all_collateral** | **bool** | Whether all currencies are used as margin: true - all currencies as margin, false - no | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


