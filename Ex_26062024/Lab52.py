#constructore
class Dog:
    name = None
    id = None

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age  # age will get print even not mention its attribute. Cause in constructore we mention


    def talk(self):
        print("Bow bow")

# Creating objects
dog1 = Dog("Whisky", 1, 3)
dog2 = Dog("Rocky", 2, 4)
dog = Dog("Tom", 3,12)

print(dog1.name, dog1.id, dog1.age)
print(dog2.name, dog2.id, dog2.age)
print(dog.name, dog.id, dog.age)
print(f'{dog1.name} has age {dog1.age}')
