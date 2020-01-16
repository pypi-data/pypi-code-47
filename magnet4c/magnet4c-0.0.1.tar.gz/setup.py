import setuptools


with open("README.md", "r", encoding='UTF-8') as RMF:
    long_description = RMF.read()

setuptools.setup(
    name='magnet4c',
    version='0.0.1',
    author='huang825172',
    author_email='1048035187@qq.com',
    description="Corpora operator for multiple file formats.",
    keywords='corpora parallel file extract replace',
    long_description=long_description,
    url = 'http://at.senhacore.xyz:3000/huang825172/Magnet',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
    install_requires=[
        'pypandoc',
    ],
    package_dir={
        '':'src',
    },
    packages=setuptools.find_packages(where='src')
)