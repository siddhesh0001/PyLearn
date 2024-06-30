#class and object example

class Car:
    def __init__(self,name,model, company):
        self.name =name
        self.model = model
        self.company = company

    def car_details(self):
        print("car name is " + self.name)
        print("car model is " + self.model)
        print("car company is " + self.company)

labo = Car("labo", "V2", "laborginig")
labo.car_details()  

#Also we can print if behaviour is not avalable

swift = Car("swift", "sx4", "maruti")
print("Car name is " +swift.name)
print("Model is " + swift.model)
print("Company name is " +swift.company)


