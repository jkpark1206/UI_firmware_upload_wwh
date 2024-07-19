from datas.element import Element
import time
from common.basepage import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



class Page_action(Page):
    # 登录页面-输入用户名，密码
    def login_input(self, username, password):
        self.input_text(Element.username, username, "输入用户名")
        self.input_text(Element.password, password, "输入密码")


    # 点击登录
    def login_click(self):
        self.action_click(Element.login,"进行登录")
        time.sleep(2)


#告警策略模块

    #切换告警策略菜单
    def warn_page_click(self):
        self.action_click(Element.warn_page,"切换告警策略菜单")
        time.sleep(2)

    #点击添加告警策略
    def add_warn_rule_click(self):
        self.action_click(Element.add_warn_rule,"添加告警策略")

    #填写告警策略名称、邮箱
    def add_warn_rule_input(self,name,mail):
        self.input_text(Element.warn_rule_name, name, "输入告警策略名称")
        self.input_text(Element.warn_rule_mail, mail, "输入告警策略名称")


    #清空告警策略名称、邮箱
    def add_warn_rule_clear(self):
        self.action_clear(Element.warn_rule_name, "输入告警策略名称")
        self.action_clear(Element.warn_rule_mail, "输入告警策略名称")

    #清空告警策略输入内容
    def add_warn_rule_text_clear(self):
        self.action_clear(Element.warn_rule_text, "清空告警内容")


    #告警策略-组件-名称-包含
    def add_warn_rule_soft_name(self,content):
        self.excute_script_click(Element.warn_rule_soft,'选择组件-告警选项')
        self.excute_script_click(Element.warn_rule_soft_name, '选择组件-名称')
        self.excute_script_click(Element.warn_rule_contain, '选择组件-名称-包含')
        self.input_text(Element.warn_rule_text, content, "输入组件名称-告警内容")


    # 告警策略-组件-版本-等于
    def add_warn_rule_soft_version_equal(self,content):
        self.excute_script_click(Element.warn_rule_soft,'选择组件')
        self.excute_script_click(Element.warn_rule_version, '选择组件-版本')
        self.excute_script_click(Element.warn_rule_version_equal, '选择组件-版本-等于')
        self.input_text(Element.warn_rule_text, content, "输入组件版本-告警内容")

    # 告警策略-组件-版本-大于
    def add_warn_rule_soft_version_than(self,content):
        self.excute_script_click(Element.warn_rule_soft,'选择组件')
        self.excute_script_click(Element.warn_rule_version, '选择组件-版本')
        self.excute_script_click(Element.warn_rule_version_than, '选择组件-版本-大于')
        self.input_text(Element.warn_rule_text, content, "输入组件版本-告警内容")

    # 告警策略-组件-版本-大于等于
    def add_warn_rule_soft_version_than_equal(self,content):
        self.excute_script_click(Element.warn_rule_soft,'选择组件')
        self.excute_script_click(Element.warn_rule_version, '选择组件-版本')
        self.excute_script_click(Element.warn_rule_version_than_equal, '选择组件-版本-大于等于')
        self.input_text(Element.warn_rule_text, content, "输入组件版本-告警内容")

    # 告警策略-组件-版本-小于
    def add_warn_rule_soft_version_less(self,content):
        self.excute_script_click(Element.warn_rule_soft,'选择组件')
        self.excute_script_click(Element.warn_rule_version, '选择组件-版本')
        self.excute_script_click(Element.warn_rule_version_less, '选择组件-版本-小于')
        self.input_text(Element.warn_rule_text, content, "输入组件版本-告警内容")

    # 告警策略-组件-版本-小于等于
    def add_warn_rule_soft_version_less_equal(self,content):
        self.excute_script_click(Element.warn_rule_soft,'选择组件')
        self.excute_script_click(Element.warn_rule_version, '选择组件-版本')
        self.excute_script_click(Element.warn_rule_version_less_equal, '选择组件-版本-小于')
        self.input_text(Element.warn_rule_text, content, "输入组件版本-告警内容")


    # 告警策略-漏洞-编号-包含
    def add_warn_rule_cve_id(self,content):
        self.excute_script_click(Element.warn_rule_cve,'选择漏洞')
        self.excute_script_click(Element.warn_rule_cve_id, '选择漏洞-编号')
        self.excute_script_click(Element.warn_rule_contain, '选择漏洞-编号-包含')
        self.input_text(Element.warn_rule_text, content, "输入漏洞-编号-告警内容")


    # 告警策略-漏洞-级别-等于
    def add_warn_rule_cve_level_equal(self,level):
        self.excute_script_click(Element.warn_rule_cve,'选择漏洞')
        self.excute_script_click(Element.warn_rule_cve_level, '选择漏洞-级别')
        self.excute_script_click(Element.warn_rule_version_equal, '选择漏洞-级别-等于')
        self.excute_script_click(Element().warn_rule_level(level), "输入漏洞-编号-告警内容")


    # 告警策略-漏洞-级别-大于等于
    def add_warn_rule_cve_level_than_equal(self,level):
        self.excute_script_click(Element.warn_rule_cve,'选择漏洞')
        self.excute_script_click(Element.warn_rule_cve_level, '选择漏洞-级别')
        self.excute_script_click(Element.warn_rule_version_than_equal, '选择漏洞-级别-大于等于')
        self.excute_script_click(Element().warn_rule_level(level), "输入漏洞-编号-告警内容")


    # 告警策略-漏洞-发布时间-早于
    def add_warn_rule_cve_ptime_before(self,time):
        self.excute_script_click(Element.warn_rule_cve,'选择漏洞')
        self.excute_script_click(Element.warn_rule_cve_ptime, '选择漏洞-发布时间')
        self.excute_script_click(Element.warn_rule_cve_ptime_before, '选择漏洞-发布时间-早于')
        self.excute_script_click(Element.warn_rule_cve_ptime_click, '点击选择日期')
        self.excute_script_click(Element().warn_rule_time_pick(time),'选择日期')


    # 告警策略-漏洞-发布时间-晚于
    def add_warn_rule_cve_ptime_after(self,time):
        self.excute_script_click(Element.warn_rule_cve,'选择漏洞')
        self.excute_script_click(Element.warn_rule_cve_ptime, '选择漏洞-发布时间')
        self.excute_script_click(Element.warn_rule_cve_ptime_after, '选择漏洞-发布时间-晚于')
        self.excute_script_click(Element.warn_rule_cve_ptime_click, '点击选择日期')
        self.excute_script_click(Element().warn_rule_time_pick(time),'选择日期')


    # 告警策略-漏洞-利用成熟度-大于等于-超危
    def add_warn_rule_cve_ripeness_critical(self):
        self.excute_script_click(Element.warn_rule_cve,'选择漏洞')
        self.excute_script_click(Element.warn_rule_cve_ripeness, '选择漏洞-利用成熟度')
        self.excute_script_click(Element.warn_rule_version_than_equal, '选择漏洞-利用成熟度-大于等于')
        self.excute_script_click(Element.warn_rule_level_critical, '超危')


    # 告警策略-漏洞-利用成熟度-大于等于-高
    def add_warn_rule_cve_ripeness_high(self):
        self.excute_script_click(Element.warn_rule_cve,'选择漏洞')
        self.excute_script_click(Element.warn_rule_cve_ripeness, '选择漏洞-利用成熟度')
        self.excute_script_click(Element.warn_rule_version_than_equal, '选择漏洞-利用成熟度-大于等于')
        self.excute_script_click(Element.warn_rule_cve_level_high, '高')


    # 告警策略-漏洞-利用成熟度-大于等于-中
    def add_warn_rule_cve_ripeness_middle(self):
        self.excute_script_click(Element.warn_rule_cve,'选择漏洞')
        self.excute_script_click(Element.warn_rule_cve_ripeness, '选择漏洞-利用成熟度')
        self.excute_script_click(Element.warn_rule_version_than_equal, '选择漏洞-利用成熟度-大于等于')
        self.excute_script_click(Element.warn_rule_cve_level_middle, '中')


    # 告警策略-漏洞-利用成熟度-大于等于-低
    def add_warn_rule_cve_ripeness_low(self):
        self.excute_script_click(Element.warn_rule_cve,'选择漏洞')
        self.excute_script_click(Element.warn_rule_cve_ripeness, '选择漏洞-利用成熟度')
        self.excute_script_click(Element.warn_rule_version_than_equal, '选择漏洞-利用成熟度-大于等于')
        self.excute_script_click(Element.warn_rule_cve_level_low, '低')

    # 告警策略-漏洞-利用成熟度-大于等于-未知
    def add_warn_rule_cve_ripeness_unknow(self):
        self.excute_script_click(Element.warn_rule_cve,'选择漏洞')
        self.excute_script_click(Element.warn_rule_cve_ripeness, '选择漏洞-利用成熟度')
        self.excute_script_click(Element.warn_rule_version_than_equal, '选择漏洞-利用成熟度-大于等于')
        self.excute_script_click(Element.warn_rule_cve_level_unknow, '未知')

    # 告警策略-漏洞-局限性-等于-是
    def add_warn_rule_cve_limit_yes(self):
        self.excute_script_click(Element.warn_rule_cve,'选择漏洞')
        self.excute_script_click(Element.warn_rule_cve_limit, '选择漏洞-局限性')
        self.excute_script_click(Element.warn_rule_version_equal, '选择漏洞-局限性-等于')
        self.excute_script_click(Element.warn_rule_cve_limit_yes, '是')

    # 告警策略-漏洞-局限性-等于-否
    def add_warn_rule_cve_limit_no(self):
        self.excute_script_click(Element.warn_rule_cve,'选择漏洞')
        self.excute_script_click(Element.warn_rule_cve_limit, '选择漏洞-局限性')
        self.excute_script_click(Element.warn_rule_version_equal, '选择漏洞-局限性-等于')
        self.excute_script_click(Element.warn_rule_cve_limit_no, '否')


    # 告警策略-开源许可证-风险等级-等于-高危
    def add_warn_rule_perm_level_high(self):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_perm_level, '选择开源许可证-风险等级')
        self.excute_script_click(Element.warn_rule_version_equal, '选择开源许可证-风险等级-等于')
        self.excute_script_click(Element.warn_rule_perm_level_high, '高危')

    # 告警策略-开源许可证-风险等级-等于-中危
    def add_warn_rule_perm_level_middle(self):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_perm_level, '选择开源许可证-风险等级')
        self.excute_script_click(Element.warn_rule_version_equal, '选择开源许可证-风险等级-等于')
        self.excute_script_click(Element.warn_rule_perm_level_middle, '中危')

    # 告警策略-开源许可证-风险等级-等于-低危
    def add_warn_rule_perm_level_low(self):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_perm_level, '选择开源许可证-风险等级')
        self.excute_script_click(Element.warn_rule_version_equal, '选择开源许可证-风险等级-等于')
        self.excute_script_click(Element.warn_rule_perm_level_low, '低危')


    # 告警策略-开源许可证-风险等级-等于-未知
    def add_warn_rule_perm_level_unknow(self):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_perm_level, '选择开源许可证-风险等级')
        self.excute_script_click(Element.warn_rule_version_equal, '选择开源许可证-风险等级-等于')
        self.excute_script_click(Element.warn_rule_perm_level_unknow, '未知')


    # 告警策略-开源许可证-风险等级-等于-未评级
    def add_warn_rule_perm_level_null(self):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_perm_level, '选择开源许可证-风险等级')
        self.excute_script_click(Element.warn_rule_version_equal, '选择开源许可证-风险等级-等于')
        self.excute_script_click(Element.warn_rule_perm_level_null, '未评级')



    # 告警策略-开源许可证-风险等级-大于等于-高危
    def add_warn_rule_perm_level_than_high(self):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_perm_level, '选择开源许可证-风险等级')
        self.excute_script_click(Element.warn_rule_version_than_equal, '选择开源许可证-风险等级-大于等于')
        self.excute_script_click(Element.warn_rule_perm_level_high, '高危')

    # 告警策略-开源许可证-风险等级-大于等于-中危
    def add_warn_rule_perm_level_than_middle(self):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_perm_level, '选择开源许可证-风险等级')
        self.excute_script_click(Element.warn_rule_version_than_equal, '选择开源许可证-风险等级-大于等于')
        self.excute_script_click(Element.warn_rule_perm_level_middle, '中危')

    # 告警策略-开源许可证-风险等级-大于等于-低危
    def add_warn_rule_perm_level_than_low(self):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_perm_level, '选择开源许可证-风险等级')
        self.excute_script_click(Element.warn_rule_version_than_equal, '选择开源许可证-风险等级-大于等于')
        self.excute_script_click(Element.warn_rule_perm_level_low, '低危')


    # 告警策略-开源许可证-风险等级-大于等于-未知
    def add_warn_rule_perm_level_than_unknow(self):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_perm_level, '选择开源许可证-风险等级')
        self.excute_script_click(Element.warn_rule_version_than_equal, '选择开源许可证-风险等级-大于等于')
        self.excute_script_click(Element.warn_rule_perm_level_unknow, '未知')


    # 告警策略-开源许可证-风险等级-大于等于-未评级
    def add_warn_rule_perm_level_than_null(self):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_perm_level, '选择开源许可证-风险等级')
        self.excute_script_click(Element.warn_rule_version_than_equal, '选择开源许可证-风险等级-大于等于')
        self.excute_script_click(Element.warn_rule_perm_level_null, '未评级')


    # 告警策略-开源许可证-著作权类型-等于-自选类型
    def add_warn_rule_copyright_equal(self, type):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_copyright, '选择开源许可证-著作权类型')
        self.excute_script_click(Element.warn_rule_version_equal, '选择开源许可证-著作权类型-等于')
        self.excute_script_click(Element().warn_rule_copyright_equal_type(type), '自选类型')


    # 告警策略-开源许可证-禁止行为-包含-自选类型
    def add_warn_rule_prohibit_contain(self, type):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_prohibit, '选择开源许可证-禁止行为')
        self.excute_script_click(Element.warn_rule_contain, '选择开源许可证-禁止行为-包含')
        self.excute_script_click(Element().warn_rule_prohibit_equal_type(type), '自选类型')


    # 告警策略-开源许可证-应用条件-包含-自选类型
    def add_warn_rule_application_contain(self, type):
        self.excute_script_click(Element.warn_rule_perm,'选择开源许可证')
        self.excute_script_click(Element.warn_rule_application, '选择开源许可证-应用条件')
        self.excute_script_click(Element.warn_rule_contain, '选择开源许可证-应用条件-包含')
        self.excute_script_click(Element().warn_rule_application_equal_type(type), '自选类型')


    #告警策略-开源许可证书-名称-包含
    def add_warn_rule_perm_name(self,content):
        self.excute_script_click(Element.warn_rule_perm,'选择-开源许可证')
        self.excute_script_click(Element.warn_rule_perm_name, '选择开源许可证-名称')
        self.excute_script_click(Element.warn_rule_contain, '选择开源许可证-名称-包含')
        self.input_text(Element.warn_rule_text, content, "输入开源许可证名称-告警内容")


    #条件组内新增一行
    def add_row(self):
        self.action_click(Element.group_add_row,'点击新增一行')


    #新增条件组
    def warn_rule_add_groups(self):
        self.action_click(Element.warn_rule_ad_group,'点击添加条件组')

    #普通用户编辑告警策略(全域用户多一列创建时间，所以element有些差别)
    def warn_rule_edit_normal(self):
        self.action_click(Element.warn_rule_edit_icon_normal,'点击修改告警策略')


    #普通用户删除告警策略(全域用户多一列创建时间，所以element有些差别)
    def warn_rule_delete_normal(self):
        self.action_click(Element.warn_rule_delete_icon_normal,'点击删除告警策略')

    #点击确认删除按钮
    def warn_rule_delete_yes(self):
        self.action_click(Element.delete_yes,'确定删除告警策略')

    #告警策略-点击保存
    def save_warn_rule(self):
        self.action_click(Element.warn_rule_save, "保存告警策略")
        time.sleep(1)

