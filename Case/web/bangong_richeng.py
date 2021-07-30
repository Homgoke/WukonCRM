from selenium import webdriver
from Public.login_web import Mylogin
from Public.make_richeng import Richeng
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import os
import time
class Testricheng(unittest.TestCase):
    def setUp(self):
        self.abc = webdriver.Edge()
        self.abc.get("http://101.133.169.100:8088/")
        self.abc.maximize_window()
        time.sleep(5)
        print("starttime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self):
        filedir = "H:/软件测试/WukongCRM/test/screenshot/"
        if not os.path.exists(filedir):
            os.makedirs(os.path.join('H:/软件测试/WukongCRM/', 'test', 'screenshot'))
        print("endTime:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        self.abc.get_screenshot_as_file(screen_name)
        self.abc.quit()

    def testWkcrm_0006(self):
        '''日程-创建日程展示'''
        Mylogin(self.abc).login() #登录
        Richeng(self.abc).make_richeng()#进入创建日程模块
        save=self.abc.find_element_by_xpath('//div[@class="footer"]/button[1]/span')#保存按钮
        save.click()#点击保存按钮
        time.sleep(5)
        title_text=self.abc.find_element_by_class_name('text').text#获取标题文本
        zhuti_text=self.abc.find_element_by_xpath('//label[@for="title"]').text#获取主题文本
        zhuti_alert=self.abc.find_element_by_xpath('//div[1]/div/div[@class="el-form-item__error"]').text#获取主题错误提醒
        starttime_text = self.abc.find_element_by_xpath('//label[@for="startTime"]').text#获取开始时间文本
        starttime_alert=self.abc.find_element_by_xpath('//div[2]/div/div[@class="el-form-item__error"]').text#获取开始时间错误提醒
        endtime_text = self.abc.find_element_by_xpath('//label[@for="endTime"]').text#获取结束时间文本
        endtime_alert=self.abc.find_element_by_xpath('//div[3]/div/div[@class="el-form-item__error"]').text  # 获取结束时间错误提醒
        owner_text = self.abc.find_element_by_xpath('//label[@for="ownerUserIds"]').text#获取参会人文本
        remark_text = self.abc.find_element_by_xpath('//label[@for="remark"]').text#获取参与人文本
        zhuti=self.abc.find_element_by_xpath('//form/div[1]/div/div/input')#定位主题输入框
        zhuti_ph=zhuti.get_attribute('placeholder')#获取主题默认内容
        starttime=self.abc.find_element_by_xpath('//form/div[2]/div/div/input')#定位开始时间输入框
        starttime_ph=starttime.get_attribute('placeholder')#获取开始时间默认内容
        endtime=self.abc.find_element_by_xpath('//form/div[3]/div/div/input')#定位结束时间输入框
        endtime_ph=endtime.get_attribute('placeholder')#获取结束时间默认内容
        remark = self.abc.find_element_by_xpath('//textarea')  # 定位备注输入框
        remark_ph = remark.get_attribute('placeholder')  # 获取备注输入框默认内容

        guanlianyewu=self.abc.find_element_by_xpath('//span/p')#关联业务按钮

        self.assertEqual('创建日程',title_text)
        self.assertEqual('主题',zhuti_text)
        self.assertEqual('开始时间',starttime_text)
        self.assertEqual('结束时间',endtime_text)
        self.assertEqual('参与人',owner_text)
        self.assertEqual('备注',remark_text)
        self.assertEqual('请输入内容',zhuti_ph)
        self.assertEqual('选择日期时间',starttime_ph)
        self.assertEqual('选择日期时间',endtime_ph)
        self.assertEqual('请输入内容', remark_ph)
        self.assertEqual('主题不能为空',zhuti_alert)
        self.assertEqual('开始时间不能为空',starttime_alert)
        self.assertEqual('结束时间不能为空',endtime_alert)
        self.assertTrue(guanlianyewu.is_displayed())

    def testWkcrm_0007(self):
        '''创建日程-主题-正常创建'''
        Mylogin(self.abc).login()  # 登录
        Richeng(self.abc).make_richeng()  # 进入创建日程模块
        zhuti = self.abc.find_element_by_xpath('//form/div[1]/div/div/input')  # 定位主题输入框
        zhuti.send_keys('发送一个主题')
        starttime = self.abc.find_element_by_xpath('//form/div[2]/div/div/input')  # 定位开始时间输入框
        starttime.send_keys('2021-01-01 00:00:00')
        endtime = self.abc.find_element_by_xpath('//form/div[3]/div/div/input')  # 定位结束时间输入框
        endtime.send_keys('2021-01-01 00:00:01')
        save = self.abc.find_element_by_xpath('//div[@class="footer"]/button[1]/span')  # 保存按钮
        save.click()
        time.sleep(1)
        alert=WebDriverWait(self.abc,10,0.2).until(EC.presence_of_element_located((By.CLASS_NAME,"el-message__content")))
        alert_text=alert.text


        self.assertEqual("新建成功",alert_text)



