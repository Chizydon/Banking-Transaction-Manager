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
bank_account.withdraw()