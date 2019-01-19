"""
文件名: {02_队列与线程}.py
日期: {2019}-{01}-{19}  {09}-{}
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

# 1). 理论上多线程执行任务是不能获取返回结果的， 因此需要一个容器来存储产生的数据；
# 2). 容器该如何选择? list(栈， 队列), tuple(元组是不可变的， 不可使用),
#         set(集合默认会去重， 所以不选择), dict
#        选择队列类型存储(FIFO===first input first output)





"""

import threading
from mytimeit import timeit
from queue import Queue


def job(li, queue):
    queue.put(sum(li))   # 将任务的执行结果存储到队列中;
@timeit
def use_thread():
    # 实例化一个队列， 用来存储每个线程执行的结果
    q = Queue()
    # q.get()  -- 出队
    # q.put(value)  -- 入队

    lis = [range(5), range(2,10), range(1000, 20000), range(3000, 10000)]
    # create 5 threads
    threads = []
    for li in lis:
        t = threading.Thread(target=job, args=(li, q))
        t.start()
        threads.append(t)
    [thread.join() for thread in threads]
    # 从队列中拿出所有线程执行的结果;
    results  = [q.get() for li in lis]
    print(results)

if __name__ == "__main__":
    use_thread()
