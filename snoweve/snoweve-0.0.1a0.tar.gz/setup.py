import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='snoweve',
    version='0.0.1-alpha',
    author='Tegar Bangun Suganda',
    author_email='tegarbangunsuganda@gmail.com',
    description='Logical Regex',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/suganda8/snoweve',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)