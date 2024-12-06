# UnifiedAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] 
**refresh_time** | **int** | Time of the most recent refresh | [optional] 
**locked** | **bool** | Whether account is locked | [optional] 
**balances** | [**dict(str, UnifiedBalance)**](UnifiedBalance.md) |  | [optional] 
**total** | **str** | Total account assets converted to USD, i.e. the sum of &#x60;(available + freeze) * price&#x60;  in all currencies (deprecated, to be deprecated, replaced by unified_account_total) | [optional] 
**borrowed** | **str** | The total borrowed amount in USD, calculated as the sum of the product of &#x60;borrowed * price&#x60; for all currencies (excluding points cards). | [optional] 
**total_initial_margin** | **str** | Total initial margin | [optional] 
**total_margin_balance** | **str** | Total margin balance | [optional] 
**total_maintenance_margin** | **str** | Total maintenance margin | [optional] 
**total_initial_margin_rate** | **str** | Total initial margin rate | [optional] 
**total_maintenance_margin_rate** | **str** | Total maintenance margin rate | [optional] 
**total_available_margin** | **str** | Total available margin | [optional] 
**unified_account_total** | **str** | Total amount of the portfolio margin account | [optional] 
**unified_account_total_liab** | **str** | Total liabilities of the portfolio margin account | [optional] 
**unified_account_total_equity** | **str** | Total equity of the portfolio margin account | [optional] 
**leverage** | **str** | Leverage | [optional] [readonly] 
**spot_order_loss** | **str** | Total order loss, in USDT | [optional] 
**spot_hedge** | **bool** | Spot hedging status, true - enabled, false - not enabled. | [optional] 
**use_funding** | **bool** | Whether to use funds as margin | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


