

import threading
import time
import _thread
def job():
    print("这是一个需要执行的任务。。。。。")
    print("当前线程的个数:", threading.active_count() )
    print("当前线程的信息:", threading.current_thread())
    time.sleep(100)
if __name__ == '__main__':
    # c创建多线程时， 需要制定该线程执行的任务
    _thread.start_new_thread(job, ())
    _thread.start_new_thread(job, ())

    # job()
    while True:
        pass
