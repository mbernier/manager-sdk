# -*- coding: utf-8 -*-

"""
bdfs

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from bdfs.api_helper import APIHelper
from bdfs.controllers.customer_api_controller import CustomerApiController


class CustomerApiControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(CustomerApiControllerTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = CustomerApiController(cls.config, cls.response_catcher)

    # Get a list of models
    def test_customer_get(self):

        # Perform the API call through the SDK function
        result = self.controller.customer_get()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


    # Get metadata information about this API resource
    def test_customer_info_get(self):

        # Perform the API call through the SDK function
        result = self.controller.customer_info_get()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


