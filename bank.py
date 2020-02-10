class bank(object):
    name1 = ""
    name2 = ""
    acctno1 = 0
    acctno2 = 0
    initial_bal = 0.0
    amt1 = 0
    amt2 = 0
    amt3 = 0
    amt4 = 0

    def accept1(self):
        print("Enter name of first,Accno,Initial balance")
        self.name1 = input()
        self.acctno1 = int(input())
        self.initial_bal = float(input())
        print("Customer Details")
        print(self.name1)
        print(self.acctno1)
        print(self.initial_bal)

    def deposite1(self):
        print("Enter the amount to be Deposite by first: ")
        self.amt1 = int(input())
        self.initial_bal = self.initial_bal + self.amt1
        print("update balance is : ", self.initial_bal)

    def widthdraw(self):
        print("Enter amount to be Withdraw by first:")
        self.amt2 = int(input())
        self.initial_bal = self.initial_bal - self.amt2
        print("Updated balance is :", self.initial_bal)

    def recorrect(self):
        self.initial_bal = initial_bal + amt2 - amt1
        print("initial balance is :", self.initial_bal)

    def accept2(self):
        print("Enter name of second,Accno,Initial balance")
        self.name2 = input()
        self.acctno2 = int(input())
        print("Customer Details")
        print(self.name2)
        print(self.acctno2)
        print(self.initial_bal)

    def deposite2(self):
        print("Enter the amount to be Deposite by second: ")
        self.amt3 = int(input())
        self.initial_bal = self.initial_bal + self.amt3
        print("update balance is : ", self.initial_bal)

    def widthdraw2(self):
        print("Enter amount to be Withdraw by second:")
        self.amt4 = int(input())
        self.initial_bal = self.initial_bal - self.amt4
        print("Updated balance is : ", self.initial_bal)
b1 = bank()
b1.accept1()
b1.deposite1()
b1.widthdraw()
b1.recorrect()
b1.accept2()
b1.deposite2()
b1.widthdraw2()
