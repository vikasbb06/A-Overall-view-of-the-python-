numbers={}
str=input("Enter the number string:")
str=str.lower().split() #split makes the differnce  
for i in str:
    if i in numbers:
        numbers[i] = numbers.get(i, 0)
        numbers[i] += 1
    else:
        numbers[i]=1 

print("The frequency of the characters in the string is:")
for digit in sorted(numbers.keys()):
    print(f" characters '{digit}' appears {numbers[digit]} times")
sorted_num=sorted(numbers.items(),key=lambda x:x[1],reverse=True)
print("----Top 3 is----")
for i in sorted_num[:3]: #range(min(3, len(sorted_num))):
    print(f"'{i[0]}' appears {i[1]} times")
 