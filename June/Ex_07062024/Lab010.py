# r stands for RAW in python

text = "abc \n xyz"
print(text)
# in this abc will print on first line and xyz will print on second line
# becasue \n is reserverd data

name = r"abc \n xyz"
print(name)
# in this it will print in one line
# we used r in the beggining to tell python that it is raw data
# it will not consider \n as new line
# it will print in one line

# now lets see how to print \n in python
print("abc \n xyz")
