import setuptools

setuptools.setup(
    name="ppcv",
    version="0.0.1",
    author="dltp-sz",
    author_email="dltp-sz@baidu.com",
    description="None",
    long_description="None",
    long_description_content_type="text/plain",
    url="https://www.paddlepaddle.org.cn/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    license='Apache 2.0',
    entry_points={'console_scripts': [
        'ppcv=ppcv.main:main',
    ]})
