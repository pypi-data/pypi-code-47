import ast
import io
import re

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding="utf8") as f:
	readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_mistune_smartypants.py', 'rb') as f:
	description = str(ast.literal_eval(_description_re.search(
		f.read().decode('utf-8')).group(1)))

setup(
	author='Jean-Paul van Oosten',
	author_email='pypi@jpvanoosten.nl',
	description=description,
	keywords='smartypants lektor',
	license='MIT',
	long_description=readme,
	long_description_content_type='text/markdown',
	name='lektor-mistune-smartypants',
	packages=find_packages(),
	py_modules=['lektor_mistune_smartypants'],
	url='https://github.com/jeanpaul/lektor-mistune-smartypants',
	version='1.0',
	install_requires=[
		'smartypants',
	],
	classifiers=[
		'Framework :: Lektor',
		'Environment :: Plugins',
		'License :: OSI Approved :: MIT License',
	],
	entry_points={
		'lektor.plugins': [
			'mistune-smartypants = lektor_mistune_smartypants:MistuneSmartypantsPlugin',
		]
	}
)
