import datetime

import requests
import random

from pyWebDevTool.util.loggerFactory import Logger

logger = Logger()
DOWNLOAD_MAX_TIMES = 3
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0;) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
]

default_timeout = (3, 10)


def getErrorText(text):
    if len(text) > 100:
        return text[0:100]
    return text


def downloadFile(url, fileStorePath, timeout=(2, 10), times=3, stream=True):
    """stream 下载大文件100M以上 设置为True,否则容易导致内存占用过大 下载失败"""
    if times == 0:
        raise IOError("下载文件错误次数达到上限")
    now = datetime.datetime.now()
    logger.info("下载文件，地址为：{}，第{}次,存储地址：{}".format(url, DOWNLOAD_MAX_TIMES - times + 1, fileStorePath))
    try:
        headers = {
            'User-Agent': random.choice(user_agent_list)
        }
        r = requests.get(url, headers=headers, timeout=timeout, stream=stream)
        logger.info("响应状态码:{}".format(r.status_code))
        if r.status_code != 200 and r.status_code != 304:
            raise IOError("下载文件:{},失败:{}".format(url, getErrorText(r.text)))
        with open(fileStorePath, "wb") as f:
            if stream:
                for chunk in r.iter_content(chunk_size=512):
                    if chunk:
                        f.write(chunk)
            else:
                f.write(r.content)
    except Exception as e:
        logger.error("下载文件{}，失败：{}".format(url, e))
        times -= 1
        downloadFile(url, fileStorePath, times=times, stream=stream)
    now_end = datetime.datetime.now()
    logger.info("文件:{},下载完成，耗时：{}s".format(url, str(now_end - now)))


def get(url, timeout=default_timeout, **kwargs):
    return request("get", url, timeout=timeout, **kwargs)


def post(url, timeout=default_timeout, **kwargs):
    return request("post", url, timeout=timeout, **kwargs)


def request(method, url, timeout=default_timeout, **kwargs):
    n_headers = {
        'User-Agent': random.choice(user_agent_list)
    }
    if 'headers' in kwargs:
        n_headers = {**n_headers, **kwargs['headers']}
        del kwargs['headers']
    return requests.request(method, url=url, headers=n_headers, timeout=timeout, **kwargs)
