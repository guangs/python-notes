# A Python set is an unordered list of immutable elements
# - Elements in a set are unordered
# - Elements in a set are unique
# - Elements in a set cannot be changed


skills = set(['Problem solving','Critical Thinking'])

# add element
skills.add("Harding Working")

# delete element
skills.remove("Critical Thinking")

# delete element, 与remove 类似，但如果找不到key，不抛出异常
skills.discard("Critical Thinking")

# delete element, 删除的element是不确定的，反正就是remove其中一个element，返回值是该element
item = skills.pop()

# remove all
skills.clear()

# frozenset返回一个immutable的新set
frozon_skills = frozenset(skills)

skills.add("Time Managing")
# frozon_skills.add("Time Managing")  #会报错

print(skills)


# 遍历
for skill in skills:
    print(skill)

for index, skill in enumerate(skills, 1):
    print(f"{index} - {skill}")


#  set comprehension

tags = {'Django', 'Pandas', 'Numpy'}

lowercase_tags = {tag.lower() for tag in tags if tag != 'Numpy'}

print(lowercase_tags)


# Union
s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

print(s1.union(s2))
print(s1 | s2)

# union 与 | 的区别： union的参数除了set，事实上只要是iterable的对象就可以， 而 | 只能是set与set之间
print(s1.union(['C#', 'Java'])) # set 与list 合并


# Intersection
s1 = {'Python', 'Java','C++'}
s2 = {'C#', 'Java', 'C++' }

# intersection 与 & 的区别，类似union 与 | 的区别， intersection接受interable对象，&只接受set
print(s1.intersection(s2))
print(s1 & s2)


# Difference
# difference 与 - 的区别也类似，difference接受iterable对象，- 只能是set之间
print(s1.difference(s2))  # {'Python'}
print(s2.difference(s1))  # {'C#'}
print(s1 - s2) # {'Python'}
print(s2 - s1) # {'C#'}


# Symmetric Difference
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
print(s1.symmetric_difference(s2)) # {'Python', 'C#'}
print(s2.symmetric_difference(s1)) # {'Python', 'C#'}
# symmetric_difference 与 ^ 的区别也类似，symmetric_difference接受iterable对象，^ 只能是set之间
print(s1 ^ s2) # {'Python', 'C#'}
print(s2 ^ s1) # {'Python', 'C#'}


# issubset
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

# issubset 与 <= 类似
print(scores.issubset(numbers))  # True
print(scores <= numbers)
print(scores < numbers)


# issuperset
print(numbers.issuperset(scores))
print(numbers >= scores)
print(numbers > scores)


# isdisjoint 无任何交集
odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}
print(odd_numbers.isdisjoint(even_numbers))


# unpacking with *
odd_numbers = set([1, 3, 5])
even_numbers = set([2, 4, 6])

numbers = set([*odd_numbers, *even_numbers])
print(numbers)