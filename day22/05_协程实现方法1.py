"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

from collections import Iterable


def job():
    for i in range(10):
        print(i)
        yield  "result: %s" %(i)

# 函数里面包含yield关键字， 调用函数返回的是生成器对象;
# yield工作原理: 如果遇到yield就停止运行， 调用next方法， 从yield停止的地方继续运行;
j = job()

# j.__next__()
# print(next(j))


# print(isinstance(j, Iterable))
for i in j:
    print(i)