from setuptools import setup


setup(
    name='drgn',
    version='0.0.0',
    python_requires='>=3.6',
    author='Omar Sandoval',
    author_email='osandov@osandov.com',
    description='Scriptable debugger library',
    long_description='drgn is not yet available on PyPI. This is a placeholder.',
    url='https://github.com/osandov/drgn',
    project_urls={
        'Bug Tracker': 'https://github.com/osandov/drgn/issues',
        'Documentation': 'https://drgn.readthedocs.io',
    },
    license='GPL-3.0+',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Debuggers',
    ],
)
