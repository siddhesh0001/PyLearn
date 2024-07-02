#global variable

a = 10

def something():
    print(a)

something()
# a = 10. we have define before the functions and it is globally declared
#so in function if we call a then it will print the value of it

b = 20
def new():
    b = 30
    print(b)
new()
#now we have define b inside the function and outside the function
#it will print b = 30 cause  b is locally declared and it is within the function
#if we print b out side the function then it will print b = 20
#cause when we call b outside the function then it will call the global variable