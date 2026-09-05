n = int(input("Enter number: "))

ones = ["Zero", "One", "Two", "Three", "Four", "Five",
        "Six", "Seven", "Eight", "Nine"]

teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
         "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["Zero", "Ten", "Twenty", "Thirty", "Forty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

if n == 0:
    print("Zero")

elif n < 10:
    print("{} only".format(ones[n]))

elif n < 20:
    print("{} only".format(teens[n-10]))

elif n < 100:
    c=tens[n//10], ones[n%10]
    print("{} only".format(c))

elif n < 1000:
    print(ones[n//100], "Hundred", end=" ")
    rem = n % 100
    
    if rem < 10:
        print("{} only".format(ones[rem]))
    elif rem < 20:
        print("{} only".format(teens[rem-10]))
    else:
        c=tens[rem//10], ones[rem%10]
        print("{} only".format(c))
