from selenium.webdriver.common.by import By


class Element:

# 登录模块
    # 输入用户名
    username = (By.XPATH, '//input[@placeholder="请输入用户名"]')
    # 输入密码
    password = (By.XPATH, '//input[@placeholder="请输入密码"]')
    # 点击登录
    login = (By.XPATH, '//span[contains(text(),"登录")]')

#登录错误提示
    #用户名/密码为空
    input_null_tip = (By.XPATH,'//div[@class="ab-form-item__error"]')

    #用户名/密码错误
    login_wrong_tip = (By.XPATH,'//p[@class="ab-alert__message"]/span') #class="ab-message__message"


#修改密码
# 修改密码
    update_password = (By.XPATH, '//a[contains(text(),"修改密码")]')
    # 输入账号
    new_username = (By.XPATH, '//input[@placeholder="请输入您的账号"]')
    # 输入新密码
    new_password = (By.XPATH, '//input[@placeholder="请输入您的密码" and @name="newpassword"]')
    # 输入密保
    mibao = (By.XPATH, '//div[@class="el-input"]//input[@placeholder="请输入您的密码"]')
    # 修改密码
    set_update = (By.XPATH, '//button[contains(text(),"修改密码")]')


#固件扫描分析
    #添加固件任务按钮
    add_task = (By.XPATH,'//span[contains(text()," 添加任务 ")]')


