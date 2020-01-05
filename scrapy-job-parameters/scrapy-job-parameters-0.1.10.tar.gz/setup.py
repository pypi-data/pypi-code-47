import os
import codecs
from setuptools import find_packages, setup


here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()


setup(
    name='scrapy-job-parameters',
    description='Scrapy downloader middleware to enable persistent storage.',
    long_description=long_description,
    author='Kpler engineering',
    author_email='engineering@kpler.com',
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
    url='http://github.com/kpler/scrapy-job-parameters-extension',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
    ],
    install_requires = [
        'scrapy',
    ],
    extras_require={
        "test": [
            'coverage==4.5',
            'flake8==3.5.0',
            'ipdb==0.10.3',
            'mock==2.0.0',
            'nose==1.3.7',
            'nose-cov==1.6',
            'nose-timer==0.7.1',
            'tox==3.0.0',
            'tox-pyenv==1.1.0'
        ]
    }
)