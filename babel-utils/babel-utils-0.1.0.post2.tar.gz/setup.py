from setuptools import setup

setup(
    name='babel-utils',
    version='0.1.0.post2',
    description='WARNING: This package has been renamed to bpc-utils!',
    long_description='⚠ DEPRECATION WARNING: This package has been renamed to [bpc-utils](https://pypi.org/project/bpc-utils)! ⚠',
    long_description_content_type='text/markdown',
    url='https://github.com/pybpc/bpc-utils',
    author='Saiyang Gou',
    author_email='gousaiyang223@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    py_modules=['babel_utils'],
    python_requires='>=3',
)
