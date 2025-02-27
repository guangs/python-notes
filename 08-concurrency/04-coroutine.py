# Python的coroutine实现，有几个阶段：Python2 yield实现 -> 第三方的gevent模块 -> Python3.4 asyncio
# 更进一步完善asyncio： Python3.5 async/await -> Python3.7 更加简化的 event loop (3.7之前的event loop要手动创建和关闭)

# coroutine 和 event loop是搭配使用的，event loop用来调度coroutine


'''
To create and pause a coroutine, you use the Python async and await keywords:

The async keyword creates a coroutine.
The await keyword pauses a coroutine.

'''

# When you add the async keyword to the function, the function becomes a coroutine:
import asyncio

async def square(number: int) -> int:
    return number*number

# 注意： await只能在async定义的coroutine里使用, 这点类似JS中async await
async def main() -> None:
    x = await square(10)
    print(f'x={x}')

    y = await square(5)
    print(f'y={y}')

    print(f'total={x+y}')

# Python3.7+ asyncio.run() can automatically create an event loop, run a coroutine and close it
# asyncio.run(main())



# asyncio.create_task()
# https://www.pythontutorial.net/python-concurrency/python-asyncio-create_task/

import asyncio
import time


async def call_api(message, result=1000, delay=3):
    print(message)
    await asyncio.sleep(delay)
    return result

async def show_message():
    for _ in range(3):
        await asyncio.sleep(1)
        print('API call is in progress...')

# if not use asyncio.create_task()
async def main():
    start = time.perf_counter()

    price = await call_api('Get stock price of GOOG...', 300)
    print(price)

    price = await call_api('Get stock price of APPL...', 400)
    print(price)

    end = time.perf_counter()
    print(f'It took {round(end-start,0)} second(s) to complete.')


# if use asyncio.create_task()
async def main():
    start = time.perf_counter()

    task_1 = asyncio.create_task(
        call_api('Get stock price of GOOG...', 300)
    )

    task_2 = asyncio.create_task(
        call_api('Get stock price of APPL...', 300)
    )

    price = await task_1
    print(price)

    price = await task_2
    print(price)

    end = time.perf_counter()
    print(f'It took {round(end-start,0)} second(s) to complete.')

# different tasks
async def main():
    start = time.perf_counter()

    message_task = asyncio.create_task(
        show_message()
    )

    task_1 = asyncio.create_task(
        call_api('Get stock price of GOOG...', 300)
    )

    task_2 = asyncio.create_task(
        call_api('Get stock price of APPL...', 300)
    )

    price = await task_1
    print(price)

    price = await task_2
    print(price)

    await message_task

    end = time.perf_counter()
    print(f'It took {round(end-start,0)} second(s) to complete.')

asyncio.run(main())



# Cancelling Tasks

from asyncio import CancelledError

async def main():
    task = asyncio.create_task(
        call_api('Calling API...', result=2000, delay=5)
    )

    if not task.done():
        print('Cancelling the task...')
        task.cancel()

    try:
        await task
    except CancelledError:
        print('Task has been cancelled.')


# asyncio.run(main())



# asyncio.wait_for(), wait for a coroutine to complete with a timeout

async def main():
    task = asyncio.create_task(
        call_api('Calling API...', result=2000, delay=5)
    )

    MAX_TIMEOUT = 3
    try:
        await asyncio.wait_for(task, timeout=MAX_TIMEOUT)
    except TimeoutError:
        print('The task was cancelled due to a timeout')

# asyncio.run(main())


# asyncio.shield(), prevents the cancellation of a task

async def main():
    task = asyncio.create_task(
        call_api('Calling API...', result=2000, delay=5)
    )

    MAX_TIMEOUT = 3
    try:
        await asyncio.wait_for(asyncio.shield(task), timeout=MAX_TIMEOUT)
    except TimeoutError:
        print('The task took more than expected and will complete soon.')
        result = await task
        print(result)

# asyncio.run(main())



# asyncio.wait(), asyncio future
# 见05-asyncio.py
