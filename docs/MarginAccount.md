# MarginAccount

Margin account detail. `base` refers to base currency, while `quotes to quote currency
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_pair** | **str** | Currency pair. | [optional] 
**account_type** | **str** | Account type, risk - risk rate account, mmr - maintenance margin market not activated | [optional] 
**leverage** | **str** | User current market leverage multiple. | [optional] 
**locked** | **bool** | Whether account is locked. | [optional] 
**risk** | **str** | Leveraged Account Current Risk Rate (Returned when the Account is a Risk Rate Account) | [optional] 
**mmr** | **str** | Leveraged Account Current Maintenance Margin Rate (returned when the Account is Account) | [optional] 
**base** | [**MarginAccountCurrency**](MarginAccountCurrency.md) |  | [optional] 
**quote** | [**MarginAccountCurrency**](MarginAccountCurrency.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


