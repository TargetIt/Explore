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

def xiaoheGet(interval, length, untilTime):
    strData = HuobiService.getKLineData(interval, length)
    jsonData = json.loads(strData)
    dataArray = []
    for kPoint in jsonData:
        # 存储收盘价信息
        dataArray.append(kPoint[4])
    return dataArray

def xiaoheSync():
    strData = HuobiService.getAccountInfo(ACCOUNT_INFO)
#    print(strData)
    jsonData = json.loads(strData)
    return (
          float(jsonData['available_cny_display']),
          float(jsonData['available_btc_display']),
          float(jsonData['frozen_cny_display']),
          float(jsonData['frozen_btc_display'])
          )
    
    #result 结构 {"result":"success","id":4176799006}
def hanxin(tradeType, amount='', price=''):
    response = None
    if(tradeType == 'buy'):
        if(price):
            response = HuobiService.buy(1,price,amount,None,None,BUY)
        else:
            response = HuobiService.buyMarket(1,amount,None,None,BUY_MARKET)
    else:
        if(price):
            response = HuobiService.sell(1,price,amount,None,None,SELL)
        else:
            response = HuobiService.sellMarket(1,amount,None,None,SELL_MARKET)
    result = json.loads(response)
    print(result['result'],result['id'])
    if(result['result'] == 'success'):
        return (True, result['id'])
    else:
        return (False, '0')
   
#   状态　0未成交　1部分成交　2已完成　3已取消    
def checkFullSuccess(orderId):
    result = HuobiService.getOrderInfo(1,orderId,ORDER_INFO)
    result = json.loads(result)
    if(result['status'] == 2):
        return True
    else:
        return False

def cancelFreezedOrder(orderId):
    result = HuobiService.cancelOrder(1,orderId,CANCEL_ORDER)
    result - json.loads(result)
    if(result['result'] == 'success'):
        return True
    else:
        return False

def test_huobi():
#    xiaoheGet()
#     xiaoheSync()
#     hanxin('buy', '0.01', '70')
#    print ("获取实时行情数据")
#    print(HuobiService.getRealtimeMarket())
#    print ("深度数据接口")
#    print(HuobiService.getDepthData())
#    print ("分时行情数据接口（K线）")
#    print(HuobiService.getKLineData("015"))
#    print ("买卖盘实时成交数据")
#    print(HuobiService.getRealtimeTradeData())
#    print ("获取账号详情")
#    print (HuobiService.getAccountInfo(ACCOUNT_INFO))
#    print ("获取所有正在进行的委托")
#    print (HuobiService.getOrders(1,GET_ORDERS))
    print ("获取订单详情")
    print (HuobiService.getOrderInfo(1,4176812565,ORDER_INFO))
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
    print ("取消订单接口")
    print (HuobiService.cancelOrder(1,4176812565,CANCEL_ORDER))   
if __name__ == "__main__":
    test_huobi()




