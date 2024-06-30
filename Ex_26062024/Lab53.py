#calcuation uisng class

class Calculator:

    def sum(self, a,b):
        return a + b

    def sub(self, a,b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

obj = Calculator()
output = obj.sum(10, 20)
output1 = obj.sub(10, 20)
print(output,  output1)
print(obj.mul(10, 20))