# coding:utf-8
# import allure
import pytest

from yamlapitest.apitestbasiclib.filetools import get_testcases
from yamlapitest.apitestbasiclib.apitestlogic import apitest

env_name = 'fat'
test_cases = get_testcases('./testcases/testcase.yaml')
print(test_cases)

    # @allure.feature('获取公司列表相关测试用例')
@pytest.mark.parametrize('test_cases',test_cases)
def test_yamlapi(test_cases):
    apitest(test_cases,env_name)