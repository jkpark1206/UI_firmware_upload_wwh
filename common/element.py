from selenium.webdriver.common.by import By
import random
import os


class Element:
# 登录模块
    # 账号
    username = (By.XPATH, '//input[@placeholder="请输入用户名"]')
    # 密码
    password = (By.XPATH, '//input[@placeholder="请输入密码"]')
    # 登录
    login = (By.CSS_SELECTOR, '#app > div > div > div.main > div > form > div:nth-child(3) > div > button > span > span')


#固件扫描
    # 添加一个任务
    add_task = (By.XPATH, '//span[contains(text()," 添加任务 ")]')


