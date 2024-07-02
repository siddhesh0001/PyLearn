#def example using match case

def allow_to_seat_in_class(name) :
    match name :
        case "sid" :
            print("allow to enter")
        case "akshay" :
            print("allow to enter")
        case _ :
            print("not allow to enter")
allow_to_seat_in_class("id")