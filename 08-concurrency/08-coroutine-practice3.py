# 读者，写者问题
# 读者写者问题是一个经典的同步问题，涉及到多个线程或协程对共享资源的访问。
# 在这个问题中，有两种类型的线程：读者和写者。读者可以同时读取共享资源，但写者在写入时需要独占访问。
# 读者和写者之间的主要问题是：如果有一个写者在写入，所有的读者都必须等待；如果有一个或多个读者在读取，写者必须等待。
# 读者写者问题的解决方案通常涉及到使用锁来控制对共享资源的访问。
# 下面是一个使用 asyncio 实现的读者写者问题的示例代码：


import asyncio

class ReadWriteLock:
    def __init__(self):
        self.readers = 0  # 当前正在读取的读者数量
        self.read_lock = asyncio.Lock()  # 用于保护读者计数的锁
        self.write_lock = asyncio.Lock()  # 写者锁，确保写操作的独占性

    async def acquire_read(self):
        async with self.read_lock:  # 确保对读者计数的线程安全
            self.readers += 1
            if self.readers == 1:  # 第一个读者需要获取写锁
                await self.write_lock.acquire()

    async def release_read(self):
        async with self.read_lock:  # 确保对读者计数的线程安全
            self.readers -= 1
            if self.readers == 0:  # 最后一个读者释放写锁
                self.write_lock.release()

    async def acquire_write(self):
        await self.write_lock.acquire()  # 写者直接获取写锁

    async def release_write(self):
        self.write_lock.release()  # 写者释放写锁


async def reader(name: str, rw_lock: ReadWriteLock):
    while True:
        print(f"{name} is waiting to read.")
        await rw_lock.acquire_read()  # 获取读锁
        try:
            print(f"{name} is reading.")
            await asyncio.sleep(1)  # 模拟读取时间
        finally:
            await rw_lock.release_read()  # 释放读锁
            print(f"{name} finished reading.")
        await asyncio.sleep(1)  # 模拟读者的其他操作时间


async def writer(name: str, rw_lock: ReadWriteLock):
    while True:
        print(f"{name} is waiting to write.")
        await rw_lock.acquire_write()  # 获取写锁
        try:
            print(f"{name} is writing.")
            await asyncio.sleep(2)  # 模拟写入时间
        finally:
            await rw_lock.release_write()  # 释放写锁
            print(f"{name} finished writing.")
        await asyncio.sleep(2)  # 模拟写者的其他操作时间


async def main():
    rw_lock = ReadWriteLock()  # 创建读写锁

    # 创建多个读者和写者任务
    readers = [asyncio.create_task(reader(f"Reader-{i}", rw_lock)) for i in range(3)]
    writers = [asyncio.create_task(writer(f"Writer-{i}", rw_lock)) for i in range(2)]

    await asyncio.gather(*readers, *writers)  # 并发运行所有任务


if __name__ == "__main__":
    asyncio.run(main())