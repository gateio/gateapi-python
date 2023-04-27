# CrossMarginBalance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **str** | Available amount | [optional] 
**freeze** | **str** | Locked amount | [optional] 
**borrowed** | **str** | Borrowed amount | [optional] 
**interest** | **str** | Unpaid interests | [optional] 
**negative_liab** | **str** | Negative Liabilities. Formula:Min[available+total+unrealized_pnl,0] | [optional] 
**futures_pos_liab** | **str** | Borrowing to Open Positions in Futures | [optional] 
**equity** | **str** | Equity. Formula: available + freeze - borrowed + total + unrealized_pnl | [optional] 
**total_freeze** | **str** | Total freeze. Formula: position_initial_margin + order_margin | [optional] 
**total_liab** | **str** | Total liabilities. Formula: Max[Abs[Min[quity - total_freeze,0], borrowed]] - futures_pos_liab | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


