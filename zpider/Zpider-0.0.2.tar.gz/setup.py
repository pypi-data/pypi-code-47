# -*- coding:utf-8 -*-
# author:Pntehan


import setuptools
import os

# 需要将那些包导入
packages = ["Zpider"]

# 第三方依赖
requires = [
    "lxml>=4.3.2",
    "urllib3>=1.24.1",
    "pysocks>=1.6.8"
]

# 自动读取version信息
about = {}
with open(os.path.join("Zpider", "__version__.py"), "r", encoding="utf-8") as f:
    exec(f.read(), about)

# 自动读取readme
with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setuptools.setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    author=about["__author__"],
    author_email=about["__author_email__"],
    packages=packages,
    include_package_data=False,
    python_requires=">=3.*",
    install_requires=requires,
    zip_safe=False,
    url="https://github.com/pntehan/Zpider",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
