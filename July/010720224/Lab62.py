#Multiple Inheratance
#It means child class can access property from multiple parent class

class father():
    def father_money(self_):
        return "100"
    def home(self):
        print("This is father home")
class mother():
    def mother_money(self):
     return "1000"
     def home(self):
         print("This is mother home")

class son(father,mother):

    def home(self):
        print("This is son home")

son = son()
print(son.father_money())
print(son.mother_money())
print(son.home()) #in this def home is common in all class. If we print it will print of son class
                   #because it will take data from local variable of same class.