#告警策略
    #告警策略菜单
    warn_page = (By.XPATH,'//p[contains(text(),"告警策略")]')

    #添加告警策略菜单
    add_warn_rule = (By.XPATH, '//span[contains(text(),"添加告警策略")]')

    # 输入告警规则名称
    warn_rule_name = (By.XPATH, '//input[@placeholder="请输入规则名称"]')

    # 输入告警规则接收邮箱
    warn_rule_mail = (By.XPATH, '//input[@placeholder="请输入邮箱地址"]')

    # 告警策略-单个条件组-组件（下拉框为input，但元素不可见，定位到下拉框中的元素，使用execute_script方法执行点击动作）
    warn_rule_soft = (By.XPATH,'//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="组件"]')

    # 告警策略-单个条件组-组件-名称
    warn_rule_soft_name = (By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="名称"]')

    # 告警策略-单个条件组-包含
    warn_rule_contain = (
    By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="包含"]')


    # 告警策略-内容输入
    warn_rule_text = (By.XPATH, '//input[@placeholder="请输入"]')


    # 告警策略-单个条件组-组件-版本
    warn_rule_version =  (By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="版本"]')

    # 告警策略-单个条件组-组件-版本-等于
    warn_rule_version_equal = (By.XPATH, '//span[text()="等于"]')


    # 告警策略-单个条件组-组件-版本-大于
    warn_rule_version_than = (By.XPATH, '//span[text()="大于"]')

    # 告警策略-单个条件组-组件-版本-大于等于
    warn_rule_version_than_equal = (By.XPATH, '//span[text()="大于等于"]')

    # 告警策略-单个条件组-组件-版本-小于
    warn_rule_version_less = (By.XPATH, '//span[text()="小于"]')

    # 告警策略-单个条件组-组件-版本-小于等于
    warn_rule_version_less_equal = (By.XPATH, '//span[text()="小于等于"]')

    # 告警策略-保存
    warn_rule_save = (By.XPATH, '//span[text()="保存"]')

    # 告警策略-创建成功提示
    warn_rule_create_success = (By.XPATH, '//p[text()="创建成功"]')

    # 告警策略-创建失败提示
    warn_rule_create_fail = (By.XPATH, '//div[@class="ab-message ab-message--error"]//p')

    #告警策略-编辑成功提示
    warn_rule_edit_success = (By.XPATH, '//p[text()="编辑成功"]')


    # 告警策略-删除成功提示
    warn_rule_delete_success = (By.XPATH, '//p[text()="删除成功"]')


    # # 告警策略-提示信息
    warn_rule_create_message = (By.XPATH, '//div[@class="ab-message ab-message--error"]//p')


    # 告警策略-单个条件组-漏洞（下拉框为input，但元素不可见，定位到下拉框中的元素，使用execute_script方法执行点击动作）
    warn_rule_cve = (By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="漏洞"]')

    # 告警策略-单个条件组-漏洞-编号
    warn_rule_cve_id = (By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="编号"]')


    # 告警策略-单个条件组-漏洞-级别
    warn_rule_cve_level = (By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="级别"]')


    # 告警策略-漏洞-级别-可输入级别等级内容进行选择
    def warn_rule_level(self,level):
        cve_level = (By.XPATH, f'//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="{level}"]')
        return cve_level

    # 告警策略-漏洞-级别-超危
    warn_rule_level_critical =(
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="超危"]')

    # 告警策略-漏洞-级别-高
    warn_rule_cve_level_high = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="高"]')


    # 告警策略-漏洞-级别-中
    warn_rule_cve_level_middle = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="中"]')


    # 告警策略-漏洞-级别-低
    warn_rule_cve_level_low = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="低"]')


    # 告警策略-漏洞-级别-未知
    warn_rule_cve_level_unknow = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="未知"]')


    # 告警策略-单个条件组-开源许可证（下拉框为input，但元素不可见，定位到下拉框中的元素，使用execute_script方法执行点击动作）
    warn_rule_perm = (By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="开源许可证"]')


    # 告警策略-单个条件组-许可证-风险等级
    warn_rule_perm_level = (By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="风险等级"]')


    # 告警策略-许可证-等级-高危
    warn_rule_perm_level_high = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="高危"]')


    # 告警策略-许可证-等级-中危
    warn_rule_perm_level_middle = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="中危"]')


    # 告警策略-许可证-等级-低危
    warn_rule_perm_level_low = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="低危"]')


    # 告警策略-许可证-等级-未知
    warn_rule_perm_level_unknow = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="未知"]')


    # 告警策略-许可证-等级-未评级
    warn_rule_perm_level_null = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="未评级"]')


    # 告警策略-单个条件组-漏洞-发布时间
    warn_rule_cve_ptime = (By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="发布时间"]')

    # 告警策略-单个条件组-漏洞-发布时间-早于
    warn_rule_cve_ptime_before = (By.XPATH, '//span[text()="早于"]')

    # 告警策略-单个条件组-漏洞-发布时间-晚于
    warn_rule_cve_ptime_after = (By.XPATH, '//span[text()="晚于"]')

    # 告警策略-单个条件组-漏洞-发布时间-时间选择
    warn_rule_cve_ptime_click = (By.XPATH, '//input[@placeholder="选择日期"]')


    # 告警策略-漏洞-发布时间-选择日期
    def warn_rule_time_pick(self, day):
        time_pick = (By.XPATH, f'//span[text()={day}]')
        return time_pick


    # 告警策略-单个条件组-漏洞-利用成熟度
    warn_rule_cve_ripeness = (By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="利用成熟度"]')


    # 告警策略-单个条件组-漏洞-局限性
    warn_rule_cve_limit = (
    By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="局限性"]')


    # 告警策略-漏洞-局限性-是
    warn_rule_cve_limit_yes = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="是"]')


    # 告警策略-漏洞-局限性-否
    warn_rule_cve_limit_no = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="否"]')


    #告警策略-开源许可证-著作权类型
    warn_rule_copyright = (By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="著作权类型"]')


    # 告警策略-开源许可证-著作权类型-等于-【copyright】
    def warn_rule_copyright_equal_type(self,type):
        copyright_type = (By.XPATH,f'//span[text()="{type}"]')
        return copyright_type

    #告警策略-开源许可证-禁止行为
    warn_rule_prohibit = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="禁止行为"]')


    # 告警策略-开源许可证-著作权类型-等于-【prohibit】
    def warn_rule_prohibit_equal_type(self,type):
        prohibit_type = (By.XPATH,f'//span[text()="{type}"]')
        return prohibit_type


    #告警策略-开源许可证-应用条件
    warn_rule_application = (
        By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="应用条件"]')


    # 告警策略-开源许可证-著作权类型-等于-【Application】
    def warn_rule_application_equal_type(self, type):
        application_type = (By.XPATH, f'//span[text()="{type}"]')
        return application_type


    # 告警策略-单个条件组-开源许可证书-名称
    warn_rule_perm_name = (By.XPATH, '//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="证书名称"]')


    #条件组1，新增一行
    group_add_row = (By.XPATH, '//div[@class="tableWarp"][1]//span[text()="新增一行"]')


    # 新增条件组
    warn_rule_ad_group = (By.XPATH, '//span[text()="添加条件组"]')


    #编辑告警策略按钮-页面上最新的一个告警策略-普通用户
    warn_rule_edit_icon_normal = (By.XPATH, '//tbody//tr[1]//td[3]//div[@class="edit"]//*[name()="svg"and @class="icon ab-icon"][1]')


    # 删除告警策略按钮-普通用户
    warn_rule_delete_icon_normal = (
    By.XPATH, '//tbody//tr[1]//td[3]//div[@class="edit"]//*[name()="svg"and @class="icon ab-icon"][2]')


    #告警策略-确定删除按钮
    delete_yes = (By.XPATH,'//span[text()=" 确定 "]')

    #告警策略-取消删除
    delete_no = (By.XPATH, '//span[text()="取消"]')


