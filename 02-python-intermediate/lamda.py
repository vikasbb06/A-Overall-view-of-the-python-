#lambda is one-line anonymnous function 
add10=lambda x:x+10
print(add10(9))
mult10= lambda x,y:x*y
print(mult10(5,9))
div10=lambda x,y,z:(x/y)*z
print(div10(5,4,2))
mylist=[(7,8),(1,2),(9,7),(4,5),(6,5)]
print(sorted(mylist,key=lambda x:x[1])) # sorting by second element of tuple
print(sorted(mylist,key=lambda x:x[0])) # sorting by first element of the tuple
print(sorted(mylist,key=lambda x:x[1],reverse=True))
#map function with lambda : map(fun,seq)
a=[1,2,3,4,5]
b=map(lambda x:x*2,a) # or we can use b=[x*2 for x in a]
print(list(b))
#filter function :filter(fun,seq)
c=filter(lambda x:x%2==0,a)
print(tuple(c))