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


class SystemTime(object):
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
        'server_time': 'int'
    }

    attribute_map = {
        'server_time': 'server_time'
    }

    def __init__(self, server_time=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, Configuration) -> None
        """SystemTime - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._server_time = None
        self.discriminator = None

        if server_time is not None:
            self.server_time = server_time

    @property
    def server_time(self):
        """Gets the server_time of this SystemTime.  # noqa: E501

        Server current time(ms).  # noqa: E501

        :return: The server_time of this SystemTime.  # noqa: E501
        :rtype: int
        """
        return self._server_time

    @server_time.setter
    def server_time(self, server_time):
        """Sets the server_time of this SystemTime.

        Server current time(ms).  # noqa: E501

        :param server_time: The server_time of this SystemTime.  # noqa: E501
        :type: int
        """

        self._server_time = server_time

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
        if not isinstance(other, SystemTime):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SystemTime):
            return True

        return self.to_dict() != other.to_dict()
