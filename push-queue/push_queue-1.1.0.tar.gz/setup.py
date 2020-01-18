#encoding=utf-8
import setuptools

with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="push_queue", # Replace with your own username
    version="1.1.0",
    author="liuyancong",
    author_email="1437255447@qq.com",
    description="A queue between thread with method push,drop old put into new",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mt6979/push_queue",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
