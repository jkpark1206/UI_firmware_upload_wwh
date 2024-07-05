from selenium.webdriver.remote.webdriver import WebDriver
from common.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from config.config import *


class BasePage:
    def __init__(self, driver: WebDriver,):
        self.driver = driver
        self.wait_time = 2

#获取元素
    def get_element(self,located,page_action):
        try:
            element = self.driver.find_element(*located)
            return element
        except:
            print(f"在{page_action} 页面， 没有找到 {located} 元素")

# 等待元素可见
    def wait_element_visibility(self, loc,page_action):
        try:
            ele = WebDriverWait(self.driver,self.wait_time).until(EC.visibility_of_element_located(loc))
            return ele
        except:
            print("等待元素可见失败")


    # 输入
    def input_text(self, loc, content, page_action):
        ele = self.get_element(loc, page_action)
        try:
            if ele == True:
                ele.clear()
            ele.send_keys(content)
        except:
            print(f"在{page_action},{loc} 元素里面，输入{content} 内容失败")


    # 点击
    def action_click(self, located, page_action):
        ele = self.get_element(located,page_action)
        try:
            ele.click()
        except:
            print(f"在{page_action} 点击 {located} 元素 失败")


    # 断言使用：等待元素可见
    def if_visibility(self, loc,page_action):
        if WebDriverWait(self.driver,self.wait_time).until(EC.visibility_of_element_located(loc)):
            return WebDriverWait(self.driver,self.wait_time).until(EC.visibility_of_element_located(loc))
        else:
            self.save_page_fail(page_action)

    #查找元素
    # def find_element(self, located, page_action):
    #     ele = self.get_element(located, page_action)


    # 保存失败页面
    def save_page_fail(self, page_action):
        for_time = time.strftime("%Y%m%d%H%M%S",time.localtime())
        save_time = "{}-{}.png".format(page_action,for_time)
        file_name = os.path.join(image_dir,save_time)
        try:
            self.driver.save_screenshot(file_name)
        except:
            print(f"在{page_action} 保存图片失败，请检查路径是否存在！！！")