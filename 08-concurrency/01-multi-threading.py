# Python thread并发这方面，推荐用ThreadPoolExecutor 代替自己创建thread
# Event用于threads之间的同步(协同)，比如 A线程做完了，然后notify B线程. 常用于不涉及资源的竞争，没有共享数据的情况
# Lock用于threads之间的互斥，避免同时修改资源
# Lock和Event是最常用的两个工具，Semaphore也常用，Condition不常用。
# Event，Semaphore和Condition都是基于Lock实现的
# Condition是基于Lock和一个队列实现的
# Event是基于Lock和Condition实现的
# Semaphore是基于Lock和一个计数器实现的
# | **工具**       | **使用频率** | **适用场景**                                   |
# |----------------|--------------|---------------------------------------------|
# | **`Lock`**     | 非常常用     | 保护共享资源，确保互斥访问。                   |
# | **`Event`**    | 常用         | 协程之间的通知和协调。                         |
# | **`Condition`**| 不常用       | 更复杂的同步机制，适合生产者-消费者模型等场景。 |
# | **`Semaphore`**| 常用         | 限制并发协程的数量（如网络请求、任务池）。      |

# concurrent.futures的类的继承关系
# Executor (抽象基类)
# ├── ThreadPoolExecutor
# └── ProcessPoolExecutor

# from concurrent.futures import ThreadPoolExecutor
#
# def task(n):
#     print(f"Task {n} is running")
#
# with ThreadPoolExecutor(max_workers=3) as executor:
#     for i in range(5):
#         executor.submit(task, i)


'''
The Thread() accepts many parameters. The main ones are:

target: specifies a function (fn) to run in the new thread.
args: specifies the arguments of the function (fn). The args argument is a tuple.

Like this:
new_thread = Thread(target=fn,args=args_tuple)
'''



'''
Thread 对象常用方法

-start   
-join
'''

from time import sleep
from threading import Thread

def task(name):
    print(f"Starting a task [{name}]...")
    sleep(1)
    print(f'done [{name}]')


