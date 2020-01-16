try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

REQUIRED_PACKAGES = [
    'pyAesCrypt==0.4.2',
    'colorama==0.4.1',
    'PyYAML==3.13',
    'binaryornot==0.4.4'
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="god_mode",
    version="1.0.3",
    author="Nicolas Lettiere",
    author_email="braum.exe@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    description="Python 3 script to easy encrypt/decrypt files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    platforms='any',
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': [
            'crypt = god_mode.crypt:main',
            'crypt2 = god_mode.crypt2:main',
            'god-mode = god_mode.crypt2:main'
        ],
    }
)
