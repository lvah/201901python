"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

$ 1). Pipe管道，进程间通信的方式, l类似于 ls | wc -l;
# 2). Pipe()返回两个连接对象, 分别代表管道的两边;
# 3). 管道通信操作的方法: send(), recv;
# 4). 管道间的通信是双向的， 既可以发送，也可以接收；
"""

import multiprocessing
# 线程通信=====(队列) ---- from queue import Queue
# 进程池中进程通信=====(队列) --- from multiprocess.Manager import Queue
# 多进程通信=========(队列)   ---- from multiprocess import Queue
import time
def after(conn):
    while True:
        print("接收到数据:", conn.recv())
        time.sleep(1)
def before(conn):
    while True:
        data = [42, None, 34, 'hello']
        conn.send(data)
        print("正在发送数据：%s" % (data))
        time.sleep(1)

def main():
    # send recv
    before_conn, after_conn = multiprocessing.Pipe()

    p1 = multiprocessing.Process(target=after, args=(after_conn,))
    p1.start()

    p2 = multiprocessing.Process(target=before, args=(before_conn,))
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
