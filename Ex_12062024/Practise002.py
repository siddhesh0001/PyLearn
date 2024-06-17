# write a program to calculate and display  the letter
# given the numeric score ( eg A,B ,C,D,F)
# based on the following grate scale :
# input score 89
# output B
# A:  90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59
# use if else

score = int(input("enter your score"))
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# we can write it in another way also

if score >= 90 and score <= 100:
    print("A")
    # we can also write it as elif score >= 90 and score <= 100:
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
elif score >= 0 and score <= 59:
    print("F")
else:
    print("Invalid score")
