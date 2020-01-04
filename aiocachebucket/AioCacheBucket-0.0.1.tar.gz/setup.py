from setuptools import setup, find_packages
import sys
 
setup(
    name="AioCacheBucket",
    version="0.0.1",
    author="Chenwe-i-lin",
    author_email="1846913566@qq.com",
    description="cache for python, base on asyncio.",
    license="MIT",
    url="https://github.com/NatriumLab/AioCacheBucket",
    packages=['AioCacheBucket'],
    install_requires=[
        "infinity4py"
    ]
)