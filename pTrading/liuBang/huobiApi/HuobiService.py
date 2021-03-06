#coding=utf-8
import huobiApi.Util as Util


HUOBI_VIEW_API="http://api.huobi.com/staticmarket";

'''
获取实时行情
'''
def getRealtimeMarket():
    res = Util.httpGetRequest(HUOBI_VIEW_API, "/ticker_btc_json.js")
    return res

'''
深度数据接口
'''
def getDepthData():
    res = Util.httpGetRequest(HUOBI_VIEW_API, "/depth_btc_json.js")
    return res

'''
分时行情数据接口（K线）
'''
def getKLineData(period, length):
    res = Util.httpGetRequest(HUOBI_VIEW_API, "/btc_kline_" + period + "_json.js?length=" + str(length))
    return res

'''
买卖盘实时成交数据
'''
def getRealtimeTradeData():
    res = Util.httpGetRequest(HUOBI_VIEW_API, "/detail_btc_json.js")
    return res


'''
行情和交易API分界线-------------------------------------------
'''

'''
获取账号详情
'''
def getAccountInfo(method):
	params = {"method":method}
	extra = {}
	res = Util.send2api(params, extra)
	return res
'''
获取所有正在进行的委托
'''
def getOrders(coinType,method):
	params = {"method":method}
	params['coin_type'] = coinType
	extra = {}
	res = Util.send2api(params, extra)
	return res
'''
获取订单详情
@param coinType
@param id
'''
def getOrderInfo(coinType,id,method):
	params = {"method":method}
	params['coin_type'] = coinType
	params['id'] = id
	extra = {}
	res = Util.send2api(params, extra)
	return res

'''
限价买入
@param coinType
@param price
@param amount
@param tradePassword
@param tradeid
@param method
'''
def buy(coinType,price,amount,tradePassword,tradeid,method):
	params = {"method":method}
	params['coin_type'] = coinType
	params['price'] = price
	params['amount'] = amount
	extra = {}
	extra['trade_password'] = tradePassword
	extra['trade_id'] = tradeid
	res = Util.send2api(params, extra)
	return res

'''
限价卖出
@param coinType
@param price
@param amount
@param tradePassword
@param tradeid
'''
def sell(coinType,price,amount,tradePassword,tradeid,method):
	params = {"method":method}
	params['coin_type'] = coinType
	params['price'] = price
	params['amount'] = amount
	extra = {}
	extra['trade_password'] = tradePassword
	extra['trade_id'] = tradeid
	res = Util.send2api(params, extra)
	return res


'''
市价买
@param coinType
@param amount
@param tradePassword
@param tradeid
'''

def buyMarket(coinType,amount,tradePassword,tradeid,method):
	params = {"method":method}
	params['coin_type'] = coinType
	params['amount'] = amount
	extra = {}
	extra['trade_password'] = tradePassword
	extra['trade_id'] = tradeid
	res = Util.send2api(params, extra)
	return res

'''
市价卖出
@param coinType
@param amount
@param tradePassword
@param tradeid
'''
def sellMarket(coinType,amount,tradePassword,tradeid,method):
	params = {"method":method}
	params['coin_type'] = coinType
	params['amount'] = amount
	extra = {}
	extra['trade_password'] = tradePassword
	extra['trade_id'] = tradeid
	res = Util.send2api(params, extra)
	return res

'''
查询个人最新10条成交订单
@param coinType
'''
def getNewDealOrders(coinType,method):
	params = {"method":method}
	params['coin_type'] = coinType
	extra = {}
	res = Util.send2api(params, extra)
	return res
'''
根据trade_id查询oder_id
@param coinType
@param tradeid
'''
def getOrderIdByTradeId(coinType,tradeid,method):
	params = {"method":method}
	params['coin_type'] = coinType
	params['trade_id'] = tradeid
	extra = {}
	res = Util.send2api(params, extra)
	return res


'''
撤销订单
@param coinType
@param id
'''

def cancelOrder(coinType,id,method):
	params = {"method":method}
	params['coin_type'] = coinType
	params['id'] = id
	extra = {}
	res = Util.send2api(params, extra)
	return res

