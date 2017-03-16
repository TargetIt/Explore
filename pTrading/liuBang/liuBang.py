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
    def __init__(self, cny_fr, btc_fr, cny_fz, btc_fz, rate):
        self.cny_fr = cny_fr
        self.btc_fr = btc_fr
        self.cny_fz = cny_fz
        self.btc_fz = btc_fz
        self.rate = rate
        self.state = "even"
        self.BuyPrice = 8000
    def order_taget(self, cny, btc):
        self.cny_fr += cny
        self.btc_fr += btc
    def sync(self, cny_fr, btc_fr, cny_fz, btc_fz):
        self.cny_fr = cny_fr
        self.btc_fr = btc_fr
        self.cny_fz = cny_fz
        self.btc_fz = btc_fz

# In[ ]:

def Initialization():
    # create mirror account
    global ok_account
    global hb_account
    ok_account = my_account(0,0,0,0,0.003)
    hb_account = my_account(0,0,0,0,0.003)
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
        print(ok_account.rate)
        print(hb_account.rate)
    #while True:
        #pass
        # Get data, xiaoHe
        # Update repository, xiaoHe
        # Cal oppotunity, zhangLiang
        # Excute the decision, hanXin
        