import time


class Mylogin(object):
    def __init__(self,driver):
        self.driver = driver

    def login(self):
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('123456')
        time.sleep(2)
        self.driver.find_element_by_xpath('//button/span').click()
        time.sleep(10)