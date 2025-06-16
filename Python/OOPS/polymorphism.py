#Duck typing
'''class duck():
    def quack(self):
        print("Quack Quack")
class person():
    def quack(self):
        print("We are typing")
d = duck()
p = person()
d.quack()'''




'''class student():
    def stu(self,name):
        self.name = name
        print("Name is", self.name)
    def stu(self,roll):
        self.roll = roll
        print("Roll no. is", self.roll)
    def stu(self, age):
        self.age = age
        print("Age is", self.age)
c = student()
c.stu('72')'''




class animal():
    def speak(self):
        print("AAAAA!")
class dog(animal):
    def speak(self):
        print("Woof Woof!")
class cat(animal):
    def speak(self):
        print("Meow Meow!")
c = cat()
c.speak()



























