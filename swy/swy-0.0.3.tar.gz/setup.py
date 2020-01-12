import setuptools
import swy

with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = [el for el in f.readlines()]

setuptools.setup(
    name='swy',
    version=swy.__version__,
    author='Haytek',
    author_email='haytek34@gmail.com',
    description='SWY Project',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Haytek/swy',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Games/Entertainment"
    ],
    python_requires='>=3.7',
    install_requires=requirements
)
