# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['china_region_data']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'china-region-data',
    'version': '0.1.3',
    'description': '中国行政区域数据',
    'long_description': '# 中国行政区域数据\n\n根据[中国政府网站](http://www.mca.gov.cn/article/sj/xzqh/2019/2019/201912251506.html)中的数据处理而成。\n\n## install\n\n```bash\npip3 install china-region-data\n```\n\n## example\n\n```python\nfrom china_region_data import 省级行政区域, 市级行政区域, 县级行政区域, Region\n\n\nfor 省级行政地区 in 省级行政区域:\n    print(省级行政地区)\n    for 市级行政地区 in 省级行政地区.下级行政区域:\n        print("  ", 市级行政地区)\n        for 县级行政地区 in 市级行政地区.下级行政区域:\n            print("    ", 县级行政地区)\n\n广东 = Region("广东省")\n深圳 = Region("深圳市")\n南山 = Region("南山区")\n\nassert 广东.name == "广东省"\n\nassert 广东.行政级别 == 1\n\nfor 广东城市 in 广东.下级行政区域:\n    assert 广东城市.行政级别 == 2\n\nassert 深圳.上级行政地区 == 广东\n\nassert 南山.上级行政地区.上级行政地区 == 广东\n\nassert 南山 in 南山.上级行政地区\n\nassert 南山 in 南山.上级行政地区.上级行政地区\n\nassert not Region("合肥市") in 广东\n```\n',
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
