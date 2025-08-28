class BankAccount:
    def __init__(self):
        self.balance = 0   # ✅ Instance variable, belongs to the object

    def deposit(self, amount):
        self.balance += amount   # ✅ Updates object’s balance
        print("Deposited:", amount, "Current Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrew:", amount, "Current Balance:", self.balance)
        else:
            print("Insufficient balance!")

# Test
account = BankAccount()
account.deposit(100)
account.withdraw(50)
account.deposit(200)
