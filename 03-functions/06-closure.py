'''
闭包的作用: 闭包使得局部变量，有了全局变量的生存周期，好处是避免了全局变量的污染，可以隐藏一些变量，制造上下文环境
Python中的装饰器, 就是用的闭包,传递的参数为函数func
'''

def increase():
    count = 0
    def closure():
        # 注意：nonlocal的使用场景正是在闭包中
        nonlocal count
        count += 1
        print(count)

    return closure

fn = increase()
fn()
fn()
fn()