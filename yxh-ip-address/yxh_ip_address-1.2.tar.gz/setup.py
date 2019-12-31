# 引入构建包信息的模块

from distutils.core import setup
import setuptools
# 定义发布的包文件的信息
import ip_address
setup(

    name="yxh_ip_address",  # 发布的包文件名称

    version="1.2",  # 发布的包的版本序号

    description="可以得到ip详情ip_address地址",  # 发布包的描述信息

    author="易小豪",  # 发布包的作者信息

    author_email="1764807112@qq.com",  # 作者联系邮箱信息

    packages=setuptools.find_packages(),
    #py_modules=['ip_address']  # 发布的包中的模块文件列表
)
