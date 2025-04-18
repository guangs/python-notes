# Python的coroutine实现，有几个阶段：Python2 yield实现 -> 第三方的gevent模块 -> Python3.4 asyncio
# 更进一步完善asyncio： Python3.5 async/await -> Python3.7 更加简化的 event loop (3.7之前的event loop要手动创建和关闭)

# coroutine 和 event loop是搭配使用的，event loop用来调度coroutine


'''
To create and pause a coroutine, you use the Python async and await keywords:

The async keyword creates a coroutine.
The await keyword pauses a coroutine.

'''



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
async def main_coroutine():
    start = time.perf_counter()

    price = await call_api('Get stock price of GOOG...', 300)
    print(price)

    price = await call_api('Get stock price of APPL...', 400)
    print(price)

    end = time.perf_counter()
    print(f'It took {round(end-start,0)} second(s) to complete.')


# if use asyncio.create_task()
async def main_task():
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
async def main_task2():
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

asyncio.run(main_coroutine())
asyncio.run(main_task())



# Cancelling Tasks

from asyncio import CancelledError

async def main_task3():
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

async def main_wait_for():
    task = asyncio.create_task(
        call_api('Calling API...', result=2000, delay=5)
    )

    MAX_TIMEOUT = 3
    try:
        await asyncio.wait_for(task, timeout=MAX_TIMEOUT)
    except TimeoutError:
        print('The task was cancelled due to a timeout')

# asyncio.run(main_wait_for())


# asyncio.shield(), prevents the cancellation of a task

async def main_shield():
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

# asyncio.run(main_shield())



# asyncio.wait(), asyncio future
# 见05-asyncio.py
