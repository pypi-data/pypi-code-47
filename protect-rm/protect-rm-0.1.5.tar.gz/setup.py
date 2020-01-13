import codecs
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="protect-rm",
    version="0.1.5",
    license='MIT',
    description="A modified version of rm-protection (https://pypi.org/project/rm-protection/) with some new implementation. Mainly for myself.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sam Sheng',
    author_email="sam_sheng@outlook.com",
    packages=['protect_rm'],
    entry_points={
        'console_scripts': [
            'rm-p=protect_rm.rm_p:rm',
            'protect=protect_rm.protect:protect',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)