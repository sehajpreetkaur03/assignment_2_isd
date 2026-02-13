import unittest
from datetime import date

from bank_account.investment_account import InvestmentAccount


class TestInvestmentAccount(unittest.TestCase):
    def test_fee_waived_after_10_years(self) -> None:
        account = InvestmentAccount(2001, 3001, 100.0, date(2013, 1, 1), 2.00)
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)

    def test_fee_added_if_new_account(self) -> None:
        account = InvestmentAccount(2002, 3002, 100.0, date.today(), 2.00)
        self.assertEqual(round(account.get_service_charges(), 2), 2.50)

    def test_name_mangling_private_attr_example(self) -> None:
        account = InvestmentAccount(2003, 3003, 0.0, date.today(), 1.99)
        self.assertEqual(round(account._InvestmentAccount__management_fee, 2), 1.99)
