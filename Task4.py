
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


class SavingsAccount(Account):

    def __init__(self, owner, balance=0, min_balance=500):
        super().__init__(owner, balance)
        self.min_balance = min_balance

  
    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise InsufficientFundsError(
                f"Insufficient funds: balance {self.balance}, requested {amount}"
            )

        self.balance -= amount
        print(f"{self.owner} withdrew {amount} -> balance {self.balance}")


priya = SavingsAccount("Priya", 1500)


try:
    priya.withdraw(1200)

except InsufficientFundsError as error:
    print("Error:", error)


try:
    priya.withdraw(800)

except InsufficientFundsError as error:
    print("Error:", error)


print(isinstance(priya, Account))

