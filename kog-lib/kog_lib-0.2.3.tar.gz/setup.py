# coding=utf-8

from setuptools import setup, find_packages

with open("README.md", "r",encoding="utf-8") as fh:  #这里就是读取readme文件的内容了。
    long_description = fh.read()


setup(
    name='kog_lib',  # '库的名称,一般写成文件夹的名字就可以了，也有的人不写成文件夹的名字，那么pip install和具体的import使用时候就不一样了，用起来会十分蛋疼，有一些包就是这样的。比如一个包，安装时候是pip install  xxx,但当你要使用时候要import yyy


    version="0.2.3",                  # 版本，每次发版本都不能重复，每次发版必须改这个地方
    description=(
        'Simple python lib, processing excel,mail,textgrid,metadata,wav; using for SurfingTech or others'   # 一个简介，别人搜索包时候，这个概要信息会显示在在搜索列表中

    ),
    long_description=long_description,    # 这是详细的，一般是交别人怎么用，很多包没写，那么在官网就造成没有使用介绍了
    long_description_content_type="text/markdown",
    author='KOG',       # 作者
    author_email='52204413@qq.com',
    # maintainer='ydf',     # 主要的工作人员
    # maintainer_email='909686719@qq.com',
    license='BSD License',
    # packages=['douban'], # 发布的包名

    packages=[
    'kog_lib',
    'kog_lib.excel',
    'kog_lib.mail',
    'kog_lib.textgrid',
    'kog_lib.metadata',
    'kog_lib.wav',
    'kog_lib.filesystem',
    'kog_lib.utils',
    ],
    platforms=["all"],
    url='',   # 这个是连接，一般写github就可以了，会从pypi跳转到这里去
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[              # 这里是依赖列表，表示运行这个包的运行某些功能还需要你安装其他的包
        'xlrd~=1.2.0',
        'xlwt~=1.3.0',
        'openpyxl~=2.6.2',
        'xlutils~=2.0.0',
        'pprint~=0.1',
        'textgrid~=1.4',
        'python_levenshtein~=0.12.0',
        'fs~=2.4.11',
        'fs.sshfs~=0.12.2',
    ]
)