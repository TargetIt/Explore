# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 23:19:38 2017

@author: Hpeng
"""
# In[ ]:
import time
from okcoinApi import Client as okp
import huobiApi.HuobiMain as hbp
# PTrading
import pTrading as pts
import logger


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
    def xiaoheSync(self, cny_fr, btc_fr, cny_fz, btc_fz):
        self.cny_fr = cny_fr
        self.btc_fr = btc_fr
        self.cny_fz = cny_fz
        self.btc_fz = btc_fz
    def display(self):
        print (self.cny_fr, self.btc_fr, self.cny_fz, self.btc_fz)

# In[ ]:

def Initialization():
    global ok_account
    global hb_account
    global ok_data
    global hb_data
    # create mirror account
    ok_account = my_account(0,0,0,0,0.003)
    hb_account = my_account(0,0,0,0,0.003)
    # test okcoin platform

    # test hbcoin platform

    # update ok platform mirror repository
    ok_account.xiaoheSync(*okp.xiaoheSync())
    # update hb platform mirror repository
    hb_account.xiaoheSync(*hbp.xiaoheSync())
    # get enough history data of ok platform
    timeInt = time.time() * 1000
    ok_data = okp.xiaoheGet('5min', 50, timeInt)
    # get enough history data of hb platform
    hb_data = hbp.xiaoheGet('005',50, timeInt)
if __name__ == "__main__":
    """This is main"""
    Initialization()
    
    if True:
        #pass
        ok_account.display()
        # Get data, xiaoHe
        theTime = time.time() * 1000
        ok_data = okp.xiaoheGet('5min', 50, theTime)
        hb_data = hbp.xiaoheGet('005', 50, theTime)
        # Update repository, xiaoHe
        ok_account.xiaoheSync(*okp.xiaoheSync())
        hb_account.xiaoheSync(*hbp.xiaoheSync())
        # Cal oppotunity, zhangLiang
        cmd1, cmd2 = pts.zhangliang(ok_account, hb_account, ok_data, hb_data)
        # Excute the decision, hanXin(tradeType, price, amount)
        if cmd1 and cmd2:
            okResult = okp.hanxin(*cmd1)
            hbResult = hbp.hanxin(*cmd2)
            logger.info(okResult)
            logger.info(hbResult)
        else:
            logger.info('no buy or sell this time')

