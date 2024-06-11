#Data type in python
#1.String,2.Integer,3.Float,4.Boolean,5.List,6.Tuple,7.Set,8.Dictionary

#We will check the type of variable using type() function

print(type("Hello World"))
print(type(10))
print(type(10.5))
print(type(True))
print(type([1,2,3]))
print(type((1, 2, 3)))

#or we can check in another way

age = 33
print(type(age))
name = "Sid"
print(type(name))

#we can use same variable for different data type. Which is not possible in other language.
#But in python it is possible.
#We can change the data type of variable.

age = 31
print(type(age))

age = "ten"
print(type(age))
