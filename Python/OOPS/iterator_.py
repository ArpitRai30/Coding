#ITERATOR

#return an iterator from a list
'''x = ['apple', 'aam', 'kiwi']
y = iter(x)
print(type(y))
print(next(y))
print(next(y))
print(next(y))'''


#return an iterator from a tuple
'''a = ('apple', 'aam', 'kiwi')
b = iter(a)
print(type(b))
print(next(b))
print(next(b))
print(next(b))'''


#return an iterator from a string
'''p = 'Ram'
q = iter(p)
print(type(q))
print(next(q))
print(next(q))
print(next(q))'''




'''x = ('aam', 'tarbooj', 'chiku', 'santra')
for i in x:
    print(i)
y = iter(x)
print(next(y))
print(next(y))
print(next(y))
print(next(y))'''




'''print(dir(int))
#create an iterator that returns numbers starting from 1, and each sequence will increase

class xyz():
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        x = self.a
        self.a += 1
        return x
obj = xyz()
print(type(obj))
myiter = iter(obj)
print(type(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))'''




#GENEATORS
'''
def xyz():
    i = 1
    while (i<=10):
        yield
        i
        i += 1
for i in xyz():
    print(i)
print(type(xyz()))
'''



'''
def square(num):
    for i in range(10):
        yield i**2
sq = square(10)
print(type(sq))
print(next(sq))
print(next(sq))
print(next(sq))
'''



'''
def xyz(x):
    while x>0:
        if x % 2 == 0:
            yield "Even"
        else:
            yield "Odd"
        x -= 1
for i in xyz(8):
    print(i)
'''




# WAP for all print all prime numbers from 5 to 50 using a generator.
'''
def prim(x,y):
    for i in range(x,y):
        s=0
        for j in range(2,i):
            if i%j == 0: 
                s = 1
        if s==0:
            yield i
                         
x = int(input("Enter start num:"))
y = int(input("Enter end num:"))
for k in prim(x,y):
    print(k)
'''



#WAP to create a generator that starts counting 0 and raise an exception when counter is equal to 10
'''
def counting():
    counter = 0
    while True:
        if counter == 10:
            raise StopIteration("Counter is 10")
        yield counter
        counter += 1
count = counting()
try:
    for counter in count:
        print(counter)
except StopIteration as e:
    print(e)
'''




#WAP to create a generator to print the fibonacci series
'''
def fib(n):
    x,y = 0,1
    for i in range(n):
        x,y = y,x+y
        yield x
n = int(input("Enter n:"))
for i in fib(n):
    print(i)
print(next(fib(10)))
'''



#WAP to print all character of the passed string in reverse order
'''
def rev(s):
    yield s[::-1]
s = input("Enter string:")
for i in rev(s):
    print(i)
'''
















