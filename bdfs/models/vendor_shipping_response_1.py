# -*- coding: utf-8 -*-

"""
bdfs

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from bdfs.models.vendor_shipping_api_post import VendorShippingApiPost


class VendorShippingResponse1(object):

    """Implementation of the 'Vendor Shipping Response1' model.

    TODO: type model description here.

    Attributes:
        id (string): TODO: type description here.
        result (VendorShippingApiPost): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "result": 'result'
    }

    def __init__(self,
                 id=None,
                 result=None):
        """Constructor for the VendorShippingResponse1 class"""

        # Initialize members of the class
        self.id = id
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
        id = dictionary.get('id')
        result = VendorShippingApiPost.from_dictionary(dictionary.get('result')) if dictionary.get('result') else None

        # Return an object of this model
        return cls(id,
                   result)
