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
from manager.controllers.security_controller import SecurityController


class SecurityControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SecurityControllerTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = SecurityController(cls.config, cls.response_catcher)

    # Use the refresh token to get a new JWT access token
    def test_security_refresh_post(self):

        # Perform the API call through the SDK function
        result = self.controller.security_refresh_post()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


