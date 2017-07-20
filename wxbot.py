#coding:utf-8

from wxpy import *
from random import choice
import time,datetime

bot = Bot(cache_path=True)

tuling = Tuling(api_key='0e8d70b241fcc4a898ee410937b0551220')


naXienian=bot.groups().search(u'那些年')[0]

fristHello=[u'亲们有没有想我？',u'Hello,我来啦!!',u'都出来聊天呢！']
naXienian.send(choice(fristHello))
msgReceiveTime=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
@bot.register(naXienian)
def reply_naXienian(msg):
    global msgReceiveTime
    msgReceiveTime=str(msg.receive_time).split('.')[0]
    tuling.do_reply(msg)

def checkMessageTime():
    autoReply=[u'Hello,我来啦!!',u'都出来聊天呢!',u'刚才我和我的朋友在讨论一些事情，我们想知道女人到底是怎么看到这个问题的，女生喜欢一个有女友的男生，应该追吗?/醉酒后的话可以相信吗?',\
               u'女生应该生气男友玩真心话大冒险吗?/接吻算是偷情吗?/你们说男人和女人谁更喜欢说谎?',\
               u'我的朋友冬瓜(一个有趣的外号)刚和女朋友分手，就是那边穿衬衫的帅哥，你觉得他要等多久才能和别的女生约会'\
               u'我需要一些女生观点，如果你跟某人交往了三个月，他不想你跟他的某个朋友太亲近，怎么回应才好，假设这个人只是朋友，不会发生什么事。',\
               u'我朋友的女朋友打算去做隆胸手术，作为送给我朋友的生日礼物，我的朋友不知道这回事，我估计他不一定会喜欢，你说我要不要跟他女朋友建议一下、还是把这件事告诉我朋友?',\
               u'如果你们对一个人没有兴趣，但是又不想伤害人家， 你们会怎么说?是这样的。我朋友和他的女朋友正在试着撮合我和另外一个女生。好吧，她是很可爱，但就不是我喜欢的类型。 我应该怎么对她说呢?'\
               u'你喜欢小马吗?(停顿)我小时候邻居有个女孩常被我欺负，她一见到小马就笑，你就像我以前的邻居小女孩^ ^~',\
               u'我叫她做刁蛮小公主，那时候我们经常为一点鸡毛蒜皮的事情吵架，我真的觉得你好像她啊，特别是鼻子。',\
               u'你偷看我这么久、你应该过来跟我说话，我不会拒绝你的',\
               ]
    while True:
        print u"开始检查时间"
        diff = int(time.mktime(datetime.datetime.now().timetuple()))-int(time.mktime(time.strptime(msgReceiveTime,'%Y-%m-%d %H:%M:%S')))
        if diff > 1200:
            naXienian.send(choice(autoReply))
        time.sleep(500)

zhangJiaBuLuo=bot.groups().search(u'张家部落')[0]
@bot.register(zhangJiaBuLuo)
def reply_zhangJiaBuLuo(msg):
    tuling.do_reply(msg)

# zhangxiang = bot.friends().search(u'张林祥')[0]
#
# msgReceiveTime=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
# @bot.register(zhangxiang)
# def reply_zhangxiang(msg):
#     global msgReceiveTime
#     msgReceiveTime=str(msg.receive_time).split('.')[0]
#     tuling.do_reply(msg)

# 保存运行测试
checkMessageTime()
embed()
