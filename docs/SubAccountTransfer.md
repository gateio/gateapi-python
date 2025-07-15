# SubAccountTransfer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_account** | **str** | Sub account user ID | 
**sub_account_type** | **str** | Target sub user&#39;s account. &#x60;spot&#x60; - spot account, &#x60;futures&#x60; - perpetual contract account, &#x60;delivery&#x60; - delivery account | [optional] [default to 'spot']
**currency** | **str** | Transfer currency name | 
**amount** | **str** | Transfer amount | 
**direction** | **str** | Transfer direction. to - transfer into sub account; from - transfer out from sub account | 
**client_order_id** | **str** | The custom ID provided by the customer serves as a safeguard against duplicate transfers. It can be a combination of letters (case-sensitive), numbers, hyphens &#39;-&#39;, and underscores &#39;_&#39;, with a length ranging from 1 to 64 characters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


