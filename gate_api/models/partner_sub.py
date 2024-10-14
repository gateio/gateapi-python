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


class PartnerSub(object):
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
    openapi_types = {'user_id': 'int', 'user_join_time': 'int', 'type': 'int'}

    attribute_map = {'user_id': 'user_id', 'user_join_time': 'user_join_time', 'type': 'type'}

    def __init__(self, user_id=None, user_join_time=None, type=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, int, int, Configuration) -> None
        """PartnerSub - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._user_join_time = None
        self._type = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if user_join_time is not None:
            self.user_join_time = user_join_time
        if type is not None:
            self.type = type

    @property
    def user_id(self):
        """Gets the user_id of this PartnerSub.  # noqa: E501

        User ID  # noqa: E501

        :return: The user_id of this PartnerSub.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this PartnerSub.

        User ID  # noqa: E501

        :param user_id: The user_id of this PartnerSub.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def user_join_time(self):
        """Gets the user_join_time of this PartnerSub.  # noqa: E501

        The time when the user joined the system, in seconds Unix timestamp  # noqa: E501

        :return: The user_join_time of this PartnerSub.  # noqa: E501
        :rtype: int
        """
        return self._user_join_time

    @user_join_time.setter
    def user_join_time(self, user_join_time):
        """Sets the user_join_time of this PartnerSub.

        The time when the user joined the system, in seconds Unix timestamp  # noqa: E501

        :param user_join_time: The user_join_time of this PartnerSub.  # noqa: E501
        :type: int
        """

        self._user_join_time = user_join_time

    @property
    def type(self):
        """Gets the type of this PartnerSub.  # noqa: E501

        Type (1-Sub-agent 2-Indirect Customer 3-Direct Customer)  # noqa: E501

        :return: The type of this PartnerSub.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PartnerSub.

        Type (1-Sub-agent 2-Indirect Customer 3-Direct Customer)  # noqa: E501

        :param type: The type of this PartnerSub.  # noqa: E501
        :type: int
        """

        self._type = type

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
        if not isinstance(other, PartnerSub):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PartnerSub):
            return True

        return self.to_dict() != other.to_dict()
