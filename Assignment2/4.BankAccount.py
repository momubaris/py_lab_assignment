class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if self.balance<amount:
            return InsufficientFunds("Insufficient funds")
        self.balance=self.balance-amount
    def transfer(self, other_account, amount):
        if self.balance<amount:
            return InsufficientFunds("Insufficient funds")
        self.withdraw(amount)
        other_account.deposit(amount)
    def get_balance(self):
        return self.balance
account1 = BankAccount("John Doe", 1000)
account2 = BankAccount("Jane Doe", 500)
account1.deposit(100)
account2.withdraw(50)
account1.transfer(account2, 200)
print(account1.get_balance())
print(account2.get_balance()) 
