import asyncio
import time


'''
https://docs.python.org/3/library/asyncio-task.html
https://www.pythontutorial.net/python-concurrency/
https://www.youtube.com/watch?v=Qb9s3UiMSTA

总结下：
1. 定义coroutine - 用 async def
2. coroutine包装成task，为了event loop可以并发执行,  asyncio.create_task(coroutine)
3. task提供了更多的控制，task.done(), task.cancel, TaskGroup
   async with asyncio.TaskGroup() as tg:  # 用法
       task1 = tg.create_task(coroutine1)
       task2 = tg.create_task(coroutine2)
4. asyncio.wait_for, 对单个task的timeout控制，asyncio.wait_for(task, timeout=MAX_TIMEOUT)
5. async with asyncio.timeout, 另一种对task的timeout的方式
   async with asyncio.timeout(10):  # 用法
       await long_running_task()
6. asyncio.wait，对多个task的控制，done, pending = await asyncio.wait([task1, task2, task3...], return_when=asyncio.FIRST_COMPLETED)
7. asyncio.gather, 执行多个task，一次返回结果  a, b = await asyncio.gather(coroutine1, coroutine2)  # coroutine会被包装成task
8. 都是用await来调用： await coroutine
                     await task
                     await asyncio.wait_for()
                     await asyncio.wait()
                     await asyncio.gather()
9. await 只允许三种类型，coroutines, Tasks, and Futures. Futures是很low-level的对象，一般应用中，不需要创建Future对象
10. asyncio.Lock, 只允许一个coroutine访问
11. asyncio.Semaphore，可允许多个coroutine访问
12. asyncio.Event, await event.wait(), event.set()

'''

