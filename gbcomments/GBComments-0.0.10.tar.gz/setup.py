import io

from setuptools import setup
from setuptools import find_packages

with io.open("README.md", "r", encoding="utf8") as f:
    readme = f.read()

setup(
    name='GBComments',
    version='0.0.10',
    py_modules=['GBComments'],
    author="WRAllen",
    author_email="1072274105@qq.com",
    # 这里会在他人搜索时显示
    description="用于生成好评差评的库",
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages("src"),
    package_dir={"": "src"},
    # github地址
    url='https://github.com/WRAllen/GBComments'
)