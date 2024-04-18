# UnifiedAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] 
**refresh_time** | **int** | Time of the most recent refresh | [optional] 
**locked** | **bool** | Whether account is locked | [optional] 
**balances** | [**dict(str, UnifiedBalance)**](UnifiedBalance.md) |  | [optional] 
**total** | **str** | The total asset value in USD, calculated as the sum of the product of &#x60;(available + freeze) * price&#x60; for all currencies. | [optional] 
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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


