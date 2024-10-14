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


class UnifiedAccount(object):
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
        'user_id': 'int',
        'refresh_time': 'int',
        'locked': 'bool',
        'balances': 'dict(str, UnifiedBalance)',
        'total': 'str',
        'borrowed': 'str',
        'total_initial_margin': 'str',
        'total_margin_balance': 'str',
        'total_maintenance_margin': 'str',
        'total_initial_margin_rate': 'str',
        'total_maintenance_margin_rate': 'str',
        'total_available_margin': 'str',
        'unified_account_total': 'str',
        'unified_account_total_liab': 'str',
        'unified_account_total_equity': 'str',
        'leverage': 'str',
        'spot_order_loss': 'str',
        'spot_hedge': 'bool',
        'use_funding': 'bool',
    }

    attribute_map = {
        'user_id': 'user_id',
        'refresh_time': 'refresh_time',
        'locked': 'locked',
        'balances': 'balances',
        'total': 'total',
        'borrowed': 'borrowed',
        'total_initial_margin': 'total_initial_margin',
        'total_margin_balance': 'total_margin_balance',
        'total_maintenance_margin': 'total_maintenance_margin',
        'total_initial_margin_rate': 'total_initial_margin_rate',
        'total_maintenance_margin_rate': 'total_maintenance_margin_rate',
        'total_available_margin': 'total_available_margin',
        'unified_account_total': 'unified_account_total',
        'unified_account_total_liab': 'unified_account_total_liab',
        'unified_account_total_equity': 'unified_account_total_equity',
        'leverage': 'leverage',
        'spot_order_loss': 'spot_order_loss',
        'spot_hedge': 'spot_hedge',
        'use_funding': 'use_funding',
    }

    def __init__(
        self,
        user_id=None,
        refresh_time=None,
        locked=None,
        balances=None,
        total=None,
        borrowed=None,
        total_initial_margin=None,
        total_margin_balance=None,
        total_maintenance_margin=None,
        total_initial_margin_rate=None,
        total_maintenance_margin_rate=None,
        total_available_margin=None,
        unified_account_total=None,
        unified_account_total_liab=None,
        unified_account_total_equity=None,
        leverage=None,
        spot_order_loss=None,
        spot_hedge=None,
        use_funding=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (int, int, bool, dict(str, UnifiedBalance), str, str, str, str, str, str, str, str, str, str, str, str, str, bool, bool, Configuration) -> None
        """UnifiedAccount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_id = None
        self._refresh_time = None
        self._locked = None
        self._balances = None
        self._total = None
        self._borrowed = None
        self._total_initial_margin = None
        self._total_margin_balance = None
        self._total_maintenance_margin = None
        self._total_initial_margin_rate = None
        self._total_maintenance_margin_rate = None
        self._total_available_margin = None
        self._unified_account_total = None
        self._unified_account_total_liab = None
        self._unified_account_total_equity = None
        self._leverage = None
        self._spot_order_loss = None
        self._spot_hedge = None
        self._use_funding = None
        self.discriminator = None

        if user_id is not None:
            self.user_id = user_id
        if refresh_time is not None:
            self.refresh_time = refresh_time
        if locked is not None:
            self.locked = locked
        if balances is not None:
            self.balances = balances
        if total is not None:
            self.total = total
        if borrowed is not None:
            self.borrowed = borrowed
        if total_initial_margin is not None:
            self.total_initial_margin = total_initial_margin
        if total_margin_balance is not None:
            self.total_margin_balance = total_margin_balance
        if total_maintenance_margin is not None:
            self.total_maintenance_margin = total_maintenance_margin
        if total_initial_margin_rate is not None:
            self.total_initial_margin_rate = total_initial_margin_rate
        if total_maintenance_margin_rate is not None:
            self.total_maintenance_margin_rate = total_maintenance_margin_rate
        if total_available_margin is not None:
            self.total_available_margin = total_available_margin
        if unified_account_total is not None:
            self.unified_account_total = unified_account_total
        if unified_account_total_liab is not None:
            self.unified_account_total_liab = unified_account_total_liab
        if unified_account_total_equity is not None:
            self.unified_account_total_equity = unified_account_total_equity
        if leverage is not None:
            self.leverage = leverage
        if spot_order_loss is not None:
            self.spot_order_loss = spot_order_loss
        if spot_hedge is not None:
            self.spot_hedge = spot_hedge
        if use_funding is not None:
            self.use_funding = use_funding

    @property
    def user_id(self):
        """Gets the user_id of this UnifiedAccount.  # noqa: E501

        User ID  # noqa: E501

        :return: The user_id of this UnifiedAccount.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UnifiedAccount.

        User ID  # noqa: E501

        :param user_id: The user_id of this UnifiedAccount.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def refresh_time(self):
        """Gets the refresh_time of this UnifiedAccount.  # noqa: E501

        Time of the most recent refresh  # noqa: E501

        :return: The refresh_time of this UnifiedAccount.  # noqa: E501
        :rtype: int
        """
        return self._refresh_time

    @refresh_time.setter
    def refresh_time(self, refresh_time):
        """Sets the refresh_time of this UnifiedAccount.

        Time of the most recent refresh  # noqa: E501

        :param refresh_time: The refresh_time of this UnifiedAccount.  # noqa: E501
        :type: int
        """

        self._refresh_time = refresh_time

    @property
    def locked(self):
        """Gets the locked of this UnifiedAccount.  # noqa: E501

        Whether account is locked  # noqa: E501

        :return: The locked of this UnifiedAccount.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this UnifiedAccount.

        Whether account is locked  # noqa: E501

        :param locked: The locked of this UnifiedAccount.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def balances(self):
        """Gets the balances of this UnifiedAccount.  # noqa: E501


        :return: The balances of this UnifiedAccount.  # noqa: E501
        :rtype: dict(str, UnifiedBalance)
        """
        return self._balances

    @balances.setter
    def balances(self, balances):
        """Sets the balances of this UnifiedAccount.


        :param balances: The balances of this UnifiedAccount.  # noqa: E501
        :type: dict(str, UnifiedBalance)
        """

        self._balances = balances

    @property
    def total(self):
        """Gets the total of this UnifiedAccount.  # noqa: E501

        The total asset value in USD, calculated as the sum of the product of `(available + freeze) * price` for all currencies.  # noqa: E501

        :return: The total of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this UnifiedAccount.

        The total asset value in USD, calculated as the sum of the product of `(available + freeze) * price` for all currencies.  # noqa: E501

        :param total: The total of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._total = total

    @property
    def borrowed(self):
        """Gets the borrowed of this UnifiedAccount.  # noqa: E501

        The total borrowed amount in USD, calculated as the sum of the product of `borrowed * price` for all currencies (excluding points cards).  # noqa: E501

        :return: The borrowed of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._borrowed

    @borrowed.setter
    def borrowed(self, borrowed):
        """Sets the borrowed of this UnifiedAccount.

        The total borrowed amount in USD, calculated as the sum of the product of `borrowed * price` for all currencies (excluding points cards).  # noqa: E501

        :param borrowed: The borrowed of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._borrowed = borrowed

    @property
    def total_initial_margin(self):
        """Gets the total_initial_margin of this UnifiedAccount.  # noqa: E501

        Total initial margin  # noqa: E501

        :return: The total_initial_margin of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._total_initial_margin

    @total_initial_margin.setter
    def total_initial_margin(self, total_initial_margin):
        """Sets the total_initial_margin of this UnifiedAccount.

        Total initial margin  # noqa: E501

        :param total_initial_margin: The total_initial_margin of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._total_initial_margin = total_initial_margin

    @property
    def total_margin_balance(self):
        """Gets the total_margin_balance of this UnifiedAccount.  # noqa: E501

        Total margin balance  # noqa: E501

        :return: The total_margin_balance of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._total_margin_balance

    @total_margin_balance.setter
    def total_margin_balance(self, total_margin_balance):
        """Sets the total_margin_balance of this UnifiedAccount.

        Total margin balance  # noqa: E501

        :param total_margin_balance: The total_margin_balance of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._total_margin_balance = total_margin_balance

    @property
    def total_maintenance_margin(self):
        """Gets the total_maintenance_margin of this UnifiedAccount.  # noqa: E501

        Total maintenance margin  # noqa: E501

        :return: The total_maintenance_margin of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._total_maintenance_margin

    @total_maintenance_margin.setter
    def total_maintenance_margin(self, total_maintenance_margin):
        """Sets the total_maintenance_margin of this UnifiedAccount.

        Total maintenance margin  # noqa: E501

        :param total_maintenance_margin: The total_maintenance_margin of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._total_maintenance_margin = total_maintenance_margin

    @property
    def total_initial_margin_rate(self):
        """Gets the total_initial_margin_rate of this UnifiedAccount.  # noqa: E501

        Total initial margin rate  # noqa: E501

        :return: The total_initial_margin_rate of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._total_initial_margin_rate

    @total_initial_margin_rate.setter
    def total_initial_margin_rate(self, total_initial_margin_rate):
        """Sets the total_initial_margin_rate of this UnifiedAccount.

        Total initial margin rate  # noqa: E501

        :param total_initial_margin_rate: The total_initial_margin_rate of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._total_initial_margin_rate = total_initial_margin_rate

    @property
    def total_maintenance_margin_rate(self):
        """Gets the total_maintenance_margin_rate of this UnifiedAccount.  # noqa: E501

        Total maintenance margin rate  # noqa: E501

        :return: The total_maintenance_margin_rate of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._total_maintenance_margin_rate

    @total_maintenance_margin_rate.setter
    def total_maintenance_margin_rate(self, total_maintenance_margin_rate):
        """Sets the total_maintenance_margin_rate of this UnifiedAccount.

        Total maintenance margin rate  # noqa: E501

        :param total_maintenance_margin_rate: The total_maintenance_margin_rate of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._total_maintenance_margin_rate = total_maintenance_margin_rate

    @property
    def total_available_margin(self):
        """Gets the total_available_margin of this UnifiedAccount.  # noqa: E501

        Total available margin  # noqa: E501

        :return: The total_available_margin of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._total_available_margin

    @total_available_margin.setter
    def total_available_margin(self, total_available_margin):
        """Sets the total_available_margin of this UnifiedAccount.

        Total available margin  # noqa: E501

        :param total_available_margin: The total_available_margin of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._total_available_margin = total_available_margin

    @property
    def unified_account_total(self):
        """Gets the unified_account_total of this UnifiedAccount.  # noqa: E501

        Total amount of the portfolio margin account  # noqa: E501

        :return: The unified_account_total of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._unified_account_total

    @unified_account_total.setter
    def unified_account_total(self, unified_account_total):
        """Sets the unified_account_total of this UnifiedAccount.

        Total amount of the portfolio margin account  # noqa: E501

        :param unified_account_total: The unified_account_total of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._unified_account_total = unified_account_total

    @property
    def unified_account_total_liab(self):
        """Gets the unified_account_total_liab of this UnifiedAccount.  # noqa: E501

        Total liabilities of the portfolio margin account  # noqa: E501

        :return: The unified_account_total_liab of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._unified_account_total_liab

    @unified_account_total_liab.setter
    def unified_account_total_liab(self, unified_account_total_liab):
        """Sets the unified_account_total_liab of this UnifiedAccount.

        Total liabilities of the portfolio margin account  # noqa: E501

        :param unified_account_total_liab: The unified_account_total_liab of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._unified_account_total_liab = unified_account_total_liab

    @property
    def unified_account_total_equity(self):
        """Gets the unified_account_total_equity of this UnifiedAccount.  # noqa: E501

        Total equity of the portfolio margin account  # noqa: E501

        :return: The unified_account_total_equity of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._unified_account_total_equity

    @unified_account_total_equity.setter
    def unified_account_total_equity(self, unified_account_total_equity):
        """Sets the unified_account_total_equity of this UnifiedAccount.

        Total equity of the portfolio margin account  # noqa: E501

        :param unified_account_total_equity: The unified_account_total_equity of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._unified_account_total_equity = unified_account_total_equity

    @property
    def leverage(self):
        """Gets the leverage of this UnifiedAccount.  # noqa: E501

        Leverage  # noqa: E501

        :return: The leverage of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._leverage

    @leverage.setter
    def leverage(self, leverage):
        """Sets the leverage of this UnifiedAccount.

        Leverage  # noqa: E501

        :param leverage: The leverage of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._leverage = leverage

    @property
    def spot_order_loss(self):
        """Gets the spot_order_loss of this UnifiedAccount.  # noqa: E501

        Total order loss, in USDT  # noqa: E501

        :return: The spot_order_loss of this UnifiedAccount.  # noqa: E501
        :rtype: str
        """
        return self._spot_order_loss

    @spot_order_loss.setter
    def spot_order_loss(self, spot_order_loss):
        """Sets the spot_order_loss of this UnifiedAccount.

        Total order loss, in USDT  # noqa: E501

        :param spot_order_loss: The spot_order_loss of this UnifiedAccount.  # noqa: E501
        :type: str
        """

        self._spot_order_loss = spot_order_loss

    @property
    def spot_hedge(self):
        """Gets the spot_hedge of this UnifiedAccount.  # noqa: E501

        Spot hedging status, true - enabled, false - not enabled.  # noqa: E501

        :return: The spot_hedge of this UnifiedAccount.  # noqa: E501
        :rtype: bool
        """
        return self._spot_hedge

    @spot_hedge.setter
    def spot_hedge(self, spot_hedge):
        """Sets the spot_hedge of this UnifiedAccount.

        Spot hedging status, true - enabled, false - not enabled.  # noqa: E501

        :param spot_hedge: The spot_hedge of this UnifiedAccount.  # noqa: E501
        :type: bool
        """

        self._spot_hedge = spot_hedge

    @property
    def use_funding(self):
        """Gets the use_funding of this UnifiedAccount.  # noqa: E501

        Whether to use funds as margin  # noqa: E501

        :return: The use_funding of this UnifiedAccount.  # noqa: E501
        :rtype: bool
        """
        return self._use_funding

    @use_funding.setter
    def use_funding(self, use_funding):
        """Sets the use_funding of this UnifiedAccount.

        Whether to use funds as margin  # noqa: E501

        :param use_funding: The use_funding of this UnifiedAccount.  # noqa: E501
        :type: bool
        """

        self._use_funding = use_funding

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
        if not isinstance(other, UnifiedAccount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UnifiedAccount):
            return True

        return self.to_dict() != other.to_dict()
