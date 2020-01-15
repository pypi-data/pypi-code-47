from distutils.core import setup

setup(
    name='phxlib',
    packages=['phxlib'],
    version='0.1.10',
    license='MIT',
    description='Library for personal use with some useful functions and tools',
    long_description='This is a set of tools to easify the task of programming '
                     'on Python (even more). This is intended for personal use.',
    author='PhoxSpark',
    author_email='lgraciamorales@icloud.com',
    url='https://gitlab.com/PhoxSpark/phxlib',
    download_url='https://gitlab.com/PhoxSpark/phxlib/-/archive/master/phxlib-master.zip',
    keywords=['library', 'tools', 'useful'],
    install_requires=[],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        # as the current state of your package
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.8',
    ],
)
