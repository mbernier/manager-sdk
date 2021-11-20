# -*- coding: utf-8 -*-

"""
bdfs

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class VendorContactApiPut(object):

    """Implementation of the 'VendorContactApi.put' model.

    TODO: type model description here.

    Attributes:
        contact_for_new_orders (bool): TODO: type description here.
        email (string): TODO: type description here.
        name (string): TODO: type description here.
        phone (string): TODO: type description here.
        vendor (object): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email": 'email',
        "name": 'name',
        "phone": 'phone',
        "contact_for_new_orders": 'contact_for_new_orders',
        "vendor": 'vendor'
    }

    def __init__(self,
                 email=None,
                 name=None,
                 phone=None,
                 contact_for_new_orders=None,
                 vendor=None):
        """Constructor for the VendorContactApiPut class"""

        # Initialize members of the class
        self.contact_for_new_orders = contact_for_new_orders
        self.email = email
        self.name = name
        self.phone = phone
        self.vendor = vendor

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
        email = dictionary.get('email')
        name = dictionary.get('name')
        phone = dictionary.get('phone')
        contact_for_new_orders = dictionary.get('contact_for_new_orders')
        vendor = dictionary.get('vendor')

        # Return an object of this model
        return cls(email,
                   name,
                   phone,
                   contact_for_new_orders,
                   vendor)
