from setuptools import setup

setup(
    name='kefrey',
    version='0.1.1',
    description='A tool to track system-wide keypress frequencies',
    url='https://github.com/matthewscholefield/kefrey',
    author='Matthew D. Scholefield',
    author_email='matthew331199@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='kefrey',
    packages=['kefrey'],
    install_requires=['pyxhook'],
    entry_points={
        'console_scripts': [
            'kefrey=kefrey.__main__:main',
            'kefrey-install=kefrey.installer:main'
        ],
    }
)
