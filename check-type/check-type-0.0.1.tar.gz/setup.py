from setuptools import setup

setup(
    name='check-type',
    version='v0.0.1',
    description='Runtime Python type checking',
    author='jsh9',
    license='MIT',
    url='https://github.com/jsh9/PySeismoSoil',
    packages=['check_type'],
    classifiers=[
        'Typing :: Typed',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    install_requires=[
        'typeguard>=2.7.1',
    ],
    python_requires='>=3.6',
    include_package_data=True,
)
