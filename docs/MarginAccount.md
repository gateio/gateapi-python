# MarginAccount

Margin account information for a trading pair. `base` corresponds to base currency account information, `quote` corresponds to quote currency account information
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_pair** | **str** | Currency pair | [optional] 
**account_type** | **str** | Account type: risk - risk rate account, mmr - maintenance margin rate account, inactive - market not activated | [optional] 
**leverage** | **str** | User&#39;s current market leverage multiplier | [optional] 
**locked** | **bool** | Whether the account is locked | [optional] 
**risk** | **str** | Current risk rate of the margin account (returned when the account is a risk rate account) | [optional] 
**mmr** | **str** | Leveraged Account Current Maintenance Margin Rate (returned when the Account is Account) | [optional] 
**base** | [**MarginAccountCurrency**](MarginAccountCurrency.md) |  | [optional] 
**quote** | [**MarginAccountCurrency**](MarginAccountCurrency.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


