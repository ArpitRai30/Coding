#WAP to form an account and write three methods for deposit, withdrawl and balance check
class acc():
    def __init__(self):
        self.bal = 0
        print("You are successfully registered")
    def depo(self):
        self.dep = int(input("Enter deposit amount"))
        self.bal += self.dep
        print("Your account balance is", self.bal)
    def withd(self):
        self.wit = int(input("Enter withdrawl amount"))
        if self.wit <= self.bal:
            self.bal -= self.wit
            print("Your account balance is", self.bal)
        else:
            print("Insufficient balance")
    def check(self):
        print(self.bal)

p = acc()
p.depo()
p.withd()
p.check()
