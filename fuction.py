def myFuction():
    print("Hello i am form function")

myFuction()
print()
print()

# refernce as arguments
def myFuction(fname):
    print(fname+ " From delhi")

myFuction("Rohan")
myFuction("Darsh")
myFuction("Darsh")
print()
print()

# arbituary arguments
def myFunction(*kids):
    print("This is kids name is " + kids[2])

myFunction("dhruv","Arvind","ANkit","jay")
print()
print()

# default parameter value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

