#
# Copyright (c) 2019 Mobikit, Inc.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

import pkg_resources
import pandas as pd
import json
from ..config import config


url = pkg_resources.resource_filename("mobikit", "reference/constants.json")
with open(url) as f:
    data = json.load(f)
    config.meta_base = data["meta_constants"]
    col_ref_url = pkg_resources.resource_filename(
        "mobikit", "reference/column_dict.csv"
    )
    config.col_ref = pd.read_csv(col_ref_url)
    county_data_url = pkg_resources.resource_filename(
        "mobikit", "reference/counties_national.csv"
    )
    config.counties_ref = pd.read_csv(county_data_url)
