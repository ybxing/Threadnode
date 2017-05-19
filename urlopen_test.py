
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
import sys
# import stringprint(string.__file__)
import time
import datetime
import urllib2
def urlhead():
    filename=open('head.txt','w')
    params = urllib.urlencode({'name': 'tom', 'age': 22})
    headers = {"Content-type": "application/x-www-form-urlencoded"
                    , "Accept": "text/plain"
                    ,"connection":"close"
                    ,"Content-Encoding":"gzip"}
#     with open('test.txt') as f:
#         
#         for i in f.read().split('\n'):
    i="http://ww4.sinaimg.cn/large/0064cTs2jw1exnxmw4ffij30os0ffwtl.jpg"
    if  'http://' in i:
        url=i
    else:
        url='http://'+i
    print url
    req_header = {
                'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4',
                'Accept':'text/html',
                'Connection':'close'
            }
    try:
        req = urllib2.Request(url,None,req_header)
        resp = urllib2.urlopen(req,None,30)
        time.sleep(20)
        print resp.headers
        time.sleep(20)
        resp.read()
        print sys.getsizeof(resp)
#             print resp.read()
#         resp = urllib2.urlopen("http://ww4.sinaimg.cn/large/0064cTs2jw1exnxmw4ffij30os0ffwtl.jpg")
#                 print resp.headers
        for i in  str(resp.headers).split('\n'):
#                     print i
            if 'content-type' in str(i).lower():
                print str(i.split(':')[-1])
                filename.write(url+" : "+str(i.split(':')[-1])+'\n')
    except Exception, e:
        print e
# print resp
def getcontentype(host,port,url,params,headers):
        try:
            httpClient = httplib.HTTPConnection(host, port)
            #发出同步请求，并获取内容  
        #     resp, content = h.request("http://www.soso.com/")  
        #     print resp  
        #     print content 
            httpClient.request("GET",url,body=params, headers=headers)
           
            response = httpClient.getresponse()
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
#     urlhead()
    import cProfile
    cProfile.run("urlhead()")
    
    