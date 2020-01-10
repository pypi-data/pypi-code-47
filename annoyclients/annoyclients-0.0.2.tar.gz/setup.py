from setuptools import setup, find_packages

__version__ = '0.0.2'
requirements = [
    'grpcio',
    'grpcio-tools'
]
setup(
    # Metadata
    name='annoyclients',
    version=__version__,
    author='USopaoglu',
    description='Annoy Client',
    # Package info
    packages=find_packages(exclude=('docs', 'tests', 'scripts')),
    zip_safe=True,
    include_package_data=True,
    install_requires=requirements,
)
