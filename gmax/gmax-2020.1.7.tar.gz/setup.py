from setuptools import setup, find_packages

setup(
    cffi_modules=["gmax/remma/remma_cpu/_build.py:ffi", "gmax/process_plink/_build.py:ffi"],
    name='gmax',
    version='2020.1.7',
    description='Genomic Multivariate Analysis eXpedited',
    long_description=open('README.rst').read(),
    author='Chao Ning',
    author_email='ningchao91@gmail.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url="https://github.com/chaoning/GMAX",
    include_package_data = True,
    install_requires=[
        'numpy>=1.16.0',
        'pandas>=0.19.0',
        'scipy>=1.1.1',
        'cffi>=1.12.0',
        'pandas_plink>=2.0.0',
    ],

)


