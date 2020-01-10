from appium import webdriver


class appium_driver:
    def __init__(self, desired_caps):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def get_driver(self):
        return self.driver
