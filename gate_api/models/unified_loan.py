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


class UnifiedLoan(object):
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
        'type': 'str',
        'amount': 'str',
        'repaid_all': 'bool',
        'text': 'str'
    }

    attribute_map = {
        'currency': 'currency',
        'type': 'type',
        'amount': 'amount',
        'repaid_all': 'repaid_all',
        'text': 'text'
    }

    def __init__(self, currency=None, type=None, amount=None, repaid_all=None, text=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, bool, str, Configuration) -> None
        """UnifiedLoan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self._type = None
        self._amount = None
        self._repaid_all = None
        self._text = None
        self.discriminator = None

        self.currency = currency
        self.type = type
        self.amount = amount
        if repaid_all is not None:
            self.repaid_all = repaid_all
        if text is not None:
            self.text = text

    @property
    def currency(self):
        """Gets the currency of this UnifiedLoan.  # noqa: E501

        Currency.  # noqa: E501

        :return: The currency of this UnifiedLoan.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this UnifiedLoan.

        Currency.  # noqa: E501

        :param currency: The currency of this UnifiedLoan.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def type(self):
        """Gets the type of this UnifiedLoan.  # noqa: E501

        type: borrow - borrow, repay - repay.  # noqa: E501

        :return: The type of this UnifiedLoan.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UnifiedLoan.

        type: borrow - borrow, repay - repay.  # noqa: E501

        :param type: The type of this UnifiedLoan.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["borrow", "repay"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def amount(self):
        """Gets the amount of this UnifiedLoan.  # noqa: E501

        The amount of lending or repaying.  # noqa: E501

        :return: The amount of this UnifiedLoan.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UnifiedLoan.

        The amount of lending or repaying.  # noqa: E501

        :param amount: The amount of this UnifiedLoan.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def repaid_all(self):
        """Gets the repaid_all of this UnifiedLoan.  # noqa: E501

        Full repayment is solely for repayment operations. When set to 'true,' it overrides the 'amount,' allowing for direct full repayment.  # noqa: E501

        :return: The repaid_all of this UnifiedLoan.  # noqa: E501
        :rtype: bool
        """
        return self._repaid_all

    @repaid_all.setter
    def repaid_all(self, repaid_all):
        """Sets the repaid_all of this UnifiedLoan.

        Full repayment is solely for repayment operations. When set to 'true,' it overrides the 'amount,' allowing for direct full repayment.  # noqa: E501

        :param repaid_all: The repaid_all of this UnifiedLoan.  # noqa: E501
        :type: bool
        """

        self._repaid_all = repaid_all

    @property
    def text(self):
        """Gets the text of this UnifiedLoan.  # noqa: E501

        User defined custom ID.  # noqa: E501

        :return: The text of this UnifiedLoan.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this UnifiedLoan.

        User defined custom ID.  # noqa: E501

        :param text: The text of this UnifiedLoan.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if not isinstance(other, UnifiedLoan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnifiedLoan):
            return True

        return self.to_dict() != other.to_dict()
