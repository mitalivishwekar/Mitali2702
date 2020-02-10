print("Welcom to the Indian Swiss")


class banking:
    def __init__(self):
        custName = input("Enter the costomer name: ")
        self.amount = 5000
        print("The amount in your A/C is 5000")

    def withdraw(self):
        self.withdraw = int(input("To be withdrawn: "))
        print("The amount you want to withdraw is :  ", self.withdraw)
        self.amount = self.amount - self.withdraw
        return self.amount

    def deposit(self):
        self.deposit = int(input("To be deposited: "))
        print("The amount you want to deposit is: ", self.deposit)
        self.amount = self.amount + self.deposit
        return self.amount

for i in range(2):
    banker = banking()
    print(banker.withdraw())
    print(banker.deposit())
