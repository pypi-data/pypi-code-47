# coding=utf-8
from setuptools import setup, find_packages

setup(
    name='coopapitestframework',
    version='1.2',
    description='python接口自动化开发基础库',
    author='wu weiping',
    author_email='115773673@qq.com  ',
    packages=find_packages(),
    keywords=['django', 'jaeger', 'jaegertracing'],
    python_requires='>=3.6',
    zip_safe=False,
    entry_points={
        'console_scripts':['yat = apitestframework.apitestmain:main']
    },
    scripts=['apitestframework/apitestmain.py']
)