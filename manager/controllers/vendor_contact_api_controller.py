# -*- coding: utf-8 -*-

"""
manager

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from manager.api_helper import APIHelper
from manager.configuration import Server
from manager.controllers.base_controller import BaseController
from manager.http.auth.o_auth_2 import OAuth2
from manager.models.vendor_contact_response import VendorContactResponse
from manager.models.vendor_contact_response_1 import VendorContactResponse1
from manager.models.vendor_contact_info_response import VendorContactInfoResponse
from manager.models.vendor_contact_response_2 import VendorContactResponse2
from manager.models.vendor_contact_response_3 import VendorContactResponse3
from manager.models.vendor_contact_response_4 import VendorContactResponse4
from manager.exceptions.m_400_exception import M400Exception


class VendorContactApiController(BaseController):

    """A Controller to access Endpoints in the manager API."""

    def __init__(self, config, call_back=None):
        super(VendorContactApiController, self).__init__(config, call_back)

    def vendor_contact_get(self):
        """Does a GET request to /vendor_contact/.

        Get a list of models

        Returns:
            VendorContactResponse: Response from the API. Items from Model

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/vendor_contact/'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise M400Exception('Bad request', _response)
        elif _response.status_code == 401:
            raise M400Exception('Unauthorized', _response)
        elif _response.status_code == 422:
            raise M400Exception('Could not process entity', _response)
        elif _response.status_code == 500:
            raise M400Exception('Fatal error', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, VendorContactResponse.from_dictionary)

        return decoded

    def vendor_contact_post(self,
                            body):
        """Does a POST request to /vendor_contact/.

        TODO: type endpoint description here.

        Args:
            body (VendorContactApiPost): Model schema

        Returns:
            VendorContactResponse1: Response from the API. Item inserted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(body=body)

        # Prepare query URL
        _url_path = '/vendor_contact/'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.post(_query_url, headers=_headers, parameters=APIHelper.json_serialize(body))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise M400Exception('Bad request', _response)
        elif _response.status_code == 401:
            raise M400Exception('Unauthorized', _response)
        elif _response.status_code == 422:
            raise M400Exception('Could not process entity', _response)
        elif _response.status_code == 500:
            raise M400Exception('Fatal error', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, VendorContactResponse1.from_dictionary)

        return decoded

    def vendor_contact_info_get(self):
        """Does a GET request to /vendor_contact/_info.

        Get metadata information about this API resource

        Returns:
            VendorContactInfoResponse: Response from the API. Item from Model

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _url_path = '/vendor_contact/_info'
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise M400Exception('Bad request', _response)
        elif _response.status_code == 401:
            raise M400Exception('Unauthorized', _response)
        elif _response.status_code == 422:
            raise M400Exception('Could not process entity', _response)
        elif _response.status_code == 500:
            raise M400Exception('Fatal error', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, VendorContactInfoResponse.from_dictionary)

        return decoded

    def vendor_contact_by_pk_delete(self,
                                    pk):
        """Does a DELETE request to /vendor_contact/{pk}.

        TODO: type endpoint description here.

        Args:
            pk (int): TODO: type description here.

        Returns:
            VendorContactResponse2: Response from the API. Item deleted

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(pk=pk)

        # Prepare query URL
        _url_path = '/vendor_contact/{pk}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'pk': {'value': pk, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.delete(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 404:
            raise M400Exception('Not found', _response)
        elif _response.status_code == 422:
            raise M400Exception('Could not process entity', _response)
        elif _response.status_code == 500:
            raise M400Exception('Fatal error', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, VendorContactResponse2.from_dictionary)

        return decoded

    def vendor_contact_by_pk_get(self,
                                 pk):
        """Does a GET request to /vendor_contact/{pk}.

        Get an item model

        Args:
            pk (int): TODO: type description here.

        Returns:
            VendorContactResponse3: Response from the API. Item from Model

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(pk=pk)

        # Prepare query URL
        _url_path = '/vendor_contact/{pk}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'pk': {'value': pk, 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.get(_query_url, headers=_headers)
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise M400Exception('Bad request', _response)
        elif _response.status_code == 401:
            raise M400Exception('Unauthorized', _response)
        elif _response.status_code == 404:
            raise M400Exception('Not found', _response)
        elif _response.status_code == 422:
            raise M400Exception('Could not process entity', _response)
        elif _response.status_code == 500:
            raise M400Exception('Fatal error', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, VendorContactResponse3.from_dictionary)

        return decoded

    def vendor_contact_by_pk_put(self,
                                 options=dict()):
        """Does a PUT request to /vendor_contact/{pk}.

        TODO: type endpoint description here.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    pk -- int -- TODO: type description here.
                    body -- VendorContactApiPut -- Model schema

        Returns:
            VendorContactResponse4: Response from the API. Item changed

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Validate required parameters
        self.validate_parameters(pk=options.get("pk"),
                                 body=options.get("body"))

        # Prepare query URL
        _url_path = '/vendor_contact/{pk}'
        _url_path = APIHelper.append_url_with_template_parameters(_url_path, {
            'pk': {'value': options.get('pk', None), 'encode': True}
        })
        _query_builder = self.config.get_base_uri()
        _query_builder += _url_path
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare headers
        _headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # Prepare and execute request
        _request = self.config.http_client.put(_query_url, headers=_headers, parameters=APIHelper.json_serialize(options.get('body')))
        OAuth2.apply(self.config, _request)
        _response = self.execute_request(_request)

        # Endpoint and global error handling using HTTP status codes.
        if _response.status_code == 400:
            raise M400Exception('Bad request', _response)
        elif _response.status_code == 401:
            raise M400Exception('Unauthorized', _response)
        elif _response.status_code == 404:
            raise M400Exception('Not found', _response)
        elif _response.status_code == 422:
            raise M400Exception('Could not process entity', _response)
        elif _response.status_code == 500:
            raise M400Exception('Fatal error', _response)
        self.validate_response(_response)

        decoded = APIHelper.json_deserialize(_response.text, VendorContactResponse4.from_dictionary)

        return decoded
