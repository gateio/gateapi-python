# MyFuturesTrade

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Trade ID. | [optional] 
**create_time** | **float** | Trading time. | [optional] 
**contract** | **str** | Futures contract. | [optional] 
**order_id** | **str** | Order ID related. | [optional] 
**size** | **int** | Trading size. | [optional] 
**close_size** | **int** | Number of closed positions:  close_size&#x3D;0 &amp;&amp; size＞0 Open long position close_size&#x3D;0 &amp;&amp; size＜0 Open short position close_size&gt;0 &amp;&amp; size&gt;0 &amp;&amp; size &lt;&#x3D; close_size Close &gt; close_size Close short position and open long position close_size&lt;0 &amp;&amp; size&lt;0 &amp;&amp; size &gt;&#x3D; close_size Close long postion close_size&lt;0 &amp;&amp; size&lt;0 &amp;&amp; size &lt; close_size Close long position and open short position | [optional] 
**price** | **str** | Trading price. | [optional] 
**role** | **str** | Trade role. Available values are &#x60;taker&#x60; and &#x60;maker&#x60;. | [optional] 
**text** | **str** | User defined information. | [optional] 
**fee** | **str** | Fee deducted. | [optional] 
**point_fee** | **str** | Points used to deduct fee. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


