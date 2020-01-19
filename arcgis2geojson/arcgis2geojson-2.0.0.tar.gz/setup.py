# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['arcgis2geojson']

package_data = \
{'': ['*']}

entry_points = \
{'console_scripts': ['arcgis2geojson = arcgis2geojson:main']}

setup_kwargs = {
    'name': 'arcgis2geojson',
    'version': '2.0.0',
    'description': 'A Python library for converting ArcGIS JSON to GeoJSON',
    'long_description': '[![Build Status](https://travis-ci.org/chris48s/arcgis2geojson.svg?branch=master)](https://travis-ci.org/chris48s/arcgis2geojson)\n[![Coverage Status](https://coveralls.io/repos/github/chris48s/arcgis2geojson/badge.svg?branch=master)](https://coveralls.io/github/chris48s/arcgis2geojson?branch=master)\n![PyPI Version](https://img.shields.io/pypi/v/arcgis2geojson.svg)\n![License](https://img.shields.io/pypi/l/arcgis2geojson.svg)\n![Python Support](https://img.shields.io/pypi/pyversions/arcgis2geojson.svg)\n\n# arcgis2geojson.py\nA Python library for converting ArcGIS JSON to GeoJSON: A partial port of ESRI\'s [arcgis-to-geojson-utils](https://github.com/Esri/arcgis-to-geojson-utils/).\n\n## Installation\n```\npip install arcgis2geojson\n```\n\n## Usage\n\n### As a Library\n\n```python\n>>> input = {\n...     \'attributes\': {\'OBJECTID\': 123},\n...     \'geometry\': {   \'rings\': [   [   [41.8359375, 71.015625],\n...                                      [56.953125, 33.75],\n...                                      [21.796875, 36.5625],\n...                                      [41.8359375, 71.015625]]],\n...                     \'spatialReference\': {\'wkid\': 4326}}}\n>>> from arcgis2geojson import arcgis2geojson\n>>> output = arcgis2geojson(input)\n>>> import pprint\n>>> pp = pprint.PrettyPrinter(indent=4)\n>>> pp.pprint(output)\n{   \'geometry\': {   \'coordinates\': [   [   [41.8359375, 71.015625],\n                                           [56.953125, 33.75],\n                                           [21.796875, 36.5625],\n                                           [41.8359375, 71.015625]]],\n                    \'type\': \'Polygon\'},\n    \'id\': 123,\n    \'properties\': {\'OBJECTID\': 123},\n    \'type\': \'Feature\'}\n```\n\n### On the Console\n\n```sh\n# convert ArcGIS json file to GeoJOSN file\n$ arcgis2geojson arcgis.json > geo.json\n\n# fetch ArcGIS json from the web and convert to GeoJSON\n$ curl "https://myserver.com/arcgis.json" | arcgis2geojson\n```\n\n\n## Licensing\n\narcgis2geojson is a derivative work of ESRI\'s [arcgis-to-geojson-utils](https://github.com/Esri/arcgis-to-geojson-utils/). Original code is Copyright 2015 by Esri and was licensed under [the Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).\n\narcgis2geojson is made available under the MIT License.\n',
    'author': 'chris48s',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chris48s/arcgis2geojson',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.4,<4.0',
}


setup(**setup_kwargs)
