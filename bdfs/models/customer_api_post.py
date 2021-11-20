# -*- coding: utf-8 -*-

"""
bdfs

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class CustomerApiPost(object):

    """Implementation of the 'CustomerApi.post' model.

    TODO: type model description here.

    Attributes:
        billing_address (string): TODO: type description here.
        email (string): TODO: type description here.
        name (string): TODO: type description here.
        phone (string): TODO: type description here.
        shipping_address (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "billing_address": 'billing_address',
        "email": 'email',
        "name": 'name',
        "phone": 'phone',
        "shipping_address": 'shipping_address'
    }

    def __init__(self,
                 billing_address=None,
                 email=None,
                 name=None,
                 phone=None,
                 shipping_address=None):
        """Constructor for the CustomerApiPost class"""

        # Initialize members of the class
        self.billing_address = billing_address
        self.email = email
        self.name = name
        self.phone = phone
        self.shipping_address = shipping_address

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
        billing_address = dictionary.get('billing_address')
        email = dictionary.get('email')
        name = dictionary.get('name')
        phone = dictionary.get('phone')
        shipping_address = dictionary.get('shipping_address')

        # Return an object of this model
        return cls(billing_address,
                   email,
                   name,
                   phone,
                   shipping_address)
