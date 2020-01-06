from distutils.core import setup


setup(
    name='GBComments',
    version='0.0.4',
    py_modules=['GBComments'],
    author="WRAllen",
    author_email="1072274105@qq.com",
    # 这里会在他人搜索时显示
    description="用于生成好评差评的库",
    long_description=open('README.md', 'r', encoding='UTF-8').read(),
    long_description_content_type="text/markdown",
    # github地址
    url='https://github.com/WRAllen/GBComments'
)