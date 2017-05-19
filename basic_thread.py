#coding:utf-8
'''
Created on 2017年5月19日

@author: Administrator
'''
import threading
import time
import random
import Queue
import httplib
import urlparse
import datetime
import sys
q=Queue.Queue(1)
print type(q)
# def myfunc(q,n):
#     print "this is "+str(n)
#     a=random.randint(0,3)
#     time.sleep(a)
#     print "this is "+str(n)+",sleep:"+str(a)
#     q.put((True,n))
# for i in range(0,100):
#     t=threading.Thread(target=myfunc,args=(q,i))
#      
#     print t.isDaemon()
#     t.setDaemon(True)
#     t.start()
# t.join()
# while True:
#     i= q.get(timeout=1)
#     if i!=None:
#         print i
#     else:
#         print i
#         break
# duilie={}
# print len(duilie)
# for i in range(0,100):
# #     print sys.getsizeof(duilie)
#     duilie[str(i)]=123
# print sys.getsizeof(duilie)
# # duilie['2']=123
# # print sys.getsizeof(duilie)
# for i in range(0,100):
# #     print sys.getsizeof(duilie)
#     duilie.pop(str(i))
# print len(duilie)
# # duilie=None
# print sys.getsizeof(duilie)
# print len(duilie)
# for i in range(0,100):
# #     print sys.getsizeof(duilie)
#     duilie[str(i)]=123
# print sys.getsizeof(duilie)
# duilie['1']=None
# print sys.getsizeof(duilie)