class BankAccount:
    def __init__(self, account_number):
        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        else:
            print("Deposit amount must be greater than 0.")
            return False

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be greater than 0.")
            return False

    def get_balance(self):
        return self.balance

account = BankAccount(123456789)
account.deposit(100)
account.withdraw(-110)
balance = account.get_balance()
print("Current balance:", balance)