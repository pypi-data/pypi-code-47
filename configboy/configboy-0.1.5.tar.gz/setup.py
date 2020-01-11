from setuptools import setup, find_packages

setup(
    name="configboy",
    version="0.1.5",
    description=("config library"),
    #license="MIT Licence",
    url="http://test.com",
    author="aaronhua",
    author_email="cjhdwyyx@163.com",
    packages=find_packages(),
    platforms=["all"],
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'configboy = configboy.run:main',
        ]
    }
)

# todo 打包命令 python setup.py bdist_wheel
# todo python setup.py sdist upload -r pypi
# if __name__ == '__main__':
#     setup(
#         name="configman",
#         version="0.1.3",
#         description=("config library"),
#         url="http://config.com",
#         author="aaronhua",
#         author_email="cjhdwyyx@163.com",
#         packages=find_packages(),  # 目录位置
#         # package_dir={'': 'config'},  # 告诉distutils包都在src下
#         platforms=["all"],
#         # package_data={'config': ['config.ini'],}, # 添加数据文件
#         entry_points={
#             'console_scripts': [
#                 'configman = configman.run:main',
#             ]
#         }
#     )
