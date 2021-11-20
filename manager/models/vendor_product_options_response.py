# -*- coding: utf-8 -*-

"""
manager

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from manager.models.description_columns import DescriptionColumns
from manager.models.label_columns import LabelColumns
from manager.models.vendor_product_options_api_get_list import VendorProductOptionsApiGetList


class VendorProductOptionsResponse(object):

    """Implementation of the 'Vendor Product Options Response' model.

    TODO: type model description here.

    Attributes:
        count (float): The total record count on the backend
        description_columns (DescriptionColumns): TODO: type description
            here.
        ids (list of string): A list of item ids, useful when you don't know
            the column id
        label_columns (LabelColumns): TODO: type description here.
        list_columns (list of string): A list of columns
        list_title (string): A title to render. Will be translated by babel
        order_columns (list of string): A list of allowed columns to sort
        result (list of VendorProductOptionsApiGetList): The result from the
            get list query

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count',
        "description_columns": 'description_columns',
        "ids": 'ids',
        "label_columns": 'label_columns',
        "list_columns": 'list_columns',
        "list_title": 'list_title',
        "order_columns": 'order_columns',
        "result": 'result'
    }

    def __init__(self,
                 count=None,
                 description_columns=None,
                 ids=None,
                 label_columns=None,
                 list_columns=None,
                 list_title=None,
                 order_columns=None,
                 result=None):
        """Constructor for the VendorProductOptionsResponse class"""

        # Initialize members of the class
        self.count = count
        self.description_columns = description_columns
        self.ids = ids
        self.label_columns = label_columns
        self.list_columns = list_columns
        self.list_title = list_title
        self.order_columns = order_columns
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
        count = dictionary.get('count')
        description_columns = DescriptionColumns.from_dictionary(dictionary.get('description_columns')) if dictionary.get('description_columns') else None
        ids = dictionary.get('ids')
        label_columns = LabelColumns.from_dictionary(dictionary.get('label_columns')) if dictionary.get('label_columns') else None
        list_columns = dictionary.get('list_columns')
        list_title = dictionary.get('list_title')
        order_columns = dictionary.get('order_columns')
        result = None
        if dictionary.get('result') is not None:
            result = [VendorProductOptionsApiGetList.from_dictionary(x) for x in dictionary.get('result')]

        # Return an object of this model
        return cls(count,
                   description_columns,
                   ids,
                   label_columns,
                   list_columns,
                   list_title,
                   order_columns,
                   result)
