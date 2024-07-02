# Encapsulation
# bind the data variable with the methods
# wrapping or blinding the data variable  with method
# Hide the data member by  using method only
# data member = Attributes / Class variables
# Method = Def function with in class / member function / behaviour

# there are 3 method private, protected, public
#Public and access outside the class
#private and access only inside the class, even access method is publice
#protected and access inside the class and child class

class MyClass:

 def __init__(self):
    self.name = "Sid"

 def public_method(self):
  print("This is a public method")

 def __private_method(self):
  print("This is a private method")

 def public_met(self):
  self.__private_method()


a = MyClass()
a.public_method()
a.public_met()  #this can access the private method as with in class we have access it
#a.__private_method() #it will show error as it is private class



