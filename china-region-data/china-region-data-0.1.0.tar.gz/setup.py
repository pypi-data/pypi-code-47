# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['china_region_data']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'china-region-data',
    'version': '0.1.0',
    'description': '中国行政区域数据',
    'long_description': '# 中国行政区域数据\n\n根据[中国政府网站](http://www.mca.gov.cn/article/sj/xzqh/2019/2019/201912251506.html)中的数据处理而成。\n\n```python\nfrom china_region_data import 省级行政区域, 市级行政区域, 县级行政区域\n\n\nfor 省级行政地区 in 省级行政区域:\n    print(省级行政地区)\n    for 市级行政地区 in 省级行政地区.下级行政区域:\n        print("  ", 市级行政地区)\n        for 县级行政地区 in 市级行政地区.下级行政区域:\n            print("    ", 县级行政地区)\n```\n',
    'author': 'abersheeran',
    'author_email': 'me@abersheeran.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/abersheeran/china-region-data',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
