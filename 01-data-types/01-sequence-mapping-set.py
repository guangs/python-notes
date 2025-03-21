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