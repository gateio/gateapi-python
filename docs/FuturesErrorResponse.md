# FuturesErrorResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | 错误标识符，错误描述如下：  请求参数或格式问题:  - INVALID_PARAM_VALUE: 参数输入值无效 - INVALID_REQUEST_BODY: 无效请求体 - MISSING_REQUIRED_PARAM: 缺少必选参数 - DUPLICATE_REQUEST: 请求过于频繁  认证相关:  - INVALID_CREDENTIALS: 认证接口缺少用户认证信息 - NO_FUTURES_ACCOUNT: 用户无期货账户  业务相关:  - NO_MATCHING: 没有匹配的对手单 - NO_MARKING_PRICE: 合约当前无标记价格 - CONTRACT_NOT_FOUND: 合约未找到 - NOT_FOUND: 请求路径不存在 - RISK_LIMIT_EXCEEDED: 委托超出风险限额 - INSUFFICIENT_BALANCE: 余额不足 - POTENTIAL_LIQUIDATION: 操作可能导致爆仓 - LEVERAGE_TOO_HIGH: 杠杆倍数设置过高 - LEVERAGE_TOO_LOW: 杠杆倍数设置过低 - ORDER_NOT_FOUND: 委托不存在 - ORDER_FINISHED: 订单已结束 - TOO_MANY_ORDERS: 过多未交易的挂单 - POSITION_NOT_FOUND: 合约无头寸信息 - POSITION_CROSS_MARGIN: 全仓不支持更新保证金 - POSITION_LOCKED: 头寸当前被锁定 - TOO_MUCH_CHANGE: 保证金超过可调范围 - RISK_LIMIT_NOT_MULTIPLE: 风险限额未按照步长调整 - RISK_LIMIT_TOO_HIGH: 超出最大风险限额 - RISK_LIMIT_TOO_lOW: 风险限额设置过低 - PRICE_TOO_DEVIATED: 下单价与标记价格相差过大 - SIZE_TOO_LARGE: 下单数量超过上限 - SIZE_TOO_SMALL: 下单数量不足下限 - LIQUIDATION_PRICE_EXCEEDED: 补仓时价格不能超过平仓价 - POSITION_IN_CLOSE: 仓位正在平仓 - POTENTIAL_BANKRUPTCY: 下单若成交，保证金无法弥补损失  服务异常： - SERVER_ERROR: 内部错误 - TOO_BUSY: 服务当前忙  | [optional] 
**message** | **str** | 详细错误描述。如果指定了 &#x60;Accept-Language&#x60; 请求头部，且支持指定语言，则描述信息会返回对应的语言  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


