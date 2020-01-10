#!/usr/bin/env python
# coding=utf8
import configparser
import os
from enum import unique, Enum

from pyWebDevTool.util import fileUtil
from pyWebDevTool.util.loggerFactory import Logger

CONFIG_INI = "config.ini"

logger = Logger()

__cf = configparser.ConfigParser()


@unique
class BaseConfigEnum(Enum):
    """配置属性枚举"""
    """属性key，属性名称"""

    section_name = "base"

    webpack_server_ip = "前端项目 ip地址"
    webpack_server_port = "前端项目r 端口"
    webpack_root_path = "前端项目相对根目录"
    webpack_plugin_path = "前端项目插件相对目录"


def print_config():
    sections = __cf.sections()
    logger.info("load config data:")
    for section in sections:
        logger.info("section:" + section)
        items = __cf.items(section)
        for item in items:
            logger.info("--" + item[0] + "=" + item[1])


def load():
    # 同级目录下执行
    filepath = fileUtil.getRootPath()
    file_name = filepath + os.path.sep + CONFIG_INI
    if not os.path.exists(file_name):
        raise OSError("配置文件：%s不存在" % file_name)
    __cf.read(file_name, encoding="utf-8")
    print_config()


load()


def get_config_val(config_enum):
    """ 获取某个item下的key对应的value值"""
    try:
        return __cf.get(config_enum.section_name.value, config_enum.name)
    except Exception as e:
        logger.error("获取配合属性：{}，{}失败,{}".format(config_enum.section_name.value, config_enum.name, e))
        return ""


def list_item(section):
    return __cf.items(section)


def save_config(config_enum, value):
    __save_config(config_enum, value)
    __write_file()


def __save_config(config_enum, value):
    sections = __cf.sections()
    # 包含item
    if sections.__contains__(config_enum.name):
        __cf.set(config_enum.section_name.value, config_enum.name, str(value))
    # 不包含item
    else:
        __cf.add_section(config_enum.name)
        __cf.set(config_enum.section_name.value, config_enum.name, str(value))


def save_configs(config_list=None):
    if config_list is not None and len(config_list) > 0:
        for config in config_list:
            logger.info("更新配置：section：{}，key：{}，值：{}".format(config.section, config.key, config.value))
            __save_config(config['config_enum'], config['value'])
        __write_file()


def __write_file():
    __cf.write(open(CONFIG_INI, 'w', encoding="utf-8"))  # 重新写入
