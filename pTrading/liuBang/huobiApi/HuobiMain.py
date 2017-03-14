#coding=utf-8

'''
本程序在 Python 3.3.0 环境下测试成功
使用方法：python HuobiMain.py
'''
#import huobiApi.Util as Util
import json
import huobiApi.HuobiService as HuobiService

ACCOUNT_INFO = "get_account_info"
GET_ORDERS = "get_orders"
ORDER_INFO = "order_info"
BUY = "buy"
BUY_MARKET = "buy_market"
CANCEL_ORDER = "cancel_order"
NEW_DEAL_ORDERS = "get_new_deal_orders"
ORDER_ID_BY_TRADE_ID = "get_order_id_by_trade_id"
SELL = "sell"
SELL_MARKET = "sell_market"

def xiaoheGet():
    strData = HuobiService.getKLineData("015")
    jsonData = json.loads(strData)
    dataDic = {}
    for kPoint in jsonData:
        # 存储收盘价信息
        dataDic[kPoint[0]] = kPoint[4]
    return dataDic

def test_huobi():
#    print ("获取实时行情数据")
#    print(HuobiService.getRealtimeMarket())
#    print ("深度数据接口")
#    print(HuobiService.getDepthData())
    print ("分时行情数据接口（K线）")
    print(HuobiService.getKLineData("015"))
#    print ("买卖盘实时成交数据")
#    print(HuobiService.getRealtimeTradeData())
#    print ("获取账号详情")
#    print (HuobiService.getAccountInfo(ACCOUNT_INFO))
#    print ("获取所有正在进行的委托")
#    print (HuobiService.getOrders(1,GET_ORDERS))
#    print ("获取订单详情")
#    print (HuobiService.getOrderInfo(1,68278313,ORDER_INFO))
#    print ("限价买入")
#    print (HuobiService.buy(1,"1","0.01",None,None,BUY))
#    print ("限价卖出")
#    print (HuobiService.sell(2,"100","0.2",None,None,SELL))
#    print ("市价买入")
#    print (HuobiService.buyMarket(2,"30",None,None,BUY_MARKET))
#    print ("市价卖出")
#    print (HuobiService.sellMarket(2,"1.3452",None,None,SELL_MARKET))
#    print ("查询个人最新10条成交订单")
#    print (HuobiService.getNewDealOrders(1,NEW_DEAL_ORDERS))
#    print ("根据trade_id查询order_id")
#    print (HuobiService.getOrderIdByTradeId(1,274424,ORDER_ID_BY_TRADE_ID))
#    print ("取消订单接口")
#    print (HuobiService.cancelOrder(1,68278313,CANCEL_ORDER))   
if __name__ == "__main__":
    test_huobi()



