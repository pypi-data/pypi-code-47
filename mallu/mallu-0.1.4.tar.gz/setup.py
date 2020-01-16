from setuptools import setup, find_packages

with open("README.md",'r') as fh:
	long_description = fh.read()

setup(
	name='mallu',
	version='0.1.4', # PEP440
	description='Package for easier Machine Learning Workflow.',
	long_description=long_description,
	long_description_content_type="text/markdown",
	py_modules=['mallu','santa','model'], 
	#package_dir ={'':'src'},
	packages = find_packages(include=('mallu','mallu.*')),
	url='https://github.com/santokalayil/mallu',
	author='Santo K Thomas',
	author_email='santokalayil@gmail.com',
	classifiers=[
			'License :: OSI Approved :: MIT License',
			'Programming Language :: Python :: 3',
			'Programming Language :: Python :: 3.7',
			'Programming Language :: Python :: 3.8',
			'Operating System :: OS Independent'
	],
	)