Banking Transaction Manager
A basic Python class for managing bank accounts.


Features
Create a bank account with an account number and balance
Deposit funds into your account
Withdraw funds from your account



Usage
Create a new instance of the Bank_account class.
Call the deposit method to add funds to your account.
Call the withdraw method to remove funds from your account.


```
Running the Code:
```
Deposit and withdrawal can't be done at a time;
You withdraw by removing the # tag while calling the withdraw method.
```
class Bank_account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self):
        addition = int(input("Enter amount you want to deposit"))
        if addition >= 1:
            return self.balance + addition
        else:
            return "You must deposit an amount"
    def withdraw(self):
        subtract = int(input("Enter the amount you want to withdraw"))
        return self.balance - subtract
bank_account = Bank_account(2202574925, 25000)
bank_account.deposit()
#bank_account.withdraw()
```
