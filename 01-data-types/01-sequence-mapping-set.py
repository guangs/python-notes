# sequence includes but not limited to: list, tuple, string, array.array, bytes, collections.deque, etc.

# sequence 实现了 __iter__, __len__, __contains__, __getitem__, __reversed__ 方法
# mapping 实现了 __iter__, __len__, __contains__, __getitem__ 方法
# set 实现了 __iter__, __len__, __contains__ 方法


# 自己实现一个sequence类Users

class Users:
    def __init__(self, user_names):
        self.user_names = user_names

    def __len__(self):
        return len(self.user_names)
    
    def __iter__(self):
        return iter(self.user_names)
    
    def __contains__(self, user_name):
        return user_name in self.user_names
    
    def __getitem__(self, index):
        return self.user_names[index]
    
    def __reversed__(self):
        return reversed(self.user_names)
    
    def __str__(self):
        return str(self.user_names)
    
    def __repr__(self):
        return f"Users({self.user_names})"


users = Users(['Alice', 'Bob', 'Charlie'])

# list comprehension
user_names = [ str(user).upper() for user in users]


# generator expression
user_names = (str(user).upper() for user in users)

# map
user_names = map(lambda user: str(user).upper(), users)

# filter
user_names = filter(lambda user: len(user) > 3, users)

# reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)

print(sum)


# 使用array.array可以节省内存空间，因为array.array只存储同一类型，而list可以存储任何类型的数据。
from array import array
scores = array('d',[60.7, 80.8, 90.9])

for score in scores:
    print(score)


# 使用collections.deque可以实现高效的插入和删除
from collections import deque
queue = deque(['Alice', 'Bob', 'Charlie'], maxlen=10)
queue.append('David')
queue.popleft()
queue.pop()
del queue[1]
print(queue)


# unpacking
odd_numbers = [1, 3, 5]
a, b, c = odd_numbers
print(a, b, c)

# unpacking with *
odd_numbers = [1, 3, 5]
even_numbers = [2, 4, 6]

numbers = [*odd_numbers, *even_numbers]
print(numbers)



# 通过基础UserList来实现一个List类Scores

from collections import UserList


class Scores(UserList):
    def __getitem__(self, index):
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        super().__setitem__(index, value)
    
    def __delitem__(self, index):
        super().__delitem__(index)

s = Scores()
s.append(1)
s.append(2)
s.pop()
print(s)




# 通过基础UserDict来实现一个mapping类PersonDict
from collections import UserDict
class PersonDict(UserDict):

    def __getitem__(self, key):
        return super().__getitem__(key)
    
    def __setitem__(self, key, value):
        super().__setitem__(key, value)
    
    def __delitem__(self, key):
        super().__delitem__(key)
    
    def __contains__(self, key):
        return super().__contains__(key)
    
    def __missing__(self, key):
        return f"{key} not found"
    

    @property
    def name(self):
        return self['name']
    
    @name.setter
    def name(self, value):
        self['name'] = value

    @property
    def age(self):
        return self['age']
    
    @age.setter
    def age(self, value):
        self['age'] = value
    

p = PersonDict()
p['name'] = 'John'
p['age'] = 25
p['contry'] = 'USA'
print(p)
p.name = 'Alice'
p.age = 23
print(p)


# mapping comprehension
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

person_upper = {key: str(value).upper() for key, value in person.items()}
print(person_upper)

# unpacking with **
odd_numbers = {1:1, 2:2, 3:3}
even_numbers = {4:4, 5:5}

numbers = {**odd_numbers, **even_numbers}
print(numbers)



def print_first_name(first_name, **kwargs):
    print(first_name)

print_first_name(**person)










# set comprehension
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = {number for number in numbers if number % 2 == 0}
print(even_numbers)
print(type(even_numbers))




# 几种sequence类型得到反序列的方法

# 字符串str
# 1. slice
s = 'hello world'
s_reversed = s[::-1] 
print(s_reversed)

# 2. reversed
# reversed 返回的是一个迭代器，需要使用join方法将迭代器转换为字符串
s_reversed = ''.join(reversed(s))
print(s_reversed)




# list
# 1. slice
l = [1, 2, 3, 4, 5]
l_reversed = l[::-1]
print(l_reversed)
# 2. reversed
# reversed 返回的是一个迭代器，需要使用list方法将迭代器转换为列表
l_reversed = list(reversed(l))
print(l_reversed)

# 3. list.reverse() 方法
# list.reverse() 方法会直接修改原列表



# tuple
# 1. slice
t = (1, 2, 3, 4, 5)
t_reversed = t[::-1]
print(t_reversed)
# 2. reversed
# reversed 返回的是一个迭代器，需要使用tuple方法将迭代器转换为元组
t_reversed = tuple(reversed(t))
print(t_reversed)




# array.array
# 1. slice
import array
a = array.array('i', [1, 2, 3, 4, 5])
a_reversed = a[::-1]
print(a_reversed)

# 2. reversed
# reversed 返回的是一个迭代器，需要使用array方法将迭代器转换为数组
a_reversed = array.array('i', reversed(a))
print(a_reversed)
# 3. array.reverse() 方法
# array.reverse() 方法会直接修改原数组




# collections.deque
from collections import deque
d = deque([1, 2, 3, 4, 5])
# 1. reversed
# reversed 返回的是一个迭代器，需要使用deque方法将迭代器转换为双端队列
d_reversed = deque(reversed(d))
print(d_reversed)
# 2. deque.reverse() 方法
# deque.reverse() 方法会直接修改原双端队列
