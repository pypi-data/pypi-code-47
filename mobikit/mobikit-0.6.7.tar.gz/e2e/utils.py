#
# Copyright (c) 2019 Mobikit, Inc.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#

from datetime import datetime
import json


def format_test(func):
    def _format_test(*args, **kwargs):
        print(f"\n\n{func}")
        print("-------------------------------")
        res = func(*args, **kwargs)
        print("-------------------------------")
        return res

    return _format_test


def record_exec_time(func):
    def _record_exec_time(*args, **kwargs):
        t1 = datetime.now()
        res = func(*args, **kwargs)
        t2 = datetime.now()
        print(f"Elapsed time: {t2 - t1}")
        return res

    return _record_exec_time


def is_json(val):
    try:
        json.loads(val)
        return True
    except ValueError:
        return False
