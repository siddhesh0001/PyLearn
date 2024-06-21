#2types of funtion. Built in and user defined

#build in funtion there are pre define or function which are already created by python
#like max(), min(), print(), type(), int(), etc

result = max(2,5)

#user defined function
#def is used to create our own function
#We can return something or they cannot retun
#We can have parameter or not have paramater

#No retun and no parameter
def print_message():
    print("Hello, World!")
print_message()

#No retun but have parameter
def greet(name="siddhesh"):
    print("hi",name)
greet()

#default parameter vaule

def print_message_default(name ="siddhesh"):
    print("hello", name)
print_message_default()
#it will print hello siddhesh as default value is given
print_message_default("Akshay")
#it will print akshay as value is given

# parameter and return value
def add_numbers(a, b):
    return a + b
result = add_numbers(2, 5)
print(result)
