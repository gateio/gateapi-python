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


class AmendOrderResult(object):
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
        'amount': 'str',
        'price': 'str',
        'amend_text': 'str',
        'succeeded': 'bool',
        'label': 'str',
        'message': 'str',
        'account': 'str',
    }

    attribute_map = {
        'order_id': 'order_id',
        'amount': 'amount',
        'price': 'price',
        'amend_text': 'amend_text',
        'succeeded': 'succeeded',
        'label': 'label',
        'message': 'message',
        'account': 'account',
    }

    def __init__(
        self,
        order_id=None,
        amount=None,
        price=None,
        amend_text=None,
        succeeded=None,
        label=None,
        message=None,
        account=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, bool, str, str, str, Configuration) -> None
        """AmendOrderResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._order_id = None
        self._amount = None
        self._price = None
        self._amend_text = None
        self._succeeded = None
        self._label = None
        self._message = None
        self._account = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if amount is not None:
            self.amount = amount
        if price is not None:
            self.price = price
        if amend_text is not None:
            self.amend_text = amend_text
        if succeeded is not None:
            self.succeeded = succeeded
        if label is not None:
            self.label = label
        if message is not None:
            self.message = message
        if account is not None:
            self.account = account

    @property
    def order_id(self):
        """Gets the order_id of this AmendOrderResult.  # noqa: E501

        Order ID  # noqa: E501

        :return: The order_id of this AmendOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this AmendOrderResult.

        Order ID  # noqa: E501

        :param order_id: The order_id of this AmendOrderResult.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def amount(self):
        """Gets the amount of this AmendOrderResult.  # noqa: E501

        Trade amount  # noqa: E501

        :return: The amount of this AmendOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AmendOrderResult.

        Trade amount  # noqa: E501

        :param amount: The amount of this AmendOrderResult.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def price(self):
        """Gets the price of this AmendOrderResult.  # noqa: E501

        Order price  # noqa: E501

        :return: The price of this AmendOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this AmendOrderResult.

        Order price  # noqa: E501

        :param price: The price of this AmendOrderResult.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def amend_text(self):
        """Gets the amend_text of this AmendOrderResult.  # noqa: E501

        The custom data that the user remarked when amending the order  # noqa: E501

        :return: The amend_text of this AmendOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._amend_text

    @amend_text.setter
    def amend_text(self, amend_text):
        """Sets the amend_text of this AmendOrderResult.

        The custom data that the user remarked when amending the order  # noqa: E501

        :param amend_text: The amend_text of this AmendOrderResult.  # noqa: E501
        :type: str
        """

        self._amend_text = amend_text

    @property
    def succeeded(self):
        """Gets the succeeded of this AmendOrderResult.  # noqa: E501

        Update success status  # noqa: E501

        :return: The succeeded of this AmendOrderResult.  # noqa: E501
        :rtype: bool
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this AmendOrderResult.

        Update success status  # noqa: E501

        :param succeeded: The succeeded of this AmendOrderResult.  # noqa: E501
        :type: bool
        """

        self._succeeded = succeeded

    @property
    def label(self):
        """Gets the label of this AmendOrderResult.  # noqa: E501

        Error indicator for failed modifications; empty when successful  # noqa: E501

        :return: The label of this AmendOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this AmendOrderResult.

        Error indicator for failed modifications; empty when successful  # noqa: E501

        :param label: The label of this AmendOrderResult.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def message(self):
        """Gets the message of this AmendOrderResult.  # noqa: E501

        Error description for failed modifications; empty when successful  # noqa: E501

        :return: The message of this AmendOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this AmendOrderResult.

        Error description for failed modifications; empty when successful  # noqa: E501

        :param message: The message of this AmendOrderResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def account(self):
        """Gets the account of this AmendOrderResult.  # noqa: E501

        Account types， spot - spot account, margin - margin account, unified - unified account, cross_margin - cross margin account.Portfolio margin accounts can only be set to `cross_margin`  # noqa: E501

        :return: The account of this AmendOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this AmendOrderResult.

        Account types， spot - spot account, margin - margin account, unified - unified account, cross_margin - cross margin account.Portfolio margin accounts can only be set to `cross_margin`  # noqa: E501

        :param account: The account of this AmendOrderResult.  # noqa: E501
        :type: str
        """

        self._account = account

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
        if not isinstance(other, AmendOrderResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AmendOrderResult):
            return True

        return self.to_dict() != other.to_dict()
