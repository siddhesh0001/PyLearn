#hierarchical inheritance
#in this we have a class (parent) and its multiple sub class (child)
#Sub class can access the property  of parent class
#but child class cannot  access the propery of another child class

class Parent():
    def BHI1(self):
        print("Parent has 1 bhk")

class Sid(Parent):
    def BHK2(self):
        print("Sid has 2 bhk")
class Sush(Parent):
    def BHK3(self):
        print("Sush has 3 bhk")
class lucky(Parent):
    def No_house(self):
        print("I have no house")

sid = Sid()
sid.BHI1()
sid.BHK2()
sush = Sush()
sush.BHI1()
sush.BHK3()
lucky = lucky()
lucky.BHI1()
lucky.No_house()
