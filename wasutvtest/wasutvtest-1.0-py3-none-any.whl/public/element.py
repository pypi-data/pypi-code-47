from WasuTvTest.public.driver import appium_driver


class element:
    def __init__(self, desired_caps):
        self.driver = appium_driver(desired_caps).get_driver()

    def by_id(self, element_id):
        ele = self.driver.find_elements_by_id(element_id)
        return ele

    def by_name(self, element_name):
        ele = self.driver.find_element_by_name(element_name)
        return ele

    def by_classname(self, element_classname):
        ele = self.driver.find_elements_by_class_name(element_classname)
        return ele

    def by_xpath(self, element_xpath):
        ele = self.driver.find_element_by_xpath(element_xpath)
        return ele

    def by_css(self, element_css):
        ele = self.driver.find_element_by_css_selector(element_css)
        return ele

    def by_link_text(self, element_link_text):
        ele = self.driver.find_element_by_link_text(element_link_text)
        return ele

    def input(self, keys):
        self.driver.send_keys(keys)
