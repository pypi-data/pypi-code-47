# coding:utf-8
# import allure
import pytest

from apitestbasiclib.apitestlogic import apitest
from apitestbasiclib.filetools import get_testcases
# class TestYamlApi:
env_name = 'fat'
    # @classmethod
    # def setup_class(cls):
test_cases = get_testcases('./testcases/testcase.yaml')
        # test_cases = get_testcases(file_path)
print(test_cases)

    # @allure.feature('获取公司列表相关测试用例')
@pytest.mark.parametrize('test_cases',test_cases)
def test_yamlapi(test_cases):
    apitest(test_cases,env_name)