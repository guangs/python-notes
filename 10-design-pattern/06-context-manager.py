'''
https://www.pythontutorial.net/advanced-python/python-context-managers/

The context manager protocol has the following methods:

__enter__() - setup the context and optionally return some object
__exit__() - cleanup the object.

If you want a class to support the context manager protocol, you need to implement these two methods.

'''

'''
In the __enter__() method, you can carry the necessary steps to setup the context.
Optionally, you can returns an object from the __enter__() method.
'''

'''
The __exit__() method accepts three arguments: exception type, exception value, and traceback object. 
All of these arguments will be None if no exception occurs.

The __exit__() method returns a boolean value, either True or False.

If the return value is True, Python will make any exception silent. Otherwise, it doesnt silence the exception.
'''


from time import perf_counter

#  自定义一个context manager，用来计算从开始到结束所经历的时间
class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False

def fibonacci(n):
    f1 = 1
    f2 = 1
    for i in range(n-1):
        f1, f2 = f2, f1 + f2

    return f1


with Timer() as timer:
    for _ in range(1, 100000):
        fibonacci(1000)

print(timer.elapsed)
