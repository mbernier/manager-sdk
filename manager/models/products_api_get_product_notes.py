# -*- coding: utf-8 -*-

"""
manager

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from manager.api_helper import APIHelper


class ProductsApiGetProductNotes(object):

    """Implementation of the 'ProductsApi.get.ProductNotes' model.

    TODO: type model description here.

    Attributes:
        action_type (string): TODO: type description here.
        changed_on (datetime): TODO: type description here.
        created_on (datetime): TODO: type description here.
        id (int): TODO: type description here.
        note (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "note": 'note',
        "action_type": 'action_type',
        "changed_on": 'changed_on',
        "created_on": 'created_on',
        "id": 'id'
    }

    def __init__(self,
                 note=None,
                 action_type=None,
                 changed_on=None,
                 created_on=None,
                 id=None):
        """Constructor for the ProductsApiGetProductNotes class"""

        # Initialize members of the class
        self.action_type = action_type
        self.changed_on = APIHelper.RFC3339DateTime(changed_on) if changed_on else None
        self.created_on = APIHelper.RFC3339DateTime(created_on) if created_on else None
        self.id = id
        self.note = note

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
        note = dictionary.get('note')
        action_type = dictionary.get('action_type')
        changed_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("changed_on")).datetime if dictionary.get("changed_on") else None
        created_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_on")).datetime if dictionary.get("created_on") else None
        id = dictionary.get('id')

        # Return an object of this model
        return cls(note,
                   action_type,
                   changed_on,
                   created_on,
                   id)
