import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from common.basepage import *
from config.config import *
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datas.element import Element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select




class Browser(unittest.TestCase):
    _testMethodDoc = '易识UI测试'
    def setUp(self) ->None:
        if Browser=='firefox':
            self.driver=webdriver.Firefox()
        if Browser=='chrome':
            self.driver=webdriver.Chrome()
        if Browser =='ie':
            self.driver=webdriver.Ie()
        else:
            # self.driver=webdriver.Chrome()
            self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.driver.maximize_window()
        self.driver.implicitly_wait(10)


    def tearDown(self) -> None:
        self.driver.quit()


#打开登录首页
    def login_url(self):
        self.driver.get("http://{}" .format(URL))


# 打开修改密码页面
    def register_url(self):
        self.driver.get("http://{}#/register".format(URL))

#固件分析页面（没法直接打开，需要登录）
    def firmware_analysis_url(self):
        self.driver.get("http://{}#/vulnerabilityScanTask".format(URL))




#登录成功
    def login_success(self):
        self.driver.get("http://{}#/vulnerabilityScanTask".format(URL))
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入用户名"]').send_keys(user_name)
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入密码"]').send_keys(passwd)
        self.driver.find_element(By.XPATH,'#app > div > div > div.main > div > form > div:nth-child(3) > div > button > span > span').click()


#点击跳转修改密码
    def register_skip(self):
        self.driver.find_element(By.XPATH,'#app > div > div > div.main > div > form > div:nth-child(3) > a').click()

#输入修改密码信息
    def register_input_data(self,username,newpasswd,S_code):
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入用户名"]').send_keys(username)
        self.driver.find_element(By.NAME,"newpassword").send_keys(newpasswd)
        self.driver.find_element(By.CSS_SELECTOR, '#app > div > div > div.main > div > form > div:nth-child(3) > div > div.el-input > input').send_keys(S_code)

#点击修改密码
    def register_click(self):
        self.driver.find_element(By.CSS_SELECTOR,'#app > div > div > div.main > div > form > div:nth-child(5) > div > div').click()

#点击返回登录页面
    def login_return_click(self):
        self.driver.find_element(By.CSS_SELECTOR,'#app > div > div > div.main > div > form > div:nth-child(4) > a').click()

#点击添加固件任务(从登录开始)
    def firmware_upload_click(self):
        self.login_success()
        self.driver.find_element(By.CSS_SELECTOR,'#app > section > section > main > div > div > div > div > div.action-bar > div.ac-bar > button > span > span').click()

#已登录，点击添加固件任务
    def firmware_upload(self):
        self.driver.find_element(By.CSS_SELECTOR,
                             '#app > section > section > main > div > div > div > div > div.action-bar > div.ac-bar > button > span > span').click()


#上传固件文件
    def upload_firmware_file(self,file):
        A = self.driver.find_element(By.XPATH,'//input[@class="ab-upload__input"]')
        A.send_keys(file)

#点击取消创建固件任务
    def firmware_cancel_click(self):
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/button[1]/span/span').click()

#固件分析任务信息输入
    def firmware_info_input(self, file: object, task_name: object, version: object, firm: object) :
        self.firmware_upload_click()
        self.driver.find_element(By.CSS_SELECTOR,'body > div.ab-dialog__wrapper > div > div.ab-dialog__content > form > div.require.ab-form-item.is-required.asterisk-left > div > div > div > input').send_keys(file)
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入任务名称"]').send_keys(task_name)
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入版本"]').send_keys(version)
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入厂商名称"]').send_keys(firm)

#已登录，上传固件，填写信息
    def firmware_info(self, file: object, task_name: object, version: object, firm: object) :
        self.firmware_upload()
        self.driver.find_element(By.CSS_SELECTOR,'body > div.ab-dialog__wrapper > div > div.ab-dialog__content > form > div.require.ab-form-item.is-required.asterisk-left > div > div > div > input').send_keys(file)
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入任务名称"]').send_keys(task_name)
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入版本"]').send_keys(version)
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入厂商名称"]').send_keys(firm)


#选择插件
    def plugin_check(self,n):
        self.driver.find_element(By.XPATH,'//*[@class="plugin-list ab-checkbox-group"]/label[{}]/span[1]/span'.format(n)).click()
        self.driver.implicitly_wait(2)


#选择所有插件-关联固件库
    def plugin_all(self):
        self.driver.find_element(By.CSS_SELECTOR,'body > div.ab-dialog__wrapper > div > div.ab-dialog__content > form > div:nth-child(2) > div > span:nth-child(2) > label > span.ab-checkbox__label').click()

