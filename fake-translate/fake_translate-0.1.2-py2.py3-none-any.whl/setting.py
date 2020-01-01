# -*- encoding: utf-8 -*-
"""
@File           : setting
@Time           : 2019/12/23
@Author         : flack
@Email          : opencoding@hotmail.com
@ide            : PyCharm
@project        : MyTest
@description    : 描述
"""
import os
import sys

BASE_DIR = os.path.basename(os.path.basename(__file__))
sys.argv.append(BASE_DIR)


VERSION = '0.1.1'

# 有道翻译地址
YOUDAO_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

# 百度翻译地址
BAIDU_URL = ''

# 谷歌翻译地址
GOOGLE_URL = ''

# 金山词霸翻译地址
POWERWORLD_URL = ''
