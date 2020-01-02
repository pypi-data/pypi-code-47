#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `eight2` package."""

import pytest

from eight2.rulus import getZhiSanhui

l = [2, 6, 10]


# print("===tiangan===")
# print(getTgHe(l))
# print(getTgChong(l))
# print(getTgKe(l))
# print("===dizhi===")
#
# print(getZhiHe(l))
# print(getZhiChong(l))
# print(getZhiXianghai(l))
# print(getZhiXiangxing(l))
# print(getZhiSanhe(l))
# # print(getZhiSanheban(l))
# print(getZhiSanhui(l))


def test_di_zhi_san_hui():
    '''
    地支三会测试
    :return:
    '''
    assert getZhiSanhui(l)


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')

# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string
#
#
# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'eight2.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output
