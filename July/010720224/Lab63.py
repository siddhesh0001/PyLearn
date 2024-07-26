#Polymorphism
#overriding


class shape():
    def area(self):
        return 0


class Rectangle(shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


shape1 = Rectangle(2, 3)

print(shape1.area())
shape2 = circle(2)
print(shape2.area())
