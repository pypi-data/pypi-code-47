# Copyright (C) 2019 Alteryx, Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
"""XGBoost classification algorithm."""
import pandas as pd

from ..utils.context_managers import CondaPrefixContext

# This is a hack, but is necessary in order for the Python SDK to resolve the DLL
# import location of XGBoost.
with CondaPrefixContext:
    import xgboost.sklearn


class XGBClassifier(xgboost.sklearn.XGBClassifier):
    """XGBClassifier classifier wrapper class."""

    def fit(self, x, y, *args, **kwargs):
        """Fit a model on training data."""
        x = self._convert_data(x)
        return super().fit(x, y, *args, **kwargs)

    def predict(self, x, *args, **kwargs):
        """Get predictions on test data."""
        x = self._convert_data(x)
        return super().predict(x, *args, **kwargs)

    def predict_proba(self, x, *args, **kwargs):
        """Get predictions with probabilities on test data."""
        x = self._convert_data(x)
        return super().predict_proba(x, *args, **kwargs)

    @staticmethod
    def _convert_data(x):
        """
        Convert incoming data to correct numpy array format if it's a dataframe.

        The XGBoost packages doesn't allow dataframes with [, ], or < in the column name.
        To avoid this issue, just use the underlying numpy ndarray as the training data.
        """
        if isinstance(x, pd.DataFrame):
            return x.values

        return x
