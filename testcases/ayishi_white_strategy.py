import time
from config.config import *
from common.action import Page_action
from common.browser import Browser
from common.basepage import Page
from datas.element import Element
from common.Random_str import *
import unittest


class Yishi_White_Test(Browser):
    _testMethodDoc = '创建白名单测试'

    # @unittest.skip
    def test_add_white_01(self):
        '''创建一条白名单策略'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_white_strategy(Ran_str(1),Ran_str(1),Ran_str(1),"未引入")
        # a = Page(self.driver).get_element(Element.alert_message, '成功提示').text
        # self.assertEqual('白名单规则保存成功', a)