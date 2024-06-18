#in if else we can use break, pass also
# break

for i in range(0, 10):
    print(i)
    if i == 5:
        break
print("out of box")
# in this it will print from 0 to 9
# but we added if i == 5 then it will print till 5 and then break futher number ie 6,7,8,9,
# and will print given function ie out of box

# pass

for a in range(0, 10):
    if a == 5:   # for multiple pass we can do if a ==5 or if a==6

        pass
    else:
     print(a)


#in this it will check number from 0 to 9
#if number is 1 equal to 5, no then print 1
#now i value is 2 --> it will check if 2 is equal to 5, no then print 2
#it will check till 5. If 5 is equal to 5 then it will pass and  will not print 5
#and then it will print remaining number ie 0,1,2,3,4,6,7,8,9

# for b in range (0,10) :
#     if b % 3 == 0:
#         print(b)
#     else:
#         print( b*2 )


