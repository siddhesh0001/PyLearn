#bank accout example

class BankAcc:

    def __init__(self):
     self.balance = 0
     self.__private_method = 100

    def public_method(self):
         print(self.__private_method())

    def deposit(self,amount):
         self.balance += amount

    def withdraw(self,amount):
         self.balance -=amount

    def show_balance(self):
        print("your balance is ", self.balance)


sbi = BankAcc()
sbi.deposit(100)
sbi.show_balance()
sbi.withdraw(50)
sbi.show_balance()

# this example is poor
#Any one can see balance and withdraw my amount.
