from setuptools import setup, find_packages

from ming import config

setup(
    name='jiuming-tools',
    # 版本 如果需要发布更新 需要调整版本号
    version=config.version,
    packages=find_packages(),
    include_package_data=True,
    # 需要的依赖
    install_requires=[
        'Click==7.0', 'psutil==5.6.7', 'PyYAML==5.2', 'paramiko==2.7.1'
    ],
    # 命令行入口
    entry_points='''
        [console_scripts]
        ming=ming.main:cli
    ''',
    author='ming',
    license='MIT',
    url='https://github.com/xujiuming/jiuming-tools',
    description='个人常用功能'
)
