from distutils.core import setup

version = '0.0.3'

setup(
    name='any_roman',
    packages=['any_roman'],
    version=version,
    license='MIT',
    description='Converts any whole number to roman numeral',
    author='Dean Kayton',
    author_email='hello@dnk8n.dev',
    url='https://gitlab.com/dnk8n/any_roman',
    download_url=f'https://gitlab.com/dnk8n/any_roman/-/archive/v{version}/any_roman-v{version}.tar.gz',
    keywords=['roman', 'numeral', 'conversion'],
    install_requires=[],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
