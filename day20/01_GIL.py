"""
# python使用多线程， 一定运行速度快么? 为什么?
- GIL(global interpreter lock)
- python解释器中任意时刻都只有一个线程在执行;
- GIL执行过程:
    - 1). 设置一个GIL；
    - 2). 切换线程去准备执行任务(Runnale就绪状态)；
    - 3). 运行；
    - 4). 可能出现的状态:
            - 线程任务执行结束;
            - time.sleep()
            - 需要获取其他的信息才能继续执行(eg: 读取文件, 需要从网络下载html网页)
    - 5). 将线程设置为睡眠状态;
    - 5). 解GIL的锁；


多线程的应用场景: I/O密集型(input, output)     --- 爬虫
不建议使用多线程的场景: 计算密集型(cpu一直占用)









"""


import threading
from mytimeit import timeit


def job(li):
    return  sum(li)


@timeit
def use_thread():
    li = range(1, 10001)
    # create 5 threads
    threads = []
    for i in range(5):
        t = threading.Thread(target=job, args=(li, ))
        t.start()
        threads.append(t)
    [thread.join() for thread in  threads]

@timeit
def use_no_thread():
    li = range(1, 10001)
    for i in range(5):
        job(li)

if __name__ == "__main__":
    use_thread()
    use_no_thread()




