'''from functools import reduce
a = [2, 3, 4, 5, 6]
b = reduce((lambda x,y: x+y), a)
print(b)'''



#choose the odd numbers for the list, find the cube of each element and calculate the sum of list
'''from functools import reduce
a = []
for i in range(1,21):
    a.append(i)
print(a)
b=list(filter(lambda x: x %2 !=0, a))
print(b)
c= list(map(lambda x: x**3, b))
print(c)
s = reduce((lambda x,y: x+y), a)
print(s)'''



'''def xyz(x):
    def pqr():
        print(x)
    pqr()
xyz(7)'''



# closure function

'''def outerfun(x):
    def innerfun():
        print(x)
    return innerfun
myfun = outerfun(7)
myfun()'''



'''def xyz():
    count = 0  #enclosing variable
    def pqr():
        nonlocal count  #this allows to modify the value of enclosing variable
        count += 1
        return count
    return xyz
x1 = xyz()
x2 = xyz()
print(x1())
print(x1())
print(x2())'''




#DECORATOR

'''def decor(func):
    def inner():
        print("----------------")
        func()
        print("----------------")
    return inner
@decor
def xyz():
    print("Hello Python")

xyz()'''



'''def mydecor(greet):
    def inner():
        greet()
        print("How are you?")
    return inner
@mydecor
def greet():
    print("Hello!")

greet()'''



'''def decor(num):
    def inner():
        a = num()
        add = a+10
        return add
    return inner
@decor
def num():
    return 10
print(num())'''



'''def hello(name):
    def inner():
        b = name()
        return 'Hello ' + b
    return inner

def uppercase(name):
    def inner():
        a = name()
        return a.upper()
    return inner

@hello
@uppercase
def name():
    return "arpit rai"
print(name())'''



#the output of the program will depend on the time. If the current time is day time then it will give the output
#playing music
'''from datetime import datetime
def condition(music):
    def inner():
        if 10 <= datetime.now().hour < 22:
            music()
        else:
            print("BAnd KAr Bhai")
    return inner

@condition
def music():
    print("Playing music")
music()'''



#write a function of addition of two numbers
'''def add_other(ad):
    def inner(x,y):
        s = ad(x,y)
        z = int(input("Enter 3rd num:"))
        return s+z
    return inner
@add_other
def ad(a,b):
    return a+b

x = int(input("Enter 1st num:"))
y = int(input("Enter 2nd num:"))
print(ad(x,y))'''




#add two numbers by taking input from user
'''import math
def dec(add):
    def inner():
        s = add()
        return f"factorial of sum is {math.factorial(s)}"
    return inner
@dec
def add():
    a = int(input("Enter 1st num:"))
    b = int(input("Enter 2nd num:"))
    print("Sum =", a+b)
    return a+b

print(add())'''







