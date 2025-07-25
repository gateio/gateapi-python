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


class CollateralLtv(object):
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
        'init_ltv': 'str',
        'alert_ltv': 'str',
        'liquidate_ltv': 'str'
    }

    attribute_map = {
        'init_ltv': 'init_ltv',
        'alert_ltv': 'alert_ltv',
        'liquidate_ltv': 'liquidate_ltv'
    }

    def __init__(self, init_ltv=None, alert_ltv=None, liquidate_ltv=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, Configuration) -> None
        """CollateralLtv - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._init_ltv = None
        self._alert_ltv = None
        self._liquidate_ltv = None
        self.discriminator = None

        if init_ltv is not None:
            self.init_ltv = init_ltv
        if alert_ltv is not None:
            self.alert_ltv = alert_ltv
        if liquidate_ltv is not None:
            self.liquidate_ltv = liquidate_ltv

    @property
    def init_ltv(self):
        """Gets the init_ltv of this CollateralLtv.  # noqa: E501

        The initial collateralization rate.  # noqa: E501

        :return: The init_ltv of this CollateralLtv.  # noqa: E501
        :rtype: str
        """
        return self._init_ltv

    @init_ltv.setter
    def init_ltv(self, init_ltv):
        """Sets the init_ltv of this CollateralLtv.

        The initial collateralization rate.  # noqa: E501

        :param init_ltv: The init_ltv of this CollateralLtv.  # noqa: E501
        :type: str
        """

        self._init_ltv = init_ltv

    @property
    def alert_ltv(self):
        """Gets the alert_ltv of this CollateralLtv.  # noqa: E501

        Warning collateralization ratio.  # noqa: E501

        :return: The alert_ltv of this CollateralLtv.  # noqa: E501
        :rtype: str
        """
        return self._alert_ltv

    @alert_ltv.setter
    def alert_ltv(self, alert_ltv):
        """Sets the alert_ltv of this CollateralLtv.

        Warning collateralization ratio.  # noqa: E501

        :param alert_ltv: The alert_ltv of this CollateralLtv.  # noqa: E501
        :type: str
        """

        self._alert_ltv = alert_ltv

    @property
    def liquidate_ltv(self):
        """Gets the liquidate_ltv of this CollateralLtv.  # noqa: E501

        The liquidation collateralization rate.  # noqa: E501

        :return: The liquidate_ltv of this CollateralLtv.  # noqa: E501
        :rtype: str
        """
        return self._liquidate_ltv

    @liquidate_ltv.setter
    def liquidate_ltv(self, liquidate_ltv):
        """Sets the liquidate_ltv of this CollateralLtv.

        The liquidation collateralization rate.  # noqa: E501

        :param liquidate_ltv: The liquidate_ltv of this CollateralLtv.  # noqa: E501
        :type: str
        """

        self._liquidate_ltv = liquidate_ltv

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
        if not isinstance(other, CollateralLtv):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CollateralLtv):
            return True

        return self.to_dict() != other.to_dict()
