# Transfer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | Transfer currency. For futures account, &#x60;currency&#x60; can be set to &#x60;POINT&#x60; or settle currency | 
**_from** | **str** | Account transferred from. &#x60;spot&#x60; - spot account. &#x60;margin&#x60; - margin account, &#x60;futures&#x60; - futures account | 
**to** | **str** | Account transferred to. &#x60;spot&#x60; - spot account. &#x60;margin&#x60; - margin account, &#x60;futures&#x60; - futures account | 
**amount** | **str** | Transfer amount | 
**currency_pair** | **str** | Margin currency pair. Required if transfer from or to margin account | [optional] 
**settle** | **str** | Futures settle currency. Required if &#x60;currency&#x60; is &#x60;POINT&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


