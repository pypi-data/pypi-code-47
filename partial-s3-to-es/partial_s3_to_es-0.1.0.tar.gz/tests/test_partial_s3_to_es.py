#!/usr/bin/env python

"""Tests for `partial_s3_to_es` package."""

import pytest
from unittest.mock import patch

from click.testing import CliRunner

from partial_s3_to_es import partial_s3_to_es
from partial_s3_to_es import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    keys = [
        "202001070941_0.gz",
        "202001070943_0.gz",
        "202001070945_0.gz",
        "202001070946_0.gz",
        "202001090629_0.gz",
        "202001090630_0.gz",
    ]
    sample_return = {
        "ResponseMetadata": {
            "RequestId": "tx0000000000001385ede11-005e182b99-4fb718-sgp1a",
            "HostId": "",
            "HTTPStatusCode": 200,
            "HTTPHeaders": {
                "transfer-encoding": "chunked",
                "x-amz-request-id": "tx0000000000001385ede11-005e182b99-4fb718-sgp1a",
                "content-type": "application/xml",
                "date": "Fri, 10 Jan 2020 07:45:29 GMT",
                "strict-transport-security": "max-age=15552000; includeSubDomains; preload",
            },
            "RetryAttempts": 0,
        },
        "IsTruncated": False,
        "Marker": "",
        "Contents": [{"Key": key} for key in keys],
        "Name": "salarium",
        "Prefix": "",
        "MaxKeys": 1000,
        "EncodingType": "url",
    }

    with patch.object(partial_s3_to_es.S3Client, "list_objects") as mock_list, patch.object(
        partial_s3_to_es.S3Client, "download_file"
    ) as mock_dl, patch.object(
        partial_s3_to_es.ESClient, "bulk"
    ) as mock_es:
        mock_list.return_value = sample_return
        content = '2020-01-01T06:30:01+00:00\ts3.test.file.test\t{"hello":"world"}'
        mock_dl.return_value = content
        result = runner.invoke(cli.main)
        assert result.exit_code == 0, result.output
        expected_data = [{'index': {'_index': 's3.test.file.test'}}, {'data': {'timestamp': '2020-01-01T06:30:01+00:00', 'index': 's3.test.file.test', 'data': '{"hello":"world"}'}}] * 6
        mock_es.assert_called_once_with(expected_data)
    assert result.exit_code == 0
    for key in keys:
        assert key in result.output, result.output

    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "Show this message and exit." in help_result.output

    invalid_dates_result = runner.invoke(cli.main, ["-s2020-01-01", "-e2000-:1-01"])
    assert invalid_dates_result.exit_code == 2, invalid_dates_result.output

    with patch.object(partial_s3_to_es.S3Client, "list_objects") as mock_list, patch.object(
        partial_s3_to_es.S3Client, "download_file"
    ) as mock_dl, patch.object(
        partial_s3_to_es.ESClient, "bulk"
    ) as mock_es:
        mock_list.return_value = sample_return
        content = '2020-01-01T06:30:01+00:00\ts3.test.file.test\t{"hello":"world"}\n' \
            '2020-01-03T06:30:01+00:00\ts3.test.file.test\t{"hello":"world"}'
        mock_dl.return_value = content
        result = runner.invoke(cli.main, ["-s2020-01-01", "-e2020-01-02"])
        expected_data = [{'index': {'_index': 's3.test.file.test'}}, {'data': {'timestamp': '2020-01-01T06:30:01+00:00', 'index': 's3.test.file.test', 'data': '{"hello":"world"}'}}] * 6
        assert result.exit_code == 0, result.output
        mock_es.assert_called_once_with(expected_data)
    for key in keys:
        assert key in result.output, result.output

    with patch.object(partial_s3_to_es.S3Client, "list_objects") as mock_list, patch.object(
        partial_s3_to_es.S3Client, "download_file"
    ) as mock_dl, patch.object(
        partial_s3_to_es.ESClient, "bulk"
    ) as mock_es:
        mock_list.return_value = sample_return
        content = '2020-01-01T06:30:01+00:00\ts3.test.file.test\t{"hello":"world"}\n' \
            '2020-01-03T06:30:01+00:00\ts3.test.file.test\t{"hello":"world"}'
        mock_dl.return_value = content
        result = runner.invoke(cli.main, ["-s2020-01-03", "-e2020-01-04"])
        expected_data = [{'index': {'_index': 's3.test.file.test'}}, {'data': {'timestamp': '2020-01-03T06:30:01+00:00', 'index': 's3.test.file.test', 'data': '{"hello":"world"}'}}] * 6
        assert result.exit_code == 0, result.output
        mock_es.assert_called_once_with(expected_data)
    for key in keys:
        assert key in result.output, result.output
