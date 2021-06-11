# CrossMarginAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID | [optional] 
**locked** | **bool** | Whether account is locked | [optional] 
**balances** | [**dict(str, CrossMarginBalance)**](CrossMarginBalance.md) |  | [optional] 
**total** | **str** | Total account value in USDT, i.e., the sum of all currencies&#39; &#x60;(available+freeze)*price*discount&#x60; | [optional] 
**borrowed** | **str** | Total borrowed value in USDT, i.e., the sum of all currencies&#39; &#x60;borrowed*price*discount&#x60; | [optional] 
**interest** | **str** | Total unpaid interests in USDT, i.e., the sum of all currencies&#39; &#x60;interest*price*discount&#x60; | [optional] 
**risk** | **str** | Risk rate. When it belows 110%, liquidation will be triggered. Calculation formula: &#x60;total / (borrowed+interest)&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


