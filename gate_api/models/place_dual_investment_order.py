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


class PlaceDualInvestmentOrder(object):
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
        'plan_id': 'str',
        'amount': 'str',
        'text': 'str'
    }

    attribute_map = {
        'plan_id': 'plan_id',
        'amount': 'amount',
        'text': 'text'
    }

    def __init__(self, plan_id=None, amount=None, text=None, local_vars_configuration=None):  # noqa: E501
        # type: (str, str, str, Configuration) -> None
        """PlaceDualInvestmentOrder - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._plan_id = None
        self._amount = None
        self._text = None
        self.discriminator = None

        self.plan_id = plan_id
        self.amount = amount
        if text is not None:
            self.text = text

    @property
    def plan_id(self):
        """Gets the plan_id of this PlaceDualInvestmentOrder.  # noqa: E501

        Plan ID.  # noqa: E501

        :return: The plan_id of this PlaceDualInvestmentOrder.  # noqa: E501
        :rtype: str
        """
        return self._plan_id

    @plan_id.setter
    def plan_id(self, plan_id):
        """Sets the plan_id of this PlaceDualInvestmentOrder.

        Plan ID.  # noqa: E501

        :param plan_id: The plan_id of this PlaceDualInvestmentOrder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and plan_id is None:  # noqa: E501
            raise ValueError("Invalid value for `plan_id`, must not be `None`")  # noqa: E501

        self._plan_id = plan_id

    @property
    def amount(self):
        """Gets the amount of this PlaceDualInvestmentOrder.  # noqa: E501

        Subscription amount, mutually exclusive with the copies field.  # noqa: E501

        :return: The amount of this PlaceDualInvestmentOrder.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PlaceDualInvestmentOrder.

        Subscription amount, mutually exclusive with the copies field.  # noqa: E501

        :param amount: The amount of this PlaceDualInvestmentOrder.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def text(self):
        """Gets the text of this PlaceDualInvestmentOrder.  # noqa: E501

        User defined information. If not empty, must follow the rules below:  1. prefixed with `t-` 2. no longer than 28 bytes without `t-` prefix 3. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)   # noqa: E501

        :return: The text of this PlaceDualInvestmentOrder.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PlaceDualInvestmentOrder.

        User defined information. If not empty, must follow the rules below:  1. prefixed with `t-` 2. no longer than 28 bytes without `t-` prefix 3. can only include 0-9, A-Z, a-z, underscore(_), hyphen(-) or dot(.)   # noqa: E501

        :param text: The text of this PlaceDualInvestmentOrder.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if not isinstance(other, PlaceDualInvestmentOrder):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PlaceDualInvestmentOrder):
            return True

        return self.to_dict() != other.to_dict()
