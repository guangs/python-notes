'''
Technically, a custom sequence type needs to implement the following methods:

__getitem__ : returns an element at a given index.
__len__ : returns the length of the sequence.
'''


from functools import lru_cache



class Fibonacci:

    def __init__(self, n) -> None:
        self.n = n

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index > self.n - 1:
                raise IndexError
            return self.__fib(index)

    def __len__(self):
        return self.n

    @classmethod
    @lru_cache  # lru_cache allows you to cache the result of a function. When you pass the same argument to the function, the function just gets the result from the cache instead of recalculating it
    def __fib(cls, n):
        # print(f'Calculate Fibonacci of {n}')
        if n < 2:
            return 1
        return cls.__fib(n-1) + cls.__fib(n-2)

# for fib in Fibonacci(5):
#     print(fib)



class OddSequence:

    def __init__(self, n) -> None:
        self.n = n
    
    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index > self.n - 1:
                raise IndexError
            return self.__odd(index)

    def __odd(self, n):
        return 2*n + 1


odds = OddSequence(5)

for odd in odds:
    print(odd)