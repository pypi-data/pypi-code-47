# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dataprep',
 'dataprep.data_connector',
 'dataprep.eda',
 'dataprep.eda.basic',
 'dataprep.eda.correlation',
 'dataprep.eda.missing',
 'dataprep.eda.outlier',
 'dataprep.tests',
 'dataprep.tests.eda']

package_data = \
{'': ['*']}

install_requires = \
['bokeh>=1.4,<1.5',
 'dask[complete]>=2.9,<2.10',
 'holoviews>=1.12,<1.13',
 'jinja2>=2.10,<2.11',
 'jsonpath2>=0.4,<0.5',
 'jsonschema>=3.1,<3.2',
 'lxml>=4.4,<4.5',
 'numpy>=1.17,<1.18',
 'pandas>=0.25,<0.26',
 'probscale>=0.2,<0.3',
 'requests>=2.22,<2.23',
 'scipy>=1.3,<1.4']

setup_kwargs = {
    'name': 'dataprep',
    'version': '0.1.0',
    'description': 'Dataprep: Data Preparation in Python',
    'long_description': '# DataPrep ![Build Status]\n[Documentation] | [Mail List & Forum] \n\nDataprep is a collection of functions that \nhelps you accomplish tasks before you build a predictive model.\n\n\n## Implementation Status\n\nCurrently, you can use `dataprep` to:\n* Collect data from common data sources (through `dataprep.data_connector`)\n* Do your exploratory data analysis (through `dataprep.eda`)\n* ...\n\n\n## Installation\n\n```bash\npip install dataprep\n```\n\n`dataprep` is in its alpha stage now, so please manually specific the version number.\n\n\n## Examples & Usages\n\nMore detailed examples can be found at the [examples] folder.\n\n### Data Connector\n\nYou can download Yelp business search result into a pandas DataFrame, \nusing two lines of code, without taking deep looking into the Yelp documentation!\n\n```python\nfrom dataprep.data_connector import Connector\n\ndc = Connector("yelp", auth_params={"access_token":"<Your yelp access token>"})\ndf = dc.query("businesses", term="ramen", location="vancouver")\n```\n![DataConnectorResult]\n\n\n### EDA\n\nThere are common tasks during the exploratory data analysis stage, \nlike a quick look at the columnar distribution, or understanding the correlations\nbetween columns. \n\nThe EDA module categorizes these EDA tasks into functions helping you finish EDA\ntasks with a single function call.\n\n* Want to understand the distributions for each DataFrame column? Use `plot`.\n```python\nfrom dataprep.eda import plot\n\ndf = ...\n\nplot(df)\n```\n<center><img src="https://github.com/sfu-db/dataprep/raw/master/assets/plot(df).png"/></center>\n\n* Want to understand the correlation between columns? Use `plot_correlation`.\n\n```python\nfrom dataprep.eda import plot_correlation\n\ndf = ...\n\nplot_correlation(df)\n```\n<center><img src="https://github.com/sfu-db/dataprep/raw/master/assets/plot_correlation(df).png" width="50%" height="50%"/></center>\n\n* Or, if you want to understand the impact of the missing values for each column, use `plot_missing`.\n\n```python\nfrom dataprep.eda import plot_missing\n\ndf = ...\n\nplot_missing(df)\n```\n<center><img src="https://github.com/sfu-db/dataprep/raw/master/assets/plot_missing(df).png" width="50%" height="50%"/></center>\n\n* You can even drill down to get more information by given `plot`, `plot_correlation` and `plot_missing` a column name.\n\n```python\ndf = ...\n\nplot_missing(df, x="some_column_name")\n```\n\n<center><img src="https://github.com/sfu-db/dataprep/raw/master/assets/plot_missing(df,x).png" width="50%"/></center>\n\nDon\'t forget to checkout the [examples] folder for detailed demonstration!\n\n## Contribution\nContribution is always welcome. \nIf you want to contribute to dataprep, be sure to read the [contribution guidelines].\n\n\n\n\n\n[Build Status]: https://img.shields.io/circleci/build/github/sfu-db/dataprep/master?style=flat-square&token=f68e38757f5c98771f46d1c7e700f285a0b9784d\n[Documentation]: https://sfu-db.github.io/dataprep/\n[Mail list & Forum]: https://groups.google.com/forum/#!forum/dataprep\n[contribution guidelines]: https://github.com/sfu-db/dataprep/blob/master/CONTRIBUTING.md\n[examples]: https://github.com/sfu-db/dataprep/tree/master/examples\n[DataConnectorResult]: https://github.com/sfu-db/dataprep/raw/master/assets/data_connector.png\n',
    'author': 'Jiannan Wang',
    'author_email': 'jnwang@sfu.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sfu-db/dataprep',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
