from setuptools import setup, find_packages

setup(
    name='python-verbal',
    use_scm_version=True,
    author_email='dev@cf-partners.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    package_data={},
    install_requires=[
        'pyyaml',
        'pymongo',
        'psutil>=2.1.1',
        'argh',
        'tornado',
        'coverage'
    ],
    setup_requires=['setuptools_scm', 'setuptools', 'twine', 'wheel'],
    entry_points={ 'console_scripts' : [
        'mongolog = verbal.mongolog:main'
    ]},
    tests_require=['nose', 'tox', 'nose-testconfig'],
    test_suite="nose.collector"
)

