class InsufficientFundsError(Exception):
    pass
class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount} -> balance {self.balance}")

   
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )

        self.balance -= amount
        print(f"{self.owner} withdrew {amount} -> balance {self.balance}")


    def show(self):
        print(f"Owner: {self.owner}")
        print(f"Balance: {self.balance}")



account1 = Account("Arun", 1000)


try:
    account1.deposit(500)
    account1.withdraw(2000)

except InsufficientFundsError as error:
    print("Error:", error)

finally:
    print("Transaction finished")
