# -*- coding: utf-8 -*-

"""
manager

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from manager.models.description_columns import DescriptionColumns
from manager.models.label_columns import LabelColumns
from manager.models.order_api_get import OrderApiGet


class OrderResponse3(object):

    """Implementation of the 'Order Response3' model.

    TODO: type model description here.

    Attributes:
        description_columns (DescriptionColumns): TODO: type description
            here.
        id (string): The item id
        label_columns (LabelColumns): TODO: type description here.
        result (OrderApiGet): TODO: type description here.
        show_columns (list of string): A list of columns
        show_title (string): A title to render. Will be translated by babel

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description_columns": 'description_columns',
        "id": 'id',
        "label_columns": 'label_columns',
        "result": 'result',
        "show_columns": 'show_columns',
        "show_title": 'show_title'
    }

    def __init__(self,
                 description_columns=None,
                 id=None,
                 label_columns=None,
                 result=None,
                 show_columns=None,
                 show_title=None):
        """Constructor for the OrderResponse3 class"""

        # Initialize members of the class
        self.description_columns = description_columns
        self.id = id
        self.label_columns = label_columns
        self.result = result
        self.show_columns = show_columns
        self.show_title = show_title

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
        description_columns = DescriptionColumns.from_dictionary(dictionary.get('description_columns')) if dictionary.get('description_columns') else None
        id = dictionary.get('id')
        label_columns = LabelColumns.from_dictionary(dictionary.get('label_columns')) if dictionary.get('label_columns') else None
        result = OrderApiGet.from_dictionary(dictionary.get('result')) if dictionary.get('result') else None
        show_columns = dictionary.get('show_columns')
        show_title = dictionary.get('show_title')

        # Return an object of this model
        return cls(description_columns,
                   id,
                   label_columns,
                   result,
                   show_columns,
                   show_title)
