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
import urllib2
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
def getcontentype(url):
        req_header = {
                        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4',
                        'Accept':'text/html',
                        'Connection':'close'
                    }
        try:
            req = urllib2.Request(url,None,req_header)
            resp = urllib2.urlopen(req,None,30)
#             print resp.read()
    #         resp = urllib2.urlopen("http://ww4.sinaimg.cn/large/0064cTs2jw1exnxmw4ffij30os0ffwtl.jpg")
#                 print resp.headers
            for i in  str(resp.headers).split('\n'):
#                     print i
                if 'content-type' in str(i).lower():
                    print url+" : "+str(i.split(':')[-1])+'\n'
                    
#                         filename.write(url+" : "+str(i.split(':')[-1])+'\n')
        except Exception, e:
            print e
class pd(threading.Thread):
    def __init__(self,q):
        super(pd,self).__init__()
        self.q=q
     
    def run(self):
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
                        self.q.put(threading.Thread(target=getcontentype,args=(url)))
                        break
#                 print i
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
    now=datetime.datetime.now()
    star()
    end=datetime.datetime.now()
    print str(end-now)