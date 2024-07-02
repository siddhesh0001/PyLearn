class Dog:
    # This is the name of the class

    # Attributes
    name = None  # This is an attribute of the class Dog
    age = None   # We set it to None so we can change it later

    # Method
    def talk(self):
        print("Woof woof")  # 'self' refers to the instance of the class

    def show_name(self):
        print(f"My name is {self.name}")  # Prints the name of the dog

# This is a blueprint of the class Dog

abc = Dog()  # This is an object of the class Dog
abc.name = "Whisky"  # We are changing the attribute of the object
abc.talk()  # Calling the method of the object
abc.show_name()  # Calling another method to show the dog's name
