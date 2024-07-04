from selenium.webdriver.remote.webdriver import WebDriver

class BasePage:

    def __init__(self, driver: WebDriver,):
        self.driver = driver
        self.wait_time = 20
        self.add_time = 1800
