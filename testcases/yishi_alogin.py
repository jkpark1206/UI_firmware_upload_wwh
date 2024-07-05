from common.browser import Browser
import time
from config.config import *
import unittest
from datas.data import *
from common.action import Task



class Yishi_Login(Browser):
    _testMethodDoc = '登录测试'

    # @unittest.skip
    def test_Login_01(self):
        '''正确用户名，正确密码'''
        super().login_url()
        super().login_input(user_name,passwd)
        super().login_click()
        self.assertEqual(f'http://{URL}#/vulnerabilityScanTask',self.driver.current_url)


    # @unittest.skip
    def test_Login_02(self):
        '''用户名错误'''
        super().login_url()
        super().login_input('roo','1234567')
        super().login_click()
        time.sleep(2)
        self.assertIn('[用户管理平台]账号/密码错误或者账户状态存在异常，请检查',self.driver.page_source)

    # @unittest.skip
    def test_Login_03(self):
        '''密码错误'''
        super().login_url()
        super().login_input('root','123456')
        super().login_click()
        self.assertIn('[用户管理平台]账号/密码错误或者账户状态存在异常，请检查', self.driver.page_source)


    # @unittest.skip
    def test_Login_04(self):
        '''密码为空'''
        super().login_url()
        super().login_input('wwh', '')
        super().login_click()
        a = self.driver.find_element(By.XPATH,'//div[@class="ab-form-item__error"]').text
        self.assertIn('请输入密码', a)


    # @unittest.skip
    def test_Login_05(self):
        '''用户名为空'''
        super().login_url()
        super().login_input('', '123456')
        super().login_click()
        self.assertIn('请输入用户名 ', self.driver.page_source)


    # @unittest.skip
    def test_Login_06(self):
        '''用户名密码均为空'''
        super().login_url()
        super().login_input('', '')
        super().login_click()
        self.assertIn('请输入用户名', self.driver.page_source)
        self.assertIn('请输入密码', self.driver.page_source)


    #
    # def test_Login_1(self):
    #     '''正确用户名、密码'''
    #     super().login_url()
    #     super().login_input('','Test123456')
    #     super().login_click()
    #     self.assertEqual(self.driver.find_element(By.XPATH, '//div[@class="ab-form-item__error"]').text,'请输入用户名','测试不通过')
    #
    #
    # def test_Login_2(self):
    #     '''错误用户名'''
    #     super().login_url()
    #     Task(self.driver).login_input('ww','Test123456')
    #     Task(self.driver).login_click()
    #     self.assertEqual(self.driver.find_element(By.XPATH, '//p[@class="ab-alert__message"]/span').text,'[用户管理平台]账号/密码错误或者账户状态存在异常，请检查')




if __name__ == "__main__":
    Yishi_Login()