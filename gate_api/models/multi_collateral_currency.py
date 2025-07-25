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


class MultiCollateralCurrency(object):
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
        'loan_currencies': 'list[MultiLoanItem]',
        'collateral_currencies': 'list[MultiCollateralItem]'
    }

    attribute_map = {
        'loan_currencies': 'loan_currencies',
        'collateral_currencies': 'collateral_currencies'
    }

    def __init__(self, loan_currencies=None, collateral_currencies=None, local_vars_configuration=None):  # noqa: E501
        # type: (list[MultiLoanItem], list[MultiCollateralItem], Configuration) -> None
        """MultiCollateralCurrency - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._loan_currencies = None
        self._collateral_currencies = None
        self.discriminator = None

        if loan_currencies is not None:
            self.loan_currencies = loan_currencies
        if collateral_currencies is not None:
            self.collateral_currencies = collateral_currencies

    @property
    def loan_currencies(self):
        """Gets the loan_currencies of this MultiCollateralCurrency.  # noqa: E501

        List of supported borrowing currencies.  # noqa: E501

        :return: The loan_currencies of this MultiCollateralCurrency.  # noqa: E501
        :rtype: list[MultiLoanItem]
        """
        return self._loan_currencies

    @loan_currencies.setter
    def loan_currencies(self, loan_currencies):
        """Sets the loan_currencies of this MultiCollateralCurrency.

        List of supported borrowing currencies.  # noqa: E501

        :param loan_currencies: The loan_currencies of this MultiCollateralCurrency.  # noqa: E501
        :type: list[MultiLoanItem]
        """

        self._loan_currencies = loan_currencies

    @property
    def collateral_currencies(self):
        """Gets the collateral_currencies of this MultiCollateralCurrency.  # noqa: E501

        List of supported collateral currencies.  # noqa: E501

        :return: The collateral_currencies of this MultiCollateralCurrency.  # noqa: E501
        :rtype: list[MultiCollateralItem]
        """
        return self._collateral_currencies

    @collateral_currencies.setter
    def collateral_currencies(self, collateral_currencies):
        """Sets the collateral_currencies of this MultiCollateralCurrency.

        List of supported collateral currencies.  # noqa: E501

        :param collateral_currencies: The collateral_currencies of this MultiCollateralCurrency.  # noqa: E501
        :type: list[MultiCollateralItem]
        """

        self._collateral_currencies = collateral_currencies

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
        if not isinstance(other, MultiCollateralCurrency):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultiCollateralCurrency):
            return True

        return self.to_dict() != other.to_dict()