# Coroutine, Future, 和 Task的关系
'''
在 Python 的 `asyncio` 中，**Task** 和 **Coroutine** 是密切相关的概念，但它们有不同的角色和功能。以下是两者的关系和区别：

---

### **1. Coroutine**
- **定义**：
  - Coroutine 是由 `async def` 定义的函数，调用后返回一个协程对象。
  - 它是 `awaitable` 对象，可以被 `await` 调用。
- **特点**：
  - Coroutine 本身不会运行，必须通过 `await` 或将其包装成 Task 才能在事件循环中执行。
  - Coroutine 是一种更底层的异步操作。


### **2. Task**
- **定义**：
  - Task 是 `asyncio` 中的一个高级抽象，用于并发运行协程。
  - 它是 `Future` 的子类，表示一个异步操作的最终结果。
- **特点**：
  - Task 会将一个 Coroutine 包装起来，并将其调度到事件循环中运行。
  - Task 是 `awaitable` 对象，可以被 `await` 调用以获取协程的结果。
  - Task 提供了更多的控制，例如 `done()` 检查是否完成、`cancel()` 取消任务等。


### **3. Coroutine 和 Task 的关系**
- **Coroutine 是 Task 的基础**：
  - Task 是对 Coroutine 的封装，用于将协程调度到事件循环中运行。
- **Task 提供了更多功能**：
  - Task 继承自 `Future`，可以通过 `done()` 检查是否完成，通过 `result()` 获取结果，通过 `cancel()` 取消任务。
- **Task 是事件循环中的执行单元**：
  - 事件循环会调度 Task，而 Task 会运行其内部的 Coroutine。

### **4. 关键区别**

| **特性**            | **Coroutine**                              | **Task**                                      |
|---------------------|--------------------------------------------|----------------------------------------------|
| **定义**            | 由 `async def` 定义，返回协程对象           | 由 `asyncio.create_task()` 创建，包装协程     |
| **运行方式**        | 必须通过 `await` 或 Task 才能运行           | 自动调度到事件循环中运行                      |
| **是否可控制**      | 无法直接控制                               | 提供 `done()`、`cancel()` 等方法              |
| **是否是 `Future`** | 否                                         | 是，继承自 `Future`，表示异步操作的最终结果   |
| **使用场景**        | 定义异步逻辑                               | 并发运行多个协程                              |

---

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



# coroutine
async def call_api(message, result=100, delay=3):
    start = time.perf_counter()
    await asyncio.sleep(delay)
    end = time.perf_counter()
    print(f'{message}: {round(end - start)} second(s) to complete.')
    return result

# await coroutine
async def main1():
    start = time.perf_counter()
    c1 = call_api('calling API 1', result=1, delay=1)
    c2 = call_api('calling API 2', result=2, delay=2)
    await c1
    await c2
    end = time.perf_counter()
    print(f'It takes total {round(end - start)} second(s) to complete.')

# await task
async def main2():
    # t1, t2 run in concurrency, then run t3 in sequence
    start = time.perf_counter()
    t1 = asyncio.create_task(call_api('calling API 1', result=1, delay=1))
    t2 = asyncio.create_task(call_api('calling API 2', result=2, delay=2))
    await t1
    await t2
    t3 = asyncio.create_task(call_api('calling API 3', result=3, delay=3))
    await t3
    end = time.perf_counter()
    print(f'It takes total {round(end - start)} second(s) to complete.')

# async with asyncio.TaskGroup()
async def main3():
    start = time.perf_counter()
    async with asyncio.TaskGroup() as tg:
        tg.create_task(call_api('calling API 1', result=1, delay=1))
        tg.create_task(call_api('calling API 2', result=2, delay=2))
    end = time.perf_counter()
    print(f'It takes total {round(end - start)} second(s) to complete.')

# await asyncio.wait_for, add timeout for a single task or single coroutine
async def main4():
    start = time.perf_counter()
    c1 = call_api('calling API 1', result=1, delay=1)
    c2 = call_api('calling API 2', result=2, delay=2)
    t1 = asyncio.create_task(c1)
    t2 = asyncio.create_task(c2)
    await asyncio.wait_for(t1, timeout=5)
    await asyncio.wait_for(t2, timeout=5)
    end = time.perf_counter()
    print(f'It takes total {round(end - start)} second(s) to complete.')

# async with asyncio.timeout(x), add timeout for tasks or coroutines
async def main5():
    start = time.perf_counter()
    t1 = asyncio.create_task(call_api('calling API 1', result=1, delay=1))
    t2 = asyncio.create_task(call_api('calling API 2', result=2, delay=2))
    async with asyncio.timeout(5):
        await t1
        await t2
    end = time.perf_counter()
    print(f'It takes total {round(end - start)} second(s) to complete.')

# await asyncio.wait, manage tasks. it does not support coroutine directly. coroutine must be wrapped into tasks
async def main6():
    start = time.perf_counter()
    t1 = asyncio.create_task(call_api('calling API 1', result=1, delay=1))
    t2 = asyncio.create_task(call_api('calling API 2', result=2, delay=2))
    done, pending = await asyncio.wait([t1, t2], timeout=5, return_when=asyncio.FIRST_COMPLETED)
    for t in done:
        print(t.result())
    for p in pending:
        print(p.done())
    end = time.perf_counter()
    print(f'It takes total {round(end - start)} second(s) to complete.')

# await asyncio.wait, manage tasks. it does not support coroutine directly. coroutine must be wrapped into tasks
async def main7():
    start = time.perf_counter()
    t1 = asyncio.create_task(call_api('calling API 1', result=1, delay=1))
    t2 = asyncio.create_task(call_api('calling API 2', result=2, delay=2))
    t3 = asyncio.create_task(call_api('calling API 3', result=3, delay=3))
    pending = (t1, t2, t3)
    while pending:
        done, pending = await asyncio.wait(
            pending,
            return_when=asyncio.FIRST_COMPLETED
        )
        result = done.pop().result()
        print(result)
    end = time.perf_counter()
    print(f'It takes total {round(end - start)} second(s) to complete.')

# await asyncio.gather, run multiple tasks or coroutines.
async def main8():
    start = time.perf_counter()
    t1 = asyncio.create_task(call_api('calling API 1', result=1, delay=1))
    t2 = asyncio.create_task(call_api('calling API 2', result=2, delay=2))
    r1, r2 = await asyncio.gather(t1, t2)
    print(r1, r2)
    end = time.perf_counter()
    print(f'It takes total {round(end - start)} second(s) to complete.')


async def set_future_result(future: asyncio.Future):
    print("Setting the result...")
    await asyncio.sleep(2)  # 模拟异步操作
    future.set_result("Future is complete!")  # 手动设置结果

# await asyncio.Future
async def main9():
    # 创建一个 Future 对象
    my_future = asyncio.Future()

    # 创建一个任务来设置 Future 的结果
    asyncio.create_task(set_future_result(my_future))

    # 等待 Future 完成并获取结果
    result = await my_future
    print(result)  # 输出: Future is complete!

# asyncio.Lock的作用
# - 异步变同步，多个coroutine一个一个地访问共享资源，被Lock保护的区域是一个整体，不被coroutine的调度机制打断的


# 一个共享资源，可能是一个变量，也可能是一个文件等等
counter = 0

lock = asyncio.Lock()
async def increment_counter(name: str):
    global counter
    async with lock:
        print(f"{name} has acquired the lock!")
        local_counter = counter
        await asyncio.sleep(1)  # 模拟一些异步操作，因为有了Lock, 所以确保这步会一直等待，不会被其他coroutine打乱
        counter = local_counter + 1
        print(f"{name} has updated the counter to {counter}")

    print(f"{name} has released the lock!")

# async with asyncio.Lock
async def main10():
    # 启动多个协程
    await asyncio.gather(
        increment_counter("Task 1"),
        increment_counter("Task 2"),
        increment_counter("Task 3"),
    )


# 创建一个 Semaphore，最多允许 2 个协程同时运行
semaphore = asyncio.Semaphore(2)

async def access_resource(name: str, delay: int):
    print(f"{name} is waiting to acquire the semaphore...")

    # 获取信号量
    async with semaphore:
        print(f"{name} has acquired the semaphore!")
        await asyncio.sleep(delay)  # 模拟异步操作
        print(f"{name} has released the semaphore!")

# async with asyncio.Semaphore
async def main11():
    # 启动多个协程
    await asyncio.gather(
        access_resource("Task 1", 2),
        access_resource("Task 2", 1),
        access_resource("Task 3", 3),
        access_resource("Task 4", 1),
    )


# asyncio.Event
event = asyncio.Event()

async def waiter(name: str):
    print(f"{name} is waiting for the event...")
    await event.wait()  # 等待事件触发
    print(f"{name} has been notified!")

async def notifier():
    print("Notifier is setting the event...")
    await asyncio.sleep(2)  # 模拟一些异步操作
    event.set()  # 触发事件
    print("Notifier has set the event!")

async def main12():
    # 启动多个等待协程和一个通知协程
    await asyncio.gather(
        waiter("Task 1"),
        waiter("Task 2"),
        notifier(),
    )



async def main():
    print('-' * 5 + 'await coroutine' + '-' * 5)
    await main1()

    print('-' * 5 + 'await task' + '-' * 5)
    await main2()

    print('-' * 5 + 'async with asyncio.TaskGroup' + '-' * 5)
    await main3()

    print('-' * 5 + 'await asyncio.wait_for' + '-' * 5)
    await main4()

    print('-' * 5 + 'async with asyncio.timeout' + '-' * 5)
    await main5()

    print('-' * 5 + 'await asyncio.wait' + '-' * 5)
    await main6()

    print('-' * 5 + 'await asyncio.wait' + '-' * 5)
    await main7()

    print('-' * 5 + 'await asyncio.gather' + '-' * 5)
    await main8()

    print('-' * 5 + 'await asyncio.Future' + '-' * 5)
    await main9()

    print('-' * 5 + 'async with asyncio.Lock' + '-' * 5)
    await main10()

    print('-' * 5 + 'async with asyncio.Semaphore' + '-' * 5)
    await main11()

    print('-' * 5 + 'await asyncio.Event.wait' + '-' * 5)
    await main12()

if __name__ == '__main__':
    asyncio.run(main12())
