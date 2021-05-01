"""
Implement abstract classes, static methods and multiple inheritance
A mini banking system

In a banking system the following elements exist:

    Accounts
    Current accounts
    Deposit Accounts
    Credit cards

Accounts have

    Balance
    Rate of interest
    Customer
    An ability to lodge money
    An ability to withdraw money
    An ability to send alerts to the owner via email or SMS

Current accounts have, in addition to all accounts

    An overdraft limit
    An interest rate which is always negative
    An ability to indicate how much credit is available

Deposit accounts have, in addition to all accounts

    An interest rate which is always positive

Customers have

    Name
    Address
    Email
    Phone number
    preferred method of communication

The system needs a mechanism to communicate which should be available for customers and also should be fired when an
account balance changes

Implement self scenario using abstract, static and class methods as appropriate. Use a mixin class as necessary to
implement the multiple inheritance functionality. Is there an alternative (better?) way to implement the multiple
inheritance functionality?

You should override or extend methods as appropriate. You should also indicate privacy where appropriate and use
decorators where appropriate.
"""

from abc import abstractmethod, ABCMeta
from datetime import datetime


class CommunicationMixin:
    def communicate(self, **kwargs):
        if type not in kwargs and kwargs["type"] not in ("email", "phone"):
            return False
        if kwargs["type"] == "email":
            print("Sending mail to {}...".format(kwargs["target"]))
        elif kwargs["type"] == "phone":
            print("Calling {}...".format(kwargs["target"]))


class Account(metaclass=ABCMeta):
    _interest_rate = 0.0

    @abstractmethod
    def __init__(self, customer):
        if not isinstance(customer, Customer):
            self._customer = \
                Customer.make_customer_from_string("UNKNOWN,,nobody@nowhere.com,999-9999")
        else:
            self._customer = customer
        self._balance = 0.0
        self._transaction_history = []

    def lodge(self, amount):
        if amount > 0:
            self._balance += amount
            self._transaction_history.append((datetime.now(), amount))

    def withdraw(self, amount):
        if amount > 0:
            self._balance -= amount
            self._transaction_history.append((datetime.now(), amount * -1))


    @staticmethod
    def terms_and_conditions():
        return "Some load of old nonsense"

    @property
    @classmethod
    def interest_rate(cls):
        return cls._interest_rate

    @interest_rate.setter
    @classmethod
    def interest_rate(cls, rate):
        if rate > 0.0:
            cls.interest_rate = rate

    def apply_interest(self):
        self._balance += self._balance * __class__._interest_rate

    @property
    def customer(self):
        return self._customer

    @property
    def balance(self):
        return self._balance

    @property
    def transaction_history(self):
        return self._transaction_history

class Customer(CommunicationMixin):
    _num_customers = 0
    def __init__(self, name, address, email, phone):
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone
        __class__._num_customers += 1

    def __str__(self):
        return "{},\n{},\n{},\n{}"\
            .format(self.name, self._address, self._email, self._phone)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @classmethod
    def make_customer_from_string(cls, cust_string):
        if isinstance(cust_string, str):
            try:
                split_string = cust_string.split(",")
                return cls(*split_string)
            except Exception as e:
                pass

    @property
    @classmethod
    def num_customers(cls):
        return cls._num_customers

    def communicate(self, **kwargs):
        message = kwargs["message"]
        comm_stuff = {"type": "email", "target": self, "message": message}
        super().communicate(**comm_stuff)


class CurrentAccount(Account, CommunicationMixin):
    def __init__(self, customer, overdraft_limit=0.0):
        self._overdraft_limit = overdraft_limit
        super().__init__(customer)

    def lodge(self, amount):
        super().lodge(amount)
        comm_stuff = {"type": "email", "target": self.customer, "message": "Hello"}
        self.communicate(**comm_stuff)

    def withdraw(self, amount):
        super().withdraw(amount)
        self.communicate("email", "Withdrawing...")

    def communicate(self, **kwargs):
        message = kwargs["message"]
        comm_stuff = {"type": "email", "target": self, "message": message}
        super().communicate(comm_stuff)

    @property
    def available_funds(self):
        return self.balance + self._overdraft_limit



if __name__ == "__main__":
    joe = Customer("Joe Bloggs", "", "joe@x.com", "087-999-8888")
    joe_ca = CurrentAccount(joe)

    joe.communicate(message="How's it going?")


    bad_customer = Customer.make_customer_from_string("tom smith,,tom@email.com,122-3456")
    random_account = Account()

