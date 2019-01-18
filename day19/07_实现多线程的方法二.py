
import threading
import time
import _thread
def job():
    print("这是一个需要执行的任务。。。。。")
    print("当前线程的个数:", threading.active_count() )
    time.sleep(1)
    print("当前线程的信息:", threading.current_thread())



if __name__ == '__main__':
    # c创建多线程时， 需要制定该线程执行的任务
    t1 = threading.Thread(target=job )
    t2 = threading.Thread(target=job)
    t1.start()
    t2.start()
    print(threading.active_count())

    # 出现的问题: 主线程执行结束， 但是子线程还在运行。
    # 等待所有的子线程执行结束之后， 再执行主线程
    t1.join()
    t2.join()
    print("程序执行结束.....")