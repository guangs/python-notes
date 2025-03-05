# __getitem__() and __setitem__() are magic methods for indexing and slicing, for in loops
# __getattr__() and __setattr__() are magic methods for attribute access
# __delattr__() is a magic method for deleting attributes
# __call__() is a magic method for calling objects as functions
# __str__() is a magic method for string representation
# __repr__() is a magic method for object representation
# __len__() is a magic method for determining the length of objects
# __iter__() is a magic method for creating iterators
# __contains__() is a magic method for checking the existence of elements
# __bool__() is a magic method for boolean conversion

# __add__() is a magic method for addition
# __sub__() is a magic method for subtraction
# __mul__() is a magic method for multiplication
# __truediv__() is a magic method for division
# __floordiv__() is a magic method for floor division
# __mod__() is a magic method for modulus
# __pow__() is a magic method for exponentiation
# __lshift__() is a magic method for left shift
# __rshift__() is a magic method for right shift
# __and__() is a magic method for bitwise AND
# __or__() is a magic method for bitwise OR
# __xor__() is a magic method for bitwise XOR
# __invert__() is a magic method for bitwise inversion
# __neg__() is a magic method for negation
# __pos__() is a magic method for unary plus
# __abs__() is a magic method for absolute value
# __complex__() is a magic method for complex numbers
# __int__() is a magic method for integer conversion
# __float__() is a magic method for floating-point conversion
# __round__() is a magic method for rounding
# __index__() is a magic method for integer conversion
# __enter__() is a magic method for with statement
# __exit__() is a magic method for with statement
# __copy__() is a magic method for copying objects
# __deepcopy__() is a magic method for deep copying objects
# __bool__() is a magic method for boolean conversion
# __format__() is a magic method for string formatting
# __hash__() is a magic method for hash values
# __next__() is a magic method for next iteration
# __reduce__() is a magic method for serialization
# __reduce_ex__() is a magic method for serialization
# __getnewargs__() is a magic method for serialization
# __getstate__() is a magic method for serialization
# __setstate__() is a magic method for serialization
# __dict__() is a magic method for dictionary representation
# __dir__() is a magic method for directory representation
# __reversed__() is a magic method for reverse iteration


# 实现__len__和__getitem__方法，使得对象可以像标准的Python序列一样

# for i in x:  语句其实在背后调用了iter(x)函数，iter函数又调用了x.__iter__()方法或x.__getitem__()方法，所以要实现迭代，需要实现__iter__或__getitem__方法