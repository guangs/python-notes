

'''
The following are examples of immutable objects:

- Numbers (int, float, bool,…)
- Strings
- Tuples
- Frozen sets


And the following are examples of mutable objects:
- Lists
- Sets
- Dictionaries
'''

# https://cloud.tencent.com/developer/article/1534815
# Python中的对象分为可散列和不可散列两种类型
# 在Python内置的对象类型中，只有那些不可变对象，比如整数、浮点数、字符串、元组等，才是可散列的

# 如果一个对象是可哈希的,那么在它的生存期内必须不可变(而且该对象需要一个哈希函数),而且可以和其他对象比较(需要比较方法).比较值相同的对象一定有相同的哈希值，即一个对象必须要包含有以下几个魔术方法：
# __eq__():用于比较两个对象是否相等
# __cmp__():用于比较两个对象的大小关系，它与__eq__只要有一个就可以了
# __hash__()：实际上就是哈希函数（散列函数），返回经过运算得到的哈希值


# __repr__和__str__的区别
# __repr__是给机器看的，__str__是给人看的
# __str__是在print的时候调用的，__repr__是在交互模式下直接输入变量调用的
# __str__ 的目的是 readable，也就是让程序员可以清楚的知道这个类是什么类型，包含了什么含义
# __repr__ 的目的是 executable，也就是其输出结果可以让让 Python 的内置函数 eval 执行
# 如果没有__str__，而有__repr__，则__str__=__repr__
# 如果没有__repr__，而有__str__，则__repr__=__str__
# 如果都没有，则打印对象的地址
# 如果只保留一个，建议保留__repr__，因为__str__是给用户看的，而__repr__是给机器看的
# >>> from datetime import date
# >>> today = date.today()
# >>> str(today)
# '2021-01-18'
# >>> repr(today)
# 'datetime.date(2021, 1, 18)'