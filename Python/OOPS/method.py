#instance, class and static method
'''class student():
    college = "NIET"    #class variable
    city = "Greater Noida"  #class variable

    def __init__(self):    #instance method
        self.name = input("Enter the name: ")    
        self.age = int(input("Enter the age: "))

    @classmethod  
    def college_info(cls):    #class method
        print("College Name:", cls.college)
        print("City:", cls.city)

    @staticmethod    #static method
    def average(x,y):
        av = (x+y)/2
        print(av)

s1 = student()
s1.college_info()
s1.average(20,30)'''




#__add__ method

'''num = 10
#num += 5
print(num)
num = num.__add__(5)
print(num)'''




'''x= 'RAM'
y = x.__add__('5')
print(y)'''




#__str__ method

'''y = 'RAMAYAN'
x = y.__str__
print(x)'''




'''class student():
    def __init__(self, name, age, roll):
        self.name = name
        self.age = age
        self.roll = roll
    def display(self):
        return f"{self.name}"
    def __repr__(self):
        return f"{self.age}----repr"
    def __str__(self):
        return f"{self.age}----str"

s1 = student("Arpit", 20, 1)
print(s1)'''





# define a custom class Mass, and then use the __add__ magic method to define how to add two instance of this class
#this will allow us to add masses in kg and g properly.
'''class mass:
    def __init__(self, kg = 0, g = 0):
        self.kg = kg + g//1000
        self.g = g % 1000
    def __add__(self, other):
        total_kg = self.kg + other.kg
        total_g = self.g + other.g
        if total_g >= 1000:
            total_kg = total_kg + total_g//1000
            total_g = total_g % 1000
        return mass(total_kg, total_g)
    def __repr__(self):
        return f"{self.kg}kg and {self.g}g"

m1 = mass(1/2, 1650)
m2 = mass(1/4, 500)
m3 = m1 + m2
print(m3)'''



#__add__magic method for difference of weights
'''class Mass:
    def __init__(self, kg=0, g=0):
        self.kg = kg + g//1000
        self.g = g%1000
    def __sub__(self, other):
        if self.kg >= other.kg:
            total_kg = self.kg - other.kg
            if self.g >= other.g:
                total_g = self.g - other.g
            else:
                total_kg -= 1
                self.g += 1000
                total_g = self.g - other.g
            return Mass(total_kg, total_g)
        else:
            print("Mass cannot be negative")
    def __repr__(self):
        return f"{self.kg}kg and {self.g}g"
m1 = Mass(6,200)
m2 = Mass(4,300)
m3 = m1 - m2
print(m3)'''




# define a custom class distance, and then use the __add__ magic method to define how to add two instance of this class
#this will allow us to add distances in km and m properly.








#magic method __lt__ with class:

#compare the marks (3 subject) of students
'''class xyz():
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def __gt__(self, other):
        r1 = self.m1 + self.m2 + self.m3
        r2 = other.m1 + other.m2 + other.m3
        if r1>r2:
            return True
        else:
            return False

s1 = xyz(21, 23, 43)
s2 = xyz(12, 54, 34)
if s1>s2:
    print("S1 secure high  marks")
else:
    print("S2 secure  high marks")'''




#__new__ method     #only method which is called before construct
'''class cse:
     def __new__(self):
         print("Hello New")
         self.__init__(self)
     def __init__(self):
         print("Constructor")
c = cse()'''



#object as an argument
'''class cse:
    def __init__(self,name):
        self.name = name
def display(obj):
    print(f"Name is {obj.name}")
obj = cse("Arpit")
#obj.display()
display(obj)'''









