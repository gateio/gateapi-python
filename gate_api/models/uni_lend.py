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


class UniLend(object):
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
        'currency': 'str',
        'current_amount': 'str',
        'amount': 'str',
        'lent_amount': 'str',
        'frozen_amount': 'str',
        'min_rate': 'str',
        'interest_status': 'str',
        'reinvest_left_amount': 'str',
        'create_time': 'int',
        'update_time': 'int',
    }

    attribute_map = {
        'currency': 'currency',
        'current_amount': 'current_amount',
        'amount': 'amount',
        'lent_amount': 'lent_amount',
        'frozen_amount': 'frozen_amount',
        'min_rate': 'min_rate',
        'interest_status': 'interest_status',
        'reinvest_left_amount': 'reinvest_left_amount',
        'create_time': 'create_time',
        'update_time': 'update_time',
    }

    def __init__(
        self,
        currency=None,
        current_amount=None,
        amount=None,
        lent_amount=None,
        frozen_amount=None,
        min_rate=None,
        interest_status=None,
        reinvest_left_amount=None,
        create_time=None,
        update_time=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (str, str, str, str, str, str, str, str, int, int, Configuration) -> None
        """UniLend - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._currency = None
        self._current_amount = None
        self._amount = None
        self._lent_amount = None
        self._frozen_amount = None
        self._min_rate = None
        self._interest_status = None
        self._reinvest_left_amount = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if currency is not None:
            self.currency = currency
        if current_amount is not None:
            self.current_amount = current_amount
        if amount is not None:
            self.amount = amount
        if lent_amount is not None:
            self.lent_amount = lent_amount
        if frozen_amount is not None:
            self.frozen_amount = frozen_amount
        if min_rate is not None:
            self.min_rate = min_rate
        if interest_status is not None:
            self.interest_status = interest_status
        if reinvest_left_amount is not None:
            self.reinvest_left_amount = reinvest_left_amount
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def currency(self):
        """Gets the currency of this UniLend.  # noqa: E501

        Currency  # noqa: E501

        :return: The currency of this UniLend.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this UniLend.

        Currency  # noqa: E501

        :param currency: The currency of this UniLend.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def current_amount(self):
        """Gets the current_amount of this UniLend.  # noqa: E501

        Current amount  # noqa: E501

        :return: The current_amount of this UniLend.  # noqa: E501
        :rtype: str
        """
        return self._current_amount

    @current_amount.setter
    def current_amount(self, current_amount):
        """Sets the current_amount of this UniLend.

        Current amount  # noqa: E501

        :param current_amount: The current_amount of this UniLend.  # noqa: E501
        :type: str
        """

        self._current_amount = current_amount

    @property
    def amount(self):
        """Gets the amount of this UniLend.  # noqa: E501

        Total amount  # noqa: E501

        :return: The amount of this UniLend.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this UniLend.

        Total amount  # noqa: E501

        :param amount: The amount of this UniLend.  # noqa: E501
        :type: str
        """

        self._amount = amount

    @property
    def lent_amount(self):
        """Gets the lent_amount of this UniLend.  # noqa: E501

        Lent amount  # noqa: E501

        :return: The lent_amount of this UniLend.  # noqa: E501
        :rtype: str
        """
        return self._lent_amount

    @lent_amount.setter
    def lent_amount(self, lent_amount):
        """Sets the lent_amount of this UniLend.

        Lent amount  # noqa: E501

        :param lent_amount: The lent_amount of this UniLend.  # noqa: E501
        :type: str
        """

        self._lent_amount = lent_amount

    @property
    def frozen_amount(self):
        """Gets the frozen_amount of this UniLend.  # noqa: E501

        Frozen amount  # noqa: E501

        :return: The frozen_amount of this UniLend.  # noqa: E501
        :rtype: str
        """
        return self._frozen_amount

    @frozen_amount.setter
    def frozen_amount(self, frozen_amount):
        """Sets the frozen_amount of this UniLend.

        Frozen amount  # noqa: E501

        :param frozen_amount: The frozen_amount of this UniLend.  # noqa: E501
        :type: str
        """

        self._frozen_amount = frozen_amount

    @property
    def min_rate(self):
        """Gets the min_rate of this UniLend.  # noqa: E501

        Minimum interest rate  # noqa: E501

        :return: The min_rate of this UniLend.  # noqa: E501
        :rtype: str
        """
        return self._min_rate

    @min_rate.setter
    def min_rate(self, min_rate):
        """Sets the min_rate of this UniLend.

        Minimum interest rate  # noqa: E501

        :param min_rate: The min_rate of this UniLend.  # noqa: E501
        :type: str
        """

        self._min_rate = min_rate

    @property
    def interest_status(self):
        """Gets the interest_status of this UniLend.  # noqa: E501

        Interest status: interest_dividend - regular dividend, interest_reinvest - interest reinvestment  # noqa: E501

        :return: The interest_status of this UniLend.  # noqa: E501
        :rtype: str
        """
        return self._interest_status

    @interest_status.setter
    def interest_status(self, interest_status):
        """Sets the interest_status of this UniLend.

        Interest status: interest_dividend - regular dividend, interest_reinvest - interest reinvestment  # noqa: E501

        :param interest_status: The interest_status of this UniLend.  # noqa: E501
        :type: str
        """

        self._interest_status = interest_status

    @property
    def reinvest_left_amount(self):
        """Gets the reinvest_left_amount of this UniLend.  # noqa: E501

        Amount not reinvested  # noqa: E501

        :return: The reinvest_left_amount of this UniLend.  # noqa: E501
        :rtype: str
        """
        return self._reinvest_left_amount

    @reinvest_left_amount.setter
    def reinvest_left_amount(self, reinvest_left_amount):
        """Sets the reinvest_left_amount of this UniLend.

        Amount not reinvested  # noqa: E501

        :param reinvest_left_amount: The reinvest_left_amount of this UniLend.  # noqa: E501
        :type: str
        """

        self._reinvest_left_amount = reinvest_left_amount

    @property
    def create_time(self):
        """Gets the create_time of this UniLend.  # noqa: E501

        Created time of the lending order  # noqa: E501

        :return: The create_time of this UniLend.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UniLend.

        Created time of the lending order  # noqa: E501

        :param create_time: The create_time of this UniLend.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this UniLend.  # noqa: E501

        Upated time of the lending order  # noqa: E501

        :return: The update_time of this UniLend.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this UniLend.

        Upated time of the lending order  # noqa: E501

        :param update_time: The update_time of this UniLend.  # noqa: E501
        :type: int
        """

        self._update_time = update_time

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
        if not isinstance(other, UniLend):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UniLend):
            return True

        return self.to_dict() != other.to_dict()
