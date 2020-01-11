"""
The unit test for database.
"""
import json
from copy import deepcopy

import pytest
from moto import mock_dynamodb2
from testfixtures import TempDirectory

from lorien.database.commit import commit_tuning_log
from lorien.database.query import query_result_by_tasks, query_table_by_targets
from lorien.database.table import create_table, delete_table, list_tables
from lorien.database.util import (convert_to_db_dict, convert_to_db_list, convert_to_dict,
                                  convert_to_list, gen_primary_key, parse_target)
from tvm.autotvm.record import load_from_file


@pytest.fixture
def fixture_log():
    # pylint:disable=missing-docstring, redefined-outer-name

    log_history = [{
        "i": [
            "cuda", "topi_nn_conv2d",
            [["TENSOR", [1, 192, 14, 14], "float32"], ["TENSOR", [64, 192, 1, 1], "float32"],
             [1, 1], [0, 0], [1, 1], "NCHW", "float32"], {},
            [
                "conv2d", [1, 192, 14, 14, "float32"], [64, 192, 1, 1, "float32"], [1, 1], [0, 0],
                [1, 1], "NCHW", "float32"
            ], {
                "i":
                0,
                "t":
                "direct",
                "c":
                "",
                "e": [["tile_f", "sp", [-1, 1, 1, 1]], ["tile_y", "sp", [-1, 1, 1, 1]],
                      ["tile_x", "sp", [-1, 1, 1, 1]], ["tile_rc", "sp", [-1, 1]],
                      ["tile_ry", "sp", [-1, 1]], ["tile_rx", "sp", [-1, 1]],
                      ["auto_unroll_max_step", "ot", 0], ["unroll_explicit", "ot", 0]]
            }
        ],
        "r": [[6.910177325863514e-05], 0, 3.3606743812561035, 1571384808.112297],
        "v":
        0.1
    }, {
        "i": [
            "cuda", "topi_nn_conv2d",
            [["TENSOR", [1, 192, 14, 14], "float32"], ["TENSOR", [64, 192, 1, 1], "float32"],
             [1, 1], [0, 0], [1, 1], "NCHW", "float32"], {},
            [
                "conv2d", [1, 192, 14, 14, "float32"], [64, 192, 1, 1, "float32"], [1, 1], [0, 0],
                [1, 1], "NCHW", "float32"
            ], {
                "i":
                1,
                "t":
                "direct",
                "c":
                "",
                "e": [["tile_f", "sp", [-1, 2, 1, 1]], ["tile_y", "sp", [-1, 1, 1, 1]],
                      ["tile_x", "sp", [-1, 1, 1, 1]], ["tile_rc", "sp", [-1, 1]],
                      ["tile_ry", "sp", [-1, 1]], ["tile_rx", "sp", [-1, 1]],
                      ["auto_unroll_max_step", "ot", 0], ["unroll_explicit", "ot", 0]]
            }
        ],
        "r": [[0.0001789090005619872], 0, 3.503542423248291, 1571384811.1822321],
        "v":
        0.1
    }, {
        "i": [
            "cuda", "topi_nn_conv2d",
            [["TENSOR", [1, 192, 14, 14], "float32"], ["TENSOR", [64, 192, 1, 1], "float32"],
             [1, 1], [0, 0], [1, 1], "NCHW", "float32"], {},
            [
                "conv2d", [1, 192, 14, 14, "float32"], [64, 192, 1, 1, "float32"], [1, 1], [0, 0],
                [1, 1], "NCHW", "float32"
            ], {
                "i":
                2,
                "t":
                "direct",
                "c":
                "",
                "e": [["tile_f", "sp", [-1, 4, 1, 1]], ["tile_y", "sp", [-1, 1, 1, 1]],
                      ["tile_x", "sp", [-1, 1, 1, 1]], ["tile_rc", "sp", [-1, 1]],
                      ["tile_ry", "sp", [-1, 1]], ["tile_rx", "sp", [-1, 1]],
                      ["auto_unroll_max_step", "ot", 0], ["unroll_explicit", "ot", 0]]
            }
        ],
        "r": [[0.00010959697682797598], 0, 3.3525550365448, 1571384814.0914505],
        "v":
        0.1
    }, {
        "i": [
            "cuda", "topi_nn_conv2d",
            [["TENSOR", [1, 192, 14, 14], "float32"], ["TENSOR", [64, 192, 1, 1], "float32"],
             [1, 1], [0, 0], [1, 1], "NCHW", "float32"], {},
            [
                "conv2d", [1, 192, 14, 14, "float32"], [64, 192, 1, 1, "float32"], [1, 1], [0, 0],
                [1, 1], "NCHW", "float32"
            ], {
                "i":
                3,
                "t":
                "direct",
                "c":
                "",
                "e": [["tile_f", "sp", [-1, 8, 1, 1]], ["tile_y", "sp", [-1, 1, 1, 1]],
                      ["tile_x", "sp", [-1, 1, 1, 1]], ["tile_rc", "sp", [-1, 1]],
                      ["tile_ry", "sp", [-1, 1]], ["tile_rx", "sp", [-1, 1]],
                      ["auto_unroll_max_step", "ot", 0], ["unroll_explicit", "ot", 0]]
            }
        ],
        "r": [[7.696898659974661e-05], 0, 3.386526107788086, 1571384817.0555751],
        "v":
        0.1
    }, {
        "i": [
            "cuda", "topi_nn_conv2d",
            [["TENSOR", [1, 192, 14, 14], "float32"], ["TENSOR", [64, 192, 1, 1], "float32"],
             [1, 1], [0, 0], [1, 1], "NCHW", "float32"], {},
            [
                "conv2d", [1, 192, 14, 14, "float32"], [64, 192, 1, 1, "float32"], [1, 1], [0, 0],
                [1, 1], "NCHW", "float32"
            ], {
                "i":
                4,
                "t":
                "direct",
                "c":
                "",
                "e": [["tile_f", "sp", [-1, 16, 1, 1]], ["tile_y", "sp", [-1, 1, 1, 1]],
                      ["tile_x", "sp", [-1, 1, 1, 1]], ["tile_rc", "sp", [-1, 1]],
                      ["tile_ry", "sp", [-1, 1]], ["tile_rx", "sp", [-1, 1]],
                      ["auto_unroll_max_step", "ot", 0], ["unroll_explicit", "ot", 0]]
            }
        ],
        "r": [[6.983315277467744e-05], 0, 3.373988151550293, 1571384819.997475],
        "v":
        0.1
    }]
    return log_history


