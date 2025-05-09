# 哲学家就餐问题
# 关键是要避免死锁和资源竞争
# 这是一个经典的并发问题，涉及多个哲学家和叉子。每个哲学家在思考和吃饭之间切换。
# 左叉子和右叉子是共享资源，哲学家需要同时持有两把叉子才能吃饭。


### **关键点**
# 1. **线程安全**：
#    - 使用 `asyncio.Lock` 确保叉子（共享资源）的线程安全。

# 2. **死锁避免**：
#    - 每个哲学家按照固定顺序获取叉子（先左后右），避免循环等待。

# 3. **协程并发**：
#    - 使用 `asyncio.create_task` 和 `asyncio.gather` 实现哲学家之间的并发行为。



import asyncio

class Philosopher:
    def __init__(self, name, left_fork, right_fork):
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork

    async def dine(self):
        while True:
            print(f"{self.name} is thinking.")
            await asyncio.sleep(1)  # 模拟思考时间

            # 尝试获取左叉子
            async with self.left_fork:
                print(f"{self.name} picked up the left fork.")
                # 尝试获取右叉子
                async with self.right_fork:
                    print(f"{self.name} picked up the right fork.")
                    print(f"{self.name} is eating.")
                    await asyncio.sleep(2)  # 模拟吃饭时间

                print(f"{self.name} put down the right fork.")
            print(f"{self.name} put down the left fork.")


async def main():
    # 创建 5 把叉子（异步锁）
    forks = [asyncio.Lock() for _ in range(5)]

    # 创建 5 个哲学家
    philosophers = [
        Philosopher(f"Philosopher-{i}", forks[i], forks[(i + 1) % 5])
        for i in range(5)
    ]

    # 创建哲学家的任务
    tasks = [asyncio.create_task(philosopher.dine()) for philosopher in philosophers]

    # 运行哲学家任务
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
