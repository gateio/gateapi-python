# SubAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remark** | **str** | Remark | [optional] 
**login_name** | **str** | 子账户登陆名：仅支持字母、数字、下划线，不可包含其他非法字符。 | 
**password** | **str** | The sub-account&#39;s password. (Default: the same as main account&#39;s password) | [optional] 
**email** | **str** | The sub-account&#39;s email address. (Default: the same as main account&#39;s email address) | [optional] 
**state** | **int** | Sub-account status: 1-normal, 2-locked | [optional] [readonly] 
**type** | **int** | Sub-account type: 1-Regular sub-account, 3-Cross margin sub-account | [optional] [readonly] 
**user_id** | **int** | Sub-account user ID | [optional] [readonly] 
**create_time** | **int** | Created time | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


