# -*- coding: utf-8 -*-

"""
bdfs

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ProductNotesApiGetProducts(object):

    """Implementation of the 'ProductNotesApi.get.Products' model.

    TODO: type model description here.

    Attributes:
        customer_photos (string): TODO: type description here.
        handle (string): TODO: type description here.
        id (int): TODO: type description here.
        name (string): TODO: type description here.
        options (string): TODO: type description here.
        product_type (string): TODO: type description here.
        seo_description (string): TODO: type description here.
        seo_name (string): TODO: type description here.
        sku (string): TODO: type description here.
        tags (string): TODO: type description here.
        variations (string): TODO: type description here.
        vendor_photos (string): TODO: type description here.
        vendor_sku (string): TODO: type description here.
        vendor_url (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "handle": 'handle',
        "name": 'name',
        "sku": 'sku',
        "vendor_sku": 'vendor_sku',
        "vendor_url": 'vendor_url',
        "customer_photos": 'customer_photos',
        "id": 'id',
        "options": 'options',
        "product_type": 'product_type',
        "seo_description": 'seo_description',
        "seo_name": 'seo_name',
        "tags": 'tags',
        "variations": 'variations',
        "vendor_photos": 'vendor_photos'
    }

    def __init__(self,
                 handle=None,
                 name=None,
                 sku=None,
                 vendor_sku=None,
                 vendor_url=None,
                 customer_photos=None,
                 id=None,
                 options=None,
                 product_type=None,
                 seo_description=None,
                 seo_name=None,
                 tags=None,
                 variations=None,
                 vendor_photos=None):
        """Constructor for the ProductNotesApiGetProducts class"""

        # Initialize members of the class
        self.customer_photos = customer_photos
        self.handle = handle
        self.id = id
        self.name = name
        self.options = options
        self.product_type = product_type
        self.seo_description = seo_description
        self.seo_name = seo_name
        self.sku = sku
        self.tags = tags
        self.variations = variations
        self.vendor_photos = vendor_photos
        self.vendor_sku = vendor_sku
        self.vendor_url = vendor_url

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
        handle = dictionary.get('handle')
        name = dictionary.get('name')
        sku = dictionary.get('sku')
        vendor_sku = dictionary.get('vendor_sku')
        vendor_url = dictionary.get('vendor_url')
        customer_photos = dictionary.get('customer_photos')
        id = dictionary.get('id')
        options = dictionary.get('options')
        product_type = dictionary.get('product_type')
        seo_description = dictionary.get('seo_description')
        seo_name = dictionary.get('seo_name')
        tags = dictionary.get('tags')
        variations = dictionary.get('variations')
        vendor_photos = dictionary.get('vendor_photos')

        # Return an object of this model
        return cls(handle,
                   name,
                   sku,
                   vendor_sku,
                   vendor_url,
                   customer_photos,
                   id,
                   options,
                   product_type,
                   seo_description,
                   seo_name,
                   tags,
                   variations,
                   vendor_photos)
