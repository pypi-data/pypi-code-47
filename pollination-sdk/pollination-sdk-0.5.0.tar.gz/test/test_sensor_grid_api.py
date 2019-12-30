# coding: utf-8

"""
    pollination.cloud

    Pollination Cloud API  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pollination_sdk
from pollination_sdk.api.sensor_grid_api import SensorGridApi  # noqa: E501
from pollination_sdk.rest import ApiException


class TestSensorGridApi(unittest.TestCase):
    """SensorGridApi unit test stubs"""

    def setUp(self):
        self.api = pollination_sdk.api.sensor_grid_api.SensorGridApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create(self):
        """Test case for create

        Create a Sensor Grid  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete a Sensor Grid  # noqa: E501
        """
        pass

    def test_get(self):
        """Test case for get

        Get a Sensor Grid  # noqa: E501
        """
        pass

    def test_get_sensors(self):
        """Test case for get_sensors

        Get Sensors  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        Get Sensor Grids  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
