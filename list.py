from audioop import reverse


thisList = ["Darshan", "Haresh","Arvind","Ankit"]
print(thisList)
print()

#Add items in list
thisList[1] = "Savdas"
print(thisList)
print()

#insert item in list
thisList.insert(1,"Hardik")
print(thisList)
print()

# extend method
tropical = ["Ashwin", "AJit", "Naresh"]
thisList.extend(tropical)
print(thisList)
print()

# clear method
tropical.clear()
print(tropical)
print()

# If element contain H then append in new list
newlist = []

for x in thisList:
    if "d" in x:
        newlist.append(x)
print(newlist)
print()

# sort list 
newlist.sort()
print(newlist)
print()

# Reverse sorting means decending
number = [12,43,64,23,86,32]
number.sort(reverse = True)
print(number)

