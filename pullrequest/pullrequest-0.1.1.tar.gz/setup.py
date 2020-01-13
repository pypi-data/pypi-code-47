from setuptools import setup, find_packages


setup(
    name='pullrequest',
    version='0.1.1',
    author='Eero Rikalainen',
    author_email='eerorika@gmail.com',
    url='https://github.com/eerorika/pullrequest',
    description='Create pullrequest to git service',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'PyGithub',
        'python-gitlab',
        'requests_oauthlib',
    ],
    entry_points={
        'console_scripts': [
            'pullrequest = pullrequest.cli:main'
        ]
    },
)
