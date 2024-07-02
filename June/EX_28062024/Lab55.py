#Automation log in page example using class and object

class LoginPage:

    def __init__(self,emai,password):
        self.email = email
        self.password = password

    def login_conform(self):
        if self.password == "sid@11" and self.email == "sid@gmail.com" :
            print("login sucess")
        else:
            print("login failed")
#user input
email = input("enter your email")
password = input("enter your password")
page = LoginPage(email, password)
page.login_conform()

#by default input
sid = LoginPage("sid@gmail.in","sid11")
sid.login_conform()