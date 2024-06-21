# a leap year is divided by 4
#but not by 100 unless it is also divided by 400
#use  and if else  staatemet

year = int(input("Enter a year: "))
#year = 2000

# year % 4 ==0 --> divided by 4
# year % 100!=0 --> Not divided by 100
# year % 400==0 --> Is divided by 400

if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a leap year")
