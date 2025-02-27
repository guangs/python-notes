# lambda 表达式

triple = lambda x: x * 3
print(triple(3))


sum = lambda x, y: x + y
print(sum(2,3))


# lambda 表达式只支持一行，如果是多行语句，可以用放入数组中，但是并不建议这样做
multiline  = lambda x, y: (
    print(x),
    print(y),
    x + y
)
# 返回的其实是一个数组
print(multiline(1, 3)[2])
