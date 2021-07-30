import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Shenpi(object):
    def __init__(self,driver):
        self.driver=driver

    def make_shenpi(self):
        shenpi=WebDriverWait(self.driver,10,0.2).until(EC.presence_of_element_located((By.XPATH,"//a[6]/li/span")))
        shenpi.click()#进入审批页面
        make_shenpi=WebDriverWait(self.driver,10,0.2).until(EC.presence_of_element_located((By.XPATH,'//main[@id="workbench-main-container"]/div/div/div[1]/button/span')))
        make_shenpi.click()#进入新建审批
        time.sleep(5)


