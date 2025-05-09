# 协程挂起自己，让出自己的执行权，把控制权交给事件循环的情况有：
# 1. await 操作，一定让出控制权
# 2. 遇到锁，取决于能否获得锁，如果获得则继续，否则让出控制权
#           async with aysncio.Lock()，
#           async with asyncio.Semaphore()，
#           async with asyncio.Condition()，
#           async with asyncio.Event()



# 生产者，消费者问题
# 生产者消费者模式是一个经典的并发编程问题，通常用于解决生产者和消费者之间的协调问题。
# 在这个模式中，生产者负责生产数据并将其放入队列中，而消费者则从队列中取出数据进行处理。
# 生产者和消费者之间通过一个共享的队列进行通信。

# 使用 asyncio.Queue 实现生产者消费者模式
# 这种方式简单易用，适合大多数场景
# asyncio.Queue 是线程安全的，支持异步操作
# 下面是一个使用 asyncio.Queue 实现的生产者消费者模式的示例


import asyncio


async def consumer1(name: str, store: asyncio.Queue):
    while True:
        item = await store.get()  # 从队列中消费数据
        print(f"{name} consumed {item}")
        store.task_done()  # 标记任务完成
        await asyncio.sleep(1)  # 模拟消费时间


async def producer1(name: str, store: asyncio.Queue):
    while True:
        if not store.full():  # 检查队列是否已满
            item = f"item-{store.qsize() + 1}"
            await store.put(item)  # 异步向队列中添加数据
            print(f"{name} produced {item}")
        else:
            print(f"{name} waiting for space in the queue...")
        await asyncio.sleep(0.5)  # 模拟生产时间


async def main1():
    store = asyncio.Queue(maxsize=5)  # 队列最大长度为 5
    # 创建生产者和消费者任务
    consumers = [asyncio.create_task(consumer1(f"consumer-{i}", store)) for i in range(2)]
    producers = [asyncio.create_task(producer1(f"producer-{i}", store)) for i in range(1)]
    await asyncio.gather(*consumers, *producers)



# 使用 deque 和 asyncio.Lock 实现生产者消费者模式
# 这种方式可以更灵活地控制队列的大小和访问
# 但是需要手动管理锁和队列的大小
# 注意：deque 是线程安全的，但在异步环境中使用时需要额外的锁来确保线程安全
# 下面是一个使用 deque 和 asyncio.Lock 实现的生产者消费者模式的示例
from collections import deque

async def consumer2(name: str, store: deque, lock: asyncio.Lock):
    while True:
        async with lock:  # 获取锁，确保线程安全
            if store:  # 检查队列是否有数据
                item = store.popleft()  # 从队列左侧取出数据
                print(f"{name} consumed {item}")
            else:
                print(f"{name} waiting for items...")
        await asyncio.sleep(1)  # 模拟消费时间


async def producer2(name: str, store: deque, lock: asyncio.Lock, max_size: int):
    while True:
        async with lock:  # 获取锁，确保线程安全
            if len(store) < max_size:  # 检查队列是否已满
                item = f"item-{len(store) + 1}"
                store.append(item)  # 向队列右侧添加数据
                print(f"{name} produced {item}")
            else:
                print(f"{name} waiting for space in the queue...")
        await asyncio.sleep(0.5)  # 模拟生产时间


async def main2():
    store = deque()  # 使用 deque 作为队列
    lock = asyncio.Lock()  # 创建一个异步锁
    max_size = 5  # 队列最大长度

    # 创建生产者和消费者任务
    consumers = [asyncio.create_task(consumer2(f"consumer-{i}", store, lock)) for i in range(2)]
    producers = [asyncio.create_task(producer2(f"producer-{i}", store, lock, max_size)) for i in range(1)]

    await asyncio.gather(*consumers, *producers)


if __name__ == '__main__':
    asyncio.run(main1())

