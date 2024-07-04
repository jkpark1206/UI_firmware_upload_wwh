from common.browser import Browser
import time
from config.config import *
import unittest
from selenium.webdriver.common.by import By


class Yishi_firmware_analysis(Browser):
    _testMethodDoc = '固件扫描分析'

    # @unittest.skip
    def test_upload_01(self):
        '''跳转上传固件页面'''
        super().firmware_upload_click()
        try:
           self.assertIn('点击上传',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_01.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_01.__doc__+'.png')


    # @unittest.skip
    def test_upload_02(self):
        '''成功上传固件任务-全选不关联固件库'''
        self.firmware_upload_click()
        file1 = [r"C:\\Users\\anban\\Desktop\\gujianhuizong\\test\\sun.img",
                r"C:\\Users\\anban\\Desktop\\gujianhuizong\\test\\boot.img",
                r"C:\\Users\\anban\\Desktop\\gujianhuizong\\test\\340g.bin"]
        super().upload_firmware_file(file1)
        time.sleep(5)
        # super().upload_firmware_file(file1)
        # time.sleep(5)
        try:
            self.assertNotIn('全插件扫描，漏洞库更新时自动提醒扫描该固件',self.driver.page_source)
        except Exception as e:
            print(self.test_upload_02.__doc__+'运行失败',e)
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_02.__doc__+'.png')


    # @unittest.skip
    def test_upload_03(self):
        '''成功上传固件任务-关联固件库'''
        super().firmware_info_input(firm_path_B,'',FirmName(firm_path_B),'关联固件库')
        super().plugin_all()
        super().upload_click()
        super().task_start()
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_03.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_03.__doc__+'.png')

    # @unittest.skip
    def test_upload_04(self):
        '''成功上传固件任务-不勾选 软件成分探测& CVE漏洞查找  插件'''
        super().firmware_info_input(firm_path_B,'','不勾选软件成分探测&CVE漏洞查找插件','自动化测试')
        super().plugin_check(1)
        super().plugin_check(4)
        super().upload_click()
        super().task_start()
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_04.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_04.__doc__+'.png')

    # @unittest.skip
    def test_upload_05(self):
        '''成功上传固件任务-不勾选  CVE漏洞查找  插件'''
        super().firmware_info_input(firm_path_B,'','不勾选CVE漏洞查找','自动化测试')
        super().plugin_check(2)
        super().plugin_check(4)
        super().upload_click()
        super().task_start()

        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_05.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_05.__doc__+'.png')

    # @unittest.skip
    def test_upload_06(self):
        '''成功上传固件任务-不勾选 文件类型分析 / CPU架构分析 /CWE缺陷查找/ 文件哈希值分析 插件'''
        super().firmware_info_input(r'C:\Users\anban\Desktop\gujianhuizong\test\zsy.zip','zsy.zip','file/cpu/cwe/hash0','file/cpu/cwe/hash0')
        super().plugin_check(3)
        super().upload_click()
        super().task_start()
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_06.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_06.__doc__+'.png')

    # @unittest.skip
    def test_upload_07(self):
        '''成功上传固件任务-不勾选 CPU架构分析 插件'''
        super().firmware_info_input(r'C:\Users\anban\Desktop\gujianhuizong\test\zsy.zip','zsy.zip','cpu0','cpu0')
        super().plugin_check(4)
        super().upload_click()
        super().task_start()
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_07.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_07.__doc__+'.png')

    # @unittest.skip
    def test_upload_08(self):
        '''成功上传固件任务-不勾选 CWE缺陷查找 插件'''
        super().firmware_info_input(firm_path_B,'','不勾选CWE缺陷查找','自动化测试')
        super().upload_click()
        super().task_start()
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_08.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_08.__doc__+'.png')

    # @unittest.skip
    def test_upload_09(self):
        '''成功上传固件任务-不勾选 文件哈希值分析 插件'''
        super().firmware_info_input(r'C:\Users\anban\Desktop\gujianhuizong\test\zsy.zip','zsy.zip','hash0','hash0')
        super().plugin_check(8)
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_09.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_09.__doc__+'.png')

    # @unittest.skip
    def test_upload_10(self):
        '''成功上传固件任务-不勾选 签名分析 插件'''
        super().firmware_info_input(r'C:\Users\anban\Desktop\gujianhuizong\test\zsy.zip','zsy.zip','sign0','sign0')
        super().plugin_check(5)
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_10.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_10.__doc__+'.png')

    # @unittest.skip
    def test_upload_11(self):
        '''成功上传固件任务-不勾选 加密算法分析 插件'''
        super().firmware_info_input(firm_path_B,'','不勾选加密算法分析','自动化测试')
        super().plugin_check(3)
        super().plugin_check(4)
        super().upload_click()
        super().task_start()
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_11.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_11.__doc__+'.png')

    # @unittest.skip
    def test_upload_12(self):
        '''成功上传固件任务-不勾选  ELF分析 插件'''
        super().firmware_info_input(firm_path_B,'','不勾选ELF分析','自动化测试')
        super().plugin_check(5)
        super().plugin_check(4)
        super().upload_click()
        super().task_start()

        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_12.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_12.__doc__+'.png')

    # @unittest.skip
    def test_upload_13(self):
        '''成功上传固件任务-不勾选 IP地址URI和Email探测 插件'''
        super().firmware_info_input(r'C:\Users\anban\Desktop\gujianhuizong\test\zsy.zip','zsy.zip','ip0','ip0')
        super().plugin_check(10)
        super().plugin_check(6)
        super().upload_click()
        super().task_start()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_13.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_13.__doc__+'.png')

    # @unittest.skip
    def test_upload_14(self):
        '''成功上传固件任务-不勾选 敏感信息 插件'''
        super().firmware_info_input(firm_path_B,'','不勾选敏感信息','自动化测试')
        super().plugin_check(7)
        super().plugin_check(4)
        super().upload_click()
        super().task_start()
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_14.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_14.__doc__+'.png')

    # @unittest.skip
    def test_upload_15(self):
        '''成功上传固件任务-不勾选 安全编译选项识别 插件'''
        super().firmware_info_input(firm_path_B,'','不勾选安全编译选项识别','自动化测试')
        super().plugin_check(6)
        super().plugin_check(4)
        super().upload_click()
        super().task_start()

        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(self.test_upload_15.__doc__+'运行失败',e)
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_15.__doc__+'.png')

    # @unittest.skip
    def test_upload_16(self):
        '''上传固件任务失败-不勾选插件'''
        super().firmware_info_input(firm_path_B,'','不勾选插件','自动化测试')
        super().plugin_none()
        try:
            add_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/button[2]')  #定位添加固件按钮
            answer = add_button.is_enabled()  #判断元素是否可点击，False为不可点击，True为可点击
            self.assertIs(False,answer)   #未勾选插件时，添加任务按钮不可点击，断言为False
        except Exception as e:
            print(self.test_upload_16.__doc__+'运行失败',e)
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_16.__doc__+'.png')

    # @unittest.skip
    def test_upload_17(self):
        '''上传固件任务失败-不上传文件'''
        super().firmware_nofile('file','none','none')
        try:
            add_button = self.driver.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div/button[2]')  # 定位添加固件按钮
            answer = add_button.is_enabled()  # 判断元素是否可点击，False为不可点击，True为可点击
            self.assertIs(False,answer)
        except Exception as e:
            print(self.test_upload_17.__doc__+'运行失败',e)
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_17.__doc__+'.png')

    # @unittest.skip
    def test_upload_18(self):
        '''上传固件任务失败-不输入版本名称'''
        super().firmware_info_input(firm_path_B,'','','自动化测试')
        super().upload_click_unable()
        try:
            a = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ab-form-item__error"]').text
            self.assertIn('请输入版本', a)
            add_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/button[2]')  # 定位添加固件按钮
            answer = add_button.is_enabled()  # 判断元素是否可点击，False为不可点击，True为可点击
            self.assertIs(False, answer)
        except Exception as e:
            print(e,self.test_upload_18.__doc__+'运行失败')
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_18.__doc__+'.png')

    # @unittest.skip
    def test_upload_19(self):
        '''上传固件任务失败-不输入厂商名称'''
        super().firmware_info_input(firm_path_B,'','不输入厂商名称','')
        super().upload_click_unable()
        try:
            a = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ab-form-item__error"]').text
            self.assertIn('请输入厂商', a)
            add_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/button[2]')  # 定位添加固件按钮
            answer = add_button.is_enabled()  # 判断元素是否可点击，False为不可点击，True为可点击
            self.assertIs(False, answer)
        except Exception as e:
            print(e,self.test_upload_19.__doc__+'运行失败')
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_19.__doc__+'.png')

    # @unittest.skip
    def test_upload_20(self):
        '''上传固件任务失败-版本为空格'''
        super().firmware_info_input(firm_path_B,'',' ','版本为空格')
        try:
            a = self.driver.find_element(By.CSS_SELECTOR, 'div[class="ab-form-item__error"]').text
            self.assertIn('版本号不能只包含空格', a)
            add_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/button[2]')  # 定位添加固件按钮
            answer = add_button.is_enabled()  # 判断元素是否可点击，False为不可点击，True为可点击
            self.assertIs(False, answer)
        except Exception as e:
            print(e,self.test_upload_20.__doc__+'运行失败')
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_20.__doc__+'.png')

    # @unittest.skip
    def test_upload_21(self):
        '''上传固件任务失败-厂商为空格'''
        super().firmware_info_input(firm_path_B,'','厂商为空格',' ')

        try:
            a = self.driver.find_element(By.CSS_SELECTOR,'div[class="ab-form-item__error"]').text
            self.assertIn('厂商名称不能只包含空格',a)
            add_button = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/button[2]')  # 定位添加固件按钮
            answer = add_button.is_enabled()  # 判断元素是否可点击，False为不可点击，True为可点击
            self.assertIs(False, answer)
        except Exception as e:
            print(e,self.test_upload_21.__doc__+'运行失败')
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_21.__doc__+'.png')

    # @unittest.skip
    def test_upload_22(self):
        '''可取消上传固件任务'''
        super().firmware_info_input(firm_path_B,'','取消上传固件任务','自动化测试')
        super().firmware_cancel_click()

        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(e,self.test_upload_22.__doc__+'运行失败')
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_22.__doc__+'.png')

    # @unittest.skip
    def test_upload_23(self):
        '''覆盖相同任务'''
        super().firmware_info_input(same_task, '', FirmName(same_task), '全选不关联固件库')
        super().plugin_check(4)
        super().upload_click()
        super().firmware_info(same_task, '', FirmName(same_task), '全选不关联固件库')
        super().plugin_check(4)
        super().same_task_continue()
        time.sleep(wait_time)
        try:
           self.assertNotIn('将固件添加至固件库，漏洞库更新时自动提醒扫描该固件。',self.driver.page_source)
        except Exception as e:
           print(e,self.test_upload_23.__doc__+'运行失败')
           self.driver.get_screenshot_as_file(image_dir+self.test_upload_23.__doc__+'.png')

    # @unittest.skip
    def test_upload_24(self):
        '''任务名称筛选任务'''
        super().login_success()
        super().task_name_search('zsy.zip')
        time.sleep(2)
        try:
            self.assertIn('zsy.zip',self.driver.page_source)
        except Exception as e:
            print(e,self.test_upload_24.__doc__+'运行失败')
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_24.__doc__+'.png')

    # @unittest.skip
    def test_upload_25(self):
        '''时间筛选任务'''
        super().login_success()
        super().task_time_search('2022-12-29 00:28:46','2022-12-29 00:28:46')
        time.sleep(2)
        try:
            self.assertNotIn(' R6300-V1.0.2.76_1.0.57.chk ',self.driver.page_source)
        except Exception as e:
            print(e,self.test_upload_25.__doc__+'运行失败')
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_25.__doc__+'.png')

    # @unittest.skip
    def test_upload_26(self):
        '''输入厂商筛选任务'''
        super().login_success()
        super().task_firm_search('all')
        time.sleep(2)
        try:
            self.assertNotIn(' R6300-V1.0.2.76_1.0.57.chk ',self.driver.page_source)
        except Exception as e:
            print(e,self.test_upload_26.__doc__+'运行失败')
            self.driver.get_screenshot_as_file(image_dir+self.test_upload_26.__doc__+'.png')


if __name__ == '__main__':
    Yishi_firmware_analysis()
