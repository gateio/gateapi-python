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


class AccountDetail(object):
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
        'ip_whitelist': 'list[str]',
        'currency_pairs': 'list[str]',
        'user_id': 'int',
        'key': 'AccountDetailKey',
    }

    attribute_map = {
        'ip_whitelist': 'ip_whitelist',
        'currency_pairs': 'currency_pairs',
        'user_id': 'user_id',
        'key': 'key',
    }

    def __init__(
        self, ip_whitelist=None, currency_pairs=None, user_id=None, key=None, local_vars_configuration=None
    ):  # noqa: E501
        # type: (list[str], list[str], int, AccountDetailKey, Configuration) -> None
        """AccountDetail - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._ip_whitelist = None
        self._currency_pairs = None
        self._user_id = None
        self._key = None
        self.discriminator = None

        if ip_whitelist is not None:
            self.ip_whitelist = ip_whitelist
        if currency_pairs is not None:
            self.currency_pairs = currency_pairs
        if user_id is not None:
            self.user_id = user_id
        if key is not None:
            self.key = key

    @property
    def ip_whitelist(self):
        """Gets the ip_whitelist of this AccountDetail.  # noqa: E501

        IP whitelist  # noqa: E501

        :return: The ip_whitelist of this AccountDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._ip_whitelist

    @ip_whitelist.setter
    def ip_whitelist(self, ip_whitelist):
        """Sets the ip_whitelist of this AccountDetail.

        IP whitelist  # noqa: E501

        :param ip_whitelist: The ip_whitelist of this AccountDetail.  # noqa: E501
        :type: list[str]
        """

        self._ip_whitelist = ip_whitelist

    @property
    def currency_pairs(self):
        """Gets the currency_pairs of this AccountDetail.  # noqa: E501

        CurrencyPair whitelisting  # noqa: E501

        :return: The currency_pairs of this AccountDetail.  # noqa: E501
        :rtype: list[str]
        """
        return self._currency_pairs

    @currency_pairs.setter
    def currency_pairs(self, currency_pairs):
        """Sets the currency_pairs of this AccountDetail.

        CurrencyPair whitelisting  # noqa: E501

        :param currency_pairs: The currency_pairs of this AccountDetail.  # noqa: E501
        :type: list[str]
        """

        self._currency_pairs = currency_pairs

    @property
    def user_id(self):
        """Gets the user_id of this AccountDetail.  # noqa: E501

        User ID  # noqa: E501

        :return: The user_id of this AccountDetail.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AccountDetail.

        User ID  # noqa: E501

        :param user_id: The user_id of this AccountDetail.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def key(self):
        """Gets the key of this AccountDetail.  # noqa: E501


        :return: The key of this AccountDetail.  # noqa: E501
        :rtype: AccountDetailKey
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this AccountDetail.


        :param key: The key of this AccountDetail.  # noqa: E501
        :type: AccountDetailKey
        """

        self._key = key

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
        if not isinstance(other, AccountDetail):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountDetail):
            return True

        return self.to_dict() != other.to_dict()