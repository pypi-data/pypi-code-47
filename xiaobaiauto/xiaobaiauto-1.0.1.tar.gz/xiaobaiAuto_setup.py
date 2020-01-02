import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="xiaobaiauto", # Replace with your own username
    version="1.0.1",
    author="Tser",
    author_email="807447312@qq.com",
    description="xiaobaiauto framework 简化定位并集成日志搜集、报告生成、邮件发送等功能",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/big_touch/",
    packages=setuptools.find_packages(),
    keywords="xiaobai auto automation test framework",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    # py_modules = ['xiaobaiAuto.cp37-win_amd64.pyd'],
    install_requires=[
    	"selenium"
    ],
    package_data = {
        'xiaobaiauto': ['xiaobaiauto.cp37-win_amd64.pyd', 'HTMLTestRunner.py'],
    },
)
