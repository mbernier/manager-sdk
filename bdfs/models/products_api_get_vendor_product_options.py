# -*- coding: utf-8 -*-

"""
bdfs

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ProductsApiGetVendorProductOptions(object):

    """Implementation of the 'ProductsApi.get.VendorProductOptions' model.

    TODO: type model description here.

    Attributes:
        handle_generation (string): TODO: type description here.
        id (int): TODO: type description here.
        options (string): TODO: type description here.
        product_type (string): TODO: type description here.
        sku_generation (string): TODO: type description here.
        variations (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_type": 'product_type',
        "handle_generation": 'handle_generation',
        "id": 'id',
        "options": 'options',
        "sku_generation": 'sku_generation',
        "variations": 'variations'
    }

    def __init__(self,
                 product_type=None,
                 handle_generation=None,
                 id=None,
                 options=None,
                 sku_generation=None,
                 variations=None):
        """Constructor for the ProductsApiGetVendorProductOptions class"""

        # Initialize members of the class
        self.handle_generation = handle_generation
        self.id = id
        self.options = options
        self.product_type = product_type
        self.sku_generation = sku_generation
        self.variations = variations

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
        product_type = dictionary.get('product_type')
        handle_generation = dictionary.get('handle_generation')
        id = dictionary.get('id')
        options = dictionary.get('options')
        sku_generation = dictionary.get('sku_generation')
        variations = dictionary.get('variations')

        # Return an object of this model
        return cls(product_type,
                   handle_generation,
                   id,
                   options,
                   sku_generation,
                   variations)
