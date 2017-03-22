# -*- coding: utf-8 -*-

# In[3]:

import logging  
import logging.handlers  
import time

dateTime = time.time()  
LOG_FILE = 'logDir\\log' + time.strftime('%Y-%m-%d',time.localtime(time.time())) + '.log'  
  
handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler   
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'  

formatter = logging.Formatter(fmt)   # 实例化formatter  
handler.setFormatter(formatter)      # 为handler添加formatter  
  
logger = logging.getLogger('tst_new')    # 获取名为tst的logger  
         # 为logger添加handler  
logger.setLevel(logging.DEBUG)  

#logging.basicConfig(filename='tst.log', level=logging.DEBUG)
#logger = logging.getLogger('testlog')
#streamhandler = logging.StreamHandler()
#streamhandler.setLevel(logging.DEBUG)
#formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s')
#streamhandler.setFormatter(formatter)

if not len(logger.handlers):
    logger.addHandler(handler)
def info(content):
    #logger.addHandler(handler)  
    logger.info(content)
    #logger.removeHandler(handler)
def debug(content):
    #logger.removeHandler(handler)
    logger.debug(content)
    #logger.removeHandler(handler)
def error(content):    
    logger.error(content)
def critical(content):   
    logger.critical(content)
def warn(content):    
    logger.warn(content)
def loggerList(title, array, level='info'):
    content = title + ': ';
    for item in array:
        content = content + ', ' + str(item)
    if(level == 'info'):
        info(content)
def loggerAccount(title, account, level='info'):
    content = title + ': '
    content += 'cny_fr: ' + str(account.cny_fr) + ', '
    content += 'btc_fr: ' + str(account.btc_fr) + ', '
    content += 'cny_fz: ' + str(account.cny_fz) + ', '
    content += 'btc_fz: ' + str(account.btc_fz) + ', '
    content += 'rate: ' + str(account.rate) + ', '
    content += 'state: ' + str(account.state) + ', '
    content += 'BuyPrice: ' + str(account.BuyPrice) + ', '
    if(level == 'info'):
        info(content)