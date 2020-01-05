from setuptools import setup

with open('README.rst') as readme_file:
    long_description = readme_file.read()

with open('requirements.txt') as req_file:
    requirements = [r.strip() for r in req_file.readlines()]

setup(
    name='arbeiter',
    version='1.0.0',
    author='Daniel Andersson',
    author_email='daniel.4ndersson@gmail.com',
    description=('Correct and compute raw score of memory competitor\'s '
                 'recall data'),
    long_description=long_description,
    keywords='memory memorization iam wmc recall',
    url='https://gitlab.com/Penlect/arbeiter',
    install_requires=requirements,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    python_requires='>=3.6',
    packages=['arbeiter'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Other Audience',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)