# -*- coding: utf-8 -*-

"""
bdfs

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from bdfs.models.vendor_contact_api_put import VendorContactApiPut


class VendorContactResponse4(object):

    """Implementation of the 'Vendor Contact Response4' model.

    TODO: type model description here.

    Attributes:
        result (VendorContactApiPut): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "result": 'result'
    }

    def __init__(self,
                 result=None):
        """Constructor for the VendorContactResponse4 class"""

        # Initialize members of the class
        self.result = result

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
        result = VendorContactApiPut.from_dictionary(dictionary.get('result')) if dictionary.get('result') else None

        # Return an object of this model
        return cls(result)
