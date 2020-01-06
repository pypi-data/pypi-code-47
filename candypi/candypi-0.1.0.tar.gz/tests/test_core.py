#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import pytest

from candypi import check_directory


class TestCheckDirectory(object):
    
    @pytest.mark.skip(reason='This test cannot run in CI env.')
    def test_check_directory(self):
        TESTS = [
            ('/Users/iwasa/work/mogbee')
        ]

        for t in TESTS:
            # print(t)
            assert check_directory(t) == t

    def test_patherror(self):
        with pytest.raises(FileExistsError):
            check_directory('/work')
    
    def test_git_exist_error(self):
        with pytest.raises(FileExistsError):
            check_directory('/User/iwasa/work')
