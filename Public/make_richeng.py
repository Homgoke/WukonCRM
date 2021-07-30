from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
class Richeng(object):
    def __init__(self,driver):
        self.driver=driver

    def make_richeng(self):
        richeng=WebDriverWait(self.driver,10,0.2).until(EC.presence_of_element_located((By.XPATH,"//a[2]/li/span")))#定位日程按钮
        richeng.click()# 进入日程
        make_richeng=WebDriverWait(self.driver,10,0.2).until(EC.presence_of_element_located((By.XPATH,"/html/body/div/section/section/main/div/div/div/button/span")))#定位创建日程按钮
        make_richeng.click()#进入创建日程