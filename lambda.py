x = lambda a,b,c : a+b+c
print(x(4,5,6))
print()
print()

# use another function
def myFunction(n):
    return lambda a : a*n
myDoubler = myFunction(2) 
print(myDoubler(11))
print()
