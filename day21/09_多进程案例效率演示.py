"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
import threading
import time

from mytimeit import  timeit
import multiprocessing
def job(li):
    return  sum(li)
@timeit
def use_thread():
    li = range(1, 100000000)
    # create 5 threads
    threads = []
    for i in range(5):
        t = threading.Thread(target=job, args=(li, ))
        t.start()
        threads.append(t)
    [thread.join() for thread in  threads]

@timeit
def use_no_thread():
    li = range(1, 100000000)
    for i in range(5):
        job(li)


@timeit
def use_process():
    li = range(1, 100000000)
    # create 5 threads
    processes = []
    # 1). 开启的进程书是有瓶颈的， 取决于CPU个数,
    # 2). 如果处理的数据比较小， 不建议使用多进程,因为创建进程和销毁进程需要时间;
    # 3). 如果处理数据足够大， 0《进程数《cpu个数;
    for i in range(5):
        p = multiprocessing.Process(target=job, args=(li,))
        p.start()
        processes.append(p)
    [process.join() for process in processes]


if __name__ == "__main__":
    use_thread()
    use_process()
    use_no_thread()
