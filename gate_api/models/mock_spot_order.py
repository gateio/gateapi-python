# coding: utf-8

"""
    Gate API v4

    Welcome to Gate.io API  APIv4 provides spot, margin and futures trading operations. There are public APIs to retrieve the real-time market statistics, and private APIs which needs authentication to trade on user's behalf.  # noqa: E501

    Contact: support@mail.gate.io
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class MockSpotOrder(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {'currency_pairs': 'str', 'order_price': 'str', 'count': 'str', 'left': 'str', 'type': 'str'}

    attribute_map = {
        'currency_pairs': 'currency_pairs',
        'order_price': 'order_price',
        'count': 'count',
        'left': 'left',
        'type': 'type',
    }

    def __init__(
        self, currency_pairs=None, order_price=None, count=None, left=None, type=None, local_vars_configuration=None
    ):  # noqa: E501
        # type: (str, str, str, str, str, Configuration) -> None
        """MockSpotOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency_pairs = None
        self._order_price = None
        self._count = None
        self._left = None
        self._type = None
        self.discriminator = None

        self.currency_pairs = currency_pairs
        self.order_price = order_price
        if count is not None:
            self.count = count
        self.left = left
        self.type = type

    @property
    def currency_pairs(self):
        """Gets the currency_pairs of this MockSpotOrder.  # noqa: E501

        Currency pair  # noqa: E501

        :return: The currency_pairs of this MockSpotOrder.  # noqa: E501
        :rtype: str
        """
        return self._currency_pairs

    @currency_pairs.setter
    def currency_pairs(self, currency_pairs):
        """Sets the currency_pairs of this MockSpotOrder.

        Currency pair  # noqa: E501

        :param currency_pairs: The currency_pairs of this MockSpotOrder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency_pairs is None:  # noqa: E501
            raise ValueError("Invalid value for `currency_pairs`, must not be `None`")  # noqa: E501

        self._currency_pairs = currency_pairs

    @property
    def order_price(self):
        """Gets the order_price of this MockSpotOrder.  # noqa: E501

        Price  # noqa: E501

        :return: The order_price of this MockSpotOrder.  # noqa: E501
        :rtype: str
        """
        return self._order_price

    @order_price.setter
    def order_price(self, order_price):
        """Sets the order_price of this MockSpotOrder.

        Price  # noqa: E501

        :param order_price: The order_price of this MockSpotOrder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and order_price is None:  # noqa: E501
            raise ValueError("Invalid value for `order_price`, must not be `None`")  # noqa: E501

        self._order_price = order_price

    @property
    def count(self):
        """Gets the count of this MockSpotOrder.  # noqa: E501

        Initial order quantity for spot trading pairs, not involved in actual calculation.  Currently only supports three currencies: BTC, ETH.  # noqa: E501

        :return: The count of this MockSpotOrder.  # noqa: E501
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this MockSpotOrder.

        Initial order quantity for spot trading pairs, not involved in actual calculation.  Currently only supports three currencies: BTC, ETH.  # noqa: E501

        :param count: The count of this MockSpotOrder.  # noqa: E501
        :type: str
        """

        self._count = count

    @property
    def left(self):
        """Gets the left of this MockSpotOrder.  # noqa: E501

        Unfilled quantity, involved in actual calculation.  # noqa: E501

        :return: The left of this MockSpotOrder.  # noqa: E501
        :rtype: str
        """
        return self._left

    @left.setter
    def left(self, left):
        """Sets the left of this MockSpotOrder.

        Unfilled quantity, involved in actual calculation.  # noqa: E501

        :param left: The left of this MockSpotOrder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and left is None:  # noqa: E501
            raise ValueError("Invalid value for `left`, must not be `None`")  # noqa: E501

        self._left = left

    @property
    def type(self):
        """Gets the type of this MockSpotOrder.  # noqa: E501

        Order type, sell - sell order, buy - buy order.  # noqa: E501

        :return: The type of this MockSpotOrder.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MockSpotOrder.

        Order type, sell - sell order, buy - buy order.  # noqa: E501

        :param type: The type of this MockSpotOrder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict()) if hasattr(item[1], "to_dict") else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MockSpotOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MockSpotOrder):
            return True

        return self.to_dict() != other.to_dict()
