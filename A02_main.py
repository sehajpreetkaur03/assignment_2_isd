"""
A program to demonstrate the use of the BankAccount subclasses.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""


# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import *
from datetime import date


# 2. Create an instance of a ChequingAccount with values of your
# choice including a balance which is below the overdraft limit.

try:
    cheq = ChequingAccount(
        account_number=1001,
        client_number=2001,
        balance=-200.00,
        date_created=date.today(),
        overdraft_limit=-100.00,
        overdraft_rate=0.05
    )
except Exception as exc:
    print("Error creating ChequingAccount:", exc)
    cheq = None


# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the
# current state of the ChequingAccount created in step 2.
if cheq is not None:
    print(cheq)
    print(f"Service Charges: ${cheq.get_service_charges():,.2f}")


# 4a. Use ChequingAccount instance created in step 2 to deposit
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the
# current state of the ChequingAccount created in step 2.
if cheq is not None:
    try:
        cheq.deposit(150.00)  
    except Exception as exc:
        print("Error depositing into ChequingAccount:", exc)

    print(cheq)
    print(f"Service Charges: ${cheq.get_service_charges():,.2f}")


print("===================================================")


# 5. Create an instance of a SavingsAccount with values of your
# choice including a balance which is above the minimum balance.
try:
    sav = SavingsAccount(
        account_number=1002,
        client_number=2002,
        balance=200.00,        
        date_created=date.today(),
        minimum_balance=50.00
    )
except Exception as exc:
    print("Error creating SavingsAccount:", exc)
    sav = None


# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.
if sav is not None:
    print(sav)
    print(f"Service Charges: ${sav.get_service_charges():,.2f}")


# 7a. Use this SavingsAccount instance created in step 5 to withdraw
# enough money from the savings account to cause the balance to fall
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the
# current state of the SavingsAccount created in step 5.
if sav is not None:
    try:
        sav.withdraw(160.00)
    except Exception as exc:
        print("Error withdrawing from SavingsAccount:", exc)

    print(sav)
    print(f"Service Charges: ${sav.get_service_charges():,.2f}")


print("===================================================")


# 8. Create an instance of an InvestmentAccount with values of your
# choice including a date created within the last 10 years.
try:
    invest_new = InvestmentAccount(
        account_number=1003,
        client_number=2003,
        balance=1000.00,
        date_created=date(2020, 1, 1), 
        management_fee=2.55
    )
except Exception as exc:
    print("Error creating InvestmentAccount (new):", exc)
    invest_new = None


# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the
# current state of the InvestmentAccount created in step 8.
if invest_new is not None:
    print(invest_new)
    print(f"Service Charges: ${invest_new.get_service_charges():,.2f}")


# 10. Create an instance of an InvestmentAccount with values of your
# choice including a date created prior to 10 years ago.
try:
    invest_old = InvestmentAccount(
        account_number=1004,
        client_number=2004,
        balance=1000.00,
        date_created=date(2010, 1, 1), 
        management_fee=2.55
    )
except Exception as exc:
    print("Error creating InvestmentAccount (old):", exc)
    invest_old = None


# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the
# current state of the InvestmentAccount created in step 10.
if invest_old is not None:
    print(invest_old)
    print(f"Service Charges: ${invest_old.get_service_charges():,.2f}")


print("===================================================")


# 12. Update the balance of each account created in steps 2, 5, 8 and 10
# by using the withdraw method of the superclass and withdrawing
# the service charges determined by each instance invoking the
# polymorphic get_service_charges method.
accounts = []
if cheq is not None:
    accounts.append(cheq)
if sav is not None:
    accounts.append(sav)
if invest_new is not None:
    accounts.append(invest_new)
if invest_old is not None:
    accounts.append(invest_old)

for acct in accounts:
    try:
        charges = acct.get_service_charges() 
        acct.withdraw(charges)              
    except Exception as exc:
        print("Error withdrawing service charges:", exc)


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
for acct in accounts:
    print(acct)
    print(f"Service Charges (now): ${acct.get_service_charges():,.2f}")
    print()
