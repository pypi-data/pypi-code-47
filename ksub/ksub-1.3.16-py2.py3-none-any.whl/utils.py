# -*- coding: utf-8 -*-
import os
import platform
import re
import sys
from logging import handlers

import six
import logging

from ksub import config

log = logging.getLogger('main.utils')


def decode_file_name(name):
    """
    压缩包内文件名解码
    :param name:
    :return:
    """
    # log.debug('decode string: {}'.format(name))
    if six.PY3:
        try:
            name = name.encode('cp437')
        except UnicodeEncodeError as _:
            pass
    if isinstance(name, six.binary_type):
        try:
            name = name.decode('utf-8')
        except UnicodeDecodeError as _:
            try:
                name = name.decode('gbk')
            except UnicodeDecodeError as _:
                pass
    # log.debug('decode result: {}'.format(name))
    return name


def init_log(name='main', level=logging.INFO):
    # 日志配置
    # 子模块以main开头，里面的 Logger就会复用这里的配置
    logger = logging.getLogger(name)
    logger.setLevel(level=level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # Handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level=level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    log_dir = os.path.expanduser('~/.ksub/logs/')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = log_dir + 'ksub.log'
    file_handler = handlers.TimedRotatingFileHandler(filename=log_file, when='D', backupCount=1)
    file_handler.setLevel(level=level)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def num2cn(episode):
    """
    数字转为中文，1-99没问题  P.S.如果有电视剧超过100季，算我输！
    :param episode:
    :return:
    """
    ret = ''
    cn_basic = '一二三四五六七八九十'
    a = episode // 10
    b = episode % 10

    if a >= 2:
        ret += cn_basic[a-1]
    if a >= 1:
        ret += cn_basic[9]
    if b >= 1:
        ret += cn_basic[b-1]
    return ret


def get_alpha(string):
    """
    提取字符串里的字母与数字
    :param string:
    :return: 转为小写
    """
    if not string:
        return string
    result = ''.join(re.split(r'[^A-Za-z0-9]', string))
    return result.lower()


def lang_ext_weight(label):
    # log.debug(os.path.basename(label))
    log.debug('计算weight文字: {}'.format(label))
    weight = 0
    lang = ''
    # if sub_dict is None:
    #     sub_dict = {}
    # lang_weight_counted = False
    # label = sub_dict.get('label', '')
    for index, alias_key in enumerate(config.lang):
        if alias_key in config.lang_alias:
            match, lang = is_match_alias(alias_key, label)
            if match:
                log.debug('match_alias: {}'.format(lang))
                # sub_dict['lang'] = lang
                # lang_weight_counted = True
                weight += (len(config.lang) - index) * 10
                break
            # for alias in config.lang_alias.get(l):
            #     if alias in label:

        else:

            if alias_key in label:
                lang = alias_key
                # sub_dict['lang'] = l
                weight += (len(config.lang) - index) * 10
                break
                # lang_weight_counted = True

        # if lang_weight_counted:
        #     break

    for index, e in enumerate(config.extension):
        if e in label:
            weight += len(config.extension) - index
            break
    return weight, lang


def is_match_alias(key, title):
    lang = ''
    words = config.lang_alias.get(key)
    for word in words:
        if type(word) == tuple:
            # if (word[0] == '中英' or word[0] == '双语') and word[0] in title and '简' in title:
            #     return True, word[0]
            if word[0] in title and word[1] in title:
                lang = words[0][0] + '&' + words[0][1]
                return True, lang
        else:
            if word in title:
                lang = words[0]
                return True, lang
    return False, lang


def notify(title, text):
    """
    通知
    :param title: 通知标题
    :param text: 通知内容
    :return:
    """
    # debug模式 或 在终端运行不提示
    if config.debug or sys.stdin.isatty():
        return
    if platform.system() == 'Darwin':
        os.system("""
            osascript -e 'display notification "{}" with title "{}"'
            """.format(text, title))
    elif platform.system() == 'Windows':
        pass


if __name__ == '__main__':
    pass
