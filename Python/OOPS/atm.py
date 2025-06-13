#WAP to form an account and write three methods for deposit, withdrawl and balance check
class acc():
    def __init__(self):
        self.bal = 0
        print("You are successfully registered")
    def depo(self, depo):
        self.bal += depo
        print("Amount {} is credited to your account".format(depo))
        print("Your account balance is", self.bal)
    def wit(self, wit):
        if 0 < wit <= self.bal:
            self.bal -= wit
            print("Amount {} is debited from your account".format(wit))
            print("Your account balance is", self.bal)
        else:
            print("Insufficient balance")
    def check(self):
        print("Your account balance is",self.bal)

p = acc()
while True:
    print("Choose operation from menu")
    print("1. Check balance")
    print("2. Deposit amount")
    print("3. Withdraw amount")
    print("4. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        p.check()
    elif choice == 2:
        d = int(input("Enter deposit amount:"))
        p.depo(d)
    elif choice == 3:
        w = int(input("Enter withdrawl amount:"))
        p.wit(w)
    elif choice == 4:
        break
    else:
        print("Invalid input")
