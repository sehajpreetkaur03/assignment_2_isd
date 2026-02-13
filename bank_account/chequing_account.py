"""
chequing_account.py

Defines the ChequingAccount class, which extends BankAccount.

ChequingAccount adds overdraft rules and overrides get_service_charges()
to implement Chequing-specific service charge calculations.
"""

from __future__ import annotations

from datetime import date

from bank_account.bank_account import BankAccount


class ChequingAccount(BankAccount):
    """
    Represents a chequing account.

    Attributes:
        __overdraft_limit (float): Limit before overdraft fees apply.
        __overdraft_rate (float): Rate used for overdraft fee calculation.
    """

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date,
        overdraft_limit: float,
        overdraft_rate: float,
    ) -> None:
        """
        Initializes a ChequingAccount instance with validation.

        Defaults (if conversion fails):
            overdraft_limit -> -100
            overdraft_rate -> 0.05

        Args:
            account_number (int): Account number.
            client_number (int): Client number.
            balance (float): Initial balance.
            date_created (date): Date created.
            overdraft_limit (float): Overdraft limit.
            overdraft_rate (float): Overdraft rate.
        """
        super().__init__(account_number, client_number, balance, date_created)

        # ---- overdraft_limit validation ----
        try:
            self.__overdraft_limit: float = float(overdraft_limit)
        except (TypeError, ValueError):
            self.__overdraft_limit = -100.0

        # ---- overdraft_rate validation ----
        try:
            self.__overdraft_rate: float = float(overdraft_rate)
        except (TypeError, ValueError):
            self.__overdraft_rate = 0.05

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the chequing account.

        Returns:
            str: Formatted chequing account details.
        """
        limit_str = f"${self.__overdraft_limit:,.2f}"
        rate_str = f"{self.__overdraft_rate * 100:.2f}%"
        return (
            f"{super().__str__()}\n"
            f"Overdraft Limit: {limit_str} Overdraft Rate: {rate_str} Account Type: Chequing"
        )

    def get_service_charges(self) -> float:
        """
        Calculates service charges for a ChequingAccount.

        Rules:
            If balance >= overdraft_limit -> BASE_SERVICE_CHARGE
            Else -> BASE_SERVICE_CHARGE + (overdraft_limit - balance) * overdraft_rate

        Returns:
            float: Calculated service charges.
        """
        if self.balance >= self.__overdraft_limit:
            return self.BASE_SERVICE_CHARGE

        return self.BASE_SERVICE_CHARGE + (self.__overdraft_limit - self.balance) * self.__overdraft_rate
