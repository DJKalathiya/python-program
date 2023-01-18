# convert json to perse 
import json

x = '{"name":"Darshan","age":21,"city":"surat"}'

y = json.loads(x)

print(y["age"])
print()
print()

# convet python object to json string
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)
print(y)

# This code is not run in this, why i can't find is sorry
