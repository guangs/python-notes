# process并发这方面，也推荐用ProcessPoolExecutor来代替手动创建process
# process之间的同步，通过Event来实现
# process之间的冲突，通过Lock来实现. 但是进程之间，内存数据是彼此隔离的，不共享，所以不存在内存数据冲突的事情，但是对于IO设备，比如打印机等还是有冲突的情况


import time
import multiprocessing

def task(n=100_000_000):
    while n:
        n -= 1

def main():
    start = time.perf_counter()

    p1 = multiprocessing.Process(target=task)
    p2 = multiprocessing.Process(target=task)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish = time.perf_counter()

    print(f'It took {finish-start: .2f} second(s) to finish')

# main()



# ProcessPoolExecutor


from time import sleep, perf_counter
from concurrent.futures import ProcessPoolExecutor

def task(id, name):
    print(f'Starting the task {id}[{name}]...')
    sleep(1)
    return f'Done with task {id}[{name}]'


def main():
    start = perf_counter()

    with ProcessPoolExecutor() as executor:
        # 注意：submit(fun, arg1, arg2)的参数， 并且有返回值
        f1 = executor.submit(task, 1, "task1")
        f2 = executor.submit(task, 2, "task2")

        print(f1.result())
        print(f2.result())


    with ProcessPoolExecutor() as executor:
        # 注意：map(func, *args1, *args2)的参数， 并且有返回值
        results = executor.map(task, [1, 2], ["task1", "task2"])
        for result in results:
            print(result)

    finish = perf_counter()
    print(f"It took {finish-start} second(s) to finish.")

# main()



# Lock

from multiprocessing import Lock, Process

def task(id, lock):
    lock.acquire()
    print(f"Process{id} acquire printer")
    sleep(1)
    print(f"Process{id} release printer")
    lock.release()

def main():
    lock = Lock()
    p1 = Process(target=task, args=(1, lock))
    p2 = Process(target=task, args=(2, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("main process done")

main()


# Pipe
# 用于process之间的同步

from multiprocessing import Event, Process

def task(event: Event, id: int) -> None:
    event.wait()
    event.clear()
    print(f'Process {id} started. Waiting for the signal....')
    sleep(1)
    print(f'Received signal. The process {id} was completed.')

def main() -> None:
    event = Event()

    p1 = Process(target=task, args=(event,1))
    p2 = Process(target=task, args=(event,2))

    p1.start()
    p2.start()

    print('Blocking the main process for 3 seconds...')
    sleep(3) 
    # 在event没有被set时，p1和p2处在等待的状态
    event.set()
    print("main process done")

# main()