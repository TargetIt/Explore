# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 23:19:38 2017

@author: Hpeng
"""

## hubi
#from Util import *
#import HuobiService

## ok
#from OkcoinSpotAPI import OKCoinSpot
#from OkcoinFutureAPI import OKCoinFuture

# PTrading


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
    global ok_account
    global hb_account
    ok_account = my_account(0,0,0.003)
    hb_account = my_account(0,0,0.003)

if __name__ == "__main__":
    """This is main"""
    Initialization()
    if True:
        print(ok_account.Fee)
        print(hb_account.Fee)
    #while True:
        #pass
        # Get data，xiaoHe
        # Update repository, xiaoHe
        # Cal oppotunity, zhangLiang
        # Excute the decision, hanXin