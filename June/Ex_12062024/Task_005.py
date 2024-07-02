# 3. Factorial
# n = 5
# 5! -->5*4*3*2*1 -> 120
# 3! -> 3*2*1 -> 6
# 4! -> 4*3*2*1 -> 24

n = 5
factorial = 1

# for i in  range (1, n+1):
#     factorial = factorial * i
# print(factorial)

#or

while n > 0 :
    factorial = factorial * n
    n = n-1
print(factorial)