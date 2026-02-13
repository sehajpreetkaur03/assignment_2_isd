"""
investment_account.py

Defines the InvestmentAccount class, which extends BankAccount.

InvestmentAccount adds management fee rules and overrides get_service_charges()
to implement Investment-specific service charge calculations.
"""

from __future__ import annotations

from datetime import date, timedelta

from bank_account.bank_account import BankAccount


class InvestmentAccount(BankAccount):
    """
    Represents an investment account.

    Attributes:
        TEN_YEARS_AGO (date): Today's date minus ten years.
        __management_fee (float): Flat management fee (may be waived after 10 years).
    """

    TEN_YEARS_AGO: date = date.today() - timedelta(days=10 * 365.25)

    def __init__(
        self,
        account_number: int,
        client_number: int,
        balance: float,
        date_created: date,
        management_fee: float,
    ) -> None:
        """
        Initializes an InvestmentAccount instance with validation.

        Default (if conversion fails):
            management_fee -> 2.55

        Args:
            account_number (int): Account number.
            client_number (int): Client number.
            balance (float): Initial balance.
            date_created (date): Date created.
            management_fee (float): Management fee.
        """
        super().__init__(account_number, client_number, balance, date_created)

        # ---- management_fee validation ----
        try:
            self.__management_fee: float = float(management_fee)
        except (TypeError, ValueError):
            self.__management_fee = 2.55

    def __str__(self) -> str:
        """
        Returns a formatted string representation of the investment account.

        If account is more than 10 years old, management fee is waived.

        Returns:
            str: Formatted investment account details.
        """
        if self._date_created <= self.TEN_YEARS_AGO:
            fee_str = "Waived"
        else:
            fee_str = f"${self.__management_fee:,.2f}"

        return (
            f"{super().__str__()}\n"
            f"Date Created: {self._date_created} Management Fee: {fee_str} Account Type: Investment"
        )

    def get_service_charges(self) -> float:
        """
        Calculates service charges for an InvestmentAccount.

        Rules:
            If date_created is more than 10 years ago -> BASE_SERVICE_CHARGE
            Else -> BASE_SERVICE_CHARGE + management_fee

        Returns:
            float: Calculated service charges.
        """
        if self._date_created <= self.TEN_YEARS_AGO:
            return self.BASE_SERVICE_CHARGE

        return self.BASE_SERVICE_CHARGE + self.__management_fee
