import requests
from bs4 import BeautifulSoup
import json

def getStoreInfo(pagenum,getinfotext):
    try:
        resptext=requests.get('http://ybj.sh.gov.cn/xxcx/ddyd.jsp?pageno='+str(pagenum)+'&qxcode=&unitname=&address=').text
        soup = BeautifulSoup(resptext,'html5lib')
        for i in soup.select('[bgcolor="#FFFFFF"] > td'):
            getinfotext.append(i.get_text())
    except Exception as e:
        print(e)
    return getinfotext

def getAllStoreInfo():
    getinfotext = []
    for pn in range(100):
        #print('第'+str(pn)+'页')
        getStoreInfo(pn,getinfotext)
    return getinfotext


def getStoredict(getinfotext):
    address = []
    storename = []
    for i in getinfotext:
        if getinfotext.index(i) % 4 == 1:
            storename.append(i)
        elif getinfotext.index(i) % 4 == 2:
            address.append(i)
    storedict = dict(zip(storename,address))
    print(len(storedict))
    return storedict
def main():
    return getStoredict(getAllStoreInfo())

print(json.dumps(main(),ensure_ascii=False))
