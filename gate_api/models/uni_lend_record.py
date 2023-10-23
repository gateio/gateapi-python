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


class UniLendRecord(object):
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
        'amount': 'str',
        'last_wallet_amount': 'str',
        'last_lent_amount': 'str',
        'last_frozen_amount': 'str',
        'type': 'str',
        'create_time': 'int',
    }

    attribute_map = {
        'currency': 'currency',
        'amount': 'amount',
        'last_wallet_amount': 'last_wallet_amount',
        'last_lent_amount': 'last_lent_amount',
        'last_frozen_amount': 'last_frozen_amount',
        'type': 'type',
        'create_time': 'create_time',
    }

    def __init__(
        self,
        currency=None,
        amount=None,
        last_wallet_amount=None,
        last_lent_amount=None,
        last_frozen_amount=None,
        type=None,
        create_time=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, str, str, int, Configuration) -> None
        """UniLendRecord - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self._amount = None
        self._last_wallet_amount = None
        self._last_lent_amount = None
        self._last_frozen_amount = None
        self._type = None
        self._create_time = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if amount is not None:
            self.amount = amount
        if last_wallet_amount is not None:
            self.last_wallet_amount = last_wallet_amount
        if last_lent_amount is not None:
            self.last_lent_amount = last_lent_amount
        if last_frozen_amount is not None:
            self.last_frozen_amount = last_frozen_amount
        if type is not None:
            self.type = type
        if create_time is not None:
            self.create_time = create_time

    @property
    def currency(self):
        """Gets the currency of this UniLendRecord.  # noqa: E501

        Currency name  # noqa: E501

        :return: The currency of this UniLendRecord.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this UniLendRecord.

        Currency name  # noqa: E501

        :param currency: The currency of this UniLendRecord.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this UniLendRecord.  # noqa: E501

        current amount  # noqa: E501

        :return: The amount of this UniLendRecord.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UniLendRecord.

        current amount  # noqa: E501

        :param amount: The amount of this UniLendRecord.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def last_wallet_amount(self):
        """Gets the last_wallet_amount of this UniLendRecord.  # noqa: E501

        Last wallet amount  # noqa: E501

        :return: The last_wallet_amount of this UniLendRecord.  # noqa: E501
        :rtype: str
        """
        return self._last_wallet_amount

    @last_wallet_amount.setter
    def last_wallet_amount(self, last_wallet_amount):
        """Sets the last_wallet_amount of this UniLendRecord.

        Last wallet amount  # noqa: E501

        :param last_wallet_amount: The last_wallet_amount of this UniLendRecord.  # noqa: E501
        :type: str
        """

        self._last_wallet_amount = last_wallet_amount

    @property
    def last_lent_amount(self):
        """Gets the last_lent_amount of this UniLendRecord.  # noqa: E501

        Last lent amount  # noqa: E501

        :return: The last_lent_amount of this UniLendRecord.  # noqa: E501
        :rtype: str
        """
        return self._last_lent_amount

    @last_lent_amount.setter
    def last_lent_amount(self, last_lent_amount):
        """Sets the last_lent_amount of this UniLendRecord.

        Last lent amount  # noqa: E501

        :param last_lent_amount: The last_lent_amount of this UniLendRecord.  # noqa: E501
        :type: str
        """

        self._last_lent_amount = last_lent_amount

    @property
    def last_frozen_amount(self):
        """Gets the last_frozen_amount of this UniLendRecord.  # noqa: E501

        Last frozen amount  # noqa: E501

        :return: The last_frozen_amount of this UniLendRecord.  # noqa: E501
        :rtype: str
        """
        return self._last_frozen_amount

    @last_frozen_amount.setter
    def last_frozen_amount(self, last_frozen_amount):
        """Sets the last_frozen_amount of this UniLendRecord.

        Last frozen amount  # noqa: E501

        :param last_frozen_amount: The last_frozen_amount of this UniLendRecord.  # noqa: E501
        :type: str
        """

        self._last_frozen_amount = last_frozen_amount

    @property
    def type(self):
        """Gets the type of this UniLendRecord.  # noqa: E501

        Record type: lend - lend, redeem - redeem  # noqa: E501

        :return: The type of this UniLendRecord.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UniLendRecord.

        Record type: lend - lend, redeem - redeem  # noqa: E501

        :param type: The type of this UniLendRecord.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def create_time(self):
        """Gets the create_time of this UniLendRecord.  # noqa: E501

        Created time  # noqa: E501

        :return: The create_time of this UniLendRecord.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UniLendRecord.

        Created time  # noqa: E501

        :param create_time: The create_time of this UniLendRecord.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

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
        if not isinstance(other, UniLendRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UniLendRecord):
            return True

        return self.to_dict() != other.to_dict()