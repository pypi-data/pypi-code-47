from typing import List

import pytest
import requests

from python_request_fanout.requester import HTTPMethod, Requester

request_list_1 = [
    requests.Request(
        HTTPMethod.GET.name,
        url="https://www.uchile.cl/uchile/framework/skins/uchile20-home/css/img/logo-universidad-de-chile.svg"
    ),
    requests.Request(
        HTTPMethod.GET.name,
        url="https://github.githubassets.com/images/spinners/octocat-spinner-128.gif"
    ),
]


@pytest.mark.parametrize(
    "case, request_list",
    [
        (
                "test1", request_list_1
        ),
    ],
)
def test_do_requests_test(case: str, request_list: List[requests.Request]):
    resp = Requester.do_requests(request_list)
    assert len(resp) == 2
