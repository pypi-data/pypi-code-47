import setuptools
__author__ = 'Nguyen Quang Cuong'
__email__ = 'cuong.nguyen@f4.intek.edu.vn'
__version = '1.0.0'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spriteutil-intek-2020-nqcuong96",
    author=__author__,
    author_email=__email__,
    version=__version,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url="https://github.com/intek-training-jsc/sprite-sheet-nqcuong96",
    packages=['sprite_sheet'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'numpy==1.18.1',
        'pillow==7.0.0',
        'setuptools==45.0.0',
        'wheel==0.33.6',
        'twine==3.1.1',
        'pipfile==0.0.2'
    ],
    python_requires='>=3.7',
)
