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


class CancelOrderResult(object):
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
        'currency_pair': 'str',
        'id': 'str',
        'text': 'str',
        'succeeded': 'bool',
        'label': 'str',
        'message': 'str',
        'account': 'str'
    }

    attribute_map = {
        'currency_pair': 'currency_pair',
        'id': 'id',
        'text': 'text',
        'succeeded': 'succeeded',
        'label': 'label',
        'message': 'message',
        'account': 'account'
    }

    def __init__(self, currency_pair=None, id=None, text=None, succeeded=None, label=None, message=None, account=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, bool, str, str, str, Configuration) -> None
        """CancelOrderResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency_pair = None
        self._id = None
        self._text = None
        self._succeeded = None
        self._label = None
        self._message = None
        self._account = None
        self.discriminator = None

        if currency_pair is not None:
            self.currency_pair = currency_pair
        if id is not None:
            self.id = id
        if text is not None:
            self.text = text
        if succeeded is not None:
            self.succeeded = succeeded
        if label is not None:
            self.label = label
        if message is not None:
            self.message = message
        if account is not None:
            self.account = account

    @property
    def currency_pair(self):
        """Gets the currency_pair of this CancelOrderResult.  # noqa: E501

        Order currency pair  # noqa: E501

        :return: The currency_pair of this CancelOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._currency_pair

    @currency_pair.setter
    def currency_pair(self, currency_pair):
        """Sets the currency_pair of this CancelOrderResult.

        Order currency pair  # noqa: E501

        :param currency_pair: The currency_pair of this CancelOrderResult.  # noqa: E501
        :type: str
        """

        self._currency_pair = currency_pair

    @property
    def id(self):
        """Gets the id of this CancelOrderResult.  # noqa: E501

        Order ID  # noqa: E501

        :return: The id of this CancelOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CancelOrderResult.

        Order ID  # noqa: E501

        :param id: The id of this CancelOrderResult.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this CancelOrderResult.  # noqa: E501

        Custom order information  # noqa: E501

        :return: The text of this CancelOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this CancelOrderResult.

        Custom order information  # noqa: E501

        :param text: The text of this CancelOrderResult.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def succeeded(self):
        """Gets the succeeded of this CancelOrderResult.  # noqa: E501

        Whether cancellation succeeded  # noqa: E501

        :return: The succeeded of this CancelOrderResult.  # noqa: E501
        :rtype: bool
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this CancelOrderResult.

        Whether cancellation succeeded  # noqa: E501

        :param succeeded: The succeeded of this CancelOrderResult.  # noqa: E501
        :type: bool
        """

        self._succeeded = succeeded

    @property
    def label(self):
        """Gets the label of this CancelOrderResult.  # noqa: E501

        Error label when failed to cancel the order; emtpy if succeeded  # noqa: E501

        :return: The label of this CancelOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CancelOrderResult.

        Error label when failed to cancel the order; emtpy if succeeded  # noqa: E501

        :param label: The label of this CancelOrderResult.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def message(self):
        """Gets the message of this CancelOrderResult.  # noqa: E501

        Error message when failed to cancel the order; empty if succeeded  # noqa: E501

        :return: The message of this CancelOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CancelOrderResult.

        Error message when failed to cancel the order; empty if succeeded  # noqa: E501

        :param message: The message of this CancelOrderResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def account(self):
        """Gets the account of this CancelOrderResult.  # noqa: E501

        Default is empty (deprecated)  # noqa: E501

        :return: The account of this CancelOrderResult.  # noqa: E501
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this CancelOrderResult.

        Default is empty (deprecated)  # noqa: E501

        :param account: The account of this CancelOrderResult.  # noqa: E501
        :type: str
        """

        self._account = account

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
        if not isinstance(other, CancelOrderResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CancelOrderResult):
            return True

        return self.to_dict() != other.to_dict()
