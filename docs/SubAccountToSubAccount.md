# SubAccountToSubAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Transfer currency name | 
**sub_account_type** | **str** | Transfer from the account. (deprecate, use &#x60;sub_account_from_type&#x60; and &#x60;sub_account_to_type&#x60; instead) | [optional] 
**sub_account_from** | **str** | Transfer from the user id of the sub-account | 
**sub_account_from_type** | **str** | Transfer from the account.  &#x60;spot&#x60; - spot account, &#x60;futures&#x60; - perpetual contract account, &#x60;cross_margin&#x60; - cross margin account | 
**sub_account_to** | **str** | Transfer to the user id of the sub-account | 
**sub_account_to_type** | **str** | Transfer to the account.  &#x60;spot&#x60; - spot account, &#x60;futures&#x60; - perpetual contract account, &#x60;cross_margin&#x60; - cross margin account | 
**amount** | **str** | Transfer amount | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


