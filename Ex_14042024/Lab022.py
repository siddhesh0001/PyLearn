#switch case
#in python it also called match case
#imp in api automation

number =  int(input("enter the number "))
match number :
    case 1 :
        print("your number is 1")
    case 2 :
        print("your number is 2")
    case 3 :
        print("your number is 3")
    case 4 :
        print("your number is 4")
    case _ :
        print("not a valid number")
