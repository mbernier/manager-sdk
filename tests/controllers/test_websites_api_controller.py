# -*- coding: utf-8 -*-

"""
manager

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

import json
import dateutil.parser

from tests.controllers.controller_test_base import ControllerTestBase
from tests.test_helper import TestHelper
from tests.http_response_catcher import HttpResponseCatcher
from manager.api_helper import APIHelper
from manager.controllers.websites_api_controller import WebsitesApiController


class WebsitesApiControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(WebsitesApiControllerTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = WebsitesApiController(cls.config, cls.response_catcher)

    # Get a list of models
    def test_websites_get(self):

        # Perform the API call through the SDK function
        result = self.controller.websites_get()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


    # Get metadata information about this API resource
    def test_websites_info_get(self):

        # Perform the API call through the SDK function
        result = self.controller.websites_info_get()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


