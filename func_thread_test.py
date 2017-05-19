#coding:utf-8
'''
Created on 2017年5月18日

@author: Administrator
'''
import threading
import time
import random
import Queue
import httplib
import urlparse
import datetime
def myfunc(n):
    print "this is "+str(n)
    a=random.randint(0,3)
    time.sleep(a)
    print "this is "+str(n)+",sleep:"+str(a)
    return True
# tlist=[]
# for i in range(0,5):
# q=Queue.Queue(10)
# print q.
import urllib
params = urllib.urlencode({'name': 'tom', 'age': 22})
headers = {"Content-type": "application/x-www-form-urlencoded"
                    , "Accept": "text/plain"
                    ,"connection":"close"
                    ,"Content-Encoding":"gzip"}
def getcontentype(host,port,url,params,headers):
        try:
            httpClient = httplib.HTTPConnection(host, port)
            #发出同步请求，并获取内容  
        #     resp, content = h.request("http://www.soso.com/")  
        #     print resp  
        #     print content 
            httpClient.request("GET",url,body=params, headers=headers)
           
            response = httpClient.getresponse()
            for i in response.getheaders():
#                 print i[0]
                if str(i[0]).lower()=='content-type':
                    print url+" : "+str(i[1])+'\n'
        except Exception, e:
            print e
class pd(threading.Thread):
    def __init__(self,q):
        super(pd,self).__init__()
        self.q=q
     
    def run(self):
        now=datetime.datetime.now()
        print "start："+str(now)
        with open('test.txt') as f:
            for i in f.read().split('\n'):
    #     i="http://ww4.sinaimg.cn/large/0064cTs2jw1exnxmw4ffij30os0ffwtl.jpg"
                if 'http://' in i:
                    url=i
                else:
                    url='http://'+i
                 
                urlp=urlparse.urlparse(url)
                host=urlp.hostname
                port =urlp.port
                while True:
                    if self.q.full():
                        time.sleep(1)
                    else:
                        self.q.put(threading.Thread(target=getcontentype,args=(host,port,url,params,headers)))
                        break
#                 print i
        end=datetime.datetime.now()
        print  "+++++++++++++++++++++++++++++++++++++++++"+str(end-now)
        self.q.put(None)
class cs(threading.Thread):
    def __init__(self,q):
        super(cs,self).__init__()
        self.q=q
    def run(self):
        n=0
        while 1:
            if self.q.empty():
                time.sleep(1)
#                 n+=1
#                 if n>3:
#                     break
            else:
                n-=1
                value=self.q.get()
                if value !=None:
                    value.start()
                else:
                    break
def star():
    q=Queue.Queue(100)
    p=pd(q)
    p.start()
    c=cs(q)
    c.start()
if __name__=="__main__":
    star()