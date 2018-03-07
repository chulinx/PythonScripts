#coding:utf-8                    
import requests                  
import time
import gevent
from gevent import monkey

start = time.time()              
urls = [
        'http://www.heroku.com',
        'http://www.baidu.com',
        'http://www.163.com',
        'http://www.sina.com',
        'http://www.heroku.com',
        'http://blog.csdn.net'
        ]
monkey.patch_all()

def getstatus(url):
    print url+':'+str(requests.get(url).status_code) 

jobs= [gevent.spawn(getstatus,url) for url in urls]
#gevent.joinall([
#    gevent.spawn(getstatus,'http://www.heroku.com'),
#    gevent.spawn(getstatus,'http://www.baidu.com'),
#    gevent.spawn(getstatus,'http://www.163.com'),
#    gevent.spawn(getstatus,'http://www.sina.com'),
#    gevent.spawn(getstatus,'http://www.heroku.com'),
#    gevent.spawn(getstatus,'http://blog.csdn.net'),
#    ])
gevent.joinall(jobs)
end=time.time()
print "code run time is"+str(end-start)
