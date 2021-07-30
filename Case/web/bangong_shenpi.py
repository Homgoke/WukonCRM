from selenium import webdriver
from Public.login_web import Mylogin
from Public.make_shenpi import Shenpi
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import unittest
import os
import time
class Testshenpi(unittest.TestCase):
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

    def testWkcrm_0091(self):
        '''审批-新建普通审批-审批内容'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        ptsp=self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[1]')#定位普通审批按钮
        ptsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@class="el-form-item__content"]/div/input').send_keys('普通普通普通审批')#定位审批内容输入框，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()#点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')#查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span').click()  # 点击保存
        alert=WebDriverWait(self.abc,10,0.2).until(EC.presence_of_element_located((By.CLASS_NAME,'el-message__content')))
        alert=alert.text

        self.assertEqual('操作成功',alert)

    def testWkcrm_0097(self):
        '''审批-新建请假审批-请假类型-加班'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        jbsp=self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[2]')#定位996审批按钮
        jbsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@class="el-form-item__content"]/div/input').send_keys('996996996996')#定位审批内容输入框，输入内容
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[2]/div/div/input').send_keys('2021-01-04 00:00:00')#输入开始时间
        self.abc.find_element_by_xpath('//div[3]/div/div/input').send_keys('2021-01-05 00:00:01')#输入结束时间
        self.abc.find_element_by_xpath('//div[4]/div/div/input').send_keys('1')#输入加班总天数
        time.sleep(2)
        save=self.abc.find_element_by_css_selector('div.handle-bar>button:nth-child(2)>span')
        ActionChains(self.abc).double_click(save).perform()# 双击保存
        alert=WebDriverWait(self.abc,10,0.2).until(EC.presence_of_element_located((By.CLASS_NAME,'el-message__content')))
        alert=alert.text

        self.assertEqual('操作成功',alert)



    def testWkcrm_0098(self):
        '''审批-新建请假审批-审批内容'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        qjsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[42]')  # 定位请假审批按钮
        qjsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div/div[@class="el-textarea"]/textarea').send_keys(
            '请假请假offoffoff')  # 定位请假审批事由输入框，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save = self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()  # 点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text
        ftext=WebDriverWait(self.abc,10,0.2).until(EC.presence_of_element_located((By.XPATH,'//div[@id="examine-list-boxmy"]/div[1]/div/div/p')))
        ftext=ftext.text

        self.assertEqual('操作成功', alert)
        self.assertEqual('请假请假offoffoff',ftext)

    def testWkcrm_0099(self):
        '''新建请假审批-开始时间-输入正确时间'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        qjsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[42]')  # 定位请假审批按钮
        qjsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div/div[@class="el-textarea"]/textarea').send_keys(
            '请假请假offoffoff输入时间')  # 定位请假审批事由输入框，输入内容
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@class="crm-create-body"]/form/div[3]/div/div/input').send_keys('2021-06-30 00:00:00')#输入日期
        self.abc.find_element_by_xpath('//div[@class="el-picker-panel__footer"]/button[2]').click()#点击确定
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save = self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()  # 点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text
        ftext=WebDriverWait(self.abc,10,0.2).until(EC.presence_of_element_located((By.XPATH,'//div[@id="examine-list-boxmy"]/div[1]/div/div/p')))
        ftext=ftext.text

        self.assertEqual('操作成功', alert)
        self.assertEqual('请假请假offoffoff输入时间',ftext)

    def testWkcrm_0100(self):
        '''新建请假审批-开始时间-选择正确时间'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        qjsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[42]')  # 定位请假审批按钮
        qjsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div/div[@class="el-textarea"]/textarea').send_keys(
            '请假请假offoffoff选择时间')  # 定位请假审批事由输入框，输入内容
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@class="crm-create-body"]/form/div[3]/div/div/input').click()#点击日期输入框
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@class="el-picker-panel__footer"]/button[1]').click()#点击’此刻‘
        self.abc.find_element_by_xpath('//div[@class="el-picker-panel__footer"]/button[2]').click()#点击确定
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save = self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()  # 点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text
        ftext=WebDriverWait(self.abc,10,0.2).until(EC.presence_of_element_located((By.XPATH,'//div[@id="examine-list-boxmy"]/div[1]/div/div/p')))
        ftext=ftext.text

        self.assertEqual('操作成功', alert)
        self.assertEqual('请假请假offoffoff选择时间',ftext)

    def testWkcrm_0143(self):
        '''审批-新建差旅审批-差旅事由'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        clsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[3]')  # 定位差旅报销按钮
        clsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div[@class="el-form-item__content"]/div/input').send_keys('差旅差旅事由事由')  # 定位差旅事由输入框，输入内容
        self.abc.find_element_by_xpath('//div[@class="expense-item"]/div[2]/div[5]/div/input').send_keys('1')#定位交通费，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save=self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()#点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text

        self.assertEqual('操作成功', alert)


    def testWkcrm_0144(self):
        '''审批-新建差旅审批-备注'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        clsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[3]')  # 定位差旅报销按钮
        clsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div[@class="el-form-item__content"]/div/input').send_keys('差旅差旅事由事由')  # 定位差旅事由输入框，输入内容
        self.abc.find_element_by_xpath('//div[1]/textarea[@class="el-textarea__inner"]').send_keys('差旅差旅备注备注')#定位备注框并输入
        self.abc.find_element_by_xpath('//div[@class="expense-item"]/div[2]/div[5]/div/input').send_keys('1')#定位交通费，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save=self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()#点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text

        self.assertEqual('操作成功', alert)

    def testWkcrm_0145(self):
        '''新建差旅审批-费用明细-出发城市'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        clsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[3]')  # 定位差旅报销按钮
        clsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div[@class="el-form-item__content"]/div/input').send_keys('差旅差旅事由事由')  # 定位差旅事由输入框，输入内容
        self.abc.find_element_by_xpath('//div[1]/textarea[@class="el-textarea__inner"]').send_keys('差旅差旅备注备注')#定位备注框并输入
        self.abc.find_element_by_xpath('//div/div/div[1]/div[2]/input').send_keys('中国广东')#定位出发城市并输入
        self.abc.find_element_by_xpath('//div[@class="expense-item"]/div[2]/div[5]/div/input').send_keys('1')#定位交通费，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save=self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()#点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text

        self.assertEqual('操作成功', alert)

    def testWkcrm_0146(self):
        '''新建差旅审批-费用明细-目的城市'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        clsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[3]')  # 定位差旅报销按钮
        clsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div[@class="el-form-item__content"]/div/input').send_keys('差旅差旅事由事由')  # 定位差旅事由输入框，输入内容
        self.abc.find_element_by_xpath('//div[1]/textarea[@class="el-textarea__inner"]').send_keys('差旅差旅备注备注')#定位备注框并输入
        self.abc.find_element_by_xpath('//div/div/div[1]/div[2]/input').send_keys('中国广东')#定位出发城市并输入
        self.abc.find_element_by_xpath('//div/div/div[2]/div[2]/input').send_keys('日本东京')  # 定位出发城市并输入
        self.abc.find_element_by_xpath('//div[@class="expense-item"]/div[2]/div[5]/div/input').send_keys('1')#定位交通费，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save=self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()#点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text

        self.assertEqual('操作成功', alert)

    def testWkcrm_0147(self):
        '''新建差旅审批-开始时间-输入正确时间'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        clsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[3]')  # 定位差旅报销按钮
        clsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div[@class="el-form-item__content"]/div/input').send_keys('差旅差旅事由事由')  # 定位差旅事由输入框，输入内容
        self.abc.find_element_by_xpath('//div[1]/textarea[@class="el-textarea__inner"]').send_keys('差旅差旅备注备注')#定位备注框并输入
        self.abc.find_element_by_xpath('//div/div/div[1]/div[2]/input').send_keys('中国广东')#定位出发城市并输入
        self.abc.find_element_by_xpath('//div/div/div[2]/div[2]/input').send_keys('日本东京')  # 定位出发城市并输入
        self.abc.find_element_by_xpath('//div/div/div[3]/div[2]/input').send_keys('2021-01-01')  # 定位并输入开始时间
        self.abc.find_element_by_xpath('//div[@class="expense-item"]/div[2]/div[5]/div/input').send_keys('1')#定位交通费，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save=self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()#点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text

        self.assertEqual('操作成功', alert)

    def testWkcrm_0148(self):
        '''新建差旅审批-开始时间-选择正确时间'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        clsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[3]')  # 定位差旅报销按钮
        clsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div[@class="el-form-item__content"]/div/input').send_keys(
            '差旅差旅事由事由')  # 定位差旅事由输入框，输入内容
        self.abc.find_element_by_xpath('//div[1]/textarea[@class="el-textarea__inner"]').send_keys(
            '差旅差旅备注备注')  # 定位备注框并输入
        self.abc.find_element_by_xpath('//div/div/div[1]/div[2]/input').send_keys('中国广东')  # 定位出发城市并输入
        self.abc.find_element_by_xpath('//div/div/div[2]/div[2]/input').send_keys('日本东京')  # 定位出发城市并输入
        self.abc.find_element_by_xpath('//div/div/div[3]/div[2]/input').click()#点击开始时间输入框
        self.abc.find_element_by_xpath('//table[1]/tbody/tr[3]/td[1]/div/span').click()  # 定位并选择开始时间
        self.abc.find_element_by_xpath('//div[@class="expense-item"]/div[2]/div[5]/div/input').send_keys(
            '1')  # 定位交通费，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save = self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()  # 点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text

        self.assertEqual('操作成功', alert)

    def testWkcrm_0149(self):
        '''新建差旅审批-结束时间-输入正确时间'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        clsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[3]')  # 定位差旅报销按钮
        clsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div[@class="el-form-item__content"]/div/input').send_keys(
            '差旅差旅事由事由')  # 定位差旅事由输入框，输入内容
        self.abc.find_element_by_xpath('//div[1]/textarea[@class="el-textarea__inner"]').send_keys(
            '差旅差旅备注备注')  # 定位备注框并输入
        self.abc.find_element_by_xpath('//div/div/div[1]/div[2]/input').send_keys('中国广东')  # 定位出发城市并输入
        self.abc.find_element_by_xpath('//div/div/div[2]/div[2]/input').send_keys('日本东京')  # 定位出发城市并输入
        self.abc.find_element_by_xpath('//div/div/div[3]/div[2]/input').send_keys('2021-01-01') # 定位并输入开始时间
        self.abc.find_element_by_xpath('//div/div/div[4]/div[2]/input').send_keys('2021-02-01')# 定位并输入结束时间
        self.abc.find_element_by_xpath('//div[@class="expense-item"]/div[2]/div[5]/div/input').send_keys(
            '1')  # 定位交通费，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save = self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()  # 点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text

        self.assertEqual('操作成功', alert)

    def testWkcrm_0150(self):
        '''新建差旅审批-结束时间-选择正确时间'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        clsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[3]')  # 定位差旅报销按钮
        clsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div[@class="el-form-item__content"]/div/input').send_keys(
            '差旅差旅事由事由')  # 定位差旅事由输入框，输入内容
        self.abc.find_element_by_xpath('//div[1]/textarea[@class="el-textarea__inner"]').send_keys(
            '差旅差旅备注备注')  # 定位备注框并输入
        self.abc.find_element_by_xpath('//div/div/div[1]/div[2]/input').send_keys('中国广东')  # 定位出发城市并输入
        self.abc.find_element_by_xpath('//div/div/div[2]/div[2]/input').send_keys('日本东京')  # 定位出发城市并输入
        self.abc.find_element_by_xpath('//div/div/div[4]/div[2]/input').click()#点击结束时间框
        self.abc.find_element_by_xpath('//table[1]/tbody/tr[4]/td[1]/div/span').click()  # 定位并选择结束时间
        self.abc.find_element_by_xpath('//div[@class="expense-item"]/div[2]/div[5]/div/input').send_keys(
            '1')  # 定位交通费，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save = self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()  # 点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text

        self.assertEqual('操作成功', alert)

    def testWkcrm_0153(self):
        '''新建差旅审批-费用明细-交通费'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        clsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[3]')  # 定位差旅报销按钮
        clsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div[@class="el-form-item__content"]/div/input').send_keys('差旅差旅事由事由')  # 定位差旅事由输入框，输入内容
        self.abc.find_element_by_xpath('//div[@class="expense-item"]/div[2]/div[5]/div/input').send_keys('1')#定位交通费，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save=self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()#点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text

        self.assertEqual('操作成功', alert)

    def testWkcrm_0154(self):
        '''新建差旅审批-费用明细-住宿费'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        clsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[3]')  # 定位差旅报销按钮
        clsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div[@class="el-form-item__content"]/div/input').send_keys('差旅差旅事由事由')  # 定位差旅事由输入框，输入内容
        self.abc.find_element_by_xpath('//div[@class="expense-item"]/div[2]/div[6]/div/input').send_keys('1')#定位住宿费，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save=self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()#点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text

        self.assertEqual('操作成功', alert)

    def testWkcrm_0155(self):
        '''新建差旅审批-费用明细-餐饮费'''
        Mylogin(self.abc).login()
        Shenpi(self.abc).make_shenpi()
        clsp = self.abc.find_element_by_xpath('//div[@class="categorys"]/div[1]/div[3]')  # 定位差旅报销按钮
        clsp.click()
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[1]/div[@class="el-form-item__content"]/div/input').send_keys(
            '差旅差旅事由事由')  # 定位差旅事由输入框，输入内容
        self.abc.find_element_by_xpath('//div[@class="expense-item"]/div[2]/div[7]/div/input').send_keys(
            '1')  # 定位住宿费，输入内容
        time.sleep(2)
        self.abc.find_element_by_class_name('add-item').click()  # 点击添加员工
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('admin')  # 查找员工admin
        time.sleep(2)
        self.abc.find_element_by_xpath('//div[@role="group"]/label').click()  # 选择下属admin
        save = self.abc.find_element_by_xpath('//div[@class="handle-bar"]/button[2]/span')
        save.click()  # 点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-message__content')))
        alert = alert.text

        self.assertEqual('操作成功', alert)