#
# Copyright (c) 2019 Mobikit, Inc.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

import os

api_token = os.getenv("MOBIKIT_TEST_TOKEN")
schema = os.getenv("MOBIKIT_TEST_SCHEMA")
feed_id = int(os.getenv("MOBIKIT_TEST_FEED"))
