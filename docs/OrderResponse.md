# OrderResponse

下单返回
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | Order ID | [optional] 
**tx_hash** | **str** | Transaction Hash | [optional] 
**side** | **str** | 买单或者卖单 - buy - sell | [optional] 
**usdt_amount** | **str** | Amount | [optional] 
**currency** | **str** | 币 | [optional] 
**currency_amount** | **str** | Currency amount | [optional] 
**status** | **int** | Order Status - &#x60;0&#x60; : All - &#x60;1&#x60; : Processing - &#x60;2&#x60; : Successful - &#x60;3&#x60; : Failed - &#x60;4&#x60; : Canceled - &#x60;5&#x60; : Buy order placed but transfer not completed - &#x60;6&#x60; : Cancelled order with transfer not complete | [optional] 
**gas_mode** | **str** | Trading mode affects slippage selection - &#x60;speed&#x60; : Smart mode - &#x60;custom&#x60; : Custom mode, uses &#x60;slippage&#x60; parameter | [optional] 
**chain** | **str** | 链 | [optional] 
**gas_fee** | **str** | Miner Fee (USDT-based) | [optional] 
**transaction_fee** | **str** | Trading Fee (USDT-based) | [optional] 
**failed_reason** | **str** | Failure reason (if any) | [optional] 
**create_time** | **int** | 创建时间（时间戳） | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


