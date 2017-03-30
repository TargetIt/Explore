#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8
#客户端调用，用于查看API返回结果
import json

from okcoinApi.OkcoinSpotAPI import OKCoinSpot
import keyInfo as keyInfo
#初始化apikey，secretkey,url
apikey = keyInfo.okCoinApiKey
secretkey = keyInfo.okCoinSecretKey
okcoinRESTURL = 'www.okcoin.cn'   #请求注意：国内账号需要 修改为 www.okcoin.cn  

#现货API
okcoinSpot = OKCoinSpot(okcoinRESTURL,apikey,secretkey)

def xiaoheSync():
    userinfo_str = okcoinSpot.userinfo()
    userinfo = json.loads(userinfo_str)
    return (
    float(userinfo['info']['funds']['free']['cny']),
    float(userinfo['info']['funds']['free']['btc']),
    float(userinfo['info']['funds']['freezed']['cny']),
    float(userinfo['info']['funds']['freezed']['btc'])
    )
    
def xiaoheGet(smpPeriod, smpLen, smpUntil=''):
    rsp = okcoinSpot.kline('btc_cny',smpPeriod, smpLen)
    
    rsp = [rsp[i][-2] for i in range(len(rsp))]
    return rsp

  #result 结构 {"result":"success","id":4176799006}
def hanxin(tradeType, amount='', price=''):
    rsp = okcoinSpot.trade('btc_cny', tradeType, price, amount)
    rsp = json.loads(rsp)
    if rsp['result'] is "true":
        return (True, rsp["order_id"])
    else:
        return (False, 0)
 
#   status:-1:已撤销  0:未成交  1:部分成交  2:完全成交 4:撤单处理中    
def checkFullSuccess(orderId):
    result = okcoinSpot.orderinfo('btc_cny', orderId)
    result = json.loads(result)
    orderInfo = result['orders'][0]
    if(orderInfo['status'] == 2):
        return True
    else:
        return False

def cancelFreezedOrder(orderId):
    result = okcoinSpot.cancelOrder('btc_cny',orderId)
    result = json.loads(result)
    return result['result']

def test_ok():
    
#    print (u' 现货行情 ')
#    print (okcoinSpot.ticker('btc_cny'))
#    
#    print (u' 现货深度 ')
#    print (okcoinSpot.depth('btc_cny'))
    
#    print (u' 现货历史交易信息 ')
#    print (okcoinSpot.trades())
    
#    print (u' 获取K线交易数据 ')
#    print (okcoinSpot.kline('btc_cny','3min', 5))
    
    print (u' 用户现货账户信息 ')
    print (okcoinSpot.userinfo())
     
#    print (u' 现货下单 ')
#    print (okcoinSpot.trade('btc_cny','buy','6998','0.01'))
    
    #print (u' 现货批量下单 ')
    #print (okcoinSpot.batchTrade('btc_cny','buy','[{price:0.1,amount:0.2},{price:0.1,amount:0.2}]'))
    
#    print (u' 现货取消订单 ')
#    print (okcoinSpot.cancelOrder('btc_cny','8552036127'))
    
    print (u' 现货订单信息查询 ')
    print (okcoinSpot.orderinfo('btc_cny','8552036127'))
    
    #print (u' 现货批量订单信息查询 ')
    #print (okcoinSpot.ordersinfo('btc_cny','18243800,18243801,18243644','0'))
    
#    print (u' 现货历史订单信息查询 ')
#    print (okcoinSpot.orderHistory('btc_cny','0','1','2'))
    
    #print (u' 期货行情信息')
    #print (okcoinFuture.future_ticker('btc_cny','this_week'))
    
    #print (u' 期货市场深度信息')
    #print (okcoinFuture.future_depth('btc_cny','this_week','6'))
    
    #print (u'期货交易记录信息') 
    #print (okcoinFuture.future_trades('btc_cny','this_week'))
    
    #print (u'期货指数信息')
    #print (okcoinFuture.future_index('btc_cny'))
    
    #print (u'美元人民币汇率')
    #print (okcoinFuture.exchange_rate())
    
    #print (u'获取预估交割价') 
    #print (okcoinFuture.future_estimated_price('btc_cny'))
    
    #print (u'获取全仓账户信息')
    #print (okcoinFuture.future_userinfo())
    
    #print (u'获取全仓持仓信息')
    #print (okcoinFuture.future_position('btc_cny','this_week'))
    
    #print (u'期货下单')
    #print (okcoinFuture.future_trade('btc_cny','this_week','0.1','1','1','0','20'))
    
    #print (u'期货批量下单')
    #print (okcoinFuture.future_batchTrade('btc_cny','this_week','[{price:0.1,amount:1,type:1,match_price:0},{price:0.1,amount:3,type:1,match_price:0}]','20'))
    
    #print (u'期货取消订单')
    #print (okcoinFuture.future_cancel('btc_cny','this_week','47231499'))
    
    #print (u'期货获取订单信息')
    #print (okcoinFuture.future_orderinfo('btc_cny','this_week','47231812','0','1','2'))
    
    #print (u'期货逐仓账户信息')
    #print (okcoinFuture.future_userinfo_4fix())
    
    #print (u'期货逐仓持仓信息')
    #print (okcoinFuture.future_position_4fix('btc_cny','this_week',1))

if __name__ == "__main__":
    test_ok()
#    print (xiaoheSync())
#    a=xiaoheGet('5min', 500)
#    print (u' 获取K线交易数据 ')
#    print (okcoinSpot.kline('btc_cny','3min', 2))
#    print (u' 现货下单 ')
#    print (okcoinSpot.trade('btc_cny','buy','0.01','0.2'))
#    print (u' 现货行情 ')
#    print (okcoinSpot.ticker('btc_cny'))
    
#    print (u' 现货订单信息查询 ')
#    print (okcoinSpot.orderinfo('btc_cny','8502392117'))

       