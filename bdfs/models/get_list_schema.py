# -*- coding: utf-8 -*-

"""
bdfs

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from bdfs.models.filter import Filter


class GetListSchema(object):

    """Implementation of the 'get_list_schema' model.

    TODO: type model description here.

    Attributes:
        columns (list of string): TODO: type description here.
        filters (list of Filter): TODO: type description here.
        keys (list of Key2Enum): TODO: type description here.
        order_column (string): TODO: type description here.
        order_direction (OrderDirectionEnum): TODO: type description here.
        page (int): TODO: type description here.
        page_size (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "columns": 'columns',
        "filters": 'filters',
        "keys": 'keys',
        "order_column": 'order_column',
        "order_direction": 'order_direction',
        "page": 'page',
        "page_size": 'page_size'
    }

    def __init__(self,
                 columns=None,
                 filters=None,
                 keys=None,
                 order_column=None,
                 order_direction=None,
                 page=None,
                 page_size=None):
        """Constructor for the GetListSchema class"""

        # Initialize members of the class
        self.columns = columns
        self.filters = filters
        self.keys = keys
        self.order_column = order_column
        self.order_direction = order_direction
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
        columns = dictionary.get('columns')
        filters = None
        if dictionary.get('filters') is not None:
            filters = [Filter.from_dictionary(x) for x in dictionary.get('filters')]
        keys = dictionary.get('keys')
        order_column = dictionary.get('order_column')
        order_direction = dictionary.get('order_direction')
        page = dictionary.get('page')
        page_size = dictionary.get('page_size')

        # Return an object of this model
        return cls(columns,
                   filters,
                   keys,
                   order_column,
                   order_direction,
                   page,
                   page_size)
