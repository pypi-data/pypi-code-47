# -*- coding: utf-8 -*-
import os
import pytest
from unipath import Path
from databases.hive_helper import HiveHelper
from system.excelHelper import ExcelHelper


def __get_script_dir():
    tmp_current_path = os.path.dirname(os.path.realpath(__file__))
    return tmp_current_path


@pytest.fixture()
def get_hive_client():
    hive_client = HiveHelper(work_path_base=__get_script_dir())
    return hive_client


class TestHiveHelper(object):
    def test_process_hive_result(self, get_hive_client, user_list):
        hive_client_tmp = get_hive_client
        data_dict = {}
        if not user_list:
            return data_dict

        user_condition = "'%s'" % "','".join(user_list)
        sql_query = "select account,dept_desc1,dept_desc2,owner from bigdata_admin.dpp_hadoop_account_owner " \
                    "where account IN (%s) and concat_ws('-', year, month, day) = date_sub(current_date, 1);" \
                    % user_condition

        result_file = hive_client_tmp.hive_query(sql_query)
        if Path(result_file).exists():
            excel = ExcelHelper(result_file, column_split="\t")
            data_dict = excel.fetch_dict_data(excel.data, "account", ["dept_desc1", "dept_desc2", "owner"])
            for data_item in data_dict.keys():
                data_dict[data_item] = data_dict[data_item][0]
        return data_dict
