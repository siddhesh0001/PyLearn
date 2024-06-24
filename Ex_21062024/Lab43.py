import time

def mydecoration(Funct):
    def wrapper():
        start_time = time.time()
        Funct()
        end_time = time.time()
        print("Time taken: " + str(end_time - start_time))
    return wrapper

@mydecoration
def myfunction():
    time.sleep(5)
   
# Call the decorated function
myfunction()
