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


class UnifiedHistoryLoanRateRates(object):
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
        'time': 'int',
        'rate': 'str'
    }

    attribute_map = {
        'time': 'time',
        'rate': 'rate'
    }

    def __init__(self, time=None, rate=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, str, Configuration) -> None
        """UnifiedHistoryLoanRateRates - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._time = None
        self._rate = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if rate is not None:
            self.rate = rate

    @property
    def time(self):
        """Gets the time of this UnifiedHistoryLoanRateRates.  # noqa: E501

        The hourly timestamp corresponding to the interest rate, in milliseconds.  # noqa: E501

        :return: The time of this UnifiedHistoryLoanRateRates.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this UnifiedHistoryLoanRateRates.

        The hourly timestamp corresponding to the interest rate, in milliseconds.  # noqa: E501

        :param time: The time of this UnifiedHistoryLoanRateRates.  # noqa: E501
        :type: int
        """

        self._time = time

    @property
    def rate(self):
        """Gets the rate of this UnifiedHistoryLoanRateRates.  # noqa: E501

        Historical interest rates for this hour.  # noqa: E501

        :return: The rate of this UnifiedHistoryLoanRateRates.  # noqa: E501
        :rtype: str
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this UnifiedHistoryLoanRateRates.

        Historical interest rates for this hour.  # noqa: E501

        :param rate: The rate of this UnifiedHistoryLoanRateRates.  # noqa: E501
        :type: str
        """

        self._rate = rate

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
        if not isinstance(other, UnifiedHistoryLoanRateRates):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnifiedHistoryLoanRateRates):
            return True

        return self.to_dict() != other.to_dict()
