from config.config import *
from common.action import Page_action
from common.browser import Browser
from common.basepage import Page
from datas.element import Element
from common.Random_str import *
import unittest



copyright = ["商业许可","宽松型","专有自由","公共领域","特殊限制","专利授权","资源有限","著佐权型","弱著佐权型","解读中"]

prohibit = ["修改和衍生","专利使用","可获得开源软件源代码","包含提醒","声明修改","责任","Tivoization禁止","保证","包含下载说明",
            "使用商标","开放源代码","保留许可信息","商标使用","技术限制禁止","专利维权（向开源软件开发者）","商用",
            "提供担保","重新许可","赔偿许可人损失","实施专利授权","使用相同许可","专利","限制更改许可","限制技术措施","版权","专利禁止",
            "剥夺","追究许可人责任","联系作者","专利限制","保留版权信息","移除或修改版权许可","技术","分发",
            "重命名开源软件或许可证的相关限制","再许可"]

Application = ["免责声明","可观察源代码","使用相同许可","不得误导性使用名称","动态链接","相同的许可证（库）","可获得开源软件源代码",
               "无责任","状态变化","重命名开源软件或许可证的相关限制","声明修改","相同的许可证（文件）","相同的许可证","相同许可证",
               "版权声明","包含下载说明","限制责任","许可","包含提醒","共享库链接","修改的分发","网络使用是分配","无保证","许可证继承",
               "保留版权信息","许可证的延续","保留原始版权声明","专利授权通知","静态链接","不附加附加限制","保留许可信息","源代码可用",
               "源代码保留","源代码可用性","修改标注","给予许可人认可","披露来源","许可和版权声明","不得用于商业用途","联系作者",
               "源代码提供","开放源代码"]



