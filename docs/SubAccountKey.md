# SubAccountKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] [readonly] 
**mode** | **int** | Mode: 1 - classic 2 - portfolio account | [optional] 
**name** | **str** | API Key Name | [optional] 
**perms** | [**list[SubAccountKeyPerms]**](SubAccountKeyPerms.md) |  | [optional] 
**ip_whitelist** | **list[str]** | IP whitelist (list will be cleared if no value is passed) | [optional] 
**key** | **str** | API Key | [optional] [readonly] 
**state** | **int** | Status: 1-Normal 2-Frozen 3-Locked | [optional] [readonly] 
**created_at** | **int** | Created time | [optional] [readonly] 
**updated_at** | **int** | Last Update Time | [optional] [readonly] 
**last_access** | **int** | Last Access Time | [optional] [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


