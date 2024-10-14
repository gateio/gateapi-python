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


class RepayMultiLoan(object):
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
    openapi_types = {'order_id': 'int', 'repay_items': 'list[MultiLoanRepayItem]'}

    attribute_map = {'order_id': 'order_id', 'repay_items': 'repay_items'}

    def __init__(self, order_id=None, repay_items=None, local_vars_configuration=None):  # noqa: E501
        # type: (int, list[MultiLoanRepayItem], Configuration) -> None
        """RepayMultiLoan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._order_id = None
        self._repay_items = None
        self.discriminator = None

        self.order_id = order_id
        self.repay_items = repay_items

    @property
    def order_id(self):
        """Gets the order_id of this RepayMultiLoan.  # noqa: E501

        Order ID  # noqa: E501

        :return: The order_id of this RepayMultiLoan.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this RepayMultiLoan.

        Order ID  # noqa: E501

        :param order_id: The order_id of this RepayMultiLoan.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and order_id is None:  # noqa: E501
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def repay_items(self):
        """Gets the repay_items of this RepayMultiLoan.  # noqa: E501

        Repay Currency Item  # noqa: E501

        :return: The repay_items of this RepayMultiLoan.  # noqa: E501
        :rtype: list[MultiLoanRepayItem]
        """
        return self._repay_items

    @repay_items.setter
    def repay_items(self, repay_items):
        """Sets the repay_items of this RepayMultiLoan.

        Repay Currency Item  # noqa: E501

        :param repay_items: The repay_items of this RepayMultiLoan.  # noqa: E501
        :type: list[MultiLoanRepayItem]
        """
        if self.local_vars_configuration.client_side_validation and repay_items is None:  # noqa: E501
            raise ValueError("Invalid value for `repay_items`, must not be `None`")  # noqa: E501

        self._repay_items = repay_items

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
        if not isinstance(other, RepayMultiLoan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RepayMultiLoan):
            return True

        return self.to_dict() != other.to_dict()