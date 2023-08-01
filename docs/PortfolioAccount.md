# PortfolioAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] 
**refresh_time** | **int** | Time of the most recent refresh | [optional] 
**locked** | **bool** | Whether account is locked | [optional] 
**balances** | [**dict(str, PortfolioMarginBalance)**](PortfolioMarginBalance.md) |  | [optional] 
**total** | **str** | Total account value in USDT, i.e., the sum of all currencies&#39; | [optional] 
**borrowed** | **str** | Total borrowed value in USDT, i.e., the sum of all currencies | [optional] 
**interest** | **str** | Total unpaid interests in USDT, i.e., the sum of all currencies | [optional] 
**total_initial_margin** | **str** | Total initial margin | [optional] 
**total_margin_balance** | **str** | Total margin balance | [optional] 
**total_maintenance_margin** | **str** | Total maintenance margin | [optional] 
**total_initial_margin_rate** | **str** | Total initial margin rate | [optional] 
**total_maintenance_margin_rate** | **str** | Total maintenance margin rate | [optional] 
**total_available_margin** | **str** | Total available margin | [optional] 
**portfolio_margin_total** | **str** | Total amount of the portfolio margin account | [optional] 
**portfolio_margin_total_liab** | **str** | Total liabilities of the portfolio margin account | [optional] 
**portfolio_margin_total_equity** | **str** | Total equity of the portfolio margin account | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


