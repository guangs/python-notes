class MyClass:
    def __init__(self):
        self.public_attr = "Public"  # 公共属性
        self._protected_attr = "Protected"  # 受保护属性
        self.__private_attr = "Private"  # 私有属性

    def get_private_attr(self):
        return self.__private_attr  # 提供方法访问私有属性

class SubClass(MyClass):
    def access_protected(self):
        return self._protected_attr  # 子类可以访问受保护属性

obj = MyClass()
print(obj.public_attr)  # 输出: Public
print(obj._protected_attr)  # 输出: Protected (外部可以访问，但不推荐)
print(obj.get_private_attr())  # 输出: Private
# print(obj.__private_attr)  # 报错: AttributeError
print(obj._MyClass__private_attr)  # 输出: Private (通过名称改写访问，不推荐)

sub_obj = SubClass()
print(sub_obj.access_protected())  # 输出: Protected