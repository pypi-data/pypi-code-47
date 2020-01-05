from setuptools import find_packages, setup


setup(
    name='scrapy-history',
    description='Scrapy downloader middleware to enable persistent storage.',
    author='Kpler engineering',
    author_email='engineering@kpler.com',
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=find_packages(),
    url='http://github.com/Kpler/scrapy-history-middleware',
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
        'boto',
        'parsedatetime',
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
