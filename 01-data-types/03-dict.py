# A key in the key-value pair must be immutable
# for example, a number, a string, a tuple, etc


# 取值
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
# use []
print(person['first_name'])
# use get
print(person.get('last_name'))
# [] 和 get的区别之一: 如果key不存在，get不抛异常
print(person.get('address')) # None
# [] 和 get的区别之二: 如果key不存在，get可以设默认值
print(person.get('address', "China")) 



# 遍历

for key in person:
    print(key)

for key, value in person.items():
    print(f"{key} - {value}")

for value in person.values():
    print(value)


# dictionary comprehension

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

new_stocks = {key: value*2 for key, value in stocks.items() if value > 150}
print(new_stocks)


# unpacking with **
odd_numbers = {1:1, 2:2, 3:3}
even_numbers = {4:4, 5:5}

numbers = {**odd_numbers, **even_numbers}
print(numbers)