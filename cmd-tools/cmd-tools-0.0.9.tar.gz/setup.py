from setuptools import find_packages, setup


def long_long_description():
    with open('README.md', 'r') as f:
        desc = f.read()
    return desc


setup(
    name='cmd-tools',
    version='0.0.9',
    description='command tools',
    long_description=long_long_description(),
    author='buglan',
    author_email='1831353087@qq.com',
    scripts=['command.py'],
    packages=find_packages(),
    install_requires=['click'],
    entry_points='''
        [console_scripts]
        hello=command:hello
        cmd=command:cmd
        define=command:define
        u=command:open_url
    ''',
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        'pytest',
    ]

)
