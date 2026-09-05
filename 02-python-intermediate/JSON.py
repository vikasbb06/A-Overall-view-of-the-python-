#json in python is also called as serilization or encoding and deserilization or decoding
import json
person={"name":"John","age":25,"city":"Sringeri","haschildren":False,"title":["engineer","developer"]}
personJSON=json.dumps(person)
print(personJSON)
#formatting
personJSON2=json.dumps(person,indent=4,sort_keys=True)
print(personJSON2)
with open("person.json","w") as f:
    json.dump(person,f,indent=4)
#deserilization:json to python object
p2=json.loads(personJSON)
print(p2)
with open("person.json","r") as f:
    p3=json.load(f)
    print(p3)