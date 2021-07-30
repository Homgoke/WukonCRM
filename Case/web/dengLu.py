from selenium import webdriver
from Public.login_web import Mylogin
import unittest
import os
import time

class Testdenglu(unittest.TestCase):
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


    def testWkcrm_0001(self):
        '''登录-正常登录'''
        self.abc.find_element_by_xpath('//button[@type="button"]').click()
        self.abc.implicitly_wait(3)
        title=self.abc.find_element_by_class_name("title").text #检查标题
        use=self.abc.find_element_by_name('username')
        use_ph=use.get_attribute('placeholder')#检测用户名默认值
        pas=self.abc.find_element_by_name('password')
        pas_ph=pas.get_attribute('placeholder') #检测密码默认值
        dlbt=self.abc.find_element_by_xpath('//button/span').text #检查登录按钮文本
        usetx=self.abc.find_element_by_xpath('//div[2]/div/div[@class="el-form-item__error"]').text #检查用户名不输入提醒
        pastx=self.abc.find_element_by_xpath('//div[3]/div/div[@class="el-form-item__error"]').text #检查密码不输入提醒
        time.sleep(5)
        Mylogin(self.abc).login()
        login_url=self.abc.current_url



        self.assertEqual("BCBX",title)
        self.assertEqual("请输入用户名",use_ph)
        self.assertEqual("请输入密码",pas_ph)
        self.assertEqual("登录",dlbt)
        self.assertEqual("请输入账号",usetx)
        self.assertEqual("密码不能小于5位",pastx)
        self.assertEqual("http://101.133.169.100:8088/index.html#/workbench/index",login_url)


if __name__ == "__main__":
    unittest.main()