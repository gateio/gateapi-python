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


class MarginTiers(object):
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
    openapi_types = {'tier': 'str', 'margin_rate': 'str', 'lower_limit': 'str', 'upper_limit': 'str', 'leverage': 'str'}

    attribute_map = {
        'tier': 'tier',
        'margin_rate': 'margin_rate',
        'lower_limit': 'lower_limit',
        'upper_limit': 'upper_limit',
        'leverage': 'leverage',
    }

    def __init__(
        self,
        tier=None,
        margin_rate=None,
        lower_limit=None,
        upper_limit=None,
        leverage=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, str, Configuration) -> None
        """MarginTiers - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tier = None
        self._margin_rate = None
        self._lower_limit = None
        self._upper_limit = None
        self._leverage = None
        self.discriminator = None

        if tier is not None:
            self.tier = tier
        if margin_rate is not None:
            self.margin_rate = margin_rate
        if lower_limit is not None:
            self.lower_limit = lower_limit
        if upper_limit is not None:
            self.upper_limit = upper_limit
        if leverage is not None:
            self.leverage = leverage

    @property
    def tier(self):
        """Gets the tier of this MarginTiers.  # noqa: E501

        Tier  # noqa: E501

        :return: The tier of this MarginTiers.  # noqa: E501
        :rtype: str
        """
        return self._tier

    @tier.setter
    def tier(self, tier):
        """Sets the tier of this MarginTiers.

        Tier  # noqa: E501

        :param tier: The tier of this MarginTiers.  # noqa: E501
        :type: str
        """

        self._tier = tier

    @property
    def margin_rate(self):
        """Gets the margin_rate of this MarginTiers.  # noqa: E501

        Discount  # noqa: E501

        :return: The margin_rate of this MarginTiers.  # noqa: E501
        :rtype: str
        """
        return self._margin_rate

    @margin_rate.setter
    def margin_rate(self, margin_rate):
        """Sets the margin_rate of this MarginTiers.

        Discount  # noqa: E501

        :param margin_rate: The margin_rate of this MarginTiers.  # noqa: E501
        :type: str
        """

        self._margin_rate = margin_rate

    @property
    def lower_limit(self):
        """Gets the lower_limit of this MarginTiers.  # noqa: E501

        Lower limit  # noqa: E501

        :return: The lower_limit of this MarginTiers.  # noqa: E501
        :rtype: str
        """
        return self._lower_limit

    @lower_limit.setter
    def lower_limit(self, lower_limit):
        """Sets the lower_limit of this MarginTiers.

        Lower limit  # noqa: E501

        :param lower_limit: The lower_limit of this MarginTiers.  # noqa: E501
        :type: str
        """

        self._lower_limit = lower_limit

    @property
    def upper_limit(self):
        """Gets the upper_limit of this MarginTiers.  # noqa: E501

        Upper limit, \"\" indicates greater than (the last tier)  # noqa: E501

        :return: The upper_limit of this MarginTiers.  # noqa: E501
        :rtype: str
        """
        return self._upper_limit

    @upper_limit.setter
    def upper_limit(self, upper_limit):
        """Sets the upper_limit of this MarginTiers.

        Upper limit, \"\" indicates greater than (the last tier)  # noqa: E501

        :param upper_limit: The upper_limit of this MarginTiers.  # noqa: E501
        :type: str
        """

        self._upper_limit = upper_limit

    @property
    def leverage(self):
        """Gets the leverage of this MarginTiers.  # noqa: E501

        Position leverage  # noqa: E501

        :return: The leverage of this MarginTiers.  # noqa: E501
        :rtype: str
        """
        return self._leverage

    @leverage.setter
    def leverage(self, leverage):
        """Sets the leverage of this MarginTiers.

        Position leverage  # noqa: E501

        :param leverage: The leverage of this MarginTiers.  # noqa: E501
        :type: str
        """

        self._leverage = leverage

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
        if not isinstance(other, MarginTiers):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MarginTiers):
            return True

        return self.to_dict() != other.to_dict()
