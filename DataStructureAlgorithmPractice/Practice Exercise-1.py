class Account:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance

    def display(self):
        print("Name:",self.name,"|","Current Balance:",self.balance)
    
    def withdraw(self,amount):
        if self.balance==0:
            print(("{0} Your account has no balance").format(self.name))
        if amount > self.balance and self.balance!=0:
            print(("{0} You have RS.{1} in your account, cannot withdraw RS.{2}").format(self.name,self.balance,amount))
        if amount < self.balance and self.balance!=0:
            self.balance-=amount
            print(self.name,"Withdrawn:",self.balance)

    def deposit(self,amount):
        self.balance+=amount
        print(self.name,"Deposited:",self.balance)

a1=Account("Bob",0)
a2=Account("Alice",0)
a1.display()
a1.withdraw(200)
a2.display()
a1.deposit(500)
a2.deposit(800)
a1.display()
a2.display()
a1.withdraw(200)
a1.display()
a2.withdraw(400)
a2.display()
a2.withdraw(600)