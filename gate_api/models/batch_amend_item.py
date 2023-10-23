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


class BatchAmendItem(object):
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
        'order_id': 'str',
        'currency_pair': 'str',
        'account': 'str',
        'amount': 'str',
        'price': 'str',
        'amend_text': 'str',
    }

    attribute_map = {
        'order_id': 'order_id',
        'currency_pair': 'currency_pair',
        'account': 'account',
        'amount': 'amount',
        'price': 'price',
        'amend_text': 'amend_text',
    }

    def __init__(
        self,
        order_id=None,
        currency_pair=None,
        account=None,
        amount=None,
        price=None,
        amend_text=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, str, str, Configuration) -> None
        """BatchAmendItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._order_id = None
        self._currency_pair = None
        self._account = None
        self._amount = None
        self._price = None
        self._amend_text = None
        self.discriminator = None

        self.order_id = order_id
        self.currency_pair = currency_pair
        if account is not None:
            self.account = account
        if amount is not None:
            self.amount = amount
        if price is not None:
            self.price = price
        if amend_text is not None:
            self.amend_text = amend_text

    @property
    def order_id(self):
        """Gets the order_id of this BatchAmendItem.  # noqa: E501

        The order ID returned upon successful creation or the custom ID specified by the user during creation (i.e., the 'text' field).  # noqa: E501

        :return: The order_id of this BatchAmendItem.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this BatchAmendItem.

        The order ID returned upon successful creation or the custom ID specified by the user during creation (i.e., the 'text' field).  # noqa: E501

        :param order_id: The order_id of this BatchAmendItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and order_id is None:  # noqa: E501
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def currency_pair(self):
        """Gets the currency_pair of this BatchAmendItem.  # noqa: E501

        Currency pair  # noqa: E501

        :return: The currency_pair of this BatchAmendItem.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this BatchAmendItem.

        Currency pair  # noqa: E501

        :param currency_pair: The currency_pair of this BatchAmendItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency_pair is None:  # noqa: E501
            raise ValueError("Invalid value for `currency_pair`, must not be `None`")  # noqa: E501

        self._currency_pair = currency_pair

    @property
    def account(self):
        """Gets the account of this BatchAmendItem.  # noqa: E501

        Default to spot, portfolio, and margin accounts if not specified. Use 'cross_margin' to query cross margin accounts. Only 'cross_margin' can be specified for portfolio margin accounts.  # noqa: E501

        :return: The account of this BatchAmendItem.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this BatchAmendItem.

        Default to spot, portfolio, and margin accounts if not specified. Use 'cross_margin' to query cross margin accounts. Only 'cross_margin' can be specified for portfolio margin accounts.  # noqa: E501

        :param account: The account of this BatchAmendItem.  # noqa: E501
        :type: str
        """

        self._account = account

    @property
    def amount(self):
        """Gets the amount of this BatchAmendItem.  # noqa: E501

        trade amount, only one of amount and price can be specified  # noqa: E501

        :return: The amount of this BatchAmendItem.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this BatchAmendItem.

        trade amount, only one of amount and price can be specified  # noqa: E501

        :param amount: The amount of this BatchAmendItem.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def price(self):
        """Gets the price of this BatchAmendItem.  # noqa: E501

        trade price, only one of amount and price can be specified  # noqa: E501

        :return: The price of this BatchAmendItem.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this BatchAmendItem.

        trade price, only one of amount and price can be specified  # noqa: E501

        :param price: The price of this BatchAmendItem.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def amend_text(self):
        """Gets the amend_text of this BatchAmendItem.  # noqa: E501

        Custom info during amending order  # noqa: E501

        :return: The amend_text of this BatchAmendItem.  # noqa: E501
        :rtype: str
        """
        return self._amend_text

    @amend_text.setter
    def amend_text(self, amend_text):
        """Sets the amend_text of this BatchAmendItem.

        Custom info during amending order  # noqa: E501

        :param amend_text: The amend_text of this BatchAmendItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amend_text is not None and len(amend_text) > 31:
            raise ValueError("Invalid value for `amend_text`, length must be less than or equal to `31`")  # noqa: E501

        self._amend_text = amend_text

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
        if not isinstance(other, BatchAmendItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchAmendItem):
            return True

        return self.to_dict() != other.to_dict()
