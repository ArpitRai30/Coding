'''class xyz():
    x=5
print(xyz)
x1 = xyz()
print(x1)
print(x1.x)
print(xyz.x)'''




'''class xyz():
    a = 10
    def func(self):
        return "HELLO"
obj = xyz()
print(obj.func())
print(xyz.func(obj))'''



'''class student():
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
    def display(self):
        print("Name :", self.name)
        print("Age:", self.age)

s1 = student()
s1.display()'''



#setdata and getdata
'''class student():
    def setdata(self, name, age):
        self.name = name
        self.age = age
    def getdata(self):
        print("name:",self.name)
        print("age:", self.age)

p = student()
q = student()
p.setdata("Arpit", 32)
q.setdata("Rai", 39)
p.getdata()
q.getdata()'''



#WAP to find the area and perimeter of rectangle and square using class
'''class polygon():
    def setdata(self):
        self.l = int(input("Enter length: "))
        self.b = int(input("Enter breadth: "))
    def getdata(self):
        if self.l == self.b:
            print("Given polygon is a square with")
            print("area = ", self.l**2)
            print("perimeter = ", 4* self.l)
        else:
            print("Given polygon is a rectangle with")
            print("area = ", self.l*self.b)
            print("perimeter = ", 2*(self.l+self.b))

9p = polygon()
p.setdata()
p.getdata()  ''' 
                           



#WAP that has a class Circle. Use a class variable to define the value of constant PI. Use this class variable to
#calculate area and circumference of a circle with specified radius
'''class circle():
    pi = 3.14
    def __init__(self):
        self.r = int(input("Enter Radius"))
        
    def area(self):
        print("perimeter = ", 2*circle.pi*self.r)
        print("area = ", circle.pi*self.r*self.r)

p = circle()
p.area()'''




#WAP that uses class to store the name and marks of students. Use list to store the  marks in three subjets
'''class store():
    def __init__(self):
        self.sub = input("Enter 3 subjects").split()
        self.l = input("Enter marks:").split()
        self.l = [int(i) for i in self.l]
    def show(self):
        print("subjects = ", self.sub)
        print("marks = ", self.l)

p = store()
p.show()'''
        


#WAP to store even and odd numbers in different lists
'''class even_odd():
    le = []
    lo = []
    def __init__(self):
        self.l = input("Enter list of numbers").split()
        self.l = [int(i) for i in self.l]
    def filt(self):
        for i in self.l:
            if i%2 == 0:
                even_odd.le.append(i)
            else:
                even_odd.lo.append(i)
        print("Even list=",even_odd.le)
        print("Odd list=",even_odd.lo)
                    
p = even_odd()
p.filt()'''



'''class num():
    even = []
    odd = []
    def __init__(self, n):
        self.n = n
        if n%2==0:
            num.even.append(n)
        else:
            num.odd.append(n)

a = num(24)
b = num(35)
c = num(34)
d = num(11)
e = num(31)
print(num.even)
print(num.odd)'''




#WAP to design an employee class with relevant data including salary. Also increment the salary of the employee by 10%
'''class emp():
    def __init__(self):
        self.name = input("Enter name of the employee")
        self.id = int(input("Enter ID of the employee"))
        self.sal = int(input("Enter salary of the employee"))
    def display(self):
        print("Name = ", self.name)
        print("ID = ", self.id)
        print("Salary = ", self.sal)
    def new(self):
        self.sal += 0.1 * self.sal
        print("Name = ", self.name)
        print("ID = ", self.id)
        print("Incremented Salary = ", self.sal)
p = emp()
p.display()
p.new()'''




#Write a class that stores a string and all its status details such as number of uppercase character, lowercase char,
#vowel char, consonant char, space.
'''class status():
    def __init__(self):
        self.up = 0
        self.low = 0
        self.vow = 0
        self.cons = 0
        self.sp = 0
        self.str = input("Enter string: ")
    def count(self):
        for i in self.str:
            if i.isupper():
                self.up += 1
            elif i.islower():
                self.low += 1
        for i in self.str:
            if i in 'aeiouAEIOU':
                self.vow += 1
            elif i.isalpha() and i not in 'aeiouAEIOU':
                self.cons += 1
        for i in self.str:
            if i == ' ':
                self.sp += 1
    def disp(self):
        print("Number of Uppercase Characters = ", self.up)
        print("Number of Lowercase Characters = ", self.low)
        print("Number of Vowel Characters = ", self.vow)
        print("Number of Consonant Characters = ", self.cons)
        print("Number of Space = ", self.sp)

p = status()
p.count()
p.disp()'''





'''class student():
    def __init__(self):
        print("1st constructor")
    def __init__(self):
        print("2nd constructor")
s1 = student()'''  #constructor overload is not allowed so it will output the last value



#WAP that has a class student that stores roll number, name and marks(in three sub)of the students. Display the
#information(roll number, name and total marks) stored about the student
'''class student():
    def __init__(self):
        self.n = input("Enter name of student:")
        self.r = int(input("Enter roll number:"))
        self.m1 = int(input("Enter marks in Subject 1:"))
        self.m2 = int(input("Enter marks in Subject 2:"))
        self.m3 = int(input("Enter marks in Subject 3:"))
    def disp(self):
        print("Name =", self.n)
        print("Roll Number =", self.r)
        print("Total Marks =", self.m1+self.m2+self.m3)
p = student()
p.disp()'''





#Built-in class functions

class person():
    def __init__(self):
        self.name = input("Enter the name:")
        self.age = int(input("Enter the age:"))
# create an instance of person
p1 = person()

# use getattr-- to get the value of an attribute
name = getattr(p1, "name")
print(f"Name:{name}")

# use setattr-- to set the value of an attribute
setattr(p1, "age", 22)
print(f"Updated Age: {p1.age}")

# use hasattr-- to check if an attribute exists
has_name = hasattr(p1, "name")
print(has_name)

# use delattr-- to delete an attribute
delattr(p1, "age")

has_age = hasattr(p1, "age")
print(has_age)























                                                                                                                  
