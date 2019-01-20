"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 
# 1.理解：
    如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows
    没有fork调用，难道在Windows上无法用Python编写多进程的程序？

    由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing
    模块就是跨平台版本的多进程模块。

    multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了
    启动一个子进程并等待其结束：
    创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。

    join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。


# 2. Process使用属性及方法

    Process 类用来描述一个进程对象。创建子进程的时候，只需要传入一个执行函数和函数的参数即可完成 Process 示例的创建。
                star() 方法启动进程，
                join() 方法实现进程间的同步，等待所有进程退出。
                close() 用来阻止多余的进程涌入进程池 Pool 造成进程阻塞。

    multiprocessing.Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
                target 是函数名字，需要调用的函数
                args 函数需要的参数，以 tuple 的形式传入


#
"""

import multiprocessing
def job():
    print("当前子进程的名称%s....." %(multiprocessing.current_process()))

# 通过类的实例化实现
p1 = multiprocessing.Process(target=job, name="我的第一个子进程")
p1.start()

# 通过类的实例化实现
p2 = multiprocessing.Process(target=job, name="我的第2个子进程")
p2.start()


# join方法， 等待所有的子进程执行结束， 再执行主进程
p1.join()
p2.join()
print("任务执行结束.....")







