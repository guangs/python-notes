# 协程间的事件通知
import asyncio

async def waiter(name: str, event: asyncio.Event):
    while True:
        print(f"{name}: Waiting for the event...")
        await event.wait()  # 等待事件被触发
        print(f"{name}: Event is set! Proceeding...")
        event.clear()  # 重置事件
        await asyncio.sleep(1)  # 模拟其他操作

async def notifier(event: asyncio.Event):
    for i in range(3):
        print(f"Notifier: Setting the event ({i+1})...")
        event.set()  # 触发事件
        await asyncio.sleep(2)  # 模拟一些工作

async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter("Waiter", event), notifier(event))

asyncio.run(main())
