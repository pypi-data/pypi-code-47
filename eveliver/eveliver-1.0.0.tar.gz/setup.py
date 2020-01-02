from setuptools import setup


if __name__ == '__main__':
    setup(
        name='eveliver',
        version='1.0.0',
        description='Some pytorch utilities for NLP',
        author='Jiaju Du',
        author_email='i@dujiaju.me',
        url='https://github.com/jiajudu/evelivers',
        packages=['eveliver'],
        install_requires=[
            'torch>=1.3.0',
            'numpy>=1.16.4'
        ]
    )
