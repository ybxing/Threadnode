#coding:utf-8
'''
Created on 2017年5月18日

@author: Administrator
'''
import socket
import time
get_str = 'GET %s HTTP/1.0\r\nHost: %s\r\nAccept: text/html\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36\r\nAccept: */*\r\n\r\n'
post_str = 'POST %s HTTP/1.1\r\nHost: %s\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36\r\n\r\n'
address=("ww4.sinaimg.cn",80)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
sock.connect(address)
print get_str % ("http://ww4.sinaimg.cn/large/0064cTs2jw1exnxmw4ffij30os0ffwtl.jpg",80)
sock.send(post_str % ("http://ww4.sinaimg.cn/large/0064cTs2jw1exnxmw4ffij30os0ffwtl.jpg",80))    

response = ''    
temp = sock.recv(2048)
while temp:
    print temp
    temp=sock.recv(2048)
# print type(temp)
# print temp
#     time.sleep(10)
#     temp = sock.recv(4096)
#     response += temp

# print  response 