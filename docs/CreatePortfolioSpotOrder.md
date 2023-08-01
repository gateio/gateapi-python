# CreatePortfolioSpotOrder

Spot order details
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | User defined information. If not empty, must follow the rules below:  1. prefixed with &#x60;t-&#x60; 2. no longer than 28 bytes without &#x60;t-&#x60; prefix 3. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)  Besides user defined information, reserved contents are listed below, denoting how the order is created:  - 101: from android - 102: from IOS - 103: from IPAD - 104: from webapp - 3: from web - 2: from apiv2 - apiv4: from apiv4  | [optional] 
**amend_text** | **str** | The custom data that the user remarked when amending the order | [optional] [readonly] 
**currency_pair** | **str** | Currency pair | 
**type** | **str** | Order Type    - limit : Limit Order - market : Market Order | [optional] [default to 'limit']
**side** | **str** | Order side | 
**amount** | **str** | When &#x60;type&#x60; is limit, it refers to base currency.  For instance, &#x60;BTC_USDT&#x60; means &#x60;BTC&#x60;  When &#x60;type&#x60; is &#x60;market&#x60;, it refers to different currency according to &#x60;side&#x60;  - &#x60;side&#x60; : &#x60;buy&#x60; means quote currency, &#x60;BTC_USDT&#x60; means &#x60;USDT&#x60; - &#x60;side&#x60; : &#x60;sell&#x60; means base currency，&#x60;BTC_USDT&#x60; means &#x60;BTC&#x60;  | 
**price** | **str** | Price can&#39;t be empty when &#x60;type&#x60;&#x3D; &#x60;limit&#x60; | [optional] 
**time_in_force** | **str** | Time in force  - gtc: GoodTillCancelled - ioc: ImmediateOrCancelled, taker only - poc: PendingOrCancelled, makes a post-only order that always enjoys a maker fee - fok: FillOrKill, fill either completely or none Only &#x60;ioc&#x60; and &#x60;fok&#x60; are supported when &#x60;type&#x60;&#x3D;&#x60;market&#x60; | [optional] [default to 'gtc']
**iceberg** | **str** | Amount to display for the iceberg order. Null or 0 for normal orders.  Hiding all amount is not supported. | [optional] 
**auto_borrow** | **bool** | When engaging in margin trading, if the account balance is insufficient, the system will automatically borrow the remaining amount to cover the deficit. | [optional] 
**auto_repay** | **bool** | Enable or disable automatic repayment for automatic borrow loan. Default is disabled. Note that:  &#x60;auto_borrow&#x60; and &#x60;auto_repay&#x60; cannot be both set to true in one order. | [optional] 
**stp_act** | **str** | Self-Trading Prevention Action. Users can use this field to set self-trade prevetion strategies  1. After users join the &#x60;STP Group&#x60;, he can pass &#x60;stp_act&#x60; to limit the user&#39;s self-trade prevetion strategy. If &#x60;stp_act&#x60; is not passed, the default is &#x60;cn&#x60; strategy。 2. When the user does not join the &#x60;STP group&#x60;, an error will be returned when passing the &#x60;stp_act&#x60; parameter。 3. If the user did not use &#39;stp_act&#39; when placing the order, &#39;stp_act&#39; will return &#39;-&#39;  - cn: Cancel newest, Cancel new orders and keep old ones - co: Cancel oldest, Cancel old orders and keep new ones - cb: Cancel both, Both old and new orders will be cancelled | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


