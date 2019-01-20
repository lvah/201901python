"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 
# 进程间通信: 生产者消费者模型, socket


# 请你说说进程间通信的集中方式?
"""


import multiprocessing
# 线程通信=====(队列) ---- from queue import Queue
# 进程池中进程通信=====(队列) --- from multiprocess.Manager import Queue
# 多进程通信=========(队列)   ---- from multiprocess import Queue
import time
class Producer(multiprocessing.Process):
    def __init__(self, queue):
        super(Producer, self).__init__()
        self.queue = queue
    def run(self):
        # 将需要通信的数据写入队列中;
        for i in range(10):
            self.queue.put(i)
            time.sleep(0.1)
            print("传递消息， 内容为%s" %(i))
class Consumer(multiprocessing.Process):
    def __init__(self, queue):
        super(Consumer, self).__init__()
        self.queue = queue
    def run(self):
        while True:
            time.sleep(0.1)
            recvData = self.queue.get()
            print("接受到另一进程传递的数据: %s" %(recvData))


if __name__ == '__main__':
    q =  multiprocessing.Queue()
    p1 = Producer(q)
    c1 = Consumer(q)

    p1.start()
    c1.start()
    p1.join()
    c1.join()