@mock_dynamodb2
def test_database(fixture_log):
    # pylint:disable=missing-docstring, redefined-outer-name

    # Fake tuned data
    with TempDirectory() as temp_dir:
        # Test table manipulation.
        table_name = create_table('topi', 'cuda', region_name='us-west-2')
        assert table_name is not None

        # Test list table.
        assert len(list_tables(region_name='us-west-2')) == 1
        assert not list_tables('non-exist-table', region_name='us-west-2')

        # Test push item.
        with pytest.raises(RuntimeError):
            commit_tuning_log('invalid-file', table_name, region_name='us-west-2')

        log_file = '{}/fake.log'.format(temp_dir.path)
        with open(log_file, 'w') as filep:
            fail_record = deepcopy(fixture_log[0])
            fail_record['r'][1] = 4  # error code is not zero
            filep.write(json.dumps(fail_record))

        # Raise for no valid records
        with pytest.raises(RuntimeError):
            commit_tuning_log(log_file, table_name, region_name='us-west-2')

        with open(log_file, 'w') as filep:
            for record in fixture_log:
                filep.write('{}\n'.format(json.dumps(record)))

        # Successfully committed.
        commit_tuning_log(log_file, table_name, region_name='us-west-2')

        # Raise due to non-existed target table.
        with pytest.raises(RuntimeError):
            query_table_by_targets(['unknown-target'], region_name='us-west-2')

        latest_names = query_table_by_targets(['cuda'], region_name='us-west-2')
        assert latest_names['cuda'] == table_name

        # Test query records.
        inp, _ = next(load_from_file(log_file))
        with pytest.raises(RuntimeError):
            # No target specified in task.
            query_result_by_tasks([inp.task], region_name='us-west-2')

        with pytest.raises(RuntimeError):
            # Wrong table name.
            query_result_by_tasks([inp.task], 'invalid-table', region_name='us-west-2')

        inp.task.target = inp.target
        result = query_result_by_tasks([inp.task], region_name='us-west-2')[0]
        assert len(result) == 1
        assert 'config' in result[0]
        assert 'latency' in result[0] and abs(result[0]['latency'] - 6.91e-05) < 1e-3
        assert 'thrpt' in result[0]

        # Test commit with result updating.
        log_file2 = '{}/fake2.log'.format(temp_dir.path)
        with open(log_file2, 'w') as filep:
            for record in fixture_log:
                record['r'][0][0] = record['r'][0][0] / 2  # Speedup by 2x.
                filep.write('{}\n'.format(json.dumps(record)))
        commit_tuning_log(log_file2, table_name, region_name='us-west-2')

        result = query_result_by_tasks([inp.task], region_name='us-west-2')[0]
        # FIXME: moto has a bug with update_item. Re-open this test after the PR is merged.
        # https://github.com/spulec/moto/pull/2675
        #assert len(result) == 2
        #assert 'latency' in result[1] and abs(result[1]['latency'] - 3.455e-05) < 1e-3

        # Remove the unit test table.
        delete_table(table_name, region_name='us-west-2')


def test_database_util(fixture_log):
    # pylint:disable=missing-docstring, redefined-outer-name

    # Fake tuned data
    with TempDirectory() as temp_dir:
        log_file = '{}/fake.log'.format(temp_dir.path)
        with open(log_file, 'w') as filep:
            filep.write('{}\n'.format(json.dumps(fixture_log[0])))

        inp, _ = next(load_from_file(log_file))
        task = inp.task

        assert gen_primary_key(task) == \
               'topi_nn_conv2d#_TENSOR__1_192_14_14__float32_' \
               '#_TENSOR__64_192_1_1__float32_#_1_1_#_0_0_#_1_1_#NCHW#float32'

        assert parse_target(str(inp.target)) == ('cuda', ' ')

        orig_list = ['string', 123.34, 345, [1, 2, None], {'a': 2, 'b': 8}]
        db_list = convert_to_db_list(orig_list)
        assert orig_list == convert_to_list(db_list)

        orig_dict = {'a': 'string', 'b': 123.45, 'c': None, 'd': [1, 2, 3], 'e': {'p': 3, 'q': 4}}
        db_dict = convert_to_db_dict(orig_dict)
        assert orig_dict == convert_to_dict(db_dict)
