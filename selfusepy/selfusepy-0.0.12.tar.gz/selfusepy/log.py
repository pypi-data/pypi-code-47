#    Copyright 2018-2019 LuomingXu
#  #
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#  #
#       http://www.apache.org/licenses/LICENSE-2.0
#  #
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#  #
#   Author : Luoming Xu
#   File Name : log.py
#   Repo: https://github.com/LuomingXu/selfusepy

import logging
from datetime import datetime, timedelta, timezone
from enum import Enum
from logging import handlers
from typing import List

from selfusepy.utils import RootPath

__all__ = ['LogTimeUTCOffset', 'Logger']


def _UTC_12(fmt, timestamp):
  return _delta_base(-12)


def _UTC_11(fmt, timestamp):
  return _delta_base(-11)


def _UTC_10(fmt, timestamp):
  return _delta_base(-10)


def _UTC_9(fmt, timestamp):
  return _delta_base(-9)


def _UTC_8(fmt, timestamp):
  return _delta_base(-8)


def _UTC_7(fmt, timestamp):
  return _delta_base(-7)


def _UTC_6(fmt, timestamp):
  return _delta_base(-6)


def _UTC_5(fmt, timestamp):
  return _delta_base(-5)


def _UTC_4(fmt, timestamp):
  return _delta_base(-4)


def _UTC_3(fmt, timestamp):
  return _delta_base(-3)


def _UTC_2(fmt, timestamp):
  return _delta_base(-2)


def _UTC_1(fmt, timestamp):
  return _delta_base(-1)


def _UTC(fmt, timestamp):
  return _delta_base(0)


def _UTC1(fmt, timestamp):
  return _delta_base(1)


def _UTC2(fmt, timestamp):
  return _delta_base(2)


def _UTC3(fmt, timestamp):
  return _delta_base(3)


def _UTC4(fmt, timestamp):
  return _delta_base(4)


def _UTC5(fmt, timestamp):
  return _delta_base(5)


def _UTC6(fmt, timestamp):
  return _delta_base(6)


def _UTC7(fmt, timestamp):
  return _delta_base(7)


def _UTC8(fmt, timestamp):
  return _delta_base(8)


def _UTC9(fmt, timestamp):
  return _delta_base(9)


def _UTC10(fmt, timestamp):
  return _delta_base(10)


def _UTC11(fmt, timestamp):
  return _delta_base(11)


def _UTC12(fmt, timestamp):
  return _delta_base(12)


def _delta_base(delta: int):
  return datetime.now(timezone(timedelta(hours = delta))).timetuple()


class LogTimeUTCOffset(Enum):
  """
  UTC_8 -> UTC-08:00
  UTC8  -> UTC+08:00
  """
  UTC_12 = _UTC_12
  UTC_11 = _UTC_11
  UTC_10 = _UTC_10
  UTC_9 = _UTC_9
  UTC_8 = _UTC_8
  UTC_7 = _UTC_7
  UTC_6 = _UTC_6
  UTC_5 = _UTC_5
  UTC_4 = _UTC_4
  UTC_3 = _UTC_3
  UTC_2 = _UTC_2
  UTC_1 = _UTC_1
  UTC = _UTC
  UTC1 = _UTC1
  UTC2 = _UTC2
  UTC3 = _UTC3
  UTC4 = _UTC4
  UTC5 = _UTC5
  UTC6 = _UTC6
  UTC7 = _UTC7
  UTC8 = _UTC8
  UTC9 = _UTC9
  UTC10 = _UTC10
  UTC11 = _UTC11
  UTC12 = _UTC12


class Logger(object):
  """
  日志类
  usage: log = Logger('error.log').logger OR log = Logger().logger
         log.info('info')
  """

  def __init__(self, filename = None, time_offset: LogTimeUTCOffset = LogTimeUTCOffset.UTC8, when = 'D', backCount = 3,
               fmt = '%(asctime)s-[%(levelname)8s]-[%(threadName)15s] %(customPathname)50s(%(lineno)d): %(message)s'):
    """
    init
    :param filename: 储存日志的文件, 为None的话就是不储存日志到文件
    :param when: 间隔的时间单位. S秒, M分, H小时, D天, W每星期(interval==0时代表星期一) midnight 每天凌晨
    :param backCount: 备份文件的个数, 如果超过这个个数, 就会自动删除
    :param time_offset: log的时间, 默认为UTC+8
    :param fmt: 日志格式
    """
    logging.Formatter.converter = time_offset
    self.logger = logging.Logger(filename)
    format_str = logging.Formatter(fmt)
    self.logger.setLevel(logging.DEBUG)  # 设置日志级别为debug, 所有的log都可以打印出来
    sh = logging.StreamHandler()  # 控制台输出
    sh.setFormatter(format_str)
    self.logger.addHandler(sh)
    self.logger.addFilter(LoggerFilter())

    if filename is not None:
      """实例化TimedRotatingFileHandler"""
      th = handlers.TimedRotatingFileHandler(filename = filename, when = when, backupCount = backCount,
                                             encoding = 'utf-8')
      th.setFormatter(format_str)  # 设置文件里写入的格式
      self.logger.addHandler(th)


class LoggerFilter(logging.Filter):

  def _s_len(self, l: List[str]):
    len: int = 0
    for item in l:
      len += item.__len__() + 1
    return len

  def _replace_underline(self, l: List[str]):
    for i, item in enumerate(l):
      l[i] = item.replace('_', '')

  def filter(self, record: logging.LogRecord):
    s = str(record.pathname).replace('\\', '/').replace(RootPath().root_path, '').replace('/', '.')[1:]
    l: List[str] = s.split('.')
    l.pop(l.__len__() - 1)  # 丢弃最后的文件扩展名'py'
    file_name = l.pop(l.__len__() - 1)
    self._replace_underline(l)  # 有些py文件以'_'开头, 需要删去, 才能取首字母
    i: int = 0
    while self._s_len(l) + file_name.__len__() + record.funcName.__len__() > 50:  # 如果超出了长度再进行缩减操作
      if i >= l.__len__():  # 实在太长了缩减不了, 就算了, 需要保证最后的文件名与函数名的完整
        break
      l[i] = l[i][0]
      i += 1

    l.append(file_name)
    l.append(record.funcName)

    record.customPathname = '.'.join('%s' % item for item in l)
    """
    不能在这边直接就修改
    >>>record.pathname = '.'.join('%s' % item for item in l)
    有可能后面的log依赖这个pathname, 那么这个pathname就被修改了, 
    而没有被系统重新赋予正确的pathname
    例如test.log包中的多层级__init__, 就会出现这种问题
    """
    return True
