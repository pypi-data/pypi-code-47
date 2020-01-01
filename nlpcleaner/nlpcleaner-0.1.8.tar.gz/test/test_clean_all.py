# -*- coding: utf-8 -*-

import pytest

from nlpcleaner import Text

def test_en_clean_all():
    txt = "MANY dogs enjoy tug and chew toys and playing 'hide and seek' with you outdoors http://www.test.it http://www.test.it"
    assert Text(txt).clean() == "many dog enjoy tug chew toy playing hide seek outdoors"

def test_it_clean_all():
    txt = "Ieri sono andato in due supermercati. Oggi volevo andare all'ippodromo. Stasera mangio la pizza con le verdure."
    assert Text(txt).clean() == "ieri andato due supermercati oggi volevo andare ippodromo stasera mangio pizza verdure"
