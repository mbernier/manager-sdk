# -*- coding: utf-8 -*-

"""
bdfs

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from bdfs.models.column_name import ColumnName


class Filters(object):

    """Implementation of the 'Filters' model.

    TODO: type model description here.

    Attributes:
        column_name (list of ColumnName): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "column_name": 'column_name'
    }

    def __init__(self,
                 column_name=None):
        """Constructor for the Filters class"""

        # Initialize members of the class
        self.column_name = column_name

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
        column_name = None
        if dictionary.get('column_name') is not None:
            column_name = [ColumnName.from_dictionary(x) for x in dictionary.get('column_name')]

        # Return an object of this model
        return cls(column_name)