def main() -> None:
    # 注意：args是一个tuple
    t1 = Thread(target=task, args=("task1",))
    t2 = Thread(target=task, args=("task2",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("main thread done")

# main()



# Inheriting from the Thread class
# - override the run() method of the Thread class, task写在run里面

class MyThread(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # task
        print(f"Starting a task [{self.name}]...")
        sleep(1)
        print(f'done [{self.name}]')

def main() -> None:
    tasks = [MyThread(name) for name in ['task1', 'task2']]

    for task in tasks:
        task.start()

    for task in tasks:
        task.join()

    print("main thread done")

# main()



# Use Threading Event to communicate between the threads
# Event object wraps a boolean flag that can be set (True) or unset (False) 
# Threads that share an Event object can check if the event is set, or wait for the event to be set.
# 
# event.set() - 发送notify
# event.wait() - 等待notify
# event.clear() - 重置notify
# event.is_set() - 是否有notify
# 
# 主线程通过event可以控制子线程的执行和退出
# 一个Event很好的例子：https://cloud.tencent.com/developer/article/2069425?areaSource=&traceId=

from threading import Event

def task(event: Event, id: int) -> None:
    event.wait()
    event.clear()
    print(f'Thread {id} started. Waiting for the signal....')
    sleep(1)
    print(f'Received signal. The thread {id} was completed.')
    # print(f"thread {id} handle non-shared resources")

def main() -> None:
    event = Event()

    t1 = Thread(target=task, args=(event,1))
    t2 = Thread(target=task, args=(event,2))

    t1.start()
    t2.start()

    print('Blocking the main thread for 3 seconds...')
    sleep(3) 
    # 在event没有被set时，t1和t2处在等待的状态
    event.set()
    print("main thread done")

main()



# Use event to stop a thread
# 主线程通过event可以控制子线程的执行和退出


def task(event: Event) -> None:
    for i in range(6):
        print(f'Running #{i+1}')
        sleep(1)
        if event.is_set():
            print('The thread was stopped prematurely.')
            break
    else:
        print('The thread was stopped maturely.')

def main() -> None:

    event = Event()
    thread = Thread(target=task, args=(event,))
    
    # start the thread
    thread.start()

    # suspend  the thread after 3 seconds
    sleep(3)

    # stop the child thread
    event.set()
   

# main()



# Daemon Threads
# daemon threads的特点是：
# - 如果所有的non-daemon threads退出了，那么daemon将自动退出, 只有daemon threads时，将无法存活
# - 比如：daemon自动跟着主线程退出，但是普通thread不会跟着主线程退出
# - Daemon线程通常是执行不是很critial的task，因为当程序退出时会被自动kill掉
# - Daemon线程的优点是，当程序退出时，不用手动停止该线程

def task():
    pass

t = Thread(target=task, args=(), daemon=True)


def show_timer():
    count = 0
    while True:
        count += 1
        sleep(1)
        print(f'Has been waiting for {count} second(s)...')

# daemon 为False时，子线程将无限循环，daemon为True时，跟着主线程退出

def main():
    t = Thread(target=show_timer, daemon=True)
    t.start()

    answer = input('Do you want to exit?\n')

# main()



# thread-safe queue
# queue 特别适合解决生产者-消费者的问题
# queue 也可以用来主线程和子线程的通信，比如：子线程把返回值放入queue中，主线程来检查各个子线程的结果

from queue import Queue, Empty

queue = Queue()
# queue.put(1)
# queue.get()
# queue.qsize()
# queue.empty()
# queue.full()
# queue.task_done()  # 队列里的每个item被视为一个task，当处理完一个task的时候，调用task_done
# queue.join()  # 等待队列为空，注意：并不是等待所有task完成。如果要等所有task完成，则需要保证queue.join的时候，所有task已经在queue里才行


# 利用queue解决生产者-消费者问题
def producer(queue):
    for i in range(1, 6):
        print(f'Inserting item {i} into the queue')
        sleep(1)
        queue.put(i)


def consumer(queue):
    while True:
        try:
            item = queue.get()
        except Empty:
            continue
        else:
            print(f'Processing item {item}')
            sleep(2)
            # 注意：处理完一个taks后，需要调用task_done才行，不然queue.join会认为task not completed
            queue.task_done()


def main():
    queue = Queue()

    # create a producer thread and start it
    producer_thread = Thread(
        target=producer,
        args=(queue,)
    )
    producer_thread.start()

    # create a consumer thread and start it
    consumer_thread = Thread(
        target=consumer,
        args=(queue,),
        daemon=True
    )
    consumer_thread.start()

    # wait for all tasks to be added to the queue
    # 注意：这是为了保证queue.join的时候，所有task已经在queue里了
    producer_thread.join()

    # wait for all tasks on the queue to be completed
    # 注意：queue.join的退出条件是队列为空，为保证所有task完成，则需要再join之前，保证所有task已经在queue里了才行
    queue.join()

# main()




# ThreadPoolExecutor
# - 为了减少反复创建线程的开销，控制线程的数量，引入thread pools，pool里的线程可以不断reuse
# - thread pool的另一个好处是，thread的create和destroy都是自动的
# - thread pool里的线程叫做 worker threads，worker thread可以反复reuse，接受不同的task，即使遇到异常也不退出

# The Executor class has three methods to control the thread pool:
# - submit()
# - map()
# - shutdown()


from time import sleep, perf_counter
from concurrent.futures import ThreadPoolExecutor

def task(id, name):
    print(f'Starting the task {id}[{name}]...')
    sleep(1)
    return f'Done with task {id}[{name}]'


def main():
    start = perf_counter()

    with ThreadPoolExecutor() as executor:
        # 注意：submit(fun, arg1, arg2)的参数， 并且有返回值
        f1 = executor.submit(task, 1, "task1")
        f2 = executor.submit(task, 2, "task2")

        print(f1.result())
        print(f2.result())   


    with ThreadPoolExecutor() as executor:
        # 注意：map(func, *args1, *args2)的参数， 并且有返回值
        results = executor.map(task, [1, 2], ["task1", "task2"])
        for result in results:
            print(result)

    finish = perf_counter()
    print(f"It took {finish-start} second(s) to finish.")

# main()





#  Lock
# lock.acquire(), lock.release()

from threading import Lock

def task(id, lock):
    lock.acquire()

    print(f'Starting the task {id}...')
    sleep(1)
    print(f'Done with task {id}')

    lock.release()

def main():
    lock = Lock()
    t1 = Thread(target=task, args=(1, lock))
    t2 = Thread(target=task, args=(2, lock))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("main thread done")

# main()