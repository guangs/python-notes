class MyClass:
    # 类属性
    class_attribute = "I am a class attribute"

    def __init__(self, value):
        # 实例属性
        self.instance_attribute = value

# 创建两个实例
obj1 = MyClass("Instance 1")
obj2 = MyClass("Instance 2")

# 访问类属性和实例属性
print(obj1.class_attribute)  # 输出: I am a class attribute
print(obj1.instance_attribute)  # 输出: Instance 1

print(obj2.class_attribute)  # 输出: I am a class attribute
print(obj2.instance_attribute)  # 输出: Instance 2

# 修改类属性
MyClass.class_attribute = "Modified class attribute"
print(obj1.class_attribute)  # 输出: Modified class attribute
print(obj2.class_attribute)  # 输出: Modified class attribute