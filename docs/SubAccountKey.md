# SubAccountKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID | [optional] [readonly] 
**mode** | **int** | Mode: 1 - classic 2 - portfolio account | [optional] 
**name** | **str** | API key name | [optional] 
**perms** | [**list[SubAccountKeyPerms]**](SubAccountKeyPerms.md) |  | [optional] 
**ip_whitelist** | **list[str]** | ip white list (list will be removed if no value is passed) | [optional] 
**key** | **str** | API Key | [optional] [readonly] 
**state** | **int** | State 1 - normal 2 - locked 3 - frozen | [optional] [readonly] 
**created_at** | **int** | Creation time | [optional] [readonly] 
**updated_at** | **int** | Last update time | [optional] [readonly] 
**last_access** | **int** | Last access time | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


