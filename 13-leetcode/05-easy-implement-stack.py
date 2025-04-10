# https://www.workat.tech/problem-solving/practice/implement-stack-array

# ./resources/05-easy-implement-stack.png

# Implement Stack using Array
# Easy
# 30
# Implement a stack using an array as the underlying container.

# The Stack class should support the following methods:

# int size()
# boolean isEmpty()
# int top()
# void push(int element)
# void pop()
# Main method:
# Stack created of size 10
# Printed: stack.top() stack.isEmpty() stack.size()
# Pushed: 5
# Printed: stack.top() stack.isEmpty() stack.size()
# Pushed: 6
# Printed: stack.top() stack.isEmpty() stack.size()
# Pushed: 7
# Printed: stack.top() stack.isEmpty() stack.size()
# Popped
# Printed: stack.top() stack.isEmpty() stack.size()
# Popped
# Printed: stack.top() stack.isEmpty() stack.size()
# Popped
# Printed: stack.top() stack.isEmpty() stack.size()


# Expected Output
# -1 true 0
# 5 false 1
# 6 false 2
# 7 false 3
# 6 false 2
# 5 false 1
# -1 true 0


from array import array

class StackError(Exception):
     pass

class Stack:
    def __init__(self, capacity=0):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self._capacity = capacity
        self._data = array('i')

    def size(self) -> int:
        return len(self._data)

    def isEmpty(self) -> bool:
        return len(self._data) == 0

    def top(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[-1]

    def push(self, element: int) -> None:
        if len(self._data) < self._capacity:
            self._data.append(element)
            print(f"{element} is pushed")
        else:
            raise StackError("stack is full")


    def pop(self) -> None:
        if len(self._data) > 0:
            element = self._data.pop()
            print(f"{element} is popped")
        else:
            raise StackError("stack is empty")

    def __str__(self) -> str:
        return f"Stack(capacity={self._capacity}, data={list(self._data)})"
