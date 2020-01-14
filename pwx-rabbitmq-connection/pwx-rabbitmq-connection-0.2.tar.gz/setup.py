from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pwx-rabbitmq-connection',
    version='0.2',
    url='',
    author='Guilherme Rosa Koerich',
    author_email='guilherme@pwx.cloud',
    description='Connection to RabbitMQ - PWX',
    keywords='connection rabbitmq pwx',
    packages=find_packages(exclude=['tests']),
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    install_requires=['pika==1.1.0'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    python_requires='>3.4',
)
