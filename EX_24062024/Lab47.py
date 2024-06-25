#filters in python
#Filter is built in function in python
#it help to you to filter element from list, tupleor set

number = [1,2,3,4,5,6,7,8,9,10]

#now filter even number from it

def is_even_no(num) :
    return num % 2 ==0

even_number = filter(is_even_no, number)
print(list(even_number))
#print(list(filter(lambda num : num % 2 ==0, number))) --> In one line we can write

def no_greater_5(abc):
    return abc>5

number_greater_5 = filter(no_greater_5, number)
print(list(number_greater_5))