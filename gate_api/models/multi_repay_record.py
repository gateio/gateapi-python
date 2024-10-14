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


class MultiRepayRecord(object):
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
        'order_id': 'int',
        'record_id': 'int',
        'init_ltv': 'str',
        'before_ltv': 'str',
        'after_ltv': 'str',
        'borrow_time': 'int',
        'repay_time': 'int',
        'borrow_currencies': 'list[RepayRecordCurrency]',
        'collateral_currencies': 'list[RepayRecordCurrency]',
        'repaid_currencies': 'list[RepayRecordRepaidCurrency]',
        'total_interest_list': 'list[RepayRecordTotalInterest]',
        'left_repay_interest_list': 'list[RepayRecordLeftInterest]',
    }

    attribute_map = {
        'order_id': 'order_id',
        'record_id': 'record_id',
        'init_ltv': 'init_ltv',
        'before_ltv': 'before_ltv',
        'after_ltv': 'after_ltv',
        'borrow_time': 'borrow_time',
        'repay_time': 'repay_time',
        'borrow_currencies': 'borrow_currencies',
        'collateral_currencies': 'collateral_currencies',
        'repaid_currencies': 'repaid_currencies',
        'total_interest_list': 'total_interest_list',
        'left_repay_interest_list': 'left_repay_interest_list',
    }

    def __init__(
        self,
        order_id=None,
        record_id=None,
        init_ltv=None,
        before_ltv=None,
        after_ltv=None,
        borrow_time=None,
        repay_time=None,
        borrow_currencies=None,
        collateral_currencies=None,
        repaid_currencies=None,
        total_interest_list=None,
        left_repay_interest_list=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        # type: (int, int, str, str, str, int, int, list[RepayRecordCurrency], list[RepayRecordCurrency], list[RepayRecordRepaidCurrency], list[RepayRecordTotalInterest], list[RepayRecordLeftInterest], Configuration) -> None
        """MultiRepayRecord - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._order_id = None
        self._record_id = None
        self._init_ltv = None
        self._before_ltv = None
        self._after_ltv = None
        self._borrow_time = None
        self._repay_time = None
        self._borrow_currencies = None
        self._collateral_currencies = None
        self._repaid_currencies = None
        self._total_interest_list = None
        self._left_repay_interest_list = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if record_id is not None:
            self.record_id = record_id
        if init_ltv is not None:
            self.init_ltv = init_ltv
        if before_ltv is not None:
            self.before_ltv = before_ltv
        if after_ltv is not None:
            self.after_ltv = after_ltv
        if borrow_time is not None:
            self.borrow_time = borrow_time
        if repay_time is not None:
            self.repay_time = repay_time
        if borrow_currencies is not None:
            self.borrow_currencies = borrow_currencies
        if collateral_currencies is not None:
            self.collateral_currencies = collateral_currencies
        if repaid_currencies is not None:
            self.repaid_currencies = repaid_currencies
        if total_interest_list is not None:
            self.total_interest_list = total_interest_list
        if left_repay_interest_list is not None:
            self.left_repay_interest_list = left_repay_interest_list

    @property
    def order_id(self):
        """Gets the order_id of this MultiRepayRecord.  # noqa: E501

        Order ID  # noqa: E501

        :return: The order_id of this MultiRepayRecord.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this MultiRepayRecord.

        Order ID  # noqa: E501

        :param order_id: The order_id of this MultiRepayRecord.  # noqa: E501
        :type: int
        """

        self._order_id = order_id

    @property
    def record_id(self):
        """Gets the record_id of this MultiRepayRecord.  # noqa: E501

        Repayment record ID  # noqa: E501

        :return: The record_id of this MultiRepayRecord.  # noqa: E501
        :rtype: int
        """
        return self._record_id

    @record_id.setter
    def record_id(self, record_id):
        """Sets the record_id of this MultiRepayRecord.

        Repayment record ID  # noqa: E501

        :param record_id: The record_id of this MultiRepayRecord.  # noqa: E501
        :type: int
        """

        self._record_id = record_id

    @property
    def init_ltv(self):
        """Gets the init_ltv of this MultiRepayRecord.  # noqa: E501

        The initial collateralization rate  # noqa: E501

        :return: The init_ltv of this MultiRepayRecord.  # noqa: E501
        :rtype: str
        """
        return self._init_ltv

    @init_ltv.setter
    def init_ltv(self, init_ltv):
        """Sets the init_ltv of this MultiRepayRecord.

        The initial collateralization rate  # noqa: E501

        :param init_ltv: The init_ltv of this MultiRepayRecord.  # noqa: E501
        :type: str
        """

        self._init_ltv = init_ltv

    @property
    def before_ltv(self):
        """Gets the before_ltv of this MultiRepayRecord.  # noqa: E501

        Ltv before the operation  # noqa: E501

        :return: The before_ltv of this MultiRepayRecord.  # noqa: E501
        :rtype: str
        """
        return self._before_ltv

    @before_ltv.setter
    def before_ltv(self, before_ltv):
        """Sets the before_ltv of this MultiRepayRecord.

        Ltv before the operation  # noqa: E501

        :param before_ltv: The before_ltv of this MultiRepayRecord.  # noqa: E501
        :type: str
        """

        self._before_ltv = before_ltv

    @property
    def after_ltv(self):
        """Gets the after_ltv of this MultiRepayRecord.  # noqa: E501

        Ltv after the operation  # noqa: E501

        :return: The after_ltv of this MultiRepayRecord.  # noqa: E501
        :rtype: str
        """
        return self._after_ltv

    @after_ltv.setter
    def after_ltv(self, after_ltv):
        """Sets the after_ltv of this MultiRepayRecord.

        Ltv after the operation  # noqa: E501

        :param after_ltv: The after_ltv of this MultiRepayRecord.  # noqa: E501
        :type: str
        """

        self._after_ltv = after_ltv

    @property
    def borrow_time(self):
        """Gets the borrow_time of this MultiRepayRecord.  # noqa: E501

        Borrowing time, timestamp in seconds.  # noqa: E501

        :return: The borrow_time of this MultiRepayRecord.  # noqa: E501
        :rtype: int
        """
        return self._borrow_time

    @borrow_time.setter
    def borrow_time(self, borrow_time):
        """Sets the borrow_time of this MultiRepayRecord.

        Borrowing time, timestamp in seconds.  # noqa: E501

        :param borrow_time: The borrow_time of this MultiRepayRecord.  # noqa: E501
        :type: int
        """

        self._borrow_time = borrow_time

    @property
    def repay_time(self):
        """Gets the repay_time of this MultiRepayRecord.  # noqa: E501

        Repayment time, timestamp in seconds.  # noqa: E501

        :return: The repay_time of this MultiRepayRecord.  # noqa: E501
        :rtype: int
        """
        return self._repay_time

    @repay_time.setter
    def repay_time(self, repay_time):
        """Sets the repay_time of this MultiRepayRecord.

        Repayment time, timestamp in seconds.  # noqa: E501

        :param repay_time: The repay_time of this MultiRepayRecord.  # noqa: E501
        :type: int
        """

        self._repay_time = repay_time

    @property
    def borrow_currencies(self):
        """Gets the borrow_currencies of this MultiRepayRecord.  # noqa: E501

        List of borrowing information  # noqa: E501

        :return: The borrow_currencies of this MultiRepayRecord.  # noqa: E501
        :rtype: list[RepayRecordCurrency]
        """
        return self._borrow_currencies

    @borrow_currencies.setter
    def borrow_currencies(self, borrow_currencies):
        """Sets the borrow_currencies of this MultiRepayRecord.

        List of borrowing information  # noqa: E501

        :param borrow_currencies: The borrow_currencies of this MultiRepayRecord.  # noqa: E501
        :type: list[RepayRecordCurrency]
        """

        self._borrow_currencies = borrow_currencies

    @property
    def collateral_currencies(self):
        """Gets the collateral_currencies of this MultiRepayRecord.  # noqa: E501

        List of collateral information  # noqa: E501

        :return: The collateral_currencies of this MultiRepayRecord.  # noqa: E501
        :rtype: list[RepayRecordCurrency]
        """
        return self._collateral_currencies

    @collateral_currencies.setter
    def collateral_currencies(self, collateral_currencies):
        """Sets the collateral_currencies of this MultiRepayRecord.

        List of collateral information  # noqa: E501

        :param collateral_currencies: The collateral_currencies of this MultiRepayRecord.  # noqa: E501
        :type: list[RepayRecordCurrency]
        """

        self._collateral_currencies = collateral_currencies

    @property
    def repaid_currencies(self):
        """Gets the repaid_currencies of this MultiRepayRecord.  # noqa: E501

        Repay Currency List  # noqa: E501

        :return: The repaid_currencies of this MultiRepayRecord.  # noqa: E501
        :rtype: list[RepayRecordRepaidCurrency]
        """
        return self._repaid_currencies

    @repaid_currencies.setter
    def repaid_currencies(self, repaid_currencies):
        """Sets the repaid_currencies of this MultiRepayRecord.

        Repay Currency List  # noqa: E501

        :param repaid_currencies: The repaid_currencies of this MultiRepayRecord.  # noqa: E501
        :type: list[RepayRecordRepaidCurrency]
        """

        self._repaid_currencies = repaid_currencies

    @property
    def total_interest_list(self):
        """Gets the total_interest_list of this MultiRepayRecord.  # noqa: E501

        Total Interest List  # noqa: E501

        :return: The total_interest_list of this MultiRepayRecord.  # noqa: E501
        :rtype: list[RepayRecordTotalInterest]
        """
        return self._total_interest_list

    @total_interest_list.setter
    def total_interest_list(self, total_interest_list):
        """Sets the total_interest_list of this MultiRepayRecord.

        Total Interest List  # noqa: E501

        :param total_interest_list: The total_interest_list of this MultiRepayRecord.  # noqa: E501
        :type: list[RepayRecordTotalInterest]
        """

        self._total_interest_list = total_interest_list

    @property
    def left_repay_interest_list(self):
        """Gets the left_repay_interest_list of this MultiRepayRecord.  # noqa: E501

        List of left repay interest  # noqa: E501

        :return: The left_repay_interest_list of this MultiRepayRecord.  # noqa: E501
        :rtype: list[RepayRecordLeftInterest]
        """
        return self._left_repay_interest_list

    @left_repay_interest_list.setter
    def left_repay_interest_list(self, left_repay_interest_list):
        """Sets the left_repay_interest_list of this MultiRepayRecord.

        List of left repay interest  # noqa: E501

        :param left_repay_interest_list: The left_repay_interest_list of this MultiRepayRecord.  # noqa: E501
        :type: list[RepayRecordLeftInterest]
        """

        self._left_repay_interest_list = left_repay_interest_list

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
        if not isinstance(other, MultiRepayRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultiRepayRecord):
            return True

        return self.to_dict() != other.to_dict()