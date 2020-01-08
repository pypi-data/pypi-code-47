from setuptools import setup, find_packages


with open('README.rst', encoding='utf-8') as f:
    long_description = ''.join(f.readlines())


setup(
    name='jdog',
    version='0.1.0',
    description='Just another Data Offline Generator',
    long_description=long_description,
    author='Petr Nymsa',
    author_email='nymsa.petr@outlook.cz',
    keywords='data generator, data generation, json scheme, scheme based, cli tool',
    license='MIT',
    url='https://github.com/petrnymsa/jdog',
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Environment :: Console',
        'Topic :: Software Development :: Libraries',
    ],
    entry_points={
        'console_scripts': [
            'jdog = jdog.cli:run',
        ],
    },
    install_requires=['Faker', 'click>=6'],
    zip_safe=False,
)
