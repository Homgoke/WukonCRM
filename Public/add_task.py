import time
class Add_task(object):
    def __init__(self,driver):
        self.driver=driver

    def add_task(self):
        self.driver.find_element_by_xpath('//div[@class="el-input"]/input').send_keys("任务任务任务")#输入正确的任务名称
        self.driver.find_element_by_xpath("//span/button[1]/span").click()#点击保存
        time.sleep(10)
