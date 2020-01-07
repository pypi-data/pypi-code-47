#!/usr/bin/env python

"""Tests for `network_connectivity_tester` package."""

from network_connectivity_tester.awsclient import AWSConnectivityTestClient


def test_ping_check():
    assert AWSConnectivityTestClient.ping_check("8.8.8.8")


def test_url_check():
    assert AWSConnectivityTestClient.url_check("https://www.google.com/")


# def test_tcp_check():
#     assert AWSConnectivityTestClient.socat(4444)
#     assert AWSConnectivityTestClient.tcp_check("127.0.0.1:4444")


