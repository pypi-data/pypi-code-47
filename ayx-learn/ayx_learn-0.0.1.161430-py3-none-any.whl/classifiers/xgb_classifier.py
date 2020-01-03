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
from ..utils.context_managers import CondaPrefixContext

# This is a hack, but is necessary in order for the Python SDK to resolve the DLL
# import location of XGBoost.
with CondaPrefixContext:
    import xgboost.sklearn


class XGBClassifier(xgboost.sklearn.XGBClassifier):
    """XGBClassifier classifier wrapper class."""
