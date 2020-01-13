from setuptools import setup, find_packages

setup(
    name="algokit",
    version="0.1.2",
    keywords=["pip", "algokit", "algorithm"],
    description="common utilities and algorithm",
    long_description="common utilities and algorithm",

    url="https://github.com/wkgreat/algokit",
    author="ke wang",
    author_email="wkgreat@outlook.com",

    #python_requires='>=2.7',
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['pandas','geographiclib'],
    data_files=[("algokit/geo", ["algokit/geo/adcodes.csv"])]
)
