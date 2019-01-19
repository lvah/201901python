"""
文件名: {04_线程同步之线程锁}.py
日期: {2019}-{01}-{19}  {11}-{}
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



# 1. 为什么需要线程锁?
    多个线程对同一个数据进行修改时， 可能会出现不可预料的情况.

# 2. 如何实现线程锁?

        # 1. 实例化一个锁对象;
            lock = threading.Lock()
        # 2. 操作变量之前进行加锁
        lock.acquire()
        # 3. 操作变量之后进行解锁
            lock.release()

"""

import threading
class AddThread(threading.Thread):
    def __init__(self, lock):
        super(AddThread, self).__init__()
        self.lock = lock
    def run(self):
        for i in range(1000000):
            # 2. 操作变量之前进行加锁
            self.lock.acquire()
            global  money
            money += 1  # money;  money+1; money=money+1;
            # 3. 操作变量之后进行解锁
            self.lock.release()

class ReduceThread(threading.Thread):
    def __init__(self, lock):
        super(ReduceThread, self).__init__()
        self.lock = lock
    def run(self):
        global money
        for i in range(1000000):
            # 2. 操作变量之前进行加锁
            lock.acquire()
            money -= 1
            # 3. 操作变量之后进行解锁
            lock.release()
if __name__ == '__main__':
    money = 0
    # 1. 实例化一个锁对象;
    lock = threading.Lock()
    t1 = AddThread(lock)
    t2 = ReduceThread(lock)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("当前金额:", money)
