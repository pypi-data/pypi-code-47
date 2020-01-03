from setuptools import setup, find_packages

version = '6.0.1'

setup(
    name='django-yarnpkg',
    version=version,
    description="Integrate django with yarnpkg",
    long_description=open('README.rst').read(),
    classifiers=[
        'Framework :: Django',
        'Programming Language :: JavaScript',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    author='Dominik George',
    author_email='nik@naturalnet.de',
    url='https://edugit.org/nik/django-yarnpkg',
    license='BSD',
    packages=find_packages(exclude=['example']),
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'django',
        'six',
    ],
    entry_points="""
      # -*- Entry points: -*-
      """,
)
