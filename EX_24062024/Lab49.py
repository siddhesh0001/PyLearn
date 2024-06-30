#recursion
#Key concept 1) Base case and 2) Recursion case

def factorical(a):
    if a == 0: #base case
        return 1
    else :
        return a * factorical(a-1)  #recursion case

print(factorical(5))
print(factorical(3))

#it will run the function until it reach or satasfied to the base case. 

