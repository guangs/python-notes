# unpacking

colors = ("red", "white", "yellow")

c1, c2, c3 = colors
c1, c2, c3 = "red", "white", "yellow"
# c1, c2 = colors # ValueError
c1, *c2 = colors

print(c1)
print(c2)
print(c3)


# swap values of two variables

x = 10
y = 20

print(f'x={x}, y={y}')

x, y = y, x

print(f'x={x}, y={y}')



# unpacking with *
odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)

numbers = (*odd_numbers, *even_numbers)
print(numbers)
