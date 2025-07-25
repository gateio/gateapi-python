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


class CountdownCancelAllFuturesTask(object):
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
        'timeout': 'int',
        'contract': 'str'
    }

    attribute_map = {
        'timeout': 'timeout',
        'contract': 'contract'
    }

    def __init__(self, timeout=None, contract=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, str, Configuration) -> None
        """CountdownCancelAllFuturesTask - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._timeout = None
        self._contract = None
        self.discriminator = None

        self.timeout = timeout
        if contract is not None:
            self.contract = contract

    @property
    def timeout(self):
        """Gets the timeout of this CountdownCancelAllFuturesTask.  # noqa: E501

        Countdown time in seconds At least 5 seconds, 0 means cancel countdown  # noqa: E501

        :return: The timeout of this CountdownCancelAllFuturesTask.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this CountdownCancelAllFuturesTask.

        Countdown time in seconds At least 5 seconds, 0 means cancel countdown  # noqa: E501

        :param timeout: The timeout of this CountdownCancelAllFuturesTask.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and timeout is None:  # noqa: E501
            raise ValueError("Invalid value for `timeout`, must not be `None`")  # noqa: E501

        self._timeout = timeout

    @property
    def contract(self):
        """Gets the contract of this CountdownCancelAllFuturesTask.  # noqa: E501

        Futures contract.  # noqa: E501

        :return: The contract of this CountdownCancelAllFuturesTask.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this CountdownCancelAllFuturesTask.

        Futures contract.  # noqa: E501

        :param contract: The contract of this CountdownCancelAllFuturesTask.  # noqa: E501
        :type: str
        """

        self._contract = contract

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
        if not isinstance(other, CountdownCancelAllFuturesTask):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CountdownCancelAllFuturesTask):
            return True

        return self.to_dict() != other.to_dict()
