#coding:utf-8
import requests
from bs4 import BeautifulSoup
import sys,time

reload(sys)
sys.setdefaultencoding('utf8')


urls=[
'http://www.tiejiang.org/wlaqgcs',
'http://www.tiejiang.org/system',
'http://www.tiejiang.org/network-administrator',
'http://www.tiejiang.org/development',
'http://www.tiejiang.org/sj',
'http://www.tiejiang.org/internet-dynamic'
]
def spider(urls):
    for url in urls:
        htmltext=requests.get(url).text
        soup=BeautifulSoup(htmltext,'html5lib')
        for p in soup.find_all('',class_='navbutton'):
            if p.get('title')==u'末页':
                allpages=p.get_text()
        for pagenum in range(1, int(allpages)):
            newurl=url+'/page/'+str(pagenum)
            htmltext=requests.get(newurl).text
            soup=BeautifulSoup(htmltext,'html5lib')
            articlelist=soup.find_all('a',class_="fancyimg home-blog-entry-thumb")
            for article in articlelist:
                print article.get('title')+'\t\t\t\t\t\t\t\t'+article.get('href')
        time.sleep(3)

spider(urls)

if __name__ == '__main__':
    urls=[
    'http://www.tiejiang.org/wlaqgcs',
    'http://www.tiejiang.org/system',
    'http://www.tiejiang.org/network-administrator',
    'http://www.tiejiang.org/development',
    'http://www.tiejiang.org/sj',
    'http://www.tiejiang.org/internet-dynamic'
    ]
    spider(urls)
