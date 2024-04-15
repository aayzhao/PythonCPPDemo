"""Methods for timing functions."""
import time

def time_function(func) -> float:
    start = time.time()
    for i in range(4_000_000):
        func(i)
    end = time.time()
    elapsed = end - start
    print("{name} executed in: {time} seconds".format(name = func.__name__, time = elapsed))
    return end - start

def compare_functions(func1, func2) -> None:
    func1_time = time_function(func1)
    func2_time = time_function(func2)
    if func2_time < func1_time:
        print("{name} executed faster".format(name = func2.__name__))
    elif func1_time < func2_time:
        print("{name} executed faster".format(name = func1.__name__))