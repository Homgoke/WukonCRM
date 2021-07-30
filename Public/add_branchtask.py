import time
class Add_branchtask(object):
    def __init__(self,driver):
        self.driver=driver

    def add_task(self):
        self.driver.find_element_by_xpath('//div[@class="el-input"]/input').send_keys("下属下属任务任务")#输入正确的任务名称
        self.driver.find_element_by_class_name('el-icon-plus').click()#点击负责人列表
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[@role="tooltip"]/div/div[1]/input').send_keys('yyy')#查找下属yyy
        time.sleep(2)
        self.driver.find_element_by_xpath('//div[@role="group"]/label').click()#选择下属yyy
        self.driver.find_element_by_xpath("//span/button[1]/span").click()#点击保存
        time.sleep(5)
