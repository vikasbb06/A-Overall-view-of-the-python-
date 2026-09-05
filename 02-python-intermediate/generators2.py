import sys
def firstn(num_given):
    nums=[]
    num=0
    while num<num_given:
        nums.append(num_given)
        num+=1
    return nums

def first_generators(num_given):
    num=0
    while num<num_given:
        yield num
        num+=1

print(sum(firstn(100)))
print(sum(first_generators(100)))

print("Generators take less memory space.That is the main advantage") if(sys.getsizeof(firstn(100000))>sys.getsizeof(first_generators(100000))) else print("Generators take more memory space than others")