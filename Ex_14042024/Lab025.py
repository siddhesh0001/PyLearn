# def example using if else condation

def allow_to_attend_class(name, password):
    if name == "sid":
        if password == "234":
            print("you are allowed")
        else:
            print("you are not allowed")


allow_to_attend_class("sid", "234")
