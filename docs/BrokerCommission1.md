# BrokerCommission1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission_time** | **int** | Commission time (Unix timestamp in seconds) | [optional] 
**user_id** | **int** | User ID | [optional] 
**group_name** | **str** | Group name | [optional] 
**amount** | **str** | The amount of commission rebates | [optional] 
**fee** | **str** | Fee | [optional] 
**fee_asset** | **str** | Fee currency | [optional] 
**rebate_fee** | **str** | The income from rebates, converted to USDT | [optional] 
**source** | **str** | Commission transaction type: Spot, Futures, Options, Alpha | [optional] 
**currency_pair** | **str** | Currency pair | [optional] 
**sub_broker_info** | [**BrokerCommissionSubBrokerInfo**](BrokerCommissionSubBrokerInfo.md) |  | [optional] 
**alpha_contract_addr** | **str** | Alpha contract address | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


