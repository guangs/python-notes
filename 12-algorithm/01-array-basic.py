from array import array

# 关于Array
# 特点：必须存储同一种类型的数据
# 优点：根据index来查改元素，速度超快O(1)；一组array只需要一个变量名
# 缺点：在头部或者中间增删元素，需要逐个移动元素，代价大速度慢O(n)；但在尾处增删是O(1)


# Create an array of integers
numbers = array('i', [1, 2, 3, 5, 7])


# Create an array of strings
names = array('u', 'hello')


# Create an array of floats
prices1 = array('f', [1.2, 10.3, 5.5, 7.8])
prices2 = array('d', [1.2, 10.3, 5.5, 7.8])


# Sum of price1 and price2  elements
prices3 = [ x + y for x, y in zip(prices1, prices2)]


# Another way to sum of price1 and price2 elements
prices3 = map(lambda x, y : x + y, prices1, prices2)


# Array methods
numbers = array('i', [1, 2, 3, 5, 7])
numbers.append(10) # add 10 to the end of the array
numbers.insert(0, 10) # add 10 to the beginning of the array
numbers.remove(10) # remove the first 10 from the array
numbers.pop() # remove the last element from the array
sorted(numbers) # return a new array, not change the original array
reversed(numbers) # return an iterator, not change the original array
numbers.index(5) # return the index of 10
numbers.count(5) # return the count of 10
numbers.reverse()   # reverse the array
numbers.clear() # remove all elements from the array
numbers.extend([1, 2, 3]) # add elements from another array to the end of the array
numbers[0] = 10 # change the first element of the array
numbers[0:2] = array('i', [100, 200]) # change the first two elements of the array
numbers[0:2] = array('i', []) # remove the first two elements of the array