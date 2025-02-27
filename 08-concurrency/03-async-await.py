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
asyncio.run(main())