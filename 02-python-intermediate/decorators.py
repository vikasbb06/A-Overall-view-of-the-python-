import functools
def my_decorator(func):
    @functools.wraps(func) #this is used to preserve the meta-data
    def wrapper(*args, **kwargs): # *args and **kwargs are the parametres of the decorates
        print("Something is happening is before the function is called")
        result=func(*args,**kwargs)
        print("Something is happening after the function is called")
        return result
    return wrapper
@my_decorator
def say_hello(name):
    print("Hello!", name)
    

print(say_hello("Vikas Bhat"))
print(help(say_hello)) #this will give the meta-data of the function
print(say_hello.__name__) #this will give the name of the function