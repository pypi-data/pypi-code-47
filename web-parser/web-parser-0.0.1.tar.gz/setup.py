from setuptools import setup, find_packages

setup(
	name = 'web-parser',
	version = '0.0.1',
	description = 'This is a parser tool which made all the stuff for you',
	author = 'Ivan Vinogradov',
	py_modules = ["web-parser", "requests", "bs4"],
	package_dir = {'': 'src'},
	python_requires='>=3.6',
	author_email="author@example.com",
    long_description= "this will come later",
    long_description_content_type="text/markdown",
    url="https://www.bit.ly/bestf2l",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)