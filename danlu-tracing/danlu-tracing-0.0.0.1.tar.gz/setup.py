#! /usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# 需要将那些包导入
packages = ["danlu_tracing"]

# 导入静态文件
file_data = [
    # ("smart/static", ["smart/static/icon.svg", "smart/static/config.json"]),
]

# 第三方依赖
requires = [
    'django',
    'opentracing',
    'jaeger_client',
    'Flask-Opentracing',
    'django_opentracing',
    'opentracing_instrumentation',
    # 'tornado_opentracing'
]


setup(
    name="danlu-tracing",  # 包名称
    version="0.0.0.1",  # 包版本
    description="danlu danlu_tracing sdk.",  # 包详细描述
    # long_description=readme,   # 长描述，通常是readme，打包到PiPy需要
    author="chenjinglai",  # 作者名称
    author_email="chenjinglai@crop.netease.com",  # 作者邮箱
    url="https://github.com/",   # 项目官网
    packages=packages,    # 项目需要的包
    # data_files=file_data,   # 打包时需要打包的数据文件，如图片，配置文件等
    # include_package_data=True,  # 是否需要导入静态数据文件
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",  # Python版本依赖
    install_requires=requires,  # 第三方库依赖
    zip_safe=False,  # 此项需要，否则卸载时报windows error
    classifiers=[    # 程序的所属分类列表
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)