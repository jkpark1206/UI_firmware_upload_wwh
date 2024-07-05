from common.page import BasePage
from common.element import Element
import time


class Task(BasePage):
    # 登录输入用户名，密码
    def login_input(self, username, password):
        self.input_text(Element.username, username, "输入用户名")
        self.input_text(Element.password, password, "输入密码")

    # 点击登录
    def login_click(self):
        self.action_click(Element.login,"进行登录")
        time.sleep(2)

    #创建任务



# if __name__ == '__main__':
#     Task().login_input('wwh', 'Test123456')
