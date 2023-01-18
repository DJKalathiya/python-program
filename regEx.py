import re
txt = "Hello , I am form surat"
x = re.search("^Hello.*surat$",txt)
y = re.findall("portugal",txt)  #find string in all txt

if x:
    print("Yes this is match")
else:
    print("Not match")
print()

if y:
    print("Yes this is match")
else:
    print("Not match")