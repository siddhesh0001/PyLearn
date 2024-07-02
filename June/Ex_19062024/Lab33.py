#more lambda example

def sum_of_two(a,b):
    return a+b

print(sum_of_two(10, 20))
#or
total = sum_of_two(10, 20)
print(total)

#by using lambda
sum_of_two = lambda a,b : a+b
print(sum_of_two(11,33))