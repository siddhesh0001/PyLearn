# double the value of list
# way 1
one_list = [1, 2, 3, 4, 5]
temp_list = []
for i in one_list:
    temp_list.append(i * 2)

print(temp_list)

# way 2
new_list = [1, 2, 3, 4, 5]
def double_item(num):
    return num * 2

double_list = list(map(double_item, new_list))

print(double_list)

# way 3 using lambda function
abc_list = [1, 2, 3, 4, 5]

double_item = lambda num: num * 2
double_list = list(map(double_item, abc_list))
print(double_list)
#or
double_list = list(map(lambda num : num * 2 , abc_list))
print(double_list)

#or
print(list(map(lambda num : num*2, abc_list)))

#or
print(list(map(lambda num : num *2, [1,2,3,4,5,6])))
