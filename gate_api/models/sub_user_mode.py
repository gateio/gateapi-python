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


class SubUserMode(object):
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
        'user_id': 'int',
        'is_unified': 'bool',
        'mode': 'str'
    }

    attribute_map = {
        'user_id': 'user_id',
        'is_unified': 'is_unified',
        'mode': 'mode'
    }

    def __init__(self, user_id=None, is_unified=None, mode=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, bool, str, Configuration) -> None
        """SubUserMode - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._is_unified = None
        self._mode = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if is_unified is not None:
            self.is_unified = is_unified
        if mode is not None:
            self.mode = mode

    @property
    def user_id(self):
        """Gets the user_id of this SubUserMode.  # noqa: E501

        User ID.  # noqa: E501

        :return: The user_id of this SubUserMode.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this SubUserMode.

        User ID.  # noqa: E501

        :param user_id: The user_id of this SubUserMode.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def is_unified(self):
        """Gets the is_unified of this SubUserMode.  # noqa: E501

        Is it a unified account?.  # noqa: E501

        :return: The is_unified of this SubUserMode.  # noqa: E501
        :rtype: bool
        """
        return self._is_unified

    @is_unified.setter
    def is_unified(self, is_unified):
        """Sets the is_unified of this SubUserMode.

        Is it a unified account?.  # noqa: E501

        :param is_unified: The is_unified of this SubUserMode.  # noqa: E501
        :type: bool
        """

        self._is_unified = is_unified

    @property
    def mode(self):
        """Gets the mode of this SubUserMode.  # noqa: E501

        Unified account mode： - `classic`: Classic account mode - `multi_currency`: Multi-currency margin mode - `portfolio`: Portfolio margin mode  # noqa: E501

        :return: The mode of this SubUserMode.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this SubUserMode.

        Unified account mode： - `classic`: Classic account mode - `multi_currency`: Multi-currency margin mode - `portfolio`: Portfolio margin mode  # noqa: E501

        :param mode: The mode of this SubUserMode.  # noqa: E501
        :type: str
        """

        self._mode = mode

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
        if not isinstance(other, SubUserMode):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubUserMode):
            return True

        return self.to_dict() != other.to_dict()