#不选择插件
    def plugin_none(self):
        A=[1,3,5,6,7]
        for n in A:
            self.driver.find_element(By.XPATH,'//*[@class="plugin-list ab-checkbox-group"]/label[{}]/span[1]/span'.format(n)).click()

#点击【添加任务】，上传固件任务
    def upload_click(self):
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/button[2]/span/span').click()
        locate = (By.XPATH,'//p[contains(text(),"成功添加任务")]')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locate))
        time.sleep(5)

#添加任务按钮为不可点击时，点击按钮
    def upload_click_unable(self):
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/button[2]').click()

#不上传文件
    def firmware_nofile(self,task_name,version,firm):
        self.firmware_upload_click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入任务名称"]').send_keys(task_name)
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入版本"]').send_keys(version)
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入厂商名称"]').send_keys(firm)

#创建相同任务（选择【继续】覆盖任务）
    def same_task_continue(self):
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/button[2]/span/span').click()
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/div[2]/div/button/span/span').click()
        locate = (By.XPATH, '//p[contains(text(),"成功添加任务")]')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locate))

# 创建相同任务（选择【取消】）
    def same_task_cancel(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[3]/div/div[2]/div[2]/div[1]/div/button').click()

#创建相同任务，任务已结束，点击查看报告
    def same_task_report(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[3]/div/div[2]/div[2]/div[2]/div[2]/button').click()

#判断创建任务是否存在相同任务，存在则【覆盖】
    def task_exit_continue(self):
        if '已有检测记录' in self.driver.page_source:
            self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[3]/div/div[2]/div[2]/div[2]/div[1]/button').click()
        else:
            exit()

#开始固件任务
    def task_start(self):
        A = self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div/div[3]/div/div/div[1]/div[3]/div/div[1]/div/table/tbody/tr[1]/td[8]/div/div/span[1]')
        A.find_element(By.CSS_SELECTOR,"use[*|href='#icon_begin_circle']").click()
        locate = (By.XPATH, '//p[contains(text(),"操作成功")]')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locate))



#根据任务名搜索
    def task_name_search(self,kw):
        self.driver.find_element(By.XPATH,'//input[@placeholder="搜索任务名称"]').send_keys(kw)

# 根据时间进行搜索
    def task_time_search(self,st_time,fin_time):
        self.driver.find_element(By.XPATH,'//input[@placeholder="开始日期"]').send_keys(st_time)
        self.driver.find_element(By.XPATH, '//input[@placeholder="结束日期"]').send_keys(fin_time)
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/button[2]/span').click()

# 根据厂商进行搜索
    def task_firm_search(self,kw):
        self.driver.find_element(By.XPATH,'//input[@placeholder="搜索厂商"]').send_keys(kw)


#切换报告对比分析菜单
    def compare_task_change(self):
        self.login_success()
        self.driver.find_element(By.CSS_SELECTOR,'#app > section > aside > div > ul > li:nth-child(2) > div > div > p').click()

#点击新建报告对比
    def compare_task_create_click(self):
        self.driver.find_element(By.CSS_SELECTOR,'#app > section > section > main > div > div > div > div > div.action-bar > div.btn-wrapper > button > span').click()
        self.driver.implicitly_wait(60)

#选择对比报告
    def compare_task_choose(self,n):
        self.driver.find_element(By.XPATH,'//tbody/tr[{}]//span[@class="el-checkbox__input"]'.format(n)).click()


#点击确认对比
    def compare_task_confirm(self):
        self.driver.find_element(By.XPATH,'//button[@class="el-button el-button--default anban-button primary medium selection-button"]').click()


#确认任务完成
    def compare_task_end(self):
        A = By.XPATH,'//tbody/tr[1]/td[4]/div/span'
        return A


#全选创建对比任务
    def compare_choose_all(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[3]/div/div[1]/div[2]/table/thead/tr/th[1]/div/label/span/span').click()

#对比报告-筛选任务
    def choose_task(self,kw):
        self.driver.find_element(By.XPATH,'//input[@placeholder="搜索扫描任务"]').send_keys(kw)
        # self.driver.find_element(By.XPATH, '//input[@placeholder="搜索扫描任务"]').clear()

#搜索厂商筛选对比任务
    def firm_click(self,firm):
        self.driver.find_element(By.XPATH,'//input[@placeholder="搜索厂商"]').send_keys(firm)

#选择时间筛选对比任务
    def time_click(self,start_time,end_time):
        self.driver.find_element(By.XPATH,'//input[@placeholder="开始日期"]').send_keys(start_time)
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH,'//input[@placeholder="结束日期"]').send_keys(end_time)
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/button[2]/span').click()

#跳转页面
    def page_skip(self,n):
        self.driver.find_element(By.XPATH,'//ul[@class="el-pager"]/li[{}]'.format(n)).click()
        time.sleep(2)

#往右跳转页面
    def page_right(self):
        self.driver.find_element(By.XPATH,'//i[@class="el-icon el-icon-arrow-right"]').click()
        time.sleep(2)

#往左跳转页面
    def page_left(self):
        self.driver.find_element(By.XPATH,'//i[@class="el-icon el-icon-arrow-left"]').click()
        time.sleep(2)

#返回对比报告列表页
    def back_compare_list(self):
        self.driver.find_element(By.XPATH,'//p[@class="back-img"]').click()

#查看对比报告
    def compare_task_report(self,n):
        self.driver.find_element(By.XPATH,'//table/tbody/tr[{}]/td[6]/div/span'.format(n)).click()

#对比报告加载
    def compare_report_load(self):
        A = (By.ID,'report_title')
        return A


#系统信息模块

#跳转系统信息菜单
    def sys_page(self):
        self.login_success()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/aside/div/ul/li[3]/div/div/p').click()
        system_load = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div/div[4]/div[4]/div/div[2]/h1[1]')
        #WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(system_load, '每日任务上限'))
        time.sleep(5)

#确认跳转系统信息菜单栏
    def system_page_load(self):
        system_load = (By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[3]/div[4]/div/div[1]/h1[1]')
        return system_load

#点击系统信息总览菜单
    def sys_all_page(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[3]/div/div[2]/span').click()


 #下载系统总的CPU图片
    def sys_all_cpu(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]').click()


#点击license管理菜单
    def sys_license_page(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[3]/div/div[3]/span').click()


#点击导入离线授权文件
    def import_offline_file(self,file):
        self.sys_license_page()
        self.driver.find_element(By.XPATH,'input[class="ab-upload__input"]').send_keys(file)
        a = (By.CSS_SELECTOR,'p[class="tips blod"]')
        WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element(a,'校验失败'))


#点击打开【在线授权】页面
    def online_update_page(self):
        self.sys_license_page()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[4]/div/div[1]/p[1]').click()

#输入授权码
    def online_empower_input(self,code):
        self.driver.find_element(By.CSS_SELECTOR,'div[class="ab-input ab-input--medium ab-input-suffix--password-clear"]>div  >input').send_keys(code)
        time.sleep(5)
#点击刷新
    def online_update_click(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[4]/div/div[2]/div[1]/button/span/span').click()
        a = (By.CSS_SELECTOR,'p[class="ab-message__message"]')
        WebDriverWait(self.driver,5).until(EC.presence_of_element_located(a))


#点击授权
    def online_empower_click(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[4]/div/div[2]/div[1]/button').click()
        # a = (By.CSS_SELECTOR,'p[class="ab-message__message"]')
        # WebDriverWait(self.driver,5).until(EC.presence_of_element_located(a))






# -------------------------------固件库管理----------------------------------------

#跳转固件库管理菜单
    def firmware_lib_page(self):
        self.driver.get("http://{}".format(URL))
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入用户名"]').send_keys(user_name)
        self.driver.find_element(By.XPATH, '//input[@placeholder="请输入密码"]').send_keys(passwd)
        self.driver.find_element(By.CSS_SELECTOR,'#app > div > div > div.main > div > form > div:nth-child(4) > div > div').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/aside/div/ul/li[5]/div/div/p[1]').click()
        lib_load = (By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[1]/div[1]/div/button/span/span')
        WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(lib_load, '添加固件'))


#上传固件库任务
    def firm_upload_click(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[1]/div[1]/div/button/span/span').click()
        add_task = (By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[4]/div/div[1]/span')
        WebDriverWait(self.driver,5).until(EC.text_to_be_present_in_element(add_task,'添加任务'))

    def file_upload_click(self,file):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/section/section/main/div/div/div/div[4]/div/div[2]/form/div/div[1]/div/div/div/input').send_keys(file)


# #下拉选项-第一个下拉框
#     def warn_soft_select(self):
#         # 下拉框为input，但元素不可见，定位到下拉框中的元素，使用execute_script方法执行点击动作
#         element = self.driver.find_element(By.XPATH,'//ul[@class="ab-scrollbar__view ab-select-dropdown__list"]//li//span[text()="组件"]')
#         self.driver.execute_script("arguments[0].click();", element)



        # s.select_by_visible_text('组件')
