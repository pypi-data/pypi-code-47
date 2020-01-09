import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

from parametergrouptotf import VERSION

setuptools.setup(
    name='aws-rds-parameter-group-to-tf',
    version=VERSION,
    author='Lev Kokotov',
    author_email='lev.kokotov@instacart.com',
    description='Create a Terraform parameter group from an AWS RDS parameter group.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/levkk/aws-rds-parameter-group-to-tf',
    install_requires=[
        'Click>=7.0',
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'parametergrouptotf = parametergrouptotf:cli',
        ]
    },
)
