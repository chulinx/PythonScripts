#coding:utf-8
import requests
import time
start = time.time()
urls = [
        'http://www.heroku.com',
        'http://www.baidu.com',
        'http://www.163.com',
        'http://www.sina.com',
        'http://www.heroku.com',
        'http://blog.csdn.net'
        ]
for i in urls:
    print i+':'+str(requests.get(i).status_code)

end = time.time()
print "code run time is "+str(end-start)
