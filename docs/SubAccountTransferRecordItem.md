# SubAccountTransferRecordItem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timest** | **str** | Transfer timestamp | [optional] [readonly] 
**uid** | **str** | Main account user ID | [optional] [readonly] 
**sub_account** | **str** | Sub account user ID | 
**sub_account_type** | **str** | Target sub-account trading account: spot - spot account, futures - perpetual contract account, delivery - delivery contract account, options - options account | [optional] [default to 'spot']
**currency** | **str** | Transfer currency name | 
**amount** | **str** | Transfer amount | 
**direction** | **str** | Transfer direction: to - transfer into sub-account, from - transfer out from sub-account | 
**source** | **str** | Source of the transfer operation | [optional] [readonly] 
**client_order_id** | **str** | Customer-defined ID to prevent duplicate transfers. Can be a combination of letters (case-sensitive), numbers, hyphens &#39;-&#39;, and underscores &#39;_&#39;. Can be pure letters or pure numbers with length between 1-64 characters | [optional] 
**status** | **str** | Sub-account transfer record status, currently only &#39;success&#39; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


