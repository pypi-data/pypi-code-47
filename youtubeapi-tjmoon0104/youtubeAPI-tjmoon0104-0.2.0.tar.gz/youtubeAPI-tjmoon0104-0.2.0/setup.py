from setuptools import setup, find_packages

setup(
    name                = 'youtubeAPI-tjmoon0104',
    version             = '0.2.0',
    description         = 'Youtube Data, Analytics, Reporting API',
    license             = 'MIT',
    author              = 'taejun',
    author_email        = 'tjmoon0104@outlook.com',
    url                 = 'https://github.com/tjmoon0104/youtubeAPI',
    download_url        = 'https://github.com/jeakwon/ccpy/archive/0.0.tar.gz',
    install_requires    =  [],
    packages            = find_packages(),
    keywords            = ['youtubeAPI'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)