import unittest
import os
from unittest import mock

from nubium_utils.faust_utils import FaustAppWrapper
from nubium_utils.faust_utils import InstrumentedApp
from nubium_utils.faust_utils import get_ssl_context


class ImplementedAppWrapper(FaustAppWrapper):

    def _init_agents(self):
        pass

    def _init_records(self):
        pass

    def _init_serializers(self):
        pass

    def _init_tables(self):
        pass

    def _init_topics(self):
        pass


class TestFaustAppWrapper(unittest.TestCase):
    """
    Tests the app wrapper
    """

    def test_app_creation(self):

        test_faust_config = {
            'id': 'test-id',
            'broker': 'kafka://test',
            'store': "memory://"
        }
        mock_monitor = mock.MagicMock()

        app_wrapper = ImplementedAppWrapper(test_faust_config, avro_client=None, metrics_manager=mock_monitor)
        assert app_wrapper.app.__class__ == InstrumentedApp


class TestFaustHelpers(unittest.TestCase):

    def test_no_ssl_context(self):
        """
        get_ssl_context returns None when `USE_SSL` env variable is False
        """
        os.environ['USE_SSL'] = 'False'

        output = get_ssl_context()
        assert output is {}

    def test_get_ssl_context(self):
        """
        SSL context configures from env variables when `USE_SSL` is True
        """
        os.environ = {'USE_SSL': 'True', 'SSL_CA_LOCATION': 'test-ca-location',
                      'SSL_CERTIFICATE_LOCATION': 'test',
                      "SSL_KEY_LOCATION": "test"}

        with mock.patch('nubium_utils.faust_utils.helpers.ssl') as ssl_patch:
            output = get_ssl_context()
            ssl_patch.create_default_context.assert_called_once()
            output.load_cert_chain.assert_called_once()
