# Execption Handling

# print("start")
# 10/0
# print("end")

# in this it will print start and then it will throw an error
# it will not print end because it will not execute code after error message

# example

try:
    print("start")
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = a / b
    print("The result is", c)
except Exception as e:  # it will handle error message and will give proper error message
                        # Also it will not stop the progrm and will print next code or line
    print(e)
    print("Please enter a valid number") #we can alsogive message as we want

print("end")