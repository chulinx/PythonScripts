#coding:utf-8
#!/usr/bin/python

import sys
reload(sys)
sys.setdefaultencoding('utf8')

import requests
import json

#获取企业微信token
def GetToken(corpid,corpsecret):
    try:
        token_url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        token_param = {'corpid':corpid,\
        'corpsecret':corpsecret}
        token_message=requests.get(token_url,params=token_param).text
        token=eval(token_message)['access_token']
    except  Exception,e:
        print e
    return token

#发送消息
def SendMessage(touser,agentid,content,token,msgtype="text",toparty='@all',totag='@all',safe=0):
    data={
   "touser" : touser,
   "toparty" : toparty,
   "totag" : totag,
   "msgtype" : msgtype,
   "agentid" : agentid,
   "text" : {
       "content" : content
        },
   "safe":safe
    }
    print data
    send_message = requests.post('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+token,data=json.dumps(data,ensure_ascii=False)).text
    print eval(send_message)[u'errmsg']


if __name__ == '__main__':
    corpid='wx10467d45ccff3861'
    corpsecret='qpGPcCrCIC-wvKjNOMXUgiU_cjvcFihxOznvG1b8sXU'
    content='你好'
    SendMessage('chulinzlx',1,content,GetToken(corpid,corpsecret))
