# coding: utf-8

"""
    Gate API

    Welcome to Gate API  APIv4 provides operations related to spot, margin, and contract trading, including public interfaces for querying market data and authenticated private interfaces for implementing API-based automated trading.  # noqa: E501

    Contact: support@mail.gate.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from gate_api.configuration import Configuration


class MarginAccountCurrency(object):
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
    openapi_types = {
        'currency': 'str',
        'available': 'str',
        'locked': 'str',
        'borrowed': 'str',
        'interest': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        'available': 'available',
        'locked': 'locked',
        'borrowed': 'borrowed',
        'interest': 'interest'
    }

    def __init__(self, currency=None, available=None, locked=None, borrowed=None, interest=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, str, str, Configuration) -> None
        """MarginAccountCurrency - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self._available = None
        self._locked = None
        self._borrowed = None
        self._interest = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if available is not None:
            self.available = available
        if locked is not None:
            self.locked = locked
        if borrowed is not None:
            self.borrowed = borrowed
        if interest is not None:
            self.interest = interest

    @property
    def currency(self):
        """Gets the currency of this MarginAccountCurrency.  # noqa: E501

        Currency name.  # noqa: E501

        :return: The currency of this MarginAccountCurrency.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this MarginAccountCurrency.

        Currency name.  # noqa: E501

        :param currency: The currency of this MarginAccountCurrency.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def available(self):
        """Gets the available of this MarginAccountCurrency.  # noqa: E501

        Amount suitable for margin trading.  # noqa: E501

        :return: The available of this MarginAccountCurrency.  # noqa: E501
        :rtype: str
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this MarginAccountCurrency.

        Amount suitable for margin trading.  # noqa: E501

        :param available: The available of this MarginAccountCurrency.  # noqa: E501
        :type: str
        """

        self._available = available

    @property
    def locked(self):
        """Gets the locked of this MarginAccountCurrency.  # noqa: E501

        Locked amount, used in margin trading.  # noqa: E501

        :return: The locked of this MarginAccountCurrency.  # noqa: E501
        :rtype: str
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this MarginAccountCurrency.

        Locked amount, used in margin trading.  # noqa: E501

        :param locked: The locked of this MarginAccountCurrency.  # noqa: E501
        :type: str
        """

        self._locked = locked

    @property
    def borrowed(self):
        """Gets the borrowed of this MarginAccountCurrency.  # noqa: E501

        Borrowed amount.  # noqa: E501

        :return: The borrowed of this MarginAccountCurrency.  # noqa: E501
        :rtype: str
        """
        return self._borrowed

    @borrowed.setter
    def borrowed(self, borrowed):
        """Sets the borrowed of this MarginAccountCurrency.

        Borrowed amount.  # noqa: E501

        :param borrowed: The borrowed of this MarginAccountCurrency.  # noqa: E501
        :type: str
        """

        self._borrowed = borrowed

    @property
    def interest(self):
        """Gets the interest of this MarginAccountCurrency.  # noqa: E501

        Unpaid interests.  # noqa: E501

        :return: The interest of this MarginAccountCurrency.  # noqa: E501
        :rtype: str
        """
        return self._interest

    @interest.setter
    def interest(self, interest):
        """Sets the interest of this MarginAccountCurrency.

        Unpaid interests.  # noqa: E501

        :param interest: The interest of this MarginAccountCurrency.  # noqa: E501
        :type: str
        """

        self._interest = interest

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
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
        if not isinstance(other, MarginAccountCurrency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarginAccountCurrency):
            return True

        return self.to_dict() != other.to_dict()
