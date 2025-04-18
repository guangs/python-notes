'''
To create and pause a coroutine, you use the Python async and await keywords:

The async keyword creates a coroutine.
The await keyword pauses a coroutine.

'''

# When you add the async keyword to the function, the function becomes a coroutine:
import asyncio
import time


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


# async def 来定义一个coroutine
async def do_homework(name: str, duration: int) -> None:
    start = time.perf_counter()
    # await 挂起自己，调用另外一个coroutine
    await asyncio.sleep(duration)
    end = time.perf_counter()
    print(f"{name} - {end-start}")


async def finish_coroutines():
    start = time.perf_counter()
    # 顺序执行，总的执行时间为13s
    coroutine1 = do_homework("cooking", 10)
    coroutine2 = do_homework("cooking", 3)
    # 此时才开始调用coroutine
    await coroutine1
    await coroutine2
    end = time.perf_counter()
    print(f"finish tasks - {end - start}")


async def finish_tasks():
    start = time.perf_counter()
    task1 = asyncio.create_task(do_homework("cooking", 10))
    task2 = asyncio.create_task(do_homework("cooking", 3))
    # coroutine包装成task后，才可以并发执行，总的执行时间为10s
    await task1
    await task2
    end = time.perf_counter()
    print(f"finish tasks - {end - start}")


asyncio.run(finish_coroutines())
print('-'* 50)
asyncio.run(finish_tasks())