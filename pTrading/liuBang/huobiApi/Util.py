#coding=utf-8
import hashlib
import time
import urllib
import urllib.parse  
import urllib.request 

import keyInfo 


#在此输入您的Key
ACCESS_KEY = keyInfo.huobiAccessKey
SECRET_KEY = keyInfo.huobiSecretKey
HUOBI_SERVICE_API="https://api.huobi.com/apiv3"


'''
发送信息到api
'''
def send2api(pParams, extra):
	pParams['access_key'] = ACCESS_KEY
	pParams['created'] = int(time.time())
	pParams['sign'] = createSign(pParams)
	if(extra) :
		for k in extra:
			v = extra.get(k)
			if(v != None):
				pParams[k] = v
		#pParams.update(extra)
	tResult = httpPostRequest(HUOBI_SERVICE_API, pParams)
	return tResult

'''
生成签名
'''
def createSign(params):
	params['secret_key'] = SECRET_KEY;
	params = sorted(params.items(), key=lambda d:d[0], reverse=False)
	message = urllib.parse.urlencode(params)
	message=message.encode(encoding='UTF8')
	m = hashlib.md5()
	m.update(message)
	m.digest()
	sig=m.hexdigest()
	return sig

'''
request
'''
def httpPostRequest(url, params):
	postdata = urllib.parse.urlencode(params)
	postdata = postdata.encode('utf-8')

	fp = urllib.request.urlopen(url, postdata)
	if fp.status != 200 :
		return None
	else:
		mybytes = fp.read()
		mystr = mybytes.decode("utf8")
		fp.close()
		return mystr
    
'''
get request
'''
def httpGetRequest(url, paramStr):
    fp = urllib.request.urlopen(url + paramStr)
    if fp.status != 200 :
        return None
    else:
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        return mystr



