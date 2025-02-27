#  while else中 else的作用

people = [{'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'Peter', 'age': 30},
        {'name': 'Jenifer', 'age': 28}]

name = input('Enter a name:')

# while 没有else
index = 0

found = False

while index < len(people):
    if people[index]["name"] == name:
        found = True
        print(people[index])
        break
    index += 1
if not found:
    print(f'{name} not found!')


# while else
index = 0

while index < len(people):
    if people[index]["name"] == name:
        print(people[index])
        break
    index += 1
else:
    print(f'{name} not found!')



# Python doesn’t support the do-while loop statement
