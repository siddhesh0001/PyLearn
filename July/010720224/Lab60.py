#inheritance
#It means we can access the properly or attribute or method of parent class in to clild class
#there are 5 types of class inheritance
#1.single inheritance
#2.multilevel inheritance
#3.hierarchical inheritance
#4.multiple inheritance
#5.hybrid inheritance

#single

class Grandparent :
    key = "abc123"
    def grandparant_method(self):
        print("I am grand parent method")

class Father(Grandparent):   #by using () and class name into it, it will inherit the class propery
    def parent_method(self):
        print("I am parent class")

son = Father()
son.grandparant_method()
son.parent_method()
print(son.key)

