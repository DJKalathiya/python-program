class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self,fname,lname):
        Person.__init__(fname,lname)


p1 = Student("Darshan","kalathiya")
p1.printname()
print()
print()
