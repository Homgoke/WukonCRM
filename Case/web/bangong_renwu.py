from selenium import webdriver
from Public.login_web import Mylogin
from Public.make_task import Task
from Public.add_branchtask import Add_branchtask
from Public.add_task import Add_task
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import os
import time
class Testrenwu(unittest.TestCase):
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

    def testWkcrm_0032(self):
        '''任务-新建任务-输入正确的任务名称'''
        Mylogin(self.abc).login()# 登录
        Task(self.abc).make_task()#进入创建任务页面
        self.abc.find_element_by_xpath('//div[@class="el-input"]/input').send_keys("这是一个任务名称")#输入正确的任务名称
        self.abc.find_element_by_xpath("//span/button[1]/span").click()#点击保存
        alert = WebDriverWait(self.abc, 10, 0.2).until(EC.presence_of_element_located((By.CLASS_NAME, "el-message__content")))
        alert_text = alert.text

        self.assertEqual("新建成功", alert_text)

    def testwkcrm_0058(self):
        '''任务-我的任务-正常显示我的任务'''
        Mylogin(self.abc).login()#登录
        Task(self.abc).make_task()#进入创建任务页面
        Add_task(self.abc).add_task()#添加任务
        new_task=self.abc.find_element_by_xpath('//div/div[1]/div/div/div/div[1]/div[@class="list-left"]/span').text

        self.assertEqual("任务任务任务",new_task)

    def testwkcrm_0059(self):
        '''任务-我的任务-查看任务'''
        Mylogin(self.abc).login()#登录
        Task(self.abc).make_task()#进入创建任务页面
        Add_task(self.abc).add_task()#添加任务
        new_task=self.abc.find_element_by_xpath('//div/div[1]/div/div/div/div[1]/div[@class="list-left"]/span')
        task_text = new_task.text
        new_task.click()
        time.sleep(3)
        task_title=self.abc.find_element_by_class_name("title-text").text

        self.assertEqual(task_title,task_text)

    def testwkcrm_0060(self):
        '''任务-我的任务-完成任务'''
        Mylogin(self.abc).login()#登录
        Task(self.abc).make_task()#进入创建任务页面
        Add_task(self.abc).add_task()#添加任务
        button=self.abc.find_element_by_xpath('//*[@id="pane-mytask"]/div/div[3]/div/div[1]/div[1]/div/label/span')
        button_class=button.get_attribute('class')
        title=self.abc.find_element_by_xpath('//*[@id="pane-mytask"]/div/div[3]/div/div[1]/div[1]/span')
        title_class=title.get_attribute('class')
        button.click()
        time.sleep(2)
        button_class_c=button.get_attribute('class')
        title_class_c=title.get_attribute('class')

        self.assertEqual('el-checkbox__input',button_class)
        self.assertEqual('el-checkbox__input is-checked is-focus',button_class_c)
        self.assertEqual('el-tooltip item-name',title_class)
        self.assertEqual('el-tooltip item-name-active',title_class_c)

    def testwkcrm_0066(self):
        '''任务-我的任务-正常显示我下属的任务'''
        Mylogin(self.abc).login()#登录
        Task(self.abc).make_task()#进入创建任务页面
        Add_branchtask(self.abc).add_task()#增加下属任务
        self.abc.find_element_by_id('tab-subtask').click()#进入我下属的任务页面
        time.sleep(3)
        task=self.abc.find_element_by_xpath('//div[@id="pane-subtask"]/div/div[3]/div/div[1]/div[1]/span')
        task_text=task.text

        self.assertEqual('下属下属任务任务',task_text)

    def testwkcrm_0067(self):
        '''任务-我下属的任务-查看任务'''
        Mylogin(self.abc).login()#登录
        Task(self.abc).make_task()#进入创建任务页面
        Add_branchtask(self.abc).add_task()#增加下属任务
        self.abc.find_element_by_id('tab-subtask').click()#进入我下属的任务页面
        time.sleep(3)
        task=self.abc.find_element_by_xpath('//div[@id="pane-subtask"]/div/div[3]/div/div[1]/div[1]/span')
        task_text=task.text
        task.click()#进入任务详细页
        time.sleep(3)
        title=self.abc.find_element_by_class_name('title-text').text

        self.assertEqual(task_text,title)

    def testwkcrm_0068(self):
        '''任务-我下属的任务-完成任务'''
        Mylogin(self.abc).login()#登录
        Task(self.abc).make_task()#进入创建任务页面
        Add_branchtask(self.abc).add_task()#增加下属任务
        self.abc.find_element_by_id('tab-subtask').click()  # 进入我下属的任务页面
        time.sleep(3)
        button=self.abc.find_element_by_xpath('//*[@id="pane-subtask"]/div/div[3]/div/div[1]/div[1]/div/label/span')
        button_class=button.get_attribute('class')
        title=self.abc.find_element_by_xpath('//*[@id="pane-subtask"]/div/div[3]/div/div[1]/div[1]/span')
        title_class=title.get_attribute('class')
        button.click()
        time.sleep(2)
        button_class_c=button.get_attribute('class')
        title_class_c=title.get_attribute('class')

        self.assertEqual('el-checkbox__input',button_class)
        self.assertEqual('el-checkbox__input is-checked is-focus',button_class_c)
        self.assertEqual('el-tooltip item-name',title_class)
        self.assertEqual('el-tooltip item-name-active',title_class_c)
        print('abc')


















