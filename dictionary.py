thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
print(thisdict)
print()

# change (add color keys)
thisdict["color"] = "white"
print(thisdict)
print()

# print all va;ue of keys
for x in thisdict:
    print(thisdict[x])
print()

# copy of dict
newCopy = thisdict.copy()
print(newCopy)
print()
