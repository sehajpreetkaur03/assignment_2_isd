"""
bank_account package initialization.

Allows importing all bank_account classes using:
from bank_account import *
"""

from bank_account.bank_account import BankAccount
from bank_account.chequing_account import ChequingAccount
from bank_account.investment_account import InvestmentAccount
from bank_account.savings_account import SavingsAccount

__all__ = [
    "BankAccount",
    "ChequingAccount",
    "InvestmentAccount",
    "SavingsAccount",
]
