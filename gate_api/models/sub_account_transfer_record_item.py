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


class SubAccountTransferRecordItem(object):
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
        'timest': 'str',
        'uid': 'str',
        'sub_account': 'str',
        'sub_account_type': 'str',
        'currency': 'str',
        'amount': 'str',
        'direction': 'str',
        'source': 'str',
        'client_order_id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'timest': 'timest',
        'uid': 'uid',
        'sub_account': 'sub_account',
        'sub_account_type': 'sub_account_type',
        'currency': 'currency',
        'amount': 'amount',
        'direction': 'direction',
        'source': 'source',
        'client_order_id': 'client_order_id',
        'status': 'status'
    }

    def __init__(self, timest=None, uid=None, sub_account=None, sub_account_type='spot', currency=None, amount=None, direction=None, source=None, client_order_id=None, status=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, str, str, str, str, str, str, str, Configuration) -> None
        """SubAccountTransferRecordItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timest = None
        self._uid = None
        self._sub_account = None
        self._sub_account_type = None
        self._currency = None
        self._amount = None
        self._direction = None
        self._source = None
        self._client_order_id = None
        self._status = None
        self.discriminator = None

        if timest is not None:
            self.timest = timest
        if uid is not None:
            self.uid = uid
        self.sub_account = sub_account
        if sub_account_type is not None:
            self.sub_account_type = sub_account_type
        self.currency = currency
        self.amount = amount
        self.direction = direction
        if source is not None:
            self.source = source
        if client_order_id is not None:
            self.client_order_id = client_order_id
        if status is not None:
            self.status = status

    @property
    def timest(self):
        """Gets the timest of this SubAccountTransferRecordItem.  # noqa: E501

        Transfer timestamp.  # noqa: E501

        :return: The timest of this SubAccountTransferRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._timest

    @timest.setter
    def timest(self, timest):
        """Sets the timest of this SubAccountTransferRecordItem.

        Transfer timestamp.  # noqa: E501

        :param timest: The timest of this SubAccountTransferRecordItem.  # noqa: E501
        :type: str
        """

        self._timest = timest

    @property
    def uid(self):
        """Gets the uid of this SubAccountTransferRecordItem.  # noqa: E501

        Main account user ID.  # noqa: E501

        :return: The uid of this SubAccountTransferRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this SubAccountTransferRecordItem.

        Main account user ID.  # noqa: E501

        :param uid: The uid of this SubAccountTransferRecordItem.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def sub_account(self):
        """Gets the sub_account of this SubAccountTransferRecordItem.  # noqa: E501

        Sub account user ID.  # noqa: E501

        :return: The sub_account of this SubAccountTransferRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._sub_account

    @sub_account.setter
    def sub_account(self, sub_account):
        """Sets the sub_account of this SubAccountTransferRecordItem.

        Sub account user ID.  # noqa: E501

        :param sub_account: The sub_account of this SubAccountTransferRecordItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sub_account is None:  # noqa: E501
            raise ValueError("Invalid value for `sub_account`, must not be `None`")  # noqa: E501

        self._sub_account = sub_account

    @property
    def sub_account_type(self):
        """Gets the sub_account_type of this SubAccountTransferRecordItem.  # noqa: E501

        Target sub user's account. `spot` - spot account, `futures` - perpetual contract account, `delivery` - delivery account  # noqa: E501

        :return: The sub_account_type of this SubAccountTransferRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._sub_account_type

    @sub_account_type.setter
    def sub_account_type(self, sub_account_type):
        """Sets the sub_account_type of this SubAccountTransferRecordItem.

        Target sub user's account. `spot` - spot account, `futures` - perpetual contract account, `delivery` - delivery account  # noqa: E501

        :param sub_account_type: The sub_account_type of this SubAccountTransferRecordItem.  # noqa: E501
        :type: str
        """

        self._sub_account_type = sub_account_type

    @property
    def currency(self):
        """Gets the currency of this SubAccountTransferRecordItem.  # noqa: E501

        Transfer currency name.  # noqa: E501

        :return: The currency of this SubAccountTransferRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SubAccountTransferRecordItem.

        Transfer currency name.  # noqa: E501

        :param currency: The currency of this SubAccountTransferRecordItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and currency is None:  # noqa: E501
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this SubAccountTransferRecordItem.  # noqa: E501

        Transfer amount.  # noqa: E501

        :return: The amount of this SubAccountTransferRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SubAccountTransferRecordItem.

        Transfer amount.  # noqa: E501

        :param amount: The amount of this SubAccountTransferRecordItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def direction(self):
        """Gets the direction of this SubAccountTransferRecordItem.  # noqa: E501

        Transfer direction. to - transfer into sub account; from - transfer out from sub account  # noqa: E501

        :return: The direction of this SubAccountTransferRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """Sets the direction of this SubAccountTransferRecordItem.

        Transfer direction. to - transfer into sub account; from - transfer out from sub account  # noqa: E501

        :param direction: The direction of this SubAccountTransferRecordItem.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and direction is None:  # noqa: E501
            raise ValueError("Invalid value for `direction`, must not be `None`")  # noqa: E501

        self._direction = direction

    @property
    def source(self):
        """Gets the source of this SubAccountTransferRecordItem.  # noqa: E501

        Where the operation is initiated from.  # noqa: E501

        :return: The source of this SubAccountTransferRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this SubAccountTransferRecordItem.

        Where the operation is initiated from.  # noqa: E501

        :param source: The source of this SubAccountTransferRecordItem.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def client_order_id(self):
        """Gets the client_order_id of this SubAccountTransferRecordItem.  # noqa: E501

        The custom ID provided by the customer serves as a safeguard against duplicate transfers. It can be a combination of letters (case-sensitive), numbers, hyphens '-', and underscores '_', with a length ranging from 1 to 64 characters.  # noqa: E501

        :return: The client_order_id of this SubAccountTransferRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._client_order_id

    @client_order_id.setter
    def client_order_id(self, client_order_id):
        """Sets the client_order_id of this SubAccountTransferRecordItem.

        The custom ID provided by the customer serves as a safeguard against duplicate transfers. It can be a combination of letters (case-sensitive), numbers, hyphens '-', and underscores '_', with a length ranging from 1 to 64 characters.  # noqa: E501

        :param client_order_id: The client_order_id of this SubAccountTransferRecordItem.  # noqa: E501
        :type: str
        """

        self._client_order_id = client_order_id

    @property
    def status(self):
        """Gets the status of this SubAccountTransferRecordItem.  # noqa: E501

        Sub-account transfer record status, currently only success.  # noqa: E501

        :return: The status of this SubAccountTransferRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SubAccountTransferRecordItem.

        Sub-account transfer record status, currently only success.  # noqa: E501

        :param status: The status of this SubAccountTransferRecordItem.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, SubAccountTransferRecordItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubAccountTransferRecordItem):
            return True

        return self.to_dict() != other.to_dict()