class Yishi_Warn_Test(Browser):
    _testMethodDoc = '创建告警策略测试'

    # @unittest.skip
    def test_add_warn_01(self):
        '''创建一条告警策略-只选择组件-名称'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input('a', '123@qq.com')
        Page_action(self.driver).add_warn_rule_soft_name('a')  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_02(self):
        '''创建一条告警策略-只选择组件-版本-等于-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(1),generate_random_email(3))
        Page_action(self.driver).add_warn_rule_soft_version_equal(Ran_str(1))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_03(self):
        '''创建一条告警策略-只选择组件-版本-大于-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(1),generate_random_email(3))
        Page_action(self.driver).add_warn_rule_soft_version_than(Ran_str(1))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_04(self):
        '''创建一条告警策略-只选择组件-版本-大于等于-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(1),generate_random_email(3))
        Page_action(self.driver).add_warn_rule_soft_version_than_equal(Ran_str(1))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_05(self):
        '''创建一条告警策略-只选择组件-版本-小于-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(1),generate_random_email(3))
        Page_action(self.driver).add_warn_rule_soft_version_less(Ran_str(1))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_06(self):
        '''创建一条告警策略-只选择组件-版本-小于等于-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(1),generate_random_email(3))
        Page_action(self.driver).add_warn_rule_soft_version_less_equal(Ran_str(1))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_07(self):
        '''创建告警策略-组件-名称为100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(2), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_soft_name(Ran_str(100))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_08(self):
        '''创建告警策略失败-组件-名称为101个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(2), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_soft_name(Ran_str(101))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text
        self.assertEqual('告警规则数值参数超出范围', a)


    # @unittest.skip
    def test_add_warn_09(self):
        '''创建告警策略失败-告警策略名称为101个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(101), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_soft_name(Ran_str(2))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text
        self.assertEqual('告警规则名称参数长度错误,最大长度为100', a)


    # @unittest.skip
    def test_add_warn_10(self):
        '''创建告警策略失败-告警邮箱为51个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(2), generate_random_email(44))
        Page_action(self.driver).add_warn_rule_soft_name(Ran_str(2))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text
        self.assertEqual('告警接收邮箱地址参数长度错误,最大长度为50', a)

    # @unittest.skip
    def test_add_warn_11(self):
        '''创建告警策略失败-告警邮箱为51个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(2), generate_random_email(44))
        Page_action(self.driver).add_warn_rule_soft_name(Ran_str(2))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text
        self.assertEqual('告警接收邮箱地址参数长度错误,最大长度为50', a)


    # @unittest.skip
    def test_add_warn_12(self):
        '''创建一条告警策略-只选择组件-版本-等于-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(2),generate_random_email(5))
        Page_action(self.driver).add_warn_rule_soft_version_equal(Ran_str(100))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_13(self):
        '''创建一条告警策略-只选择组件-版本-大于-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(2),generate_random_email(5))
        Page_action(self.driver).add_warn_rule_soft_version_than(Ran_str(100))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_14(self):
        '''创建一条告警策略-只选择组件-版本-大于等于-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5),generate_random_email(5))
        Page_action(self.driver).add_warn_rule_soft_version_than_equal(Ran_str(100))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_15(self):
        '''创建一条告警策略-只选择组件-版本-小于-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5),generate_random_email(5))
        Page_action(self.driver).add_warn_rule_soft_version_less(Ran_str(100))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_16(self):
        '''创建一条告警策略-只选择组件-版本-小于等于-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5),generate_random_email(5))
        Page_action(self.driver).add_warn_rule_soft_version_less_equal(Ran_str(100))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_17(self):
        '''创建告警策略失败-组件-版本-等于-101个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(2),generate_random_email(5))
        Page_action(self.driver).add_warn_rule_soft_version_equal(Ran_str(101))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text
        self.assertEqual('告警规则数值参数超出范围', a)

    # @unittest.skip
    def test_add_warn_18(self):
        '''创建告警策略失败-组件-版本-大于-101个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(2),generate_random_email(5))
        Page_action(self.driver).add_warn_rule_soft_version_than(Ran_str(101))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text
        self.assertEqual('告警规则数值参数超出范围', a)


    # @unittest.skip
    def test_add_warn_19(self):
        '''创建告警策略失败--组件-版本-大于等于-101个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5),generate_random_email(5))
        Page_action(self.driver).add_warn_rule_soft_version_than_equal(Ran_str(101))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text
        self.assertEqual('告警规则数值参数超出范围', a)


    # @unittest.skip
    def test_add_warn_20(self):
        '''创建告警策略失败-组件-版本-小于-101个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5),generate_random_email(5))
        Page_action(self.driver).add_warn_rule_soft_version_less(Ran_str(101))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text
        self.assertEqual('告警规则数值参数超出范围', a)


    # @unittest.skip
    def test_add_warn_21(self):
        '''创建告警策略失败-组件-版本-小于等于-101个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5),generate_random_email(5))
        Page_action(self.driver).add_warn_rule_soft_version_less_equal(Ran_str(101))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text
        self.assertEqual('告警规则数值参数超出范围', a)


    # @unittest.skip
    def test_add_warn_22(self):
        '''创建告警策略失败-告警策略名称重复'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input('a', '123@qq.com')
        Page_action(self.driver).add_warn_rule_soft_name(Ran_str(5))  #输入告警策略内容
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略成功提示').text
        self.assertEqual('告警规则名称已存在', a)


    # @unittest.skip
    def test_add_warn_23(self):
        '''创建一条告警策略-只选择漏洞-编号-单字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_id(Ran_str(1))  #输入告警策略内容-漏洞编号
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_24(self):
        '''创建一条告警策略-只选择漏洞-编号-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_id(Ran_str(100))  #输入告警策略内容-漏洞编号
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_25(self):
        '''创建一条告警策略-只选择漏洞-级别-等于-超危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_level_equal("超危")  #输入告警策略内容-漏洞级别
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_26(self):
        '''创建一条告警策略-只选择漏洞-级别-等于-高'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_level_equal("高")  #输入告警策略内容-漏洞级别
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_27(self):
        '''创建一条告警策略-只选择漏洞-级别-等于-中'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_level_equal("中")  #输入告警策略内容-漏洞级别
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_28(self):
        '''创建一条告警策略-只选择漏洞-级别-等于-低'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_level_equal("低")  #输入告警策略内容-漏洞级别
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_29(self):
        '''创建一条告警策略-只选择漏洞-级别-等于-未知'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_level_equal("未知")  #输入告警策略内容-漏洞级别
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_30(self):
        '''创建一条告警策略-只选择漏洞-级别-大于等于-超危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_level_than_equal("超危")  #输入告警策略内容-漏洞级别
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_31(self):
        '''创建一条告警策略-只选择漏洞-级别-大于等于-高'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_level_than_equal("高")  #输入告警策略内容-漏洞级别
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_32(self):
        '''创建一条告警策略-只选择漏洞-级别-大于等于-中'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_level_than_equal("中")  #输入告警策略内容-漏洞级别
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_33(self):
        '''创建一条告警策略-只选择漏洞-级别-大于等于-低'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_level_than_equal("低")  #输入告警策略内容-漏洞级别
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_34(self):
        '''创建一条告警策略-只选择漏洞-级别-大于等于-未知'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_level_than_equal("未知")  #输入告警策略内容-漏洞级别
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_35(self):
        '''创建一条告警策略-只选择漏洞-发布时间-早于'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_ptime_before("11")  #输入告警策略内容-漏洞发布时间
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_36(self):
        '''创建一条告警策略-只选择漏洞-发布时间-晚于'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_ptime_after("11")  #输入告警策略内容-漏洞发布时间
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_37(self):
        '''创建一条告警策略-只选择漏洞-利用成熟度-大于等于-超危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_ripeness_critical()  #告警策略-大于等于-超危
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_38(self):
        '''创建一条告警策略-只选择漏洞-利用成熟度-大于等于-高'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_ripeness_high()  #告警策略-大于等于-高
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_39(self):
        '''创建一条告警策略-只选择漏洞-利用成熟度-大于等于-中'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_ripeness_middle()  #告警策略-大于等于-中
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_40(self):
        '''创建一条告警策略-只选择漏洞-利用成熟度-大于等于-低'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_ripeness_low()  #告警策略-大于等于-低
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_41(self):
        '''创建一条告警策略-只选择漏洞-利用成熟度-大于等于-未知'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_ripeness_unknow()  #告警策略-大于等于-未知
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_42(self):
        '''创建一条告警策略-只选择漏洞-局限性-等于-是'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_limit_yes()  #告警策略-漏洞-局限性-等于-是
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_43(self):
        '''创建一条告警策略-只选择漏洞-局限性-等于-否'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_limit_no()  #告警策略-漏洞-局限性-等于-否
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_44(self):
        '''创建一条告警策略-只选择开源许可证-风险等级-等于-高危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_level_high()  #告警策略-开源许可证-风险等级-等于-高危
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_45(self):
        '''创建一条告警策略-只选择开源许可证-风险等级-等于-中危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_level_middle()  #告警策略-开源许可证-风险等级-等于-中危
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_46(self):
        '''创建一条告警策略-只选择开源许可证-风险等级-等于-低危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_level_low()  #告警策略-开源许可证-风险等级-等于-低危
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_47(self):
        '''创建一条告警策略-只选择开源许可证-风险等级-等于-未知'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_level_unknow()  #告警策略-开源许可证-风险等级-等于-未知
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_48(self):
        '''创建一条告警策略-只选择开源许可证-风险等级-等于-未评级'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_level_null()  #告警策略-开源许可证-风险等级-等于-未评级
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_49(self):
        '''创建一条告警策略-只选择开源许可证-风险等级-大于等于-高危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_level_than_high()  #告警策略-开源许可证-风险等级-大于等于-高危
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_50(self):
        '''创建一条告警策略-只选择开源许可证-风险等级-大于等于-中危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_level_than_middle()  #告警策略-开源许可证-风险等级-大于等于-中危
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_51(self):
        '''创建一条告警策略-只选择开源许可证-风险等级-大于等于-低危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_level_than_low()  #告警策略-开源许可证-风险等级-大于等于-低危
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_52(self):
        '''创建一条告警策略-只选择开源许可证-风险等级-大于等于-未知'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_level_than_unknow()  #告警策略-开源许可证-风险等级-大于等于-未知
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_53(self):
        '''创建一条告警策略-只选择开源许可证-风险等级-大于等于-未评级'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_level_than_null()  #告警策略-开源许可证-风险等级-大于等于-未评级
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_54(self):
        '''创建一条告警策略-开源许可证-著作权类型-等于-商业许可'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_copyright_equal("商业许可")  #告警策略-开源许可证-著作权类型-等于-商业许可
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_55(self):
        '''创建一条告警策略-开源许可证-著作权类型-等于-宽松型'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_copyright_equal("宽松型")  #告警策略-开源许可证-著作权类型-等于-宽松型
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_56(self):
        '''创建一条告警策略-开源许可证-著作权类型-等于-专有自由'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_copyright_equal("专有自由")  #告警策略-开源许可证-著作权类型-等于-专有自由
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_58(self):
        '''创建一条告警策略-开源许可证-著作权类型-等于-公共领域'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_copyright_equal("公共领域")
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_59(self):
        '''创建一条告警策略-开源许可证-著作权类型-等于-特殊限制'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_copyright_equal("特殊限制")
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_60(self):
        '''创建一条告警策略-开源许可证-著作权类型-等于-专利授予'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_copyright_equal("专利授予")
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_61(self):
        '''创建一条告警策略-开源许可证-著作权类型-等于-资源有限'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_copyright_equal("资源有限")
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_62(self):
        '''创建一条告警策略-开源许可证-著作权类型-等于-著佐权型'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_copyright_equal("著佐权型")
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_63(self):
        '''创建一条告警策略-开源许可证-著作权类型-等于-弱著佐权型'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_copyright_equal("弱著佐权型")
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_64(self):
        '''创建一条告警策略-开源许可证-著作权类型-等于-解读中'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_copyright_equal("解读中")
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_65(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-所有'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        for n in range(0,len(prohibit)):
            type = prohibit[n]
            Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)



    # @unittest.skip
    def test_add_warn_66(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-所有'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        for n in range(0,len(Application)):
            type = Application[n]
            Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_67(self):
        '''创建-告警策略失败-只选择漏洞-编号-101个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_cve_id(Ran_str(101))  #输入告警策略内容-漏洞编号
        Page_action(self.driver).save_warn_rule()
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text
        self.assertEqual('告警规则数值参数超出范围', a)


    # @unittest.skip
    def test_add_warn_68(self):
        '''创建一条告警策略-开源许可证-许可证名称-包含-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_name(Ran_str(1))
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_69(self):
        '''创建一条告警策略-开源许可证-许可证名称-包含-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_name(Ran_str(100))
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_70(self):
        '''创建告警策略失败-开源许可证-许可证名称-包含-101个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_name(Ran_str(101))
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text   #断言
        self.assertEqual('告警规则数值参数超出范围', a)


    # @unittest.skip
    def test_add_warn_71(self):
        '''创建告警策略失败-单个条件组内新增21行'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        count = 0
        while count < 20:
            Page_action(self.driver).add_row()
            count += 1
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text   #断言
        self.assertEqual('条件组1,子条件数目不能超过20条！', a)


    # @unittest.skip
    def test_add_warn_72(self):
        '''创建告警策略失败-新增21个条件组'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        count = 0
        while count < 20:
            Page_action(self.driver).warn_rule_add_groups()
            count += 1
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text
        self.assertEqual('条件组不能超过20组！', a)


    # @unittest.skip
    def test_add_warn_73(self):
        '''创建告警策略失败-条件组内容为空'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(Ran_str(5), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_perm_name("")
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_fail, '创建告警策略失败提示').text   #断言
        self.assertEqual('条件组内容不能为空!', a)


    # @unittest.skip
    def test_add_warn_74(self):
        '''编辑告警策略'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()   #修改告警策略按钮
        Page_action(self.driver).add_warn_rule_clear()
        Page_action(self.driver).add_warn_rule_input("修改策略", generate_random_email(3))
        Page_action(self.driver).add_warn_rule_text_clear()
        Page_action(self.driver).add_warn_rule_perm_name(Ran_str(2))
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text   #断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_75(self):
        '''删除告警策略'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).warn_rule_delete_normal()   #删除告警策略按钮
        Page_action(self.driver).warn_rule_delete_yes()
        a = Page(self.driver).get_element(Element.warn_rule_delete_success, '删除告警策略成功提示').text   #断言
        self.assertEqual('删除成功', a)


    # @unittest.skip
    def test_add_warn_76(self):
        '''编辑告警策略-告警策略名称\组件名称为-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()   #修改告警策略按钮
        Page_action(self.driver).add_warn_rule_clear()
        Page_action(self.driver).add_warn_rule_input(Ran_str(1), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_text_clear()   #清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_name(Ran_str(1))
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text   #断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_77(self):
        '''编辑告警策略-组件版本-等于-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()   #修改告警策略按钮
        Page_action(self.driver).add_warn_rule_clear()
        Page_action(self.driver).add_warn_rule_input(Ran_str(1), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_text_clear()   #清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_version_equal(Ran_str(1))
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text   #断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_78(self):
        '''编辑告警策略-组件版本-大于-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()   #修改告警策略按钮
        Page_action(self.driver).add_warn_rule_clear()
        Page_action(self.driver).add_warn_rule_input(Ran_str(1), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_text_clear()   #清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_version_than(Ran_str(1))
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text   #断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_79(self):
        '''编辑告警策略-组件版本-大于等于-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()   #修改告警策略按钮
        Page_action(self.driver).add_warn_rule_clear()
        Page_action(self.driver).add_warn_rule_input(Ran_str(1), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_text_clear()   #清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_version_than_equal(Ran_str(1))
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text   #断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_80(self):
        '''编辑告警策略-组件版本-小于-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()   #修改告警策略按钮
        Page_action(self.driver).add_warn_rule_clear()
        Page_action(self.driver).add_warn_rule_input(Ran_str(1), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_text_clear()   #清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_version_less(Ran_str(1))
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text   #断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_81(self):
        '''编辑告警策略-组件版本-小于等于-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()   #修改告警策略按钮
        Page_action(self.driver).add_warn_rule_clear()
        Page_action(self.driver).add_warn_rule_input(Ran_str(1), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_text_clear()   #清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_version_less_equal(Ran_str(1))
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text   #断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_82(self):
        '''编辑告警策略-组件版本-小于等于-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()   #修改告警策略按钮
        Page_action(self.driver).add_warn_rule_clear()
        Page_action(self.driver).add_warn_rule_input(Ran_str(1), generate_random_email(3))
        Page_action(self.driver).add_warn_rule_text_clear()   #清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_version_less_equal(Ran_str(1))
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text   #断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_83(self):
        '''编辑告警策略-告警策略名称\组件名称为-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_clear()
        Page_action(self.driver).add_warn_rule_input(Ran_str(100), generate_random_email(43))
        Page_action(self.driver).add_warn_rule_text_clear()  # 清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_name(Ran_str(100))
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_84(self):
        '''编辑告警策略-组件版本-等于-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_text_clear()  # 清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_version_equal(Ran_str(100))
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_85(self):
        '''编辑告警策略-组件版本-大于-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_text_clear()  # 清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_version_than(Ran_str(100))
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_86(self):
        '''编辑告警策略-组件版本-大于等于-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_text_clear()  # 清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_version_than_equal(Ran_str(100))
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_87(self):
        '''编辑告警策略-组件版本-小于-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_text_clear()  # 清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_version_less(Ran_str(100))
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_88(self):
        '''编辑告警策略-组件版本-小于等于-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_text_clear()  # 清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_version_less_equal(Ran_str(100))
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_89(self):
        '''编辑告警策略-组件版本-小于等于-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_text_clear()  # 清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_soft_version_less_equal(Ran_str(100))
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_90(self):
        '''编辑告警策略-漏洞编号-包含-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_text_clear()  # 清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_cve_id(Ran_str(1))
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_91(self):
        '''编辑告警策略-漏洞编号-包含-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_text_clear()  # 清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_cve_id(Ran_str(100))
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_92(self):
        '''编辑告警策略-漏洞-级别-等于-超危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_level_equal("超危")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_93(self):
        '''编辑告警策略-漏洞-级别-等于-高'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_level_equal("高")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_94(self):
        '''编辑告警策略-漏洞-级别-等于-中'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_level_equal("中")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_95(self):
        '''编辑告警策略-漏洞-级别-等于-低'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_level_equal("低")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_96(self):
        '''编辑告警策略-漏洞-级别-等于-未知'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_level_equal("未知")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_97(self):
        '''编辑告警策略-漏洞-级别-大于等于-超危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_level_than_equal("超危")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_98(self):
        '''编辑告警策略-漏洞-级别-大于等于-高'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_level_than_equal("高")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_99(self):
        '''编辑告警策略-漏洞-级别-大于等于-中'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_level_than_equal("中")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_100(self):
        '''编辑告警策略-漏洞-级别-大于等于-低'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_level_than_equal("低")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_101(self):
        '''编辑告警策略-漏洞-级别-大于等于-未知'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_level_than_equal("未知")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_102(self):
        '''编辑告警策略-漏洞-利用成熟度-大于等于-超危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_ripeness_critical()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_103(self):
        '''编辑告警策略-漏洞-利用成熟度-大于等于-高'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_ripeness_high()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_104(self):
        '''编辑告警策略-漏洞-利用成熟度-大于等于-中'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_ripeness_middle()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_105(self):
        '''编辑告警策略-漏洞-利用成熟度-大于等于-低'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_ripeness_low()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_106(self):
        '''编辑告警策略-漏洞-利用成熟度-大于等于-未知'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_ripeness_unknow()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_107(self):
        '''编辑告警策略-漏洞-局限性-等于-是'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_limit_yes()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_108(self):
        '''编辑告警策略-漏洞-局限性-等于-否'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_cve_limit_no()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_109(self):
        '''编辑告警策略-开源许可证-名称-包含-单个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_text_clear()  # 清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_perm_name(Ran_str(1))
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_110(self):
        '''编辑告警策略-开源许可证-名称-包含-100个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_text_clear()  # 清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_perm_name(Ran_str(100))
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_111(self):
        '''编辑告警策略-开源许可证-风险等级-等于-高危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_perm_level_high()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_112(self):
        '''编辑告警策略-开源许可证-风险等级-等于-中危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_perm_level_middle()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_113(self):
        '''编辑告警策略-开源许可证-风险等级-等于-低危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_perm_level_low()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_114(self):
        '''编辑告警策略-开源许可证-风险等级-等于-未知'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_perm_level_unknow()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_115(self):
        '''编辑告警策略-开源许可证-风险等级-等于-未评级'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_perm_level_null()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_116(self):
        '''编辑告警策略-开源许可证-风险等级-大于等于-高危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_perm_level_than_high()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_117(self):
        '''编辑告警策略-开源许可证-风险等级-大于等于-中危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_perm_level_than_middle()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_118(self):
        '''编辑告警策略-开源许可证-风险等级-大于等于-低危'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_perm_level_than_low()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_119(self):
        '''编辑告警策略-开源许可证-风险等级-大于等于-未知'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_perm_level_than_unknow()
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_120(self):
        '''编辑告警策略-开源许可证-著作权类型-等于-商业许可'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_copyright_equal("商业许可")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_121(self):
        '''编辑告警策略-开源许可证-著作权类型-等于-宽松型'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_copyright_equal("宽松型")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_122(self):
        '''编辑告警策略-开源许可证-著作权类型-等于-专有自由'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_copyright_equal("专有自由")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_123(self):
        '''编辑告警策略-开源许可证-著作权类型-等于-公共领域'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_copyright_equal("公共领域")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_124(self):
        '''编辑告警策略-开源许可证-著作权类型-等于-特殊限制'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_copyright_equal("特殊限制")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_125(self):
        '''编辑告警策略-开源许可证-著作权类型-等于-专利授予'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_copyright_equal("专利授予")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_126(self):
        '''编辑告警策略-开源许可证-著作权类型-等于-资源有限'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_copyright_equal("资源有限")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_127(self):
        '''编辑告警策略-开源许可证-著作权类型-等于-著佐权型'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_copyright_equal("著佐权型")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_128(self):
        '''编辑告警策略-开源许可证-著作权类型-等于-弱著佐权型'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_copyright_equal("弱著佐权型")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_129(self):
        '''编辑告警策略-开源许可证-著作权类型-等于-解读中'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        Page_action(self.driver).add_warn_rule_text_clear()  # 清空告警策略已输入内容
        Page_action(self.driver).add_warn_rule_copyright_equal("解读中")
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_130(self):
        '''编辑告警策略-开源许可证-禁止行为-包含-all'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        for n in range(0, len(prohibit)):
            type = prohibit[n]
            Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)

    # @unittest.skip
    def test_add_warn_131(self):
        '''编辑告警策略-开源许可证-应用条件-包含-all'''
        super().login_url()
        Page_action(self.driver).login_input(user_name, passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()  # 切换告警策略菜单
        Page_action(self.driver).warn_rule_edit_normal()  # 修改告警策略按钮
        for n in range(0, len(Application)):
            type = Application[n]
            Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  # 保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_edit_success, '编辑告警策略成功提示').text  # 断言
        self.assertEqual('编辑成功', a)


    # @unittest.skip
    def test_add_warn_132(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-专利使用'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'专利使用{Ran_str(1)}', generate_random_email(3))
        type = prohibit[1]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_133(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-可获得开源软件源代码'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'可获得开源软件源代码{Ran_str(1)}', generate_random_email(3))
        type = prohibit[2]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_134(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-包含提醒'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'包含提醒{Ran_str(1)}', generate_random_email(3))
        type = prohibit[3]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_135(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-声明修改'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'声明修改{Ran_str(1)}', generate_random_email(3))
        type = prohibit[4]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_136(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-责任'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'责任{Ran_str(1)}', generate_random_email(3))
        type = prohibit[5]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_137(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-Tivoization禁止'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'Tivoization禁止{Ran_str(1)}', generate_random_email(3))
        type = prohibit[6]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_138(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-保证'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'保证{Ran_str(1)}', generate_random_email(3))
        type = prohibit[7]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_139(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-包含下载说明'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'包含下载说明{Ran_str(1)}', generate_random_email(3))
        type = prohibit[8]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_140(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-使用商标'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'使用商标{Ran_str(1)}', generate_random_email(3))
        type = prohibit[9]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_141(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-开放源代码'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'开放源代码{Ran_str(1)}', generate_random_email(3))
        type = prohibit[10]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_142(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-保留许可信息'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'保留许可信息{Ran_str(1)}', generate_random_email(3))
        type = prohibit[11]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_143(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-商标使用'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'商标使用{Ran_str(1)}', generate_random_email(3))
        type = prohibit[12]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_144(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-技术限制禁止'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'技术限制禁止{Ran_str(1)}', generate_random_email(3))
        type = prohibit[13]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_145(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-专利维权（向开源软件开发者）'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'专利维权（向开源软件开发者）{Ran_str(1)}', generate_random_email(3))
        type = prohibit[14]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_146(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-商用'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'商用{Ran_str(1)}', generate_random_email(3))
        type = prohibit[15]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_147(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-提供担保'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'提供担保{Ran_str(1)}', generate_random_email(3))
        type = prohibit[16]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_148(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-重新许可'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'重新许可{Ran_str(1)}', generate_random_email(3))
        type = prohibit[17]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_149(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-赔偿许可人损失'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'赔偿许可人损失{Ran_str(1)}', generate_random_email(3))
        type = prohibit[18]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_150(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-实施专利授权'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'实施专利授权{Ran_str(1)}', generate_random_email(3))
        type = prohibit[19]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_151(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-使用相同许可'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'使用相同许可{Ran_str(1)}', generate_random_email(3))
        type = prohibit[20]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_152(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-专利'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'专利{Ran_str(1)}', generate_random_email(3))
        type = prohibit[21]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_153(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-限制更改许可'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'限制更改许可{Ran_str(1)}', generate_random_email(3))
        type = prohibit[22]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_154(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-限制技术措施'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'限制技术措施{Ran_str(1)}', generate_random_email(3))
        type = prohibit[23]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_155(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-版权'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'版权{Ran_str(1)}', generate_random_email(3))
        type = prohibit[24]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_156(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-专利禁止'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'专利禁止{Ran_str(1)}', generate_random_email(3))
        type = prohibit[25]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_157(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-剥夺'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'剥夺{Ran_str(1)}', generate_random_email(3))
        type = prohibit[26]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_158(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-追究许可人责任'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'追究许可人责任{Ran_str(1)}', generate_random_email(3))
        type = prohibit[27]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_159(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-联系作者'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'联系作者{Ran_str(1)}', generate_random_email(3))
        type = prohibit[28]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_160(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-专利限制'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'专利限制{Ran_str(1)}', generate_random_email(3))
        type = prohibit[29]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_161(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-保留版权信息'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'保留版权信息{Ran_str(1)}', generate_random_email(3))
        type = prohibit[30]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_162(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-移除或修改版权许可'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'移除或修改版权许可{Ran_str(1)}', generate_random_email(3))
        type = prohibit[31]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_163(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-技术'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'技术{Ran_str(1)}', generate_random_email(3))
        type = prohibit[32]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_164(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-分发'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'分发{Ran_str(1)}', generate_random_email(3))
        type = prohibit[33]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_165(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-重命名开源软件或许可证的相关限制'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'重命名开源软件或许可证的相关限制{Ran_str(1)}', generate_random_email(3))
        type = prohibit[34]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_166(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-再许可'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'再许可{Ran_str(1)}', generate_random_email(3))
        type = prohibit[35]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_167(self):
        '''创建一条告警策略-开源许可证-禁止行为-包含-修改和衍生'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'修改和衍生{Ran_str(1)}', generate_random_email(3))
        type = prohibit[0]
        Page_action(self.driver).add_warn_rule_prohibit_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_168(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-免责声明'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'免责声明{Ran_str(1)}', generate_random_email(3))
        type = Application[0]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_169(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-可观察源代码'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'可观察源代码 {Ran_str(1)}', generate_random_email(3))
        type = Application[1]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_170(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-使用相同许可'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'使用相同许可 {Ran_str(1)}', generate_random_email(3))
        type = Application[2]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_171(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-不得误导性使用名称'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'不得误导性使用名称 {Ran_str(1)}', generate_random_email(3))
        type = Application[3]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_172(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-动态链接'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'动态链接 {Ran_str(1)}', generate_random_email(3))
        type = Application[4]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_173(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-相同的许可证（库）'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'相同的许可证（库） {Ran_str(1)}', generate_random_email(3))
        type = Application[5]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_174(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-可获得开源软件源代码'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'可获得开源软件源代码（库） {Ran_str(1)}', generate_random_email(3))
        type = Application[6]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_175(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-无责任'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'无责任 {Ran_str(1)}', generate_random_email(3))
        type = Application[7]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_176(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-状态变化'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'状态变化 {Ran_str(1)}', generate_random_email(3))
        type = Application[8]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_177(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-重命名开源软件或许可证的相关限制'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'重命名开源软件或许可证的相关限制 {Ran_str(1)}', generate_random_email(3))
        type = Application[9]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_178(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-声明修改'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'声明修改 {Ran_str(1)}', generate_random_email(3))
        type = Application[10]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_179(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-相同的许可证（文件）'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'相同的许可证（文件） {Ran_str(1)}', generate_random_email(3))
        type = Application[11]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_180(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-相同的许可证'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'相同的许可证 {Ran_str(1)}', generate_random_email(3))
        type = Application[12]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_181(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-相同许可证'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'相同许可证 {Ran_str(1)}', generate_random_email(3))
        type = Application[13]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_182(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-版权声明'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'版权声明 {Ran_str(1)}', generate_random_email(3))
        type = Application[14]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_183(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-包含下载说明'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'包含下载说明 {Ran_str(1)}', generate_random_email(3))
        type = Application[15]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_184(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-限制责任'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'限制责任 {Ran_str(1)}', generate_random_email(3))
        type = Application[16]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_185(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-许可'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'许可 {Ran_str(1)}', generate_random_email(3))
        type = Application[17]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_186(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-包含提醒'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'包含提醒 {Ran_str(1)}', generate_random_email(3))
        type = Application[18]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_187(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-共享库链接'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'共享库链接 {Ran_str(1)}', generate_random_email(3))
        type = Application[19]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_188(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-修改的分发'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'修改的分发 {Ran_str(1)}', generate_random_email(3))
        type = Application[20]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_189(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-网络使用是分配'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'网络使用是分配 {Ran_str(1)}', generate_random_email(3))
        type = Application[21]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_190(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-无保证'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'无保证 {Ran_str(1)}', generate_random_email(3))
        type = Application[22]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_191(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-许可证继承'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'许可证继承 {Ran_str(1)}', generate_random_email(3))
        type = Application[23]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_192(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-保留版权信息'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'保留版权信息 {Ran_str(1)}', generate_random_email(3))
        type = Application[24]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_193(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-许可证的延续'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'许可证的延续 {Ran_str(1)}', generate_random_email(3))
        type = Application[25]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_194(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-保留原始版权声明'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'保留原始版权声明 {Ran_str(1)}', generate_random_email(3))
        type = Application[26]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_195(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-专利授权通知'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'专利授权通知 {Ran_str(1)}', generate_random_email(3))
        type = Application[27]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_196(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-静态链接'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'静态链接 {Ran_str(1)}', generate_random_email(3))
        type = Application[28]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_197(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-不附加附加限制'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'不附加附加限制 {Ran_str(1)}', generate_random_email(3))
        type = Application[29]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_198(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-保留许可信息'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'保留许可信息 {Ran_str(1)}', generate_random_email(3))
        type = Application[30]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_199(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-源代码可用'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'源代码可用 {Ran_str(1)}', generate_random_email(3))
        type = Application[31]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_200(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-源代码保留'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'源代码保留 {Ran_str(1)}', generate_random_email(3))
        type = Application[32]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_201(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-源代码可用性'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'源代码可用性 {Ran_str(1)}', generate_random_email(3))
        type = Application[33]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_202(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-修改标注'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'修改标注 {Ran_str(1)}', generate_random_email(3))
        type = Application[34]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_203(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-给与许可人认可'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'给与许可人认可 {Ran_str(1)}', generate_random_email(3))
        type = Application[35]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)


    # @unittest.skip
    def test_add_warn_204(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-披露来源'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'披露来源 {Ran_str(1)}', generate_random_email(3))
        type = Application[36]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_205(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-许可和版权声明'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'许可和版权声明 {Ran_str(1)}', generate_random_email(3))
        type = Application[37]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_206(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-不得用于商业用途'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'不得用于商业用途 {Ran_str(1)}', generate_random_email(3))
        type = Application[38]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_207(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-联系作者'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'联系作者 {Ran_str(1)}', generate_random_email(3))
        type = Application[39]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_208(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-源代码提供 '''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'源代码提供  {Ran_str(1)}', generate_random_email(3))
        type = Application[40]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)

    # @unittest.skip
    def test_add_warn_209(self):
        '''创建一条告警策略-开源许可证-应用条件-包含-开放源代码 '''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).warn_page_click()    #切换告警策略菜单
        Page_action(self.driver).add_warn_rule_click()   #添加告警策略按钮
        Page_action(self.driver).add_warn_rule_input(f'开放源代码  {Ran_str(1)}', generate_random_email(3))
        type = Application[41]
        Page_action(self.driver).add_warn_rule_application_contain(type)
        Page_action(self.driver).save_warn_rule()  #保存告警策略
        a = Page(self.driver).get_element(Element.warn_rule_create_success, '创建告警策略成功提示').text   #断言创建成功
        self.assertEqual('创建成功', a)