# loop
# Repeat a block of code multiple times
# first we will se for loop

for i in range(7):
    print(i)
    # in this it will print 0,1,2,3,4,5,6 as we know it start from 0

    # for a in range(1,7): --> Need to ask promod sir
    #     print(a)
    # # in this it will skip 0 and print 1 to 7

for i in range(1, 7,2):
    print(i)
    # in this it will print 1,3,5 as we know it start from 1 and increment by 2
    # so it will skip 2 and print 1,3,5
    # if range is (1,9,3) Then it will increment by 3
    # so it will skip 2 and print (1,4,7)
