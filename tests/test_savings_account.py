import unittest
from datetime import date

from bank_account.savings_account import SavingsAccount


class TestSavingsAccount(unittest.TestCase):
    def test_base_charge_when_above_minimum(self) -> None:
        account = SavingsAccount(3001, 4001, 500.0, date.today(), 50)
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)

    def test_premium_charge_when_below_minimum(self) -> None:
        account = SavingsAccount(3002, 4002, 49.99, date.today(), 50)
        self.assertEqual(round(account.get_service_charges(), 2), 1.00)

    def test_name_mangling_private_attr_example(self) -> None:
        account = SavingsAccount(3003, 4003, 0.0, date.today(), 50)
        self.assertEqual(account._SavingsAccount__minimum_balance, 50.0)
