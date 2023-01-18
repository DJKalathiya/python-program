mytuple = ("Darshan", "Ankit", "Jay", "Sanjay","Hardik")
print(len(mytuple))
print(mytuple)
print()

print(mytuple[-4:-1])
print()

# Add tuple into previos tuple
addtuple = ("Yash",)
mytuple += addtuple
print(mytuple)
print()

# Print all item refering to index
for i in range(len(mytuple)):
    print(mytuple[i])
print()
