from setuptools import setup
from distutils.core import setup


def getFile():
    with open('README.rst') as f:
        return f.read()


setup(
    name="actuarialCalculations",
    packages=['actuarialCalculations'],
    version='1.0.1',
    long_description_content_type='text/markdown',
    long_description=getFile(),
    author='Sadik Erisen',
    author_email='fserisen@gmail.com',
    keywords=['finance', 'annuity calculations', 'actuarial math', 'financial math',
              'amortization schedule', 'sinking fund', 'present value', 'accumulated value'],
    url = "https://github.com/francose/acturialcalculations",
    download_url = 'https://github.com/francose/acturialcalculations/archive/master.zip',
    install_requires=[
        'numpy==1.16.6',
        'pandas==0.24.2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

)
