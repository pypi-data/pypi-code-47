from setuptools import setup, find_packages

setup(
    name='boppy',
    version='0.0.1',
    description=("placeholder for boppy"),
    url='https://github.com/eexwhyzee/boppy',
    author='Minh Hoang',
    author_email='eexwhyzee@gmail.com',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3',
    install_requires=['requests'],
    test_suite='nose.collector',
    tests_require=['nose']
)
