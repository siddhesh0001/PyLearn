#recusrion example

n = 12345
def rec_sum(n):
    # base case
    if n == 0:
        return 0
    # recursive case
    else:
        return n % 10 + rec_sum(n // 10)

print(rec_sum(n))