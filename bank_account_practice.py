class BankAccount:
    def __init__(self, deposit):
        self.total = deposit

    def current_balance(self):
        return self.total

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount > self.total:
            print("you do not have enough money!")
        else:
            self.total -= withdrawal_amount

    def deposit(self, deposit_amount):
        self.total += deposit_amount




prashantAcc = BankAccount(100)
print(prashantAcc.current_balance())
prashantAcc.withdraw(20)
print(prashantAcc.current_balance())
prashantAcc.withdraw(1000)

meeraAcc = BankAccount(1000000)
print(meeraAcc.current_balance())
meeraAcc.withdraw(900)
print(meeraAcc.current_balance())
meeraAcc.withdraw(20000000)
