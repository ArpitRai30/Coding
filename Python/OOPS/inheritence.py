#single inheritence
'''class A():
    def __init__(self):
        print("Parent class consructor")
    def display1(self):
        print("Parent class method")
class B(A):
    def __init__(self):
        print("Child class constructor")
    def display(self):
        print("Child class method")
obj = B()
obj.display()    #if the method is found in child class then it will not search in parent class
obj.display1()

obj1 = A()
obj1.display1()
#obj1.display()'''    #this will raise error because we cannot access child class attribute through parent class 





'''class father():
    money = 1000
    def show(self):
        print("Parent class method")
    @classmethod
    def moneyshow(cls):
        print("Money:", cls.money)
class son(father):
    def son_show(self):
        print("Son class method")
s = son()
s.show()
s.son_show()
s.moneyshow()'''





#with constructor
'''class parent():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("Name:", self.name)
        print("Age:", self.age)
class child(parent):
    def __init__(self,name,age):
        print("Child class constructor")
s1 = child('Arpit', 11) '''   #when both class have constructors then the constructor of child class will be executed





'''class parent():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("{} is {} years old".format(self.name, self.age))
class child(parent):
    def __init__(self,name,age):
        super().__init__(name,age)
        print("Child class constructor")
s = child("Arpit", 21)'''





#Write a parent class name Rectangle, declare two method named area and perimeter. Use these methods in child class
#named square

'''class rectangle():
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        self.area = self.l * self.b
        print("Area:", self.area)
    def perimeter(self):
        self.peri = 2 * (self.l + self.b)
        print("Perimeter:", self.peri)
class square(rectangle):
    def __init__(self,l):
        super().__init__(l,l)
        super().area()
        super().perimeter()
p = square(6)
#p.area()'''





#WAP to create class Employee. Display the personal information and salary details of 5 employees using single
#inheritence
'''class employee():
    name = []
    ID = []
    sal = []
    def __init__(self):
        for i in range(0,5):
            self.n = input("Enter Employee Name:")
            employee.name.append(self.n)
            self.id = input("Enter Employee ID:")
            employee.ID.append(self.id)
            self.salary = int(input("Enter Employee Salary"))
            employee.sal.append(self.salary)
    def disp(self):
        for i in range(0,5):
            print("Name:",employee.name[i])
            print("ID:",employee.ID[i])
            print("Salary:",employee.sal[i])
class emp_detail(employee):
    def __init__(self):
        super().__init__()
        super().disp()
s = emp_detail()'''

                    #OR

'''class employee():
    def __init__(self,name,age,emp_id,salary):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.salary = salary
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("ID:", self.emp_id)
        print("Salary:", self.salary)
class employee_details(employee):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age,emp_id,salary)
        super().display()
n=[]
a=[]
empid=[]
s=[]
for i in range(1,6):
    name = input(f"Enter Employee {i} Name:")
    n.append(name)
    age = input(f"Enter Employee {i} Age:")
    a.append(age)
    id_ = input(f"Enter Employee {i} ID:")
    empid.append(id_)
    sal = input(f"Enter Employee {i} Salary:")
    s.append(sal)
print("Employee detais")
for i in range(0,5):
    employee_details(n[i],a[i],empid[i],s[i])
    print()'''





#WAP that has a class polygon. Derive two class rectangle and triangle from polygon and write methods to get the 
#details of their dimansions and hence calculate the area
'''class polygon():
    def __init__(self,sides):
        self.sides = sides
    def dimensions(self):
        dimensions = []
        for i in range(self.sides):
            dimension = float(input(f"Enter dimension of sides:"))
            dimensions.append(dimension)
        return dimensions
class triangle(polygon):
    def __init__(self):
        super().__init__(3)
        #super().dimensions()
    def area(self):
        dimensions = self.dimensions()
        b, h = dimensions[0], dimensions[1]
        area = 0.5 * b * h
        print("Area:", area)

r = triangle()
r.area()'''






#MRO (Method Resolution Order)
'''class A():
    pass
class B():
    pass
class C(A):
    pass
class D(B):
    pass
class E(C,D):
    pass
for i in E.mro():
    print(i)'''




'''class x:
    pass
class y:
    pass
class z:
    pass
class A(x,y):
    pass
class B(y,z):
    pass
class D(A,B,z):
    pass
for i in D.mro():
    print(i)'''






#Define a class complexnumber with instance variable real and imaginery. Create a function add_complex_numbers
#that takes two complex number objects as arguments and return a new complex number objects representing their sum
'''class complexnumber():
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __str__(self):
        return f"{self.real} + {self.imag}i"
def add_complex_number(num1, num2):
    r = num1.real + num2.real
    i = num1.imag + num2.imag
    return complexnumber(r, i)

n1 = input("Enter 1st complex number:").split("+")
n1 = [int(i) for i in n1]
n2 = input("Enter 2nd complex number:").split("+")
n2 = [int(i) for i in n2]
#n3 = int(input("Enter real part of 2nd number:"))
#n4 = int(input("Enter imaginery part of 2nd number:"))

c1 = complexnumber(n1[0], n1[1])
c2 = complexnumber(n2[0], n2[1])
res = add_complex_number(c1, c2)
print(res)'''
        






































