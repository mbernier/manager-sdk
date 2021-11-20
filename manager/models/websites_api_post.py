# -*- coding: utf-8 -*-

"""
manager

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class WebsitesApiPost(object):

    """Implementation of the 'WebsitesApi.post' model.

    TODO: type model description here.

    Attributes:
        api_key (string): TODO: type description here.
        api_secret (string): TODO: type description here.
        name (string): TODO: type description here.
        private_app_password (string): TODO: type description here.
        products (list of object): TODO: type description here.
        shopify_prefix (string): TODO: type description here.
        url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "shopify_prefix": 'shopify_prefix',
        "url": 'url',
        "api_key": 'api_key',
        "api_secret": 'api_secret',
        "private_app_password": 'private_app_password',
        "products": 'products'
    }

    def __init__(self,
                 name=None,
                 shopify_prefix=None,
                 url=None,
                 api_key=None,
                 api_secret=None,
                 private_app_password=None,
                 products=None):
        """Constructor for the WebsitesApiPost class"""

        # Initialize members of the class
        self.api_key = api_key
        self.api_secret = api_secret
        self.name = name
        self.private_app_password = private_app_password
        self.products = products
        self.shopify_prefix = shopify_prefix
        self.url = url

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        name = dictionary.get('name')
        shopify_prefix = dictionary.get('shopify_prefix')
        url = dictionary.get('url')
        api_key = dictionary.get('api_key')
        api_secret = dictionary.get('api_secret')
        private_app_password = dictionary.get('private_app_password')
        products = dictionary.get('products')

        # Return an object of this model
        return cls(name,
                   shopify_prefix,
                   url,
                   api_key,
                   api_secret,
                   private_app_password,
                   products)
