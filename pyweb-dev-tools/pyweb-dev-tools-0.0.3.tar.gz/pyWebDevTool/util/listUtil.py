# -*- coding: utf-8 -*-
from pyWebDevTool.util.loggerFactory import Logger

logger = Logger()


def paging(lists, page_size=10, page_number=1):
    # 总共有多少条内容
    total = len(lists)
    # 每页要显示多少条内容
    page = page_size
    paper = page_number  # 第几页
    # 用divmod得出总内容条数与每页显示条数的商和余数
    max_page, a = divmod(total, page)
    if a > 0:
        max_page = max_page + 1
        if paper < 1 or paper > max_page:
            logger.error('你输入的页码不存在，请输入1~%s页' % max_page)
            return []
        else:
            start = (paper - 1) * page
            end = paper * page
            data = lists[start:end]
            return data
    return []
