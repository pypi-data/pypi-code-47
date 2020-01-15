from distutils.core import setup
setup(
    name='phxlib',
    packages=['phxlib'],
    version='0.1.1b',
    license='MIT',
    description='Library for personal use with some useful functions and tools',
    long_description='PhxLib is a set of personal tools for personal use that '
                     'will add some automated features to Python like logging. '
                     'This will be updated anytime I need to develop a new tool.',
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
