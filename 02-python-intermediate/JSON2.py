import json
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user=User("John",25)
# as the object of the class is not directly json-serilizable, need for the user defined encoder
def user_encoder(obj): # or we can use the json.JSONEncoder class to do the same 
    if isinstance(obj,User):
        return {"name":obj.name,"age":obj.age}
    else:
        raise TypeError("Object of the type USer is not json serilizable")

userjson=json.dumps(user,default=user_encoder) # for this encoding should be done,as object is not json-serilizable 
print("Encoded:",userjson)
# for decoding 
def user_decoder(dct):
    if "name" in dct and "age" in dct:
        return User(name=dct["name"],age=dct["age"])
    return dct
user=json.loads(userjson,object_hook=user_decoder)
print("Decoded:",user)
print("Decoded:",user.name)