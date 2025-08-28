class BankAccount:
    def deposit(self, amount):
        balance = 0   # ❌ Local variable, resets every time
        balance += amount
        print("Deposited:", amount, "Current Balance:", balance)

    def withdraw(self, amount):
        balance = 0   # ❌ Local variable, resets again
        balance -= amount
        print("Withdrew:", amount, "Current Balance:", balance)

# Test
account = BankAccount()
account.deposit(100)
account.withdraw(50)
