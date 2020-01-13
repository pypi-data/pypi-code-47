from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()
setup(
    name='check_driver',
    version='1.0.0',
    description='A small check driver',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Marcelo Tavares',
    author_email='contato@mtavaresc.com.br',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    install_requires=['requests'],
    python_requires='>=3.6'
)
