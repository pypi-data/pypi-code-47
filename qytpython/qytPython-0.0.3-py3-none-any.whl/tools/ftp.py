"""
    module(ftp) - ftp上传下载.

    Main members:

        # download_file - 通过FTP链接，下载文件.
"""
__all__ = [
    'download_file'
]

import codecs
import os
import pathlib
import requests


def download_file(ftp_url, file_name, file_path=''):
    """ 通过FTP链接，下载文件.

        @params:
            ftp_url - ftp链接.
            file_name - 文件名.
            file_path - 文件路径.

        @return:
            On success - 是否成功.
    """
    file_name = os.path.join(file_path, file_name)
    if os.path.exists(file_name):
        return True
    if file_path != '':
        pathlib.Path(file_path).mkdir(parents=True, exist_ok=True)
    r = requests.get(ftp_url)
    with codecs.open(file_name, mode="wb") as fw:
        fw.write(r.content)
        return True
