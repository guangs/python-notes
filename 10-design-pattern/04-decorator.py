# encoding=utf-8
'''
装饰器是一个很著名的设计模式,经常被用于有切面需求的场景,较为经典的有插入日志、性能测试、事务处理等。
装饰器是解决这类问题的绝佳设计,有了装饰器,我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。
概括的讲,装饰器的作用就是为已经存在的对象添加额外的功能,同时并不改动已存在函数本身,也不改变原函数的调用方式。
下面就一步步看看Python中的装饰器。

装饰器模式本质: foo = deco(foo)

装饰器是利用了Python闭包的特性,对已有函数运行行为进行扩充或修改的新函数,而同时保留已有函数,不用对已有函数的代码进行修改
https://zhuanlan.zhihu.com/p/93846887
'''


# 第1种情况:装饰器本身无参数
def deco1(func):
    def wrapper(*args, **kwargs):
        print('deco1 start')
        func(*args, **kwargs)
        print('deco1 stop')
    return wrapper

@deco1
def func1(name):
    print(name)

func1("func1")

# 第2种情况:装饰器本身带参数
def deco2(arg=True):
    if arg:
        def _deco(func):
            def wrapper(*args, **kwargs):
                print('deco2 start')
                func(*args, **kwargs)
                print('deco2 stop')
            return wrapper
    else:
        def _deco(func):
            return func
    return _deco


@deco2(True)
def func2(name):
    print(name)

func2("func2")


# 装饰器调用顺序: deco1 start -> deco2 start -> func3 -> deco2 stop -> deco1 stop

@deco1
@deco2(True)
def func3(name):
    print(name)

func3('func3')


# 类作为装饰器
'''foo = Decorator(args1, args2)(foo)'''

# 第1种情况:装饰器本身无参数
class classDecorator1(object):

    def __call__(self, fn):        
        def wrapper(*args, **kwargs):
            print("class deco1 start")
            fn(*args, **kwargs)
            print("class deco1 stop")
        return wrapper


@classDecorator1()
def func4(name):
    print(name)

func4("func4")

# 第2种情况:装饰器本身带参数
class classDecorator2(object):

    def __init__(self, arg1):
        self.arg1 = arg1

    def __call__(self, fn):
        if self.arg1:    
            def wrapper(*args, **kwargs):
                print("class deco2 start")
                fn(*args, **kwargs)
                print("class deco2 stop")
            return wrapper
        else:
            return fn

@classDecorator2(True)
def func5(name):
    print(name)

func5("func5")


# When you decorate a function, you’ll lose the original function signature and documentation.
# To fix this, you can use the wraps function from the functools standard module

from functools import wraps

def currency(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'
    return wrapper


@currency
def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)

# help(net_price)
print(net_price.__name__)

if __name__ == '__main__':
    pass


