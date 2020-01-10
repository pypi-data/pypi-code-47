# -*- coding: utf-8 -*-
import json
import os
import re

from pyWebDevTool.util import fileUtil


def read_file(file_path):
    from pyWebDevTool.util.loggerFactory import Logger
    logger = Logger()
    if not os.path.exists(file_path):
        logger.info("文件不存在：{}，开始创建".format(file_path))
        fileUtil.create_file(file_path, "[]")
    with open(file_path, "r", encoding="utf-8")as f:
        content = replace_json_comment(f.read())
    return json.loads(content)


def replace_json_comment(json_str):
    # 处理// ... /n 格式非json内容
    json_str1 = re.sub(re.compile('(//[\\s\\S]*?\n)'), '', json_str)
    # 处理/*** ... */ 格式非json内容
    json_str2 = re.sub(re.compile('(/\*\*\*[\\s\\S]*?/)'), '', json_str1)
    return json_str2
