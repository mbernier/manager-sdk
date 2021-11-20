# -*- coding: utf-8 -*-

"""
manager

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class VendorShippingResponse2(object):

    """Implementation of the 'Vendor Shipping Response2' model.

    TODO: type model description here.

    Attributes:
        message (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message": 'message'
    }

    def __init__(self,
                 message=None):
        """Constructor for the VendorShippingResponse2 class"""

        # Initialize members of the class
        self.message = message

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
        message = dictionary.get('message')

        # Return an object of this model
        return cls(message)
