# generator, 函数中至少有一个yield，yield的作用是保存上下文，返回，然后从上次保存的位置继续执行
# generator 是一种iterator


def greeting():
    print('Hi!')
    yield 1
    print('How are you?')
    yield 2
    print('Are you there?')
    yield 3

# messenger = greeting()
# print(next(messenger))
# print(next(messenger))
# print(next(messenger))



# Using Python generators to create iterators

def odd_generator(n):
    for i in range(n):
        yield 2 * i + 1

# 注意：odd_generator 是生成器，生成器也是一种迭代器，支持next操作

for odd in odd_generator(5):
    print(odd)

odds = odd_generator(5)
print(next(odds))
print(next(odds))

# 注意：这种方式Odds不是生成器，生成器是函数，但是Odds是iterable
class Odds:

    def __init__(self, n) -> None:
        self.n = n
    

    def __iter__(self):
        for i in range(self.n):
            yield 2 * i + 1

for odd in Odds(5):
    print(odd)

# odds = Odds(5)
# print(next(odds))  # TypeError: 'Odds' object is not an iterator






# generator expression, 生成器表达式

# 注意：generator expression和list comprehension有点像，但是注意：用小括号
squares = (n** 2 for n in range(5) if n > 1)

for sq in squares:
    print(sq)