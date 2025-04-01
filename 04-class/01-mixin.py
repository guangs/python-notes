# Mixins是一种轻量级的多继承方式，适用于为类添加功能
# Mixin类应该提供特定的功能，而不是作为独立的类使用，并且不应该被实例化。
# Mixin类不应保持任何内部状态，即不应有实例属性

# 注意Mixin类应该放在继承列表的第一个位置，这样可以确保Mixin类的方法在其他类的方法之前被调用，Mixin中的super()方法会调用多继承中下一个类右侧类的方法

class Mixin:
    def ping(self):
        print(f"{self}.ping() in Mixin")
        super().ping()


class Root:
    def ping(self):
        print(f"{self}.ping() in Root")

class A(Root):
    def ping(self):
        print(f"{self}.ping() in A")
        super().ping()


class LeafMA(Mixin, A):
    def ping(self):
        print("ping in LeafMA")
        super().ping()


#  LeafMA的ping()方法会调用Mixin的ping()方法，Mixin的ping()方法会调用A的ping()方法，A的ping()方法会调用Root的ping()方法
#  结果是：
#  ping in LeafMA
#  LeafMA.ping() in Mixin
#  LeafMA.ping() in A
#  LeafMA.ping() in Root
#  这样就实现了Mixin的功能
#  但是Mixin不应该有实例属性，所以在Mixin类中不应该定义__init__方法
#  Mixin类应该是轻量级的，不应该有复杂的逻辑
#  Mixin类应该是单一职责的，不应该有多个功能
#  Mixin类应该是可复用的，不应该依赖于其他类
ma = LeafMA()
ma.ping()



class LeafAM(A, Mixin):
    def ping(self):
        print("ping in LeafMA")
        super().ping()

am = LeafAM()
am.ping()

#  结果是：
#  ping in LeafMA
#  LeafAM.ping() in A
#  LeafAM.ping() in Root
#  因为继承顺序的原因，Python根本就没有执行Mixin的ping()方法，所以这种形式的Mixin是无效的

#  但是如果我们把Mixin放在最前面，就可以实现Mixin的功能