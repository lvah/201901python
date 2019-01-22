"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""


import time

def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("%s函数运行时间:%.8f" % (f.__name__, end_time - start_time))
        return res

    return  wrapper