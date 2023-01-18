class myClass:
    x = 5
p1 = myClass()
print(p1.x)
print()
print()

# __init__ function 
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = Person("Darshan",20)
print(p1.name)
print(p1.age)
print()
print()

# self parameter
class Student:
    def __init__(myclass,name,age):
        myclass.name = name
        myclass.age = age
    def myfunc(abc):
        print("My name is "+abc.name)
        
p2 = Student("Darshan", 21)
p2.myfunc()
