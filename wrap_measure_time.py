from timeit import default_timer as timer
import math
import time

def measure_time(func):
    def inner(*args,**kwargs):
        start = timer()

        func(*args, **kwargs)

        end = timer()

        print(f'function {func.__name__} took {round(end - start, 4)} for execution')
    return inner

@measure_time
def factorial(num):
    time.sleep(3)
    print(math.factorial(num))

factorial(10)

    