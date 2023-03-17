# SubCrossMarginAccount

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** | User ID of the cross margin account. 0 means that the subaccount has not yet opened a cross margin account | [optional] 
**locked** | **bool** | Whether account is locked | [optional] 
**balances** | [**dict(str, CrossMarginBalance1)**](CrossMarginBalance1.md) |  | [optional] 
**total** | **str** | Total account value in USDT, i.e., the sum of all currencies&#39; &#x60;(available+freeze)*price*discount&#x60; | [optional] 
**borrowed** | **str** | Total borrowed value in USDT, i.e., the sum of all currencies&#39; &#x60;borrowed*price*discount&#x60; | [optional] 
**borrowed_net** | **str** | Total borrowed value in USDT * borrowed factor | [optional] 
**net** | **str** | Total net assets in USDT | [optional] 
**leverage** | **str** | Position leverage | [optional] 
**interest** | **str** | Total unpaid interests in USDT, i.e., the sum of all currencies&#39; &#x60;interest*price*discount&#x60; | [optional] 
**risk** | **str** | Risk rate. When it belows 110%, liquidation will be triggered. Calculation formula: &#x60;total / (borrowed+interest)&#x60; | [optional] 
**total_initial_margin** | **str** | Total initial margin | [optional] 
**total_margin_balance** | **str** | Total margin balance | [optional] 
**total_maintenance_margin** | **str** | Total maintenance margin | [optional] 
**total_initial_margin_rate** | **str** | Total initial margin rate | [optional] 
**total_maintenance_margin_rate** | **str** | Total maintenance margin rate | [optional] 
**total_available_margin** | **str** | Total available margin | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


