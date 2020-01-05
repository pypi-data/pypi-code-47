import setuptools
import distutils

long_description = """
MapsBR - Get brazilian geospatial data with Python

This package helps you get brazilian geospatial data from IBGE sources directly into a GeoPandas structure. It also has functionalities to retrieve data from an ArcGIS server.

Learn more about it in our [repository](https://github.com/phelipetls/mapsbr) or [documentation](https://mapsbr.readthedocs.io).
"""

setuptools.setup(
    name="mapsbr",
    version="0.0.3",
    author="Phelipe Teles",
    author_email="phelipe_teles@hotmail.com",
    description="Getting brazilian geospatial data with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phelipetls/mapsbr",
    packages=setuptools.find_packages(),
    install_requires=["geopandas", "requests", "descartes", "shapely", "matplotlib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    project_urls={"Documentation": "https://mapsbr.readthedocs.io/"},
)
