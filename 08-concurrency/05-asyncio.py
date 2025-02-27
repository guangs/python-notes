import asyncio
from asyncio import create_task




# The asyncio.wait()
'''
The asyncio.wait() function has the following parameters:

aws is iterable of awaitable objects that you want to run concurrently.
timeout (either int or float) specifies a maximum number of seconds to wait before returning the result.
return_when indicates when the function should return. The return_when accepts one of the constants in the table below.
'''


class APIError(Exception):
    pass


async def call_api(message, result=100, delay=3, raise_exception=False):
    print(message)
    await asyncio.sleep(delay)
    if raise_exception:
        raise APIError
    else:
        return result


async def main():
    task_1 = create_task(call_api('calling API 1...', result=1, delay=1))
    task_2 = create_task(call_api('calling API 2...', result=2, delay=2))
    task_3 = create_task(call_api('calling API 3...', result=3, delay=3))

    pending = (task_1, task_2, task_3)

    while pending:
        done, pending = await asyncio.wait(
            pending,
            return_when=asyncio.FIRST_COMPLETED
        )
        result = done.pop().result()
        print(result)


# asyncio.run(main())


# asyncio future
# in practice, you’ll rarely need to create Future objects directly

from asyncio import Future

# future的基本操作
async def main():

    my_future = Future()
    print(my_future.done())  # False
    my_future.set_result('Bright')
    print(my_future.done())  # True
    print(my_future.result())


# asyncio.run(main())


# future与await结合使用，await后面可接future对象
async def plan(my_future):
    print('Planning my future...')
    await asyncio.sleep(1)
    my_future.set_result('Bright')


def create() -> Future:
    my_future = Future()
    # 注意：核心是这个地方，定义一个future，传给了协程异步操作
    asyncio.create_task(plan(my_future))
    return my_future


async def main():
    my_future = create()
    # When you use the await keyword with a future, you pause the future until it returns a value.
    result = await my_future

    print(result)


asyncio.run(main())



# asyncio.gather()
'''
The asyncio.gather() function has two parameters:
- aws is a sequence of awaitable objects. If any object in the aws is a coroutine, the asyncio.gather() function will automatically schedule it as a task.
- return_exceptions is False by default. If an exception occurs in an awaitable object, it is immediately propagated to the task that awaits on asyncio.gather(). Other awaitables will continue to run and won't be canceled.
'''

async def call_api(message, result, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result


async def main():
    # 注意：asyncio.gather() 会自动把awaitable对象(coroutine/Future)变成task
    # 所以，这里省掉了asyncio.create_task
    a, b = await asyncio.gather(
        call_api('Calling API 1 ...', 1),
        call_api('Calling API 2 ...', 2),
        return_exceptions=True  # 允许返回异常
    )
    print(a, b)


asyncio.run(main())


# Coroutine, Future, 和 Task的关系

'''
                ---------------
                |   awaitable |
                ---------------
                  ^         ^
                  |         |
        ------------     -------------
        | coroutine|     |  Future   |
        ------------     -------------
                            ^
                            |
                         -------------
                         |  Task     |
                         -------------

Awaitable class has an abstract method __await__()
Courtine, Future, and Task are subclasses of the Awaitable abstract class
'''