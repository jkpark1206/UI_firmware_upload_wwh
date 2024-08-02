import time
from config.config import *
from common.action import Page_action
from common.browser import Browser
from common.basepage import Page
from datas.element import Element
from common.Random_str import *
import unittest


class Yishi_Strategy_Test(Browser):
    _testMethodDoc = '创建分析策略测试'

    # @unittest.skip
    def test_add_strategy_01(self):
        '''创建一条分析策略-全选插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'固件库-全选插件{Ran_str(1)}')
        Page_action(self.driver).all_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_02(self):
        '''创建一条分析策略-只勾选软件成分插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选软件成分插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).soft_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)


    # @unittest.skip
    def test_add_strategy_03(self):
        '''创建一条分析策略-只勾选cve插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选CVE插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).cve_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)


    # @unittest.skip
    def test_add_strategy_04(self):
        '''创建一条分析策略-只勾选cwe插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选CWE插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).cwe_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_05(self):
        '''创建一条分析策略-只勾选safe插件,分析策略名称为64个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选safe插件{Ran_str(55)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).safe_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)


    # @unittest.skip
    def test_add_strategy_06(self):
        '''创建一条分析策略-只勾选敏感信息插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选敏感信息插件{Ran_str(55)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).sensitive_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)


    # @unittest.skip
    def test_add_strategy_07(self):
        '''创建一条分析策略-只勾选配置项风险识别插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选配置项风险识别插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).baseline_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)


    # @unittest.skip
    def test_add_strategy_08(self):
        '''创建一条分析策略-只勾选编码规范检测插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选编码规范检测插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).compliance_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_9(self):
        '''创建一条分析策略-只勾选开源许可证插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选开源许可证插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).license_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_10(self):
        '''创建一条分析策略-全选插件-非固件库'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'全选插件-非固件库{Ran_str(1)}')
        Page_action(self.driver).cwe_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_11(self):
        '''创建一条分析策略-创建失败-策略名称为空'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click('')
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.input_null_tip, '创建失败提示').text
        self.assertIn('请输入策略名称', a)

    # @unittest.skip
    def test_add_strategy_12(self):
        '''创建一条分析策略-创建失败-策略名称为空格'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(' ')
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.alert_message, '创建失败提示').text
        self.assertEqual('策略名称参数长度错误,最小长度为1', a)

    # @unittest.skip
    def test_add_strategy_13(self):
        '''创建一条分析策略-创建失败-策略名称为65个字符'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(Ran_str(65))
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.input_null_tip, '创建失败提示').text
        self.assertIn('字段长度过长，不能超过64个字符', a)

    # @unittest.skip
    def test_add_strategy_14(self):
        '''创建一条分析策略-创建失败-未勾选插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(Ran_str(1))
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.input_null_tip, '创建失败提示').text
        self.assertIn('请选择至少一项插件配置', a)

    # @unittest.skip
    def test_add_strategy_15(self):
        '''创建一条分析策略-创建成功-只勾选用户名/密码插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选用户名/密码插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).plugin_user_passwd()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_16(self):
        '''创建一条分析策略-创建成功-只勾选IPv4插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选IPv4插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).plugin_ipv4()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_17(self):
        '''创建一条分析策略-创建成功-只勾选IPv6插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选IPv6插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).plugin_ipv6()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_18(self):
        '''创建一条分析策略-创建成功-只勾选URIs插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选URIs插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).plugin_uris()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_19(self):
        '''创建一条分析策略-创建成功-只勾选Email插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选Email插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).plugin_email()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)


    # @unittest.skip
    def test_add_strategy_20(self):
        '''创建一条分析策略-创建成功-只勾选车辆VIN码插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选车辆VIN码插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).plugin_vin()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_21(self):
        '''创建一条分析策略-创建成功-只勾选GPS坐标插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选GPS坐标插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).plugin_gps()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_22(self):
        '''创建一条分析策略-创建成功-只勾选大陆手机号插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选大陆手机号插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).plugin_phone()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_23(self):
        '''创建一条分析策略-创建成功-只勾选密钥插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选密钥插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).plugin_key()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_24(self):
        '''创建一条分析策略-创建成功-敏感信息子插件组合（phone/key/vin/user-passwd）'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'敏感信息子插件组合（phone/key/vin/user-passwd）{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).plugin_key()
        Page_action(self.driver).plugin_phone()
        Page_action(self.driver).plugin_vin()
        Page_action(self.driver).plugin_user_passwd()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_25(self):
        '''创建一条分析策略-创建成功-只勾选许可证分析子插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选许可证分析子插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).plugin_license_child()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_26(self):
        '''创建一条分析策略-创建成功-勾选兼容性分析子插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'勾选兼容性分析插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).plugin_license_conflict()
        a = Page(self.driver).get_element(Element.license_child, '许可证分析子插件不可点击').is_displayed()
        self.assertEqual(False , a)


    # @unittest.skip
    def test_add_strategy_27(self):
        '''创建一条分析策略-只勾选恶意软件检测插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'只勾选恶意软件检测插件{Ran_str(1)}')
        Page_action(self.driver).checkbox_all_cancel()
        Page_action(self.driver).malware_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_28(self):
        '''创建一条分析策略-不勾选恶意软件检测插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'不勾选恶意软件检测插件{Ran_str(1)}')
        Page_action(self.driver).all_checkbox()
        Page_action(self.driver).malware_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_29(self):
        '''创建一条分析策略-不勾选soft插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'不勾选soft插件{Ran_str(1)}')
        Page_action(self.driver).all_checkbox()
        Page_action(self.driver).soft_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)


    # @unittest.skip
    def test_add_strategy_30(self):
        '''创建一条分析策略-不勾选cve插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'不勾选cve插件{Ran_str(1)}')
        Page_action(self.driver).all_checkbox()
        Page_action(self.driver).cve_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_31(self):
        '''创建一条分析策略-不勾选cwe插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'不勾选cwe插件{Ran_str(1)}')
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)


    # @unittest.skip
    def test_add_strategy_32(self):
        '''创建一条分析策略-不勾选safe插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'不勾选safe插件{Ran_str(1)}')
        Page_action(self.driver).all_checkbox()
        Page_action(self.driver).safe_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

    # @unittest.skip
    def test_add_strategy_33(self):
        '''创建一条分析策略-不勾选敏感信息插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'不勾选敏感信息插件{Ran_str(1)}')
        Page_action(self.driver).all_checkbox()
        Page_action(self.driver).sensitive_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)


    # @unittest.skip
    def test_add_strategy_34(self):
        '''创建一条分析策略-不勾选配置项风险插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'不勾选配置项风险插件{Ran_str(1)}')
        Page_action(self.driver).all_checkbox()
        Page_action(self.driver).baseline_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)


    # @unittest.skip
    def test_add_strategy_35(self):
        '''创建一条分析策略-不勾选编码规范检测插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'不勾选编码规范检测插件{Ran_str(1)}')
        Page_action(self.driver).all_checkbox()
        Page_action(self.driver).compliance_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)


    # @unittest.skip
    def test_add_strategy_36(self):
        '''创建一条分析策略-不勾选开源许可证书插件'''
        super().login_url()
        Page_action(self.driver).login_input(user_name,passwd)
        Page_action(self.driver).login_click()
        Page_action(self.driver).add_strategy_click(f'不勾选开源许可证书插件{Ran_str(1)}')
        Page_action(self.driver).all_checkbox()
        Page_action(self.driver).license_checkbox()
        Page_action(self.driver).add_strategy_yes_click()
        a = Page(self.driver).get_element(Element.add_strategy_success, '创建成功提示').text
        self.assertEqual('分析策略创建成功！', a)