#分析策略模块

    #切换分析策略菜单
    def strategy_page_click(self):
        self.action_click(Element.strategy_page,'切换分析策略菜单')

    #点击添加分析策略、输入分析策略名称
    def add_strategy_click(self,name):
        self.strategy_page_click()
        self.action_click(Element.add_strategy_button,'点击添加策略')
        self.input_text(Element.strategy_name_input,name,"输入分析策略名称")

    #取消所有勾选插件
    def checkbox_all_cancel(self):
        plugin_values = [" 1、软件成分探测 "," 2、CVE漏洞查找 "," 3、CWE缺陷查找 "," 4、安全编译选项 ",
                         " 5、敏感信息分析 "," 6、配置项风险识别 "," 7、编码规范检测 "," 8、开源许可证书 "]
        for plugin_value in plugin_values:
            checkbox = self.driver.find_element(By.XPATH,f'//span[text()="{plugin_value}"]//..//..//span//input')
            if checkbox.is_selected():
                self.driver.find_element(By.XPATH,f'//span[text()="{plugin_value}"]//..//..//..//label').click()

    #全选插件
    def all_checkbox(self):
        self.action_click(Element.all_firmware_checkbox,"勾选全插件扫描，加入固件库")

    #勾选软件成分插件
    def soft_checkbox(self):
        self.action_click(Element.strategy_soft,"勾选软件成分插件")

    #勾选CVE插件
    def cve_checkbox(self):
        self.action_click(Element.strategy_cve,"勾选CVE插件")

    #勾选CWE插件
    def cwe_checkbox(self):
        self.action_click(Element.strategy_cwe,"勾选CWE插件")

    #勾选安全编译选项插件
    def safe_checkbox(self):
        self.action_click(Element.strategy_safe,"勾选safe插件")

    #勾选敏感信息插件
    def sensitive_checkbox(self):
        self.action_click(Element.strategy_sensitive,"勾选敏感信息插件")

    #勾选配置项风险识别插件
    def baseline_checkbox(self):
        self.action_click(Element.strategy_baseline,"勾选配置项风险识别插件")

    #勾选编码规范检测插件
    def compliance_checkbox(self):
        self.action_click(Element.strategy_compliance,"勾选编码规范检测插件")

    #勾选开源许可证书插件
    def license_checkbox(self):
        self.action_click(Element.strategy_license,"勾选开源许可证书插件")

    #勾选敏感信息-大陆手机号插件
    def plugin_phone(self):
        self.excute_script_click(Element.phone ,'点击大陆手机号勾选框')

    #勾选敏感信息-用户名/密码插件
    def plugin_user_passwd(self):
        self.excute_script_click(Element.user_passwd ,'点击用户名/密码勾选框')

    #勾选敏感信息-IPv4插件
    def plugin_ipv4(self):
        self.excute_script_click(Element.IPv4 ,'点击IPv4勾选框')

    #勾选敏感信息-IPv6插件
    def plugin_ipv6(self):
        self.excute_script_click(Element.IPv6 ,'点击IPv6勾选框')

    #勾选敏感信息-URIs插件
    def plugin_uris(self):
        self.excute_script_click(Element.URIs ,'点击URIs勾选框')

    #勾选敏感信息-Email插件
    def plugin_email(self):
        self.excute_script_click(Element.Email ,'点击Email勾选框')

    #勾选敏感信息-车辆VIN码插件
    def plugin_vin(self):
        self.excute_script_click(Element.VIN ,'点击车辆VIN码勾选框')

    #勾选敏感信息-GPS坐标插件
    def plugin_gps(self):
        self.excute_script_click(Element.GPS ,'点击GPS坐标勾选框')

    #勾选敏感信息-密钥插件
    def plugin_key(self):
        self.excute_script_click(Element.key ,'点击密钥勾选框')

    #勾许可证分析子插件
    def plugin_license_child(self):
        self.excute_script_click(Element.license_child ,'点击许可证分析勾选框')

    #勾许兼容性分析插件
    def plugin_license_conflict(self):
        self.excute_script_click(Element.license_conflict ,'点击兼容性分析勾选框')

    #分析策略-点击确认创建
    def add_strategy_yes_click(self):
        self.action_click(Element.add_strategy_yes,"点击确认创建")
        time.sleep(1)


