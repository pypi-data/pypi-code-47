from setuptools import setup


def readme():
	with open('README.md') as f:
		return f.read()


setup(
	name="pysports",
	version="1.0.1",
	license="MIT",
	description="PySports: Python module to access cricket scores and more.",
	long_description=readme(),
	long_description_content_type="text/markdown",
	url="https://github.com/bhojrampawar/pysports",
	author="Bhojram pawar",
	author_email="bhojrampawar@hotmail.com",
	packages=["pysports"],
	include_package_data=True,
	classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
	],
	install_requires=['requests'],
)
