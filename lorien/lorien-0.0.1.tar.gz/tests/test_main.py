"""
The unit test module for the main entry and init import.
"""
# pylint:disable=unused-import

import mock

from lorien.logger import get_logger
from lorien.main import Main

log = get_logger('Unit-Test')


def test_main(mocker):
    # pylint:disable=missing-docstring, redefined-outer-name

    mock_args = mock.MagicMock()
    mock_args.log_run = True
    mock_args.entry = lambda x: None
    mocker.patch('lorien.main.make_config_parser').return_value = mock_args
    mocker.patch('lorien.main.enable_log_file').return_value = None
    Main()
