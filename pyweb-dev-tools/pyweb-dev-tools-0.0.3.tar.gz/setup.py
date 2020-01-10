# -*- coding: utf-8 -*-
from distutils.core import setup

from setuptools import find_packages

filepath = 'README.md'

setup(name='pyweb-dev-tools',  # 打包后的包文件名
      version='0.0.3',
      description='pyweb-dev-tools utils for develop',  # 说明
      author='luanhaoyu',
      author_email='15951963820@163.com',
      url='https://gitee.com/luanhaoyu_admin/py-web-dev-tools',
      license="GPLv3",
      keywords="pyweb-dev-tools pyqt destop tool",
      py_modules=['pyWebDevTool.main', 'pyWebDevTool.assert_rc'],  # 你要打包的文件
      packages=find_packages(),
      include_package_data=True,
      install_requires=["PyQt5>=5.13.2",
                        "PyQtWebEngine>=5.13.2",
                        "requests>=2.22.0",
                        "PyInstaller>=3.5",
                        "numpy>=1.16.4",
                        "pywin32>=224",
                        ],  # 需要安装的依赖包
      data_files=[filepath],
      # 此项需要，否则卸载时报windows error
      classifiers=[  # 程序的所属分类列表
          "Development Status :: 3 - Alpha",
          "Topic :: Utilities",
          "License :: OSI Approved :: GNU General Public License (GPL)",
      ],
      zip_safe=False
      )
