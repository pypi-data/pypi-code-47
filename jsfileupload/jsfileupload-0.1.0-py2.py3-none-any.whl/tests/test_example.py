#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Juelich Supercomputing Centre (JSC).
# Distributed under the terms of the Modified BSD License.

import pytest

from ..upload_widget import FileUpload


def test_example_creation_blank():
    w = FileUpload()
    assert w.upload_url == 'http://localhost:8888/api/contents/'
