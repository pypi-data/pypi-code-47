import setuptools

setuptools.setup(
    name='bylogger',
    packages=['bylogger'],
    package_dir={'bylogger': 'src/bylogger'},
    version='1.0.1',
    license='MIT',
    description='Logging Library with fluent-logger wrapper',
    platforms='cross-platfom, platform-independent',
    author='Yogesh',
    author_email='yogesh@byprice.com',
    url='https://github.com/ByPrice/bylogger',
    download_url='https://github.com/ByPrice/bylogger/',
    keywords=['ByPrice', 'logger with fluent', 'fluent-logger', 'python-logging'],
    install_requires=[
        'fluent-logger==0.9.4'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
    ],
)
