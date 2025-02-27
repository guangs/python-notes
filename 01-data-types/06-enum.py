from enum import Enum


class Color(Enum):
    # Enum的成员变量一般都是常量，所以一般都大写
    RED = 1
    GREEN = 2
    BLUE = 3
    BLACK = 1
    
# enum成员有name和value两个属性
print(Color.RED.name)
print(Color.RED.value)
# in 操作
print(Color.BLUE in Color) # True
print(Color.BLUE.value == 3) # True
# 注意：这个是不等的
print(Color.BLUE == 3)  # False
# 注意：这个是不等的
print(Color.BLUE == Color.BLACK)  # False

# enum一般不需要实例化，如果实例化，需要传入参数
c = Color(1)
print(c)
print(c.name)
print(c.value)

# 注意：Enumerations are immutable
# Color.BLUE.value = 5 #AttributeError: can't set attribute


# 注意：An enumeration cannot be inherited unless it contains no members