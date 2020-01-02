#! /usr/bin/env python
# -*- coding=utf-8 -*-
"""
    author:     Tser
    time:       2019/12/20 16:32
    project:    ctpc
    file:       indexPage.py
"""
"""
    首页实例
    实现对首页的所有主要元素的定位信
    
"""

from xiaobaiAuto import pageObject

p = pageObject()
p.initWebDriver()

p._d.get('https://www.baidu.com')
e = p.findXpath(loc='//*[@id="kw"]')
e.send_keys('1111')
