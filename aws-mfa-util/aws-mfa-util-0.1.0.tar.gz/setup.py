import setuptools

with open('README.md', 'r') as fd:
    long_description = fd.read()

setuptools.setup(
    name='aws-mfa-util',
    version='0.1.0',
    author='hiroya akita',
    author_email='akky.develop@gmail.com',
    description='AWS CLIにMFA適用アカウントを作成・更新するためのツール',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    install_requires=['boto3', 'PyInquirer'],
    url='https://github.com/papi-tokei/aws-mfa-util',
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts':[
            'aws-mfa-util=aws_mfa_util:main'
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3.6',
)
