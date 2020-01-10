#!/usr/bin/env python
# coding=utf8
import os
import shutil
import zipfile


def zip(file_name, path):
    # 压缩文件夹下的所有文件，但是指定文件夹的路径不会被保存
    # 如:/home/abc/1.txt
    #			  2.txt
    #			 textdir/3.txt
    # 解压后是1.txt 2.txt textdir/3.txt  没有指定目录的路径。这是不同于zipfile的地方
    shutil.make_archive(file_name, "zip", path)


def unzip_single(src_file, dest_dir, password=None):
    ''' 解压单个文件到目标文件夹 '''
    if password is not None:
        password = password.encode()
    zf = zipfile.ZipFile(src_file)
    try:
        zf.extractall(path=dest_dir, pwd=password)
    except RuntimeError as e:
        from pyWebDevTool.util.loggerFactory import Logger
        logger = Logger()
        logger.error(e)
    zf.close()


def unzip_all(source_dir, dest_dir, password=None):
    if not os.path.isdir(source_dir):  # 如果是单一文件
        unzip_single(source_dir, dest_dir, password)
    else:
        it = os.scandir(source_dir)
        for entry in it:
            if entry.is_file() and os.path.splitext(entry.name)[1] == '.zip':
                unzip_single(entry.path, dest_dir, password)
