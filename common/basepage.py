from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.select import Select


class Page():
    def __init__(self, driver: WebDriver, ):
        self.driver = driver
        self.wait_time = 20
        self.add_time = 1800

#获取元素
    def get_element(self,located,page_action):
        try:
            element = self.driver.find_element(*located)
            return element
        except:
            print(f"在{page_action} 页面， 没有找到 {located} 元素")

# 输入
    def input_text(self, loc, content, page_action):
        ele = self.get_element(loc, page_action)
        try:
            if ele == True:
                ele.clear()
            ele.send_keys(content)
        except:
            print(f"在{page_action},{loc} 元素里面，输入{content} 内容失败")

# 点击
    def action_click(self, located, page_action):
        ele = self.get_element(located,page_action)
        try:
            ele.click()
        except:
            print(f"在{page_action} 点击 {located} 元素 失败")

# 清空
    def action_clear(self, located, page_action):
        ele = self.get_element(located, page_action)
        try:
            ele.clear()
        except:
            print(f"在{page_action} 点击 {located} 元素 失败")


# 使用execute_script方法执行点击动作
    def excute_script_click(self, located, page_action):
        ele = self.get_element(located,page_action)
        try:
            self.driver.execute_script("arguments[0].click();", ele)
        except:
            print(f"在{page_action} 点击 {located} 元素 失败")


# 获取元素某个属性值
    def action_get_attribute(self, located, attribute, page_action):
        ele = self.get_element(located,page_action)
        try:
            a = self.driver.execute_script(ele)
            a.get_attribute(attribute)
        except:
            print(f"在{page_action} 点击 {located} 元素 失败")