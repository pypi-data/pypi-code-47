from setuptools import setup, find_packages
import schnittstelle

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='schnittstelle',
    version=schnittstelle.__version__,
    author="Schicksal",
    description="A console ui interface",
    author_email='mhaisham79@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',

    install_requires=[
      'colorama'
    ],

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        "Operating System :: OS Independent",
    ],
    license="MIT license",
    keywords='console interface progress',

    url='https://github.com/mHaisham/schnittstelle',
    project_urls={
      'Source code': 'https://github.com/mHaisham/schnittstelle'
    },
    packages=find_packages(),
    python_requires='>=3.6'
)
