#coding:utf-8
'''
Created on 2017年5月18日

@author: Administrator
'''
# import  httplib2
#coding=utf8
 
import httplib, urllib
import urlparse
httpClient = None
# import stringprint(string.__file__)
import time
import datetime
import sys
def urlhead():
    filename=open('head.txt','w')
    params = urllib.urlencode({'name': 'tom', 'age': 22})
    headers = {"Content-type": "application/x-www-form-urlencoded"
                    , "Accept": "text/plain"
                    ,"connection":"close"
                    ,"Content-Encoding":"gzip"}
#     with open('test.txt') as f:
#         for i in f.read().split('\n'):
    i="http://ww4.sinaimg.cn/large/0064cTs2jw1exnxmw4ffij30os0ffwtl.jpg"
    if 'http://' in i:
        url=i
    else:
        url='http://'+i
     
    urlp=urlparse.urlparse(url)
    host=urlp.hostname
    port=(urlp.port if urlp.port!=None else 80)
    print host,port
    getcontentype(host,port,url,params,headers)
def getcontentype(host,port,url,params,headers):
        try:
            httpClient = httplib.HTTPConnection(host, port)
            #发出同步请求，并获取内容  
        #     resp, content = h.request("http://www.soso.com/")  
        #     print resp  
        #     print content 
            httpClient.request("GET",url,body=params, headers=headers)
            time.sleep(20)
            response = httpClient.getresponse()
            print response
            time.sleep(20)
            httpClient.body
            print sys.getsizeof(httpClient)
        #     print response.status
        #     print response.reason
        #     response.read()
    #         print type(response.getheaders())
            for i in response.getheaders():
                print i[0]
                if str(i[0]).lower()=='content-type':
                    print i[1]
#                     filename.write(url+" : "+str(i[1])+'\n')
         #获取头信息
#             print response.strict
        except Exception, e:
            print e
if __name__=="__main__":
    import cProfile
    cProfile.run("urlhead()")