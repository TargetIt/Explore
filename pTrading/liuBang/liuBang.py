# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 23:19:38 2017

@author: Hpeng
"""
# In[ ]:

from okcoinApi import Client as okp
import huobiApi.HuobiMain as hbp
# PTrading
import pTrading as pts

# In[ ]:

class my_account(object):
    """This is my_account"""
    def __init__(self, RMB, BitCoin, Fee):
        self.RMB = RMB
        self.BitCoin = BitCoin
        self.Fee = Fee
        self.state = "even"
        self.BuyPrice = 8000
    def order_taget(self, RMB, BitCoin):
        self.RMB += RMB
        self.BitCoin += BitCoin

# In[ ]:

def Initialization():
    # create mirror account
    global ok_account
    global hb_account
    ok_account = my_account(0,0,0.003)
    hb_account = my_account(0,0,0.003)
    # test okcoin platform
    print (u' 现货行情 ')
    print (okp.okcoinSpot.ticker('btc_cny'))
    # test hbcoin platform
    print ("获取账号详情")
    print (hbp.HuobiService.getAccountInfo(hbp.ACCOUNT_INFO))
    # update ok platform mirror repository
    
    # update hb platform mirror repository
    
    # get enough history data of ok platform
    
    # get enough history data of hb platform
    huobiData = hbp.xiaoheGet()
if __name__ == "__main__":
    """This is main"""
    Initialization()
    if True:
        print(ok_account.Fee)
        print(hb_account.Fee)
    #while True:
        #pass
        # Get data, xiaoHe
        # Update repository, xiaoHe
        # Cal oppotunity, zhangLiang
        # Excute the decision, hanXin
        