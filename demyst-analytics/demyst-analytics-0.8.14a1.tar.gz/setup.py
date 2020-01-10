from setuptools import setup


setup(
    name='demyst-analytics',

    version='0.8.14a1',

    description='',
    long_description='',

    author='Demyst Data',
    author_email='info@demystdata.com',

    license='',

    packages=['demyst.analytics'],
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'demyst-common>=0.8.14a1',
        'yattag',
        'IPython',
        'tqdm',
        'ipywidgets',
        'pandas',
        'pandas_schema'
    ],
    extra_requires={
        'type_guesser': [
            'keras',
            'tensorflow==2.0.0',
            'usaddress'
        ]
    }
)
