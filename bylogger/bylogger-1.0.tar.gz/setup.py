import setuptools

setuptools.setup(
    name='bylogger',
    packages=['bylogger'],  # this must be the same as the name above
    version='1.0',
    description='Logging Library used by ByPrice',
    author='Yogesh',
    author_email='yogesh@byprice.com',
    url='https://github.com/ByPrice/bylogger',  # use the URL to the github repo
    download_url='https://github.com/ByPrice/bylogger/',
    keywords=['ByPrice', 'logger with fluent', 'fluent-logger'],
    install_requires=[
        'fluent-logger==0.9.4'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ),
)
