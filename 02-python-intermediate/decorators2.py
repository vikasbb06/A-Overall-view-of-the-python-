import functools
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func) #this is use dto preserve the meta-data
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result=func(*args,**kwargs)
            return result
        return wrapper 
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello! {name}")

print(greet("Vikas Bhat"))
