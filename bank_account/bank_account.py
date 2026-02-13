"""
bank_account.py

Defines the BankAccount class, which represents a client bank account.

The class enforces validation, encapsulates account data, and provides
controlled methods for updating the account balance.

In Assignment 2, BankAccount becomes an abstract superclass and adds
a protected date_created attribute used by subclasses.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date


class BankAccount(ABC):
    """
    Represents a bank account.

    Attributes:
        BASE_SERVICE_CHARGE (float): Flat base service charge ($0.50).
        _account_number (int): Unique identifier for the bank account.
        _client_number (int): Identifier for the account holder.
        _balance (float): Current account balance.
        _date_created (date): Date the account was created (protected).
    """

    BASE_SERVICE_CHARGE: float = 0.50

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date,
    ) -> None:
        """
        Initializes a BankAccount instance with validation.

        Args:
            account_number (int): The bank account number.
            client_number (int): The client number associated with the account.
            balance (float): The initial account balance.
            date_created (date): The date the account was created.

        Raises:
            ValueError: If account_number is not numeric.
            ValueError: If client_number is not numeric.
        """
        # ---- account_number validation ----
        try:
            self._account_number: int = int(account_number)
        except (TypeError, ValueError) as exc:
            raise ValueError("Account number must be an integer.") from exc

        # ---- client_number validation ----
        try:
            self._client_number: int = int(client_number)
        except (TypeError, ValueError) as exc:
            raise ValueError("Client number must be an integer.") from exc

        # ---- balance validation ----
        try:
            self._balance: float = float(balance)
        except (TypeError, ValueError):
            self._balance = 0.0

        # ---- date_created validation (Assignment 2 requirement) ----
        if isinstance(date_created, date):
            self._date_created: date = date_created
        else:
            self._date_created = date.today()

    # ---- Accessors (properties) ----
    @property
    def account_number(self) -> int:
        """
        Returns the account number.

        Returns:
            int: The account number.
        """
        return self._account_number

    @property
    def client_number(self) -> int:
        """
        Returns the client number.

        Returns:
            int: The client number.
        """
        return self._client_number

    @property
    def balance(self) -> float:
        """
        Returns the current account balance.

        Returns:
            float: The account balance.
        """
        return self._balance

    # ---- Balance update helper ----
    def update_balance(self, amount: float) -> None:
        """
        Updates the account balance by adding the given amount.

        The amount may be positive or negative. If the value cannot be
        converted to a float, the balance remains unchanged.

        Args:
            amount (float): The amount to add to the balance.
        """
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            return

        self._balance += amount

    # ---- Deposit ----
    def deposit(self, amount: float) -> None:
        """
        Deposits a positive numeric amount into the account.

        Args:
            amount (float): The deposit amount.

        Raises:
            ValueError: If the amount is not numeric.
            ValueError: If the amount is not positive.
        """
        try:
            amount = float(amount)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Deposit amount: {amount} must be numeric.") from exc

        if amount <= 0:
            formatted_amount = f"${amount:,.2f}"
            raise ValueError(f"Deposit amount: {formatted_amount} must be positive.")

        self.update_balance(amount)

    # ---- Withdraw ----
    def withdraw(self, amount: float) -> None:
        """
        Withdraws a positive amount from the account.

        Args:
            amount (float): The withdrawal amount.

        Raises:
            ValueError: If the amount is not numeric.
            ValueError: If the amount is not positive.
            ValueError: If the amount exceeds the current balance.
        """
        try:
            amount = float(amount)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Withdraw amount: {amount} must be numeric.") from exc

        if amount <= 0:
            formatted_amount = f"${amount:,.2f}"
            raise ValueError(f"Withdraw amount: {formatted_amount} must be positive.")

        if amount > self._balance:
            formatted_amount = f"${amount:,.2f}"
            raise ValueError(f"Withdraw amount: {formatted_amount} exceeds balance.")

        self.update_balance(-amount)

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the bank account.

        Returns:
            str: Formatted account details.
        """
        return f"Account Number: {self._account_number} Balance: ${self._balance:,.2f}"

    @abstractmethod
    def get_service_charges(self) -> float:
        """
        Returns the calculated service charges for the bank account.

        Each subclass must implement its own service charge rules.

        Returns:
            float: The service charges.
        """
        raise NotImplementedError
