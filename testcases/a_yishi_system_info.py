import webbrowser
from selenium import webdriver
from common.browser import Browser
import time
from config.config import *
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Yishi_system(Browser):
    _testMethodDoc = '系统信息'

    # @unittest.skip
    def test_system_01(self):
        '''跳转系统信息页面'''
        super().sys_page()
        try:
            self.assertIn('每日任务上限', self.driver.page_source)
            self.assertIn('每日流量', self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir + self.test_system_01.__doc__ + '.png')
            print(e,self.test_system_01.__doc__ + '任务失败')


    # @unittest.skip
    def test_system_02(self):
        '''跳转系统信息总览页面'''
        super().sys_page()
        super().sys_all_page()
        try:
            self.assertIn('内存管理', self.driver.page_source)
            self.assertIn('硬盘管理', self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir + self.test_system_02.__doc__ + '.png')
            print(e,self.test_system_02.__doc__ + '任务失败')


    # @unittest.skip
    def test_system_03(self):
        '''跳转license管理页面'''
        super().sys_page()
        super().sys_license_page()

        try:
            self.assertIn('在线授权', self.driver.page_source)
            self.assertIn('离线授权', self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir + self.test_system_03.__doc__ + '.png')
            print(e,self.test_system_03.__doc__ + '任务失败')


    # @unittest.skip
    def test_system_04(self):
        '''导入非法离线授权文件'''
        try:
            super().sys_page()
            super().import_offline_file(illegal_offline_file)
            a = self.driver.find_element(By.CSS_SELECTOR,'p[class="ab-message__message"]').text
            self.assertIn('上传失败，请确保文件为我们提供的文件', a)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir + self.test_system_04.__doc__ + '.png')
            print(e,self.test_system_04.__doc__ + '任务失败')


    # @unittest.skip
    def test_system_05(self):
        '''在线授权-输入错误格式授权码'''
        try:
            super().sys_page()
            super().sys_license_page()
            super().online_update_page()
            super().online_empower_input(illegal_code)
            time.sleep(3)
            a = self.driver.find_element(By.CSS_SELECTOR,'div[class="ab-form-item__error"]').text
            self.assertIn('请输入正确的授权码',a)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir + self.test_system_05.__doc__ + '.png')
            print(e, self.test_system_05.__doc__ + '任务失败')


    # @unittest.skip
    def test_system_06(self):
        '''输入格式合法，但不是正确的授权码--‘1234-1234-1234-1234’'''
        try:
            super().sys_page()
            super().sys_license_page()
            super().online_update_page()
            super().online_empower_input(correct_code)
            super().online_empower_click()
            a = self.driver.find_element(By.CSS_SELECTOR,'p[class="ab-message__message"]').text
            self.assertIs('license:绑定授权失败，请联系客服！',a)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir + self.test_system_06.__doc__ + '.png')
            print(e, self.test_system_06.__doc__ + '任务失败')



if __name__ =='main':
    Yishi_system()