import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="xiaobaiautomation", # Replace with your own username
    version="0.1",
    author="Tser",
    author_email="807447312@qq.com",
    description="Xiaobai Web AutomationFramework Service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/big_touch/",
    packages=setuptools.find_packages(),
    keywords="xiaobai web automation selenium bottle",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    install_requires=[
    	"bottle",
        "selenium"
    ],
    entry_points={'console_scripts': [
        'xiaobaiautomation = xiaobaiautomation.xiaobaiautomation:main',
    ]},
)
