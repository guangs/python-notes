from functools import partial

def multiply(a, b):
    return a*b

# 参数中有些是固定值，为了减少参数，可以使用偏函数
double = partial(multiply, b=2)

result = double(10)
print(result)