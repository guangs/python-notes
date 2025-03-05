# Unpacking assigns

colors = ['red', 'blue', 'green', 'purple']
red, blue, *other = colors

print(red)   # red
print(blue)  # blue
print(other) # ['green', 'purple']


# 迭代

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for city in cities:
    print(city)

for index, city in enumerate(cities):
    print(f"{index} - {city}")


# index()

print(cities.index("Beijing"))


# map
# return an iterator
color_iter = map(lambda color_name: color_name.capitalize(), colors)
for c in color_iter:
    print(c)

# filter
color_iter = filter(lambda color_name: len(color_name) > 3, colors)
for c in color_iter:
    print(c)

# reduce
from functools import reduce
one_color_value = reduce(lambda x, y: f"{x}, {y}", colors)
print(one_color_value)


# List Comprehension，列表推导式

numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]
print(squares)

# unpacking
odd_numbers = [1, 3, 5]
a, b, c = odd_numbers
print(a, b, c)

# unpacking with *
odd_numbers = [1, 3, 5]
even_numbers = [2, 4, 6]

numbers = [*odd_numbers, *even_numbers]
print(numbers)

 
'''
会改变原list的方法有:
-append
-pop
-insert
-sort
-clear
-reverse
-extend
-remove

不会改变原list的方法有:
- + 运算
-map
-filter
-reduce
-copy
-index

'''