#bank accout example

class BankAcc:

    def __init__(self):
     self.balance = 0
     self.__private_method = 100

    def public_method(self):
         print(self.__private_method())

    def deposit(self,amount):
         self.balance += amount

    def __withdraw(self,amount):
         self.balance -=amount

    def __show_balance(self):
        print("your balance is ", self.balance)

    #to access it we have to do
    def If_you_are_auth(self,flag):
        if flag:
            self.__withdraw()
        else:
            print("you are not allowed")

    def If_you_are_auth_user(self,auth,amount):
        if auth :
            self.__withdraw(amount=amount)
        else :
            print("you are not allowed")

        # in this we have make secure our data

sbi = BankAcc()
sbi.deposit(100)

sbi.If_you_are_auth(True)



