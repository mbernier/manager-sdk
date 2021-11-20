# -*- coding: utf-8 -*-

"""
manager

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from manager.api_helper import APIHelper


class OrderNotesApiGetOrder(object):

    """Implementation of the 'OrderNotesApi.get.Order' model.

    TODO: type model description here.

    Attributes:
        changed_on (datetime): TODO: type description here.
        created_on (datetime): TODO: type description here.
        customer_order_total (float): TODO: type description here.
        customer_shipping_price (float): TODO: type description here.
        id (int): TODO: type description here.
        product_costs (float): TODO: type description here.
        profit (float): TODO: type description here.
        shipping_cost (float): TODO: type description here.
        status (StatusEnum): TODO: type description here.
        website_order_id (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "website_order_id": 'website_order_id',
        "changed_on": 'changed_on',
        "created_on": 'created_on',
        "customer_order_total": 'customer_order_total',
        "customer_shipping_price": 'customer_shipping_price',
        "id": 'id',
        "product_costs": 'product_costs',
        "profit": 'profit',
        "shipping_cost": 'shipping_cost',
        "status": 'status'
    }

    def __init__(self,
                 website_order_id=None,
                 changed_on=None,
                 created_on=None,
                 customer_order_total=None,
                 customer_shipping_price=None,
                 id=None,
                 product_costs=None,
                 profit=None,
                 shipping_cost=None,
                 status=None):
        """Constructor for the OrderNotesApiGetOrder class"""

        # Initialize members of the class
        self.changed_on = APIHelper.RFC3339DateTime(changed_on) if changed_on else None
        self.created_on = APIHelper.RFC3339DateTime(created_on) if created_on else None
        self.customer_order_total = customer_order_total
        self.customer_shipping_price = customer_shipping_price
        self.id = id
        self.product_costs = product_costs
        self.profit = profit
        self.shipping_cost = shipping_cost
        self.status = status
        self.website_order_id = website_order_id

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
        website_order_id = dictionary.get('website_order_id')
        changed_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("changed_on")).datetime if dictionary.get("changed_on") else None
        created_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_on")).datetime if dictionary.get("created_on") else None
        customer_order_total = dictionary.get('customer_order_total')
        customer_shipping_price = dictionary.get('customer_shipping_price')
        id = dictionary.get('id')
        product_costs = dictionary.get('product_costs')
        profit = dictionary.get('profit')
        shipping_cost = dictionary.get('shipping_cost')
        status = dictionary.get('status')

        # Return an object of this model
        return cls(website_order_id,
                   changed_on,
                   created_on,
                   customer_order_total,
                   customer_shipping_price,
                   id,
                   product_costs,
                   profit,
                   shipping_cost,
                   status)
