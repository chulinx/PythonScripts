#coding:utf-8
from PIL import Image,ImageEnhance
import pytesseract,time
from selenium import webdriver
import sys,re

def identCode():
    '''1.进行浏览器页面截图 2. 设置验证码位置像素 2.截取验证码并保存
    '''
    firefox_browser.save_screenshot('xxxlogin.jpg')
    im = Image.open('xxxlogin.jpg')
    box=(1001,435,1079,463)
    im.crop(box)
    newim=im.crop(box)
    newim.save('a.png')

    '''进行验证码图像处理，使其更容易识别
    '''
    im = Image.open(r'C:\Users\Administrator\Desktop\ssemonitor\tmp\a.png')
    enhancer = ImageEnhance.Color(im)
    enhancer = enhancer.enhance(0)
    enhancer = ImageEnhance.Brightness(enhancer)
    enhancer = enhancer.enhance(2)
    enhancer = ImageEnhance.Contrast(enhancer)
    enhancer = enhancer.enhance(8)
    enhancer = ImageEnhance.Sharpness(enhancer)
    im = enhancer.enhance(20)
    identcode=pytesseract.image_to_string(im)
    return identcode

def login(username,password,identcode):
    '''
    发送用户名，密码，以及验证码到对应输入框，点击登录
    '''
    firefox_browser.find_element_by_id('username').clear()
    firefox_browser.find_element_by_id('username').send_keys(username)
    firefox_browser.find_element_by_id('password').clear()
    firefox_browser.find_element_by_id('password').send_keys(password)
    firefox_browser.find_element_by_id('code').clear()
    firefox_browser.find_element_by_id('code').send_keys(identcode)
    firefox_browser.find_element_by_id('loginButton').click()
    firefox_browser.get('https://www.xxx.com/mgr_prize_log/prizeLogList.dql')

def selectCategory(item,beginTime,endTime):
    '''
    通过js操控改变日期input控件不可输入的（readOnly）属性
    '''
    beginTimeJs="document.getElementsByName('beginTime')[0].readOnly=false"
    endTimeJs="document.getElementsByName('endTime')[0].readOnly=false"
    firefox_browser.execute_script(beginTimeJs)
    firefox_browser.execute_script(endTimeJs)
    # 输入开始时间
    firefox_browser.find_elements_by_name('beginTime')[0].clear()
    firefox_browser.find_elements_by_name('beginTime')[0].send_keys('2017-07-01')
    # 输入结束时间
    firefox_browser.find_elements_by_name('endTime')[0].clear()
    firefox_browser.find_elements_by_name('endTime')[0].send_keys('2017-07-31')
    #选择奖品类型
    firefox_browser.find_element_by_xpath('//select[@id="prize_type"]/option[@value="'+str(item)+'"]').click()
    #点击查询按钮
    firefox_browser.find_elements_by_name("submit")[0].click()
    return firefox_browser.page_source

def rawNum(page_source):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page_source, 'lxml')
    rawnum=len(soup.select("table.main_data_table > tbody > tr"))
    return rawnum

def getData(rawnum):
    '''循环获取用户的uid，奖品，获奖时间，手机号，真实姓名'''
    for i in range(2, rawnum):
        uid=firefox_browser.find_element_by_xpath('//table[@class="main_data_table"]//tr['+ str(i) +']//td[2]//a[@class="uid"]').text
        prizes=firefox_browser.find_element_by_xpath('//table[@class="main_data_table"]//tr['+ str(i) +']//td[3]').text
        getPrizeTime=firefox_browser.find_element_by_xpath('//table[@class="main_data_table"]//tr['+ str(i) +']//td[7]').text
        firefox_browser.find_element_by_xpath('//table[@class="main_data_table"]//tr['+ str(i) +']//td[2]//a[@class="uid"]').click()
        time.sleep(2)
        phoneNumber=''.join(re.findall(r'\d+', firefox_browser.find_element_by_xpath('//table[@class="main_info_table"]//tr[5]//td//i').text, flags=0))
        name=firefox_browser.find_element_by_xpath('//table[@class="main_info_table"]//tr[9]//td[2]').text
        firefox_browser.back()

        print uid+name+'\t\t'+phoneNumber+'\t\t'+prizes+'\t\t'+getPrizeTime



if __name__ == '__main__':
    username="xushuang"
    password="xushuang123"
    '''1.初始化浏览器 2.打开网址 3.设置浏览器宽度和长度
    '''
    firefox_browser = webdriver.Firefox()
    firefox_browser.get('https://www.xxx.com/manage/adminLogin.jsp')
    time.sleep(2)
    firefox_browser.set_window_size(1920,1080)
    time.sleep(1)

    login(username, password, identCode())
    '''如果验证码识别错误，url地址不变的话 循环刷新验证码再登录'''
    while firefox_browser.current_url=="https://www.xxx.com/manage/adminLogin.jsp":
        login(username, password, identCode())
    print u"用户名\t\t\t\t手机号\t\t\t奖品\t\t\t\t抽奖时间"
    for item in range(1, 9):
        getData(rawNum(selectCategory(item, sys.argv[1], sys.argv[2])))
        #获取当前页面数据分几页
        totalPage=int(''.join(re.findall(r'<input name="totalPage" value="(\d+)" type="hidden">',firefox_browser.page_source)))
        if totalPage != 1:   #如果油分页，自动点击下一页爬取
            for nextPage in range(1, totalPage):
                firefox_browser.find_element_by_xpath('//th[@colspan="100"]//a[@class="next"]').click()
                time.sleep(1)
                getData(rawNum(firefox_browser.page_source))
        else:
            pass
