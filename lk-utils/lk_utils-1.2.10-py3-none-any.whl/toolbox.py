# 主要工具集
# 本模块用于快捷地导入主要的 utils. 使用方法: `from lk_utils.toolbox import *`

from os.path import exists

from . import filesniff
from . import read_and_write
from .excel_reader import ExcelReader
from .excel_writer import ExcelWriter
from .filesniff import stitch_path as pth
from .lk_browser import browser
from .lk_config import cfg
from .lk_logger import lk
from .lk_wrapper import BeautifulSoup

# 将这些命名暴露到全局空间
__all__ = [
    "exists",
    "filesniff",
    "read_and_write",
    'ExcelReader',
    'ExcelWriter',
    "pth",
    'browser',
    'cfg',
    'lk',
    'BeautifulSoup',
]
