import time

def log_execution_time(func):
    def wrapper(timeduration):
        start = time.time()
        result = func(timeduration)
        end = time.time()
        print("Execution time of function is :",end-start)
    return wrapper

@log_execution_time
def example(timeduration):
    time.sleep(timeduration) 
    print("Function executed")

example(2)

# output :
# Function executed
# Execution time of function is : 2.001305103302002
