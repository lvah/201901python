"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from concurrent.futures import  ProcessPoolExecutor


def job(id):
    print("start %d...." % (id))
    print("end %d...." % (id))

pool = ProcessPoolExecutor(max_workers=4)
#
# for id in range(10):
#     # 分配任务给子进程， 并且返回一个Future对象;
#     f1 = pool.submit(job, args=(id))
#     # 判断子进程是否执行结束?
#     print(f1.done())
#     # 查看该子进程执行的结果
#     print(f1.result())

pool.map(job, range(10))