from setuptools import setup

readme = ''
with open('readme.md', mode='r', encoding='utf-8') as fd:
    readme = fd.read()

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='ihsm_analytics',
    author='Huy Nguyen',
    author_email='huy.nguyen@ihsmarkit.com',
    # Needed to actually package something
    packages=['ihsm_analytics'],
    # Needed for dependencies
    install_requires=['numpy', 'pandas'],
    url='https://ihsmarkit.com/',
    long_description=readme,
    include_package_data=True,
    # *strongly* suggested for sharing
    version='0.0.2',
    # The license can be anything you like
    license='MIT',
    description='The package provides advanced geo-analytics functionalities.',
    # We will also need a readme eventually (there will be a warning)
    classifiers=[
        # Trove classifiers
        # The full list is here: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Operating System :: Microsoft :: Windows',
        'Topic :: Software Development :: Libraries'
    ],
    python_requires='>=3.7'
)