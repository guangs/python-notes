# https://jishuin.proginn.com/p/763bfbd2f5d0

# namedtuple很多时候是可以代替dict的，namedtuple是不可变的

from collections import namedtuple


Circle = namedtuple(
    'Circle',  # 类型的名字
    ['center_x', 'center_y', 'radius']  # 类型的属性
)

Circle = namedtuple(
    'Circle',  # 类型的名字
    'center_x center_y radius'  # 类型的属性
)

c1 = Circle(10, 20, 5)
c2 = Circle(10, 20, 5)
print(c1.center_x)
print(c1.center_y)
print(c1.radius)
print(c1 == c2)


# namedtuple 使用场景之一：函数返回多个值

# 函数返回多个值的方法有：返回tuple，返回dict，返回namedtuple
# - 返回tuple的缺点是，各个返回值是有顺序的，return a, b, c 其中a，b，c各代表什么即顺序不能乱
# - 返回dict的优点是无需记住顺序， 缺点，dict是可变数据，不能hash，而且key值不能变， return {"name":a, "age":b, "tel":c}
# - 返回namedtuple，优点是，不可变数据，无需记住顺序， return Profile(name=a, age=b, tel=c)



# 从 dict 转成 namedtuple

dict_data = {"name": "James", "age": 23, "country": "US"}

Person = namedtuple("Person", ["name", "age", "country"])

person_data = Person(**dict_data)  # 字典unpacking，解包赋值

def print_profile(name, age, country):
    print(name)
    print(age)
    print(country)

print_profile(*person_data)  # namedtupe和tuple, list 一样，也可以解包赋值，但是tuple,list加*, dict加**



# 从 namedtuple 转成 dict
person_data._asdict()  # {'name': 'James', 'age': 23, 'country': 'US'}


# 从 dict 转成 namedtuple
Person(**dict_data)  # 字典unpacking，解包赋值


# 从 namedtuple 转成 tuple
tuple(person_data) # ('James', 23, 'US')


# 从 namedtuple 转成json
import json
json.dumps(person_data._asdict())


# 用class继承定义的namedtuple
class MyPerson(Person):
    pass


mp = MyPerson(**{'name': 'Calos', 'age': 25, 'country': 'Brazil'})
print(mp.name)


# namedtuple 和 自定义class相比，优势是，你不必自己重新实现__eq__, __repr__, __init__, __hash__等方法
# namedtuple还自带 unpacking功能

