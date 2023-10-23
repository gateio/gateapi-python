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


class RepayResp(object):
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
    openapi_types = {'repaid_principal': 'str', 'repaid_interest': 'str'}

    attribute_map = {'repaid_principal': 'repaid_principal', 'repaid_interest': 'repaid_interest'}

    def __init__(self, repaid_principal=None, repaid_interest=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, Configuration) -> None
        """RepayResp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._repaid_principal = None
        self._repaid_interest = None
        self.discriminator = None

        if repaid_principal is not None:
            self.repaid_principal = repaid_principal
        if repaid_interest is not None:
            self.repaid_interest = repaid_interest

    @property
    def repaid_principal(self):
        """Gets the repaid_principal of this RepayResp.  # noqa: E501

        Principal  # noqa: E501

        :return: The repaid_principal of this RepayResp.  # noqa: E501
        :rtype: str
        """
        return self._repaid_principal

    @repaid_principal.setter
    def repaid_principal(self, repaid_principal):
        """Sets the repaid_principal of this RepayResp.

        Principal  # noqa: E501

        :param repaid_principal: The repaid_principal of this RepayResp.  # noqa: E501
        :type: str
        """

        self._repaid_principal = repaid_principal

    @property
    def repaid_interest(self):
        """Gets the repaid_interest of this RepayResp.  # noqa: E501

        Interest  # noqa: E501

        :return: The repaid_interest of this RepayResp.  # noqa: E501
        :rtype: str
        """
        return self._repaid_interest

    @repaid_interest.setter
    def repaid_interest(self, repaid_interest):
        """Sets the repaid_interest of this RepayResp.

        Interest  # noqa: E501

        :param repaid_interest: The repaid_interest of this RepayResp.  # noqa: E501
        :type: str
        """

        self._repaid_interest = repaid_interest

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
        if not isinstance(other, RepayResp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepayResp):
            return True

        return self.to_dict() != other.to_dict()