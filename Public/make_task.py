from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Task(object):
    def __init__(self,driver):
        self.driver=driver

    def make_task(self):
        task=WebDriverWait(self.driver,10,0.2).until(EC.presence_of_element_located((By.XPATH,"//a[3]/li/span")))
        task.click()#进入任务页面
        make_task=WebDriverWait(self.driver,10,0.2).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/section/section/main/div/div/div/button/span")))
        make_task.click()#进入创建任务页面
