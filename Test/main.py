import json

# with open("./Test/data.json", mode='r') as file:
#     mydata = json.loads(file.read())
#     mydict = dict(mydata)
#     print(mydict.keys())

mydata = {
    'name': "Alex",
    'age': 19,
    'emai': 'alex@gmail.com'
}

with open("./Test/test.json", mode="w") as file:
    serialized = json.dumps(mydata)
    file.write(serialized)
