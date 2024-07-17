import time
from config.config import *
from common.action import Page_action
from common.browser import Browser
from common.basepage import Page
from datas.element import Element


class Yishi_Login(Browser):
    _testMethodDoc = '登录测试'

    # @unittest.skip
    def test_Login_01(self):
        '''正确用户名，正确密码'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        a = Page(self.driver).get_element(Element.add_task, '登录成功-存在创建任务按钮').text
        self.assertIn('添加任务', a)
        # self.assertEqual(f'http://{URL}#/vulnerabilityScanTask',self.driver.current_url)


    # @unittest.skip
    def test_Login_02(self):
        '''用户名错误'''
        super().login_url()
        Page_action(self.driver).login_input('roo','1234567')
        Page_action(self.driver).login_click()
        a = Page(self.driver).get_element(Element.login_wrong_tip, '登录-密码错误').text
        self.assertIn('[用户管理平台]账号/密码错误或者账户状态存在异常，请检查', a)



    # @unittest.skip
    def test_Login_03(self):
        '''密码错误'''
        super().login_url()
        Page_action(self.driver).login_input('root','123456')
        Page_action(self.driver).login_click()
        a = Page(self.driver).get_element(Element.login_wrong_tip, '登录-密码错误').text
        self.assertIn('[用户管理平台]账号/密码错误或者账户状态存在异常，请检查', a)



    # @unittest.skip
    def test_Login_04(self):
        '''密码为空'''
        super().login_url()
        Page_action(self.driver).login_input('wwh', '')
        Page_action(self.driver).login_click()
        a = Page(self.driver).get_element(Element.login_null_tip,'登录-密码为空').text
        self.assertIn('请输入密码', a)


    # @unittest.skip
    def test_Login_05(self):
        '''用户名为空'''
        super().login_url()
        Page_action(self.driver).login_input('', '123456')
        Page_action(self.driver).login_click()
        a = Page(self.driver).get_element(Element.login_null_tip, '登录-用户名为空').text
        self.assertIn('请输入用户名', a)



    # @unittest.skip
    def test_Login_06(self):
        '''用户名密码均为空'''
        super().login_url()
        Page_action(self.driver).login_input('', '')
        Page_action(self.driver).login_click()
        self.assertIn('请输入用户名', self.driver.page_source)
        self.assertIn('请输入密码', self.driver.page_source)




if __name__ == "__main__":
    Yishi_Login()