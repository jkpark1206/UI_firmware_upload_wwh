from common.browser import Browser
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class Assert(Browser):

    # 等待元素可见
    def wait_element_visibility(self, loc,page_action):
        try:
            ele = WebDriverWait(self.driver,self.wait_time).until(EC.visibility_of_element_located(loc))
            return ele
        except:
            print(page_action)


    #元素存在page_source中
    def page_source_assert(self):
        try:
            self.assertIn('[用户管理平台]账号/密码错误或者账户状态存在异常，请检查', self.driver.page_source)
        except Exception as e:
            self.driver.get_screenshot_as_file(image_dir + self.test_Login_02.__doc__ + '.png'), print(e)