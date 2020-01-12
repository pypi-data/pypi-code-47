# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['peperoncino', 'peperoncino.processings', 'peperoncino.utils']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.17,<2.0', 'pandas>=0.25.3,<0.26.0', 'pyyaml>=5.1,<6.0']

setup_kwargs = {
    'name': 'peperoncino',
    'version': '0.0.5',
    'description': 'peperoncino: A library for easy data processing for pandas',
    'long_description': '# peperoncino: A library for easy data processing for pandas\n\n## Install\n\n```\n$ pip install peperoncino\n```\n\n## How to use\n\n### Processing DataFrame\n```python\nimport peperoncino as pp\n\npipeline = pp.Pipeline(\n    # query data\n    pp.Query("bar <= 3"),\n    # assign new feature\n    pp.Assign(hoge="foo * bar"),\n    # generate combination feature\n    pp.Combinations(["foo", "baz"], ["*", "/"]),\n    # target encoding\n    pp.TargetEncoding(["baz"], "y", ref=0),\n    # select features\n    pp.Select(\n        ["hoge", "*_foo_baz", "TARGET_ENC_baz_BY_y", "y"],\n        lackable_cols=["y"],\n    )\n)\n\n# execute the processing\ntrain_df, val_df, test_df = \\\n    pipeline.process([train_df, val_df, test_df])\n```\n\n### Predefined processings\n\n| name | description |\n| :--- | :---------- |\n| `ApplyColumn` | Apply a function to a column. |\n| `AsCategory` | Assign `category` dtype to columns. |\n| `Assign` | Assign a feature by a formula. |\n| `Combinations` | Create combination features. |\n| `DropColumns` | Drop columns. |\n| `DropDuplicates` | Drop duplicate rows. |\n| `Pipeline` | Chain processings. |\n| `Query` | Query rows by a given condition. |\n| `RenameCOlumns` | Rename columns. |\n| `Select` | Select columns. |\n| `StatsEncoding` | Encode columns by statistical values of another column. |\n| `TargetEncoding` | Target Encoding with smoothing. |\n\n### Define processing\nAll processings are subclass of `pp.BaseProcessing`.  \nAll you need is define the `_process(self, dfs: List[pd.DataFrame]) -> List[pd.DataFrame]` function.\n\n```python\nclass ExampleProcessing(pp.BaseProcessing):\n    def _process(self, dfs: List[pd.DataFrame]) -> List[pd.DataFrame]:\n        return [df + 1 for df in dfs]\n```\n\nIf your processing doesn\'t depent on each other data frames, then use `pp.SeparatedProcessing`.\n\n```python\nclass ExampleProcessing(pp.SeparatedProcessing):\n    def sep_process(self, df: pd.DataFrame) -> pd.DataFrame:\n        return df * 2\n```\n\nIf you need to merge all dataframes and then apply your processing, use `pp.MergedProcessing`.\n\n```python\nclass ExampleProcessing(pp.SeparatedProcessing):\n    def simul_process(self, df: pd.DataFrame) -> pd.DataFrame:\n        return df.assign(col1_mean=df[\'col1\'].mean())\n```\n\n\n',
    'author': 'Junki Ishikawa',
    'author_email': '69guitar1015@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.７,<4.0',
}


setup(**setup_kwargs)
