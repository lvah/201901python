"""


一个进程里面宾然有一个主线程
操作线程的模块:
    thread
    threading
"""



import _thread
import threading
import time


def job():
    print("这是一个需要执行的任务。。。。。")
    print("当前线程的个数:", threading.active_count() )
    print("当前线程的信息:", threading.current_thread())
    time.sleep(100)
if __name__ == '__main__':
    job()


