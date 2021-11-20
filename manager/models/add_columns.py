# -*- coding: utf-8 -*-

"""
manager

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class AddColumns(object):

    """Implementation of the 'AddColumns' model.

    TODO: type model description here.

    Attributes:
        page (int): TODO: type description here.
        page_size (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "page": 'page',
        "page_size": 'page_size'
    }

    def __init__(self,
                 page=None,
                 page_size=None):
        """Constructor for the AddColumns class"""

        # Initialize members of the class
        self.page = page
        self.page_size = page_size

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
        page = dictionary.get('page')
        page_size = dictionary.get('page_size')

        # Return an object of this model
        return cls(page,
                   page_size)