#白名单
    #切换白名单菜单
    # def white_page_click(self):
    #     self.action_click(Element.white_page,'切换白名单菜单页')

    #点击创建白名单
    # def add_white_click(self):
    #     self.action_click(Element.add_white_button,'点击添加白名单')

    #创建一条白名单策略
    # def add_white_strategy(self,white_name,soft_name,soft_version,type):
    #     self.white_page_click()
    #     time.sleep(2)
    #     self.add_white_click()
    #     time.sleep(2)
    #     a = self.excute_script_click(Element.white_not_introduce,'')
    #     time.sleep(2)
    #     print(a)

            # self.input_text(Element.white_name, white_name, '输入白名单规则名称')
        # self.excute_script_click(Element.white_soft_name_click , '点击输入框')
        # self.input_text(Element.white_soft_name, soft_name, '输入组件名称')
        # self.input_text(Element.white_soft_version, soft_version, '输入组件版本')
        # time.sleep(3)
        # a = self.get_element(Element.white_soft_type_id, '点击白名单类型下拉框，以便下一步获取下拉框id')
        # time.sleep(2)
        # a = self.driver.execute_script(Element.white_soft_version)
        # ActionChains(self.driver).move_to_element(a)
        # time.sleep(3)
        # print(a)
        # self.excute_script_click(Element().white_not_introduce(a, type), '点击未引入')

    # #白名单-白名单类型-未引入
    # def add_white_not_introduced(self,contribute):
    #     self.action_click(Element.white_soft_type,'点击白名单类型下拉框，以便下一步获取下拉框id')
    #     a = self.action_get_attribute(Element.white_soft_type_id,contribute,'获取未引入下拉框的id')
    #     self.excute_script_click(Element().white_not_introduce(a),'点击未引入')

