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


class OptionsPositionClose(object):
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
        'time': 'float',
        'contract': 'str',
        'side': 'str',
        'pnl': 'str',
        'text': 'str',
        'settle_size': 'str'
    }

    attribute_map = {
        'time': 'time',
        'contract': 'contract',
        'side': 'side',
        'pnl': 'pnl',
        'text': 'text',
        'settle_size': 'settle_size'
    }

    def __init__(self, time=None, contract=None, side=None, pnl=None, text=None, settle_size=None, local_vars_configuration=None):  # noqa: E501
        # type: (float, str, str, str, str, str, Configuration) -> None
        """OptionsPositionClose - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._time = None
        self._contract = None
        self._side = None
        self._pnl = None
        self._text = None
        self._settle_size = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if contract is not None:
            self.contract = contract
        if side is not None:
            self.side = side
        if pnl is not None:
            self.pnl = pnl
        if text is not None:
            self.text = text
        if settle_size is not None:
            self.settle_size = settle_size

    @property
    def time(self):
        """Gets the time of this OptionsPositionClose.  # noqa: E501

        Position close time.  # noqa: E501

        :return: The time of this OptionsPositionClose.  # noqa: E501
        :rtype: float
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this OptionsPositionClose.

        Position close time.  # noqa: E501

        :param time: The time of this OptionsPositionClose.  # noqa: E501
        :type: float
        """

        self._time = time

    @property
    def contract(self):
        """Gets the contract of this OptionsPositionClose.  # noqa: E501

        Options contract name.  # noqa: E501

        :return: The contract of this OptionsPositionClose.  # noqa: E501
        :rtype: str
        """
        return self._contract

    @contract.setter
    def contract(self, contract):
        """Sets the contract of this OptionsPositionClose.

        Options contract name.  # noqa: E501

        :param contract: The contract of this OptionsPositionClose.  # noqa: E501
        :type: str
        """

        self._contract = contract

    @property
    def side(self):
        """Gets the side of this OptionsPositionClose.  # noqa: E501

        Position side, long or short.  # noqa: E501

        :return: The side of this OptionsPositionClose.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this OptionsPositionClose.

        Position side, long or short.  # noqa: E501

        :param side: The side of this OptionsPositionClose.  # noqa: E501
        :type: str
        """
        allowed_values = ["long", "short"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and side not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `side` ({0}), must be one of {1}"  # noqa: E501
                .format(side, allowed_values)
            )

        self._side = side

    @property
    def pnl(self):
        """Gets the pnl of this OptionsPositionClose.  # noqa: E501

        PNL.  # noqa: E501

        :return: The pnl of this OptionsPositionClose.  # noqa: E501
        :rtype: str
        """
        return self._pnl

    @pnl.setter
    def pnl(self, pnl):
        """Sets the pnl of this OptionsPositionClose.

        PNL.  # noqa: E501

        :param pnl: The pnl of this OptionsPositionClose.  # noqa: E501
        :type: str
        """

        self._pnl = pnl

    @property
    def text(self):
        """Gets the text of this OptionsPositionClose.  # noqa: E501

        Text of close order.  # noqa: E501

        :return: The text of this OptionsPositionClose.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this OptionsPositionClose.

        Text of close order.  # noqa: E501

        :param text: The text of this OptionsPositionClose.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def settle_size(self):
        """Gets the settle_size of this OptionsPositionClose.  # noqa: E501

        settlement size.  # noqa: E501

        :return: The settle_size of this OptionsPositionClose.  # noqa: E501
        :rtype: str
        """
        return self._settle_size

    @settle_size.setter
    def settle_size(self, settle_size):
        """Sets the settle_size of this OptionsPositionClose.

        settlement size.  # noqa: E501

        :param settle_size: The settle_size of this OptionsPositionClose.  # noqa: E501
        :type: str
        """

        self._settle_size = settle_size

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
        if not isinstance(other, OptionsPositionClose):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OptionsPositionClose):
            return True

        return self.to_dict() != other.to_dict()
