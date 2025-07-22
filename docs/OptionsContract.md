# OptionsContract

Options contract detail.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Options contract name. | [optional] 
**tag** | **str** | tag. | [optional] 
**create_time** | **float** | Creation time. | [optional] 
**expiration_time** | **float** | Expiration time. | [optional] 
**is_call** | **bool** | &#x60;true&#x60; means call options, while &#x60;false&#x60; is put options. | [optional] 
**multiplier** | **str** | Multiplier used in converting from invoicing to settlement currency. | [optional] 
**underlying** | **str** | Underlying. | [optional] 
**underlying_price** | **str** | Underlying price (quote currency). | [optional] 
**last_price** | **str** | Last trading price. | [optional] 
**mark_price** | **str** | Current mark price (quote currency). | [optional] 
**index_price** | **str** | Current index price (quote currency). | [optional] 
**maker_fee_rate** | **str** | Maker fee rate, where negative means rebate. | [optional] 
**taker_fee_rate** | **str** | Taker fee rate. | [optional] 
**order_price_round** | **str** | Minimum order price increment. | [optional] 
**mark_price_round** | **str** | Minimum mark price increment. | [optional] 
**order_size_min** | **int** | Minimum order size the contract allowed. | [optional] 
**order_size_max** | **int** | Maximum order size the contract allowed. | [optional] 
**order_price_deviate** | **str** | The positive and negative offset allowed between the order price and the current mark price, that &#x60;order_price&#x60; must meet the following conditions:   order_price is within the range of mark_price +/- order_price_deviate * underlying_price and does not distinguish between buy and sell orders | [optional] 
**ref_discount_rate** | **str** | Referral fee rate discount. | [optional] 
**ref_rebate_rate** | **str** | Referrer commission rate. | [optional] 
**orderbook_id** | **int** | Current orderbook ID. | [optional] 
**trade_id** | **int** | Current trade ID. | [optional] 
**trade_size** | **int** | Historical accumulated trade size. | [optional] 
**position_size** | **int** | Current total long position size. | [optional] 
**orders_limit** | **int** | Maximum number of open orders. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


