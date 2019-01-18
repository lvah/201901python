
import threading
import time
import _thread



class MyThread(threading.Thread):
    def __init__(self, jobName):
        super(MyThread, self).__init__()
        self.jobName = jobName

    # 重写run方法， 实现多线程， 因为start方法执行时， 调用的是run方法;
    # run方法里面编写的内容就是你要执行的任务；
    def run(self):
        print("这是一个需要执行的任务%s。。。。。" %(self.jobName))
        print("当前线程的个数:", threading.active_count() )
        time.sleep(1)
        print("当前线程的信息:", threading.current_thread())
if __name__ == '__main__':
    t1 = MyThread("name1")
    t2 = MyThread("name2")
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("程序执行结束.....")