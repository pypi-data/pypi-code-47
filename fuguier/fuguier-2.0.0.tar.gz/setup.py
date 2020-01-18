'''
@Author: your name
@Date: 2020-01-18 14:54:38
@LastEditTime : 2020-01-18 17:10:05
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \MyPython\src\setup.py
'''
# coding: utf-8
 
from setuptools import setup, find_packages
setup(
    name = 'fuguier',  # 项目名称，pip show 包名 中的包名
    version = '2.0.0',
    packages = find_packages("src"), # src模块的保存目录
    package_dir = {"": "src"},       #告诉setuptools包都在src目录下
    package_data = {                 #配置其他文件的打包处理
        #任何包中有.txt文件， 都包含它
        "": ["*.txt", "*.info", "*.properties"],
        #
        "": ["data/*.*"],
    },
    #包含包data文件夹中的*.dat文件
    exclude = ["*.test", "*.test.*", "test.*", "test"],
   
    
)