"""
Scenario 1: Non-Parameterized Decorator
Description: 
You're building a logging system for a web application. 
Create a decorator that logs the function name and 
execution time of any function it decorates.
"""

from time import perf_counter_ns
from typing import Callable
from functools import wraps

def logger(func:Callable):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = perf_counter_ns()
        result = func(*args,**kwargs)
        end = perf_counter_ns()
        print(f"Name:{func.__name__} --- Execution Time: {end-start} ns")
        return result
    return wrapper

@logger
def adder(x,y):
    """
    Equivalent to adder = logger(adder) 
    """
    return x+y

@logger
def subtractor(x,y):
    """
    Equivalent to subtractor = logger(subtractor) 
    """
    return x-y

print(adder(6,8))
#Output:
# Name:adder --- Execution Time: 1600 ns
#14

print(subtractor(6,8))
#Output:
# Name:subtractor --- Execution Time: 700 ns
# -2