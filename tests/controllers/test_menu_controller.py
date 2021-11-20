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
from manager.controllers.menu_controller import MenuController


class MenuControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(MenuControllerTests, cls).setUpClass()
        cls.response_catcher = HttpResponseCatcher()
        cls.controller = MenuController(cls.config, cls.response_catcher)

    # Get the menu data structure. Returns a forest like structure with the menu the user has access to
    def test_menu_get(self):

        # Perform the API call through the SDK function
        result = self.controller.menu_get()

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