if __name__ == '__main__':
    copyright = ["商业许可", "宽松型", "专有自由", "公共领域", "特殊限制", "专利授权", "资源有限", "著佐权型", "弱著佐权型", "解读中"]

    prohibit = ["专利使用", "可获得开源软件源代码", "包含提醒", "声明修改", "责任", "Tivoization禁止", "保证", "包含下载说明",
                "使用商标", "开放源代码", "保留许可信息", "商标使用", "技术限制禁止", "专利维权（向开源软件开发者）", "商用",
                "提供担保", "重新许可", "赔偿许可人损失", "实施专利授权", "使用相同许可", "专利", "限制更改许可", "限制技术措施", "版权", "专利禁止",
                "剥夺", "追究许可人责任", "联系作者", "专利限制", "保留版权信息", "移除或修改版权许可", "技术", "分发",
                "重命名开源软件或许可证的相关限制", "再许可", "修改和衍生"]

    Application = ["免责声明", "可观察源代码", "使用相同许可", "不得误导性使用名称", "动态链接", "相同的许可证（库）", "可获得开源软件源代码",
                   "无责任", "状态变化", "重命名开源软件或许可证的相关限制", "声明修改", "相同的许可证（文件）", "相同的许可证", "相同许可证",
                   "版权声明", "包含下载说明", "限制责任", "许可", "包含提醒", "共享库链接", "修改的分发", "网络使用是分配", "无保证", "许可证继承",
                   "保留版权信息", "许可证的延续", "保留原始版权声明", "专利授权通知", "静态链接", "不附加附加限制", "保留许可信息", "源代码可用",
                   "源代码保留", "源代码可用性", "修改标注", "给予许可人认可", "披露来源", "许可和版权声明", "不得用于商业用途", "联系作者",
                   "源代码提供", "开放源代码"]
    print(len(prohibit),Application[27])
