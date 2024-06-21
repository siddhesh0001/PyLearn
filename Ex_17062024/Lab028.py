# *agrs
# *args means any number of arguments can be passed to the function
# def print_arguments(*args):
#     """
#     This function takes any number of arguments and prints them out.
#     """
#     for arg in args:
#         print(arg)

def print_arguments(*args):
    for i in args:
        print(i, sep= "")
print_arguments("siddhesh", 12 , "by")