# UnifiedCollateralReq

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collateral_type** | **int** | 用户设置抵押物模式 0(all)-全部币种作为抵押物,1(custom)-自定义币种作为抵押物,collateral_type为0(all)时，enable_list与disable_list参数无效 | [optional] 
**enable_list** | **list[str]** | 币种列表，collateral_type&#x3D;1(custom)表示追加的逻辑 | [optional] 
**disable_list** | **list[str]** | 取消列表，表示取消的逻辑 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


