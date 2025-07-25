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


class Transfer(object):
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
        '_from': 'str',
        'to': 'str',
        'amount': 'str',
        'currency_pair': 'str',
        'settle': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        '_from': 'from',
        'to': 'to',
        'amount': 'amount',
        'currency_pair': 'currency_pair',
        'settle': 'settle'
    }

    def __init__(self, currency=None, _from=None, to=None, amount=None, currency_pair=None, settle=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, str, str, str, Configuration) -> None
        """Transfer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self.__from = None
        self._to = None
        self._amount = None
        self._currency_pair = None
        self._settle = None
        self.discriminator = None

        self.currency = currency
        self._from = _from
        self.to = to
        self.amount = amount
        if currency_pair is not None:
            self.currency_pair = currency_pair
        if settle is not None:
            self.settle = settle

    @property
    def currency(self):
        """Gets the currency of this Transfer.  # noqa: E501

        Transfer currency. For futures account, `currency` can be set to `POINT` or settle currency  # noqa: E501

        :return: The currency of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Transfer.

        Transfer currency. For futures account, `currency` can be set to `POINT` or settle currency  # noqa: E501

        :param currency: The currency of this Transfer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def _from(self):
        """Gets the _from of this Transfer.  # noqa: E501

        Account to transfer from.  # noqa: E501

        :return: The _from of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Transfer.

        Account to transfer from.  # noqa: E501

        :param _from: The _from of this Transfer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and _from is None:  # noqa: E501
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501
        allowed_values = ["spot", "margin", "futures", "delivery", "options"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and _from not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `_from` ({0}), must be one of {1}"  # noqa: E501
                .format(_from, allowed_values)
            )

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this Transfer.  # noqa: E501

        Account to transfer to.  # noqa: E501

        :return: The to of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Transfer.

        Account to transfer to.  # noqa: E501

        :param to: The to of this Transfer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and to is None:  # noqa: E501
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501
        allowed_values = ["spot", "margin", "futures", "delivery", "options"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and to not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `to` ({0}), must be one of {1}"  # noqa: E501
                .format(to, allowed_values)
            )

        self._to = to

    @property
    def amount(self):
        """Gets the amount of this Transfer.  # noqa: E501

        Transfer amount.  # noqa: E501

        :return: The amount of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Transfer.

        Transfer amount.  # noqa: E501

        :param amount: The amount of this Transfer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency_pair(self):
        """Gets the currency_pair of this Transfer.  # noqa: E501

        Margin currency pair. Required if transfer from or to margin account.  # noqa: E501

        :return: The currency_pair of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this Transfer.

        Margin currency pair. Required if transfer from or to margin account.  # noqa: E501

        :param currency_pair: The currency_pair of this Transfer.  # noqa: E501
        :type: str
        """

        self._currency_pair = currency_pair

    @property
    def settle(self):
        """Gets the settle of this Transfer.  # noqa: E501

        Futures settle currency. Required if transferring from or to futures account  # noqa: E501

        :return: The settle of this Transfer.  # noqa: E501
        :rtype: str
        """
        return self._settle

    @settle.setter
    def settle(self, settle):
        """Sets the settle of this Transfer.

        Futures settle currency. Required if transferring from or to futures account  # noqa: E501

        :param settle: The settle of this Transfer.  # noqa: E501
        :type: str
        """

        self._settle = settle

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
        if not isinstance(other, Transfer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Transfer):
            return True

        return self.to_dict() != other.to_dict()
