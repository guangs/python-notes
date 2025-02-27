

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