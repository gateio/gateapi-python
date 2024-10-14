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


class MockSpotBalance(object):
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
    openapi_types = {'currency': 'str', 'equity': 'str'}

    attribute_map = {'currency': 'currency', 'equity': 'equity'}

    def __init__(self, currency=None, equity=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, Configuration) -> None
        """MockSpotBalance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self._equity = None
        self.discriminator = None

        self.currency = currency
        self.equity = equity

    @property
    def currency(self):
        """Gets the currency of this MockSpotBalance.  # noqa: E501

        Currency name  # noqa: E501

        :return: The currency of this MockSpotBalance.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this MockSpotBalance.

        Currency name  # noqa: E501

        :param currency: The currency of this MockSpotBalance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def equity(self):
        """Gets the equity of this MockSpotBalance.  # noqa: E501

        Currency equity, where equity = balance - borrowed, represents the net delta exposure  of your spot positions, which can be negative. Currently only supports three currencies: BTC, ETH.  # noqa: E501

        :return: The equity of this MockSpotBalance.  # noqa: E501
        :rtype: str
        """
        return self._equity

    @equity.setter
    def equity(self, equity):
        """Sets the equity of this MockSpotBalance.

        Currency equity, where equity = balance - borrowed, represents the net delta exposure  of your spot positions, which can be negative. Currently only supports three currencies: BTC, ETH.  # noqa: E501

        :param equity: The equity of this MockSpotBalance.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and equity is None:  # noqa: E501
            raise ValueError("Invalid value for `equity`, must not be `None`")  # noqa: E501

        self._equity = equity

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
        if not isinstance(other, MockSpotBalance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MockSpotBalance):
            return True

        return self.to_dict() != other.to_dict()