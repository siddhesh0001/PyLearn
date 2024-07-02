#what if we have multiple condation
#find the max bet 3 number

num1 = int(input("enter num 1"))
num2 = int(input("enter num 2"))
num3 = int(input("enter num 3"))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 >num3:
    print(num2)
else: print(num3)