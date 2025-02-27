# https://www.pythontutorial.net/advanced-python/python-iter/
# iterator, iterable, sequence的关系是
# - iterable 范围最大，只要实现__iter__就可以
# - sequence是iterable的，而且可以用下标访问，需要实现__len__和__getitem__
# - iterator是iterable的，支持next()访问，需要实现__iter__和__next__
# - 可以用内置方法iter(iterable)或iter(sequence)来把iterable或sequence转为iterator


colors = ['red', 'green', 'blue']
colors_iter = iter(colors)
print(next(colors_iter))
print(next(colors_iter))
print(next(colors_iter))

colors_iter2 = iter(colors)
for c in colors_iter2:
    print(c)



'''

An iterator is an object that implements:

__iter__ method that returns the object itself.
__next__ method that returns the next item. If all the items have been returned, the method raises a StopIteration exception.

'''

# custom iterator

class OddIterator:

    def __init__(self, n) -> None:
        self.n = n
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= self.n:
            raise StopIteration
        self.index += 1
        return self.index*2 - 1


odds = OddIterator(5)
# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))
# print(next(odds))
for odd in odds:
    print(odd)




# 定义一个类Odds，通过利用OddIterator，使Odds成为iterable, 注意Odds不是iterator

class Odds:

    def __init__(self, n) -> None:
        self.n = n
    

    def __iter__(self):
        return OddIterator(self.n)


odds = Odds(5)
for odd in odds:
    print(odd)