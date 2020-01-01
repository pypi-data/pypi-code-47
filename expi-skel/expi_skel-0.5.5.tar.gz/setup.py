from setuptools import setup, find_packages

with open("README.rst", "r") as f:
    readme = f.read()

setup(
    name='expi_skel',
    version='0.5.5',
    author='2665093 Ontario Inc.',
    url='https://2665093.ca',
    author_email='chris@2665093.ca',
    packages=['expi_skel'],
    package_data={
        '': ['vi/*.vi', 'expi.json', ],
        },
    description='A package template for use with the Extender Package Index.',
    long_description=readme,
    include_package_data=True,
    install_requires=[
        'extools',
        # 'openpyxl',
        # 'markdown',
        # 'boto3',
    ],
    # Valid classifiers: https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Win32 (MS Windows)",
        "Intended Audience :: End Users/Desktop",
        "License :: Other/Proprietary License",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3.4",
    ],
    keywords=[
        "Orchid", "Extender", "Sage 300", "Automation",
    ],
    download_url="https://expi.2665093.ca/2665093/expi_skel",
)
