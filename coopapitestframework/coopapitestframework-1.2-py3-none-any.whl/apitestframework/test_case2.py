# coding:utf-8
import pytest
# import allure

from apitestbasiclib.apitestlogic import apitest
from apitestbasiclib.filetools import get_testcases

env_name = 'fat'
test_cases = get_testcases('./testcases/testcase.yaml')
print(test_cases)

# @allure
@pytest.mark.parametrize('test_cases',test_cases)
def test_yamlapi(test_cases):
    apitest(test_cases,env_name)