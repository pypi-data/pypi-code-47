import setuptools


with open("README.md", "r", encoding='UTF-8') as RMF:
    long_description = RMF.read()

setuptools.setup(
    name='pavis',
    version='0.0.3',
    author='huang825172',
    author_email='1048035187@qq.com',
    description="Parallel corpora version control engine",
    keywords='corpora parallel version control',
    long_description=long_description,
    url = 'http://at.senhacore.xyz:3000/huang825172/Pavis',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
    python_requires='>=3.6',
    install_requires=[
        'PyMySQL',
        'SQLAlchemy'
    ],
    package_dir={
        '':'src',
    },
)
