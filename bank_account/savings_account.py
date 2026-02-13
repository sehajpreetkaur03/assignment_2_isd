"""
savings_account.py

Defines the SavingsAccount class, which extends BankAccount.

SavingsAccount adds minimum balance rules and overrides get_service_charges()
to implement Savings-specific service charge calculations.
"""

from __future__ import annotations

from datetime import date

from bank_account.bank_account import BankAccount


class SavingsAccount(BankAccount):
    """
    Represents a savings account.

    Attributes:
        SERVICE_CHARGE_PREMIUM (float): Multiplier when balance drops below minimum.
        __minimum_balance (float): Minimum balance before premium charges apply.
    """

    SERVICE_CHARGE_PREMIUM: float = 2.00

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date,
        minimum_balance: float,
    ) -> None:
        """
        Initializes a SavingsAccount instance with validation.

        Default (if conversion fails):
            minimum_balance -> 50

        Args:
            account_number (int): Account number.
            client_number (int): Client number.
            balance (float): Initial balance.
            date_created (date): Date created.
            minimum_balance (float): Minimum balance.
        """
        super().__init__(account_number, client_number, balance, date_created)

        # ---- minimum_balance validation ----
        try:
            self.__minimum_balance: float = float(minimum_balance)
        except (TypeError, ValueError):
            self.__minimum_balance = 50.0

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the savings account.

        Returns:
            str: Formatted savings account details.
        """
        min_str = f"${self.__minimum_balance:,.2f}"
        return (
            f"{super().__str__()}\n"
            f"Minimum Balance: {min_str} Account Type: Savings"
        )

    def get_service_charges(self) -> float:
        """
        Calculates service charges for a SavingsAccount.

        Returns:
            float: Calculated service charges.
        """
        if self.balance >= self.__minimum_balance:
            return self.BASE_SERVICE_CHARGE

        return self.BASE_SERVICE_CHARGE * self.SERVICE_CHARGE_PREMIUM


