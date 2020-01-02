#! /usr/bin/env python
# -*- coding=utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class pageObject(object):

    _wd = webdriver
    _d  = object

    def initWebDriver(self,
                      driverPath=None,
                      is_headless=False,
                      is_max=False,
                      is_min=False,
                      wait=30,
                      *args, **kwargs):
        """
                初始化浏览器对象
        :param driver:      浏览器驱动
        :param is_headless: 是否无界面
        :param is_max:      是否最大化
        :param is_min:      是否最小化
        :param wait:        隐式等待时间（单位：秒）
        :param args:
        :param kwargs:
        :return:            返回浏览器对象
        """
        options = Options()
        if is_headless:
            options.add_argument("--headless")
        try:
            if driverPath:
                self._d = self._wd.Chrome(chrome_options=options, executable_path=driverPath)
            else:
                self._d = self._wd.Chrome(chrome_options=options)
        except Exception as e:
            raise ("初始化浏览器失败：", e)
        if wait > 0:
            self._d.implicitly_wait(wait)
        if is_max:
            self._d.maximize_window()
        elif is_min:
            self._d.minimize_window()
    
    def xpath(self, loc, timeout=5, step=0.5, *args, **kwargs):
        """
                定位元素
        :param loc:             xpath表达式
        :param timeout:         定位等待时间
        :param step:            检测的时间
        :param index:           定位目标索引
        :param args:
        :param kwargs:
        :return:
        """
        return WebDriverWait(self._d, timeout, step).until(
            EC.presence_of_element_located((By.XPATH, loc))
        )

    def switchWindow(self, index=1, *args, **kwargs):
        """
                切换标签页
        :param index:       标签页的索引值
        :param args:
        :param kwargs:
        :return:
        """
        try:
            self._d.switch_to.window(self._d.window_handles[index])
        except:
            raise ("index需要为正整数，表示标签页的索引值")

    def switchFrame(self, index=0, *args, **kwargs):
        """
                切换内嵌页
        :param index:       内嵌页的索引值
        :param args:
        :param kwargs:
        :return:
        """
        try:
            self._d.switch_to.frame(self.xpath('//iframe', index=index))
        except:
            raise ("index需要为正整数，表示标签页的索引值")

    def switchFrame2Window(self):
        try:
            self._d.switch_to.default_content()
        except:
            raise ("已经在本网页不需要切换")

    def alertYes(self):
        """
                点击JS弹出框确认按钮
        :return:
        """
        try:
            alert = self._d.switch_to.alert
            alert.accept()
        except:
            raise ("切换失败")

    def alertNo(self):
        """
                点击JS弹出框取消按钮
        :return:
        """
        try:
            alert = self._d.switch_to.alert
            alert.dismiss()
        except:
            raise ("切换失败")

    def alertSend(self, data):
        """
                JS弹出框输入内容
        :param data:    输入的内容
        :return:
        """
        try:
            alert = self._d.switch_to.alert
            alert.send_keys(data)
        except:
            raise ("切换失败")

    def move_and_stop(self, loc):
        """
                悬停到某元素上
        :param loc:     目标元素xpath表达式
        :return:
        """
        ac = ActionChains(self._d)
        ac.move_to_element(self.xpath(loc=loc)).perform()

    def move(self, src_loc, tag_loc):
        """
                从源元素位置拖动到目标元素位置
        :param src_loc:     源元素xpath表达式
        :param tag_loc:     目标元素xpath表达式
        :return:
        """
        ac = ActionChains(self._d)
        ac.drag_and_drop(self.xpath(loc=src_loc), self.xpath(loc=tag_loc)).perform()