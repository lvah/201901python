"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

_thread, threading, multiprocessing



# 池子， 只放制定个线程(10个线程),




"""

# python3.2版本之后才有的;
from concurrent.futures import  ThreadPoolExecutor

def job(num):
    # 需要执行的任务
    print("这是一个%s任务" %(num))
    return  "执行结果:%s" %(num)
if __name__ == '__main__':
    #  1. 实例化线城池对象,线城池里面包含5个线程执行任务;
    pool = ThreadPoolExecutor(max_workers=5)
    futures = []
    for i in range(1000):
        # 往线程池里面扔需要执行的任务， 返回的是一个对象(_base.Future())，
        f1 = pool.submit(job, i)
        futures.append(f1)

    # 判断第一个任务是否执行结束；
    futures[0].done()

    # 获取任务的执行结果;
    print(futures[0].result())









