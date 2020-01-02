import os
import re
import json
from setuptools import setup


def get_version():
    """
    提取出 mdparser/version.json 中提取出 version 的值
    """

    # base_dir 项目根目录(mdparser)
    base_dir = os.path.dirname(__file__)

    # version.json 的全路径
    file_path_version_json = os.path.join(base_dir, "mdparser/version.py")

    # 打开 vesion.json 读取其中内容，并返回 version 字段的值
    with open(file_path_version_json) as f_version:

        # 由于 version.json 不可能超过 4096 所以可以看成读取了全部内容
        s = f_version.read(4096)

        # 转换成 json 并返回 version 的值
        version_dict = json.loads(s)
        return version_dict.get('version', '0.0.0')


version = get_version()

setup(name='mdparser',
      version=version,
      description='mdparser',
      author="Neeky",
      author_email="neeky@live.com",
      maintainer='Neeky',
      maintainer_email='neeky@live.com',
      scripts=['bin/mdparser'],
      packages=['mdparser'],
      #package_data={'mdparser': ['static/cnfs/*']},
      url='https://github.com/Neeky/dmparser',
      install_requires=['mysql-connector-python==8.0.18', 'markdown==3.1.1'],
      python_requires='>=3.6.*',
      classifiers=[
           'Development Status :: 4 - Beta',
           'Intended Audience :: Developers',
           'Operating System :: POSIX',
           'Operating System :: MacOS :: MacOS X',
           'Programming Language :: Python :: 3.6',
           'Programming Language :: Python :: 3.7',
           'Programming Language :: Python :: 3.8']
      )
