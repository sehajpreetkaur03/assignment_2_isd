import unittest
from datetime import date

from bank_account.chequing_account import ChequingAccount


class TestChequingAccount(unittest.TestCase):
    def test_init_invalid_date_created_defaults_today(self) -> None:
        account = ChequingAccount(1001, 2001, 0.0, "bad-date", -100, 0.05)
        # _date_created is protected, so we can check it directly
        self.assertEqual(account._date_created, date.today())

    def test_service_charge_base_when_above_limit(self) -> None:
        account = ChequingAccount(1002, 2002, -50.0, date.today(), -100, 0.05)
        self.assertEqual(round(account.get_service_charges(), 2), 0.50)

    def test_service_charge_when_below_limit(self) -> None:
        account = ChequingAccount(1003, 2003, -600.0, date.today(), -100, 0.05)
        self.assertEqual(round(account.get_service_charges(), 2), 25.50)

    def test_name_mangling_private_attr_example(self) -> None:
        account = ChequingAccount(1004, 2004, 0.0, date.today(), -100, 0.05)
        self.assertEqual(account._ChequingAccount__overdraft_limit, -100.0)