#分析策略
    #分析策略菜单
    strategy_page = (By.XPATH,'//p[text()="分析策略" ]')

    #添加分析策略按钮
    add_strategy_button = (By.XPATH,'//span[text()=" 添加策略 " ]')

    #添加策略弹框-策略名称
    strategy_name = (By.XPATH,'//label[text()=" 策略名称 "]')

    #查找上一层元素（父元素）
    parent_element = (By.XPATH,'..')

    #输入策略名称
    strategy_name_input = (By.XPATH,'//label[text()=" 策略名称 "]//..//div//div//div//input')

    #全插件扫描-勾选框
    all_firmware_checkbox = (By.XPATH,'//input[@value="全插件扫描，漏洞库更新时自动提醒扫描该固件"]//..')

    #软件成分插件勾选框
    strategy_soft = (By.XPATH,'//span[text()=" 1、软件成分探测 "]//..//..//..//label')

    # CVE插件勾选框
    strategy_cve = (By.XPATH, '//span[text()=" 2、CVE漏洞查找 "]//..//..//..//label')

    #CWE插件勾选框
    strategy_cwe = (By.XPATH, '//span[text()=" 3、CWE缺陷查找 "]//..//..//..//label')

    #安全编译选项插件勾选框
    strategy_safe = (By.XPATH, '//span[text()=" 4、安全编译选项 "]//..//..//span')

    #敏感信息分析插件勾选框
    strategy_sensitive = (By.XPATH, '//span[text()=" 5、敏感信息分析 "]//..//..//..//label')

    #配置项风险插件勾选框
    strategy_baseline = (By.XPATH, '//span[text()=" 6、配置项风险识别 "]//..//..//..//label')

    #编码规范检测插件勾选框
    strategy_compliance = (By.XPATH, '//span[text()=" 7、编码规范检测 "]//..//..//..//label')

    #开源许可证书插件勾选框
    strategy_license = (By.XPATH, '//span[text()=" 8、开源许可证书 "]//..//..//..//label')

    #恶意软件检测
    strategy_malware = (By.XPATH, '//span[text()=" 9、恶意软件检测 "]//..//..//..//label')

    #密钥勾选框
    key = (By.XPATH, '//span[text()=" 密钥 "]//..//span')

    #用户名/密码
    user_passwd = (By.XPATH, '//span[text()=" 用户名/密码 "]//..//span')

    # IPv4
    IPv4 = (By.XPATH, '//span[text()=" IPv4 "]//..//span')

    # IPv6
    IPv6 = (By.XPATH, '//span[text()=" IPv6 "]//..//span')

    # URIs
    URIs  = (By.XPATH, '//span[text()=" URIs "]//..//span')

    # Email
    Email  = (By.XPATH, '//span[text()=" Email "]//..//span')

    # 车辆VIN码
    VIN = (By.XPATH, '//span[text()=" 车辆VIN码 "]//..//span')

    # GPS
    GPS = (By.XPATH, '//span[text()=" GPS坐标 "]//..//span')

    # phone
    phone = (By.XPATH, '//span[text()=" 大陆手机号 "]//..//span')

    # 许可证分析
    license_child = (By.XPATH, '//span[text()=" 许可证分析 "]//..//span')

    # 兼容性分析
    license_conflict = (By.XPATH, '//span[text()=" 兼容性分析 "]//..//span')

    #确认创建
    add_strategy_yes = (By.XPATH,'//span[text()="确认创建"]')

    #分析策略创建成功提示
    add_strategy_success = (By.XPATH,'//div[@class="ab-message ab-message--success"]//p')

    #弹框提示信息
    alert_message = (By.XPATH,'//p[@class="ab-message__message"]')


#白名单
    #白名单菜单
    white_page = (By.XPATH,'//p[text()="白名单" ]')

    # 添加白名单按钮
    add_white_button = (By.XPATH, '//span[text()=" 添加白名单规则 " ]')

    # 添加白名单弹框-规则名称
    white_name = (By.XPATH, '//input[@placeholder="请输入规则名称"]')

    #点击组件名称输入框
    white_soft_name_click = (By.XPATH ,'//input[@placeholder="请输入"]//..//..')

    #输入组件名称
    white_soft_name = (By.XPATH ,'//input[@placeholder="请输入"]')

    # 输入组件版本
    white_soft_version = (By.XPATH, '//input[@placeholder="请选择组件版本"]')

    # 输入组件白名单类型
    white_soft_type = (By.XPATH, '//table//tbody//tr[1]//td[3][@class="ab-table_1_column_3 ab-table__cell"]')

    #获取组件白名单类型下拉框id
    white_soft_type_id = (By.XPATH ,'//table//tbody//tr[1]//td[3]//div[@class="select-trigger ab-tooltip__trigger"]')

    #选择未引入
    # def white_not_introduce(self,id,type):
    #     not_introduce_element = (By.XPATH,f'//div[@id="{id}"]//span[text()="{type}"]')
    #     return not_introduce_element
    white_not_introduce = (By.XPATH, '//span[text()="未引入"]')