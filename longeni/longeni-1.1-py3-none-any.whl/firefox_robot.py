from selenium import webdriver


class FireFoxRobot:

    def __init__(self, base_url, timer=None):
        self.timer = timer
        self.driver = webdriver.Firefox(executable_path="./geckodriver")
        self.base_url = base_url
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.link = None

    def load_url(self):
        self.driver.get(self.base_url)

    def send_xpath_and_click(self, xpath_string):
        self.link = self.driver.find_element_by_xpath(xpath_string)
        self.link.click()

    def send_xpath_and_write(self, xpath_string, data):
        self.link = self.driver.find_element_by_xpath(xpath_string)
        self.link.send_keys(data)

    def send_xpath_and_clear(self, xpath_string):
        self.link = self.driver.find_element_by_xpath(xpath_string)
        self.link.clear()

    def close_windows(self):
        self.driver.close()

    def close_and_exit_all(self):
        self.driver.quit()


