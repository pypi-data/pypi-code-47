from unittest.mock import Mock

import dli
from dli.analytics import AnalyticsHandler


class TestAnalyticsHandler:

    def test_properly_creates_handler(self):
        logger = Mock()
        dli_client = Mock(logger=logger)
        analytics_handler = AnalyticsHandler(dli_client)

        assert analytics_handler._app_name == 'SDK'
        assert analytics_handler._app_version == dli.__version__
        assert analytics_handler._client == dli_client
        assert analytics_handler._logger == logger

    def test_handles_internal_exceptions(self):
        exception_to_be_thrown = ValueError()
        session = Mock(post=Mock(side_effect=exception_to_be_thrown))
        environment = Mock(consumption='someurl')
        dli_client = Mock(session=session, _environment=environment)
        analytics_handler = AnalyticsHandler(dli_client)

        analytics_handler.create_event('user', 'org', properties={})

        session.post.assert_called_once()
        analytics_handler._logger.exception.assert_called_once_with(
            'Error while sending analytics: ', exception_to_be_thrown
        )

    def test_sends_proper_message_on_proper_input(self):
        session = Mock()
        environment = Mock(consumption='someurl')
        dli_client = Mock(session=session, _environment=environment)
        analytics_handler = AnalyticsHandler(dli_client)

        analytics_handler.create_event('user', 'org', properties={})

        session.post.assert_called_once_with(
            '/analytics/', json={
                'data': [{'attributes': {
                    'application_name': 'SDK',
                    'application_version': dli.__version__,
                    'user_id': 'user',
                    'entity': None,
                    'action': None,
                    'organisation_id': 'org',
                    'result': None,
                    'properties': {}}}]
            }
        )

    def test_sends_message_with_filtered_out_properties(self):
        session = Mock()
        environment = Mock(consumption='someurl')
        dli_client = Mock(session=session, _environment=environment)
        analytics_handler = AnalyticsHandler(dli_client)
        properties = {
            'package_id': '1',
            'dataset_id': '2',
            'name': 'some_name',
            'dataset_name': 'd_name',
            'datafile_id': 'datafile_id',
            'dictionary_id': 'dictionary_id',
            'api_key': 'key',
            'unknown': 'property'
        }
        analytics_handler.create_event('user', 'org', properties=properties)

        properties.pop('unknown')
        session.post.assert_called_once_with(
            '/analytics/', json={
                'data': [{'attributes': {
                    'application_name': 'SDK',
                    'application_version': dli.__version__,
                    'user_id': 'user',
                    'entity': None,
                    'action': None,
                    'organisation_id': 'org',
                    'result': None,
                    'properties': properties}}]
            }
        )
