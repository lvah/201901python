"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows
没有fork调用，难道在Windows上无法用Python编写多进程的程序？

由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing
模块就是跨平台版本的多进程模块。

multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了
启动一个子进程并等待其结束：
创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。

join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。

"""

import multiprocessing



class MyProcess(multiprocessing.Process):
    # 重写run方法=====start方法默认执行run方法
    def run(self):
        print("当前子进程的名称%s....." % (multiprocessing.current_process()))

p1 = MyProcess(name="first")
p1.start()
p2 = MyProcess(name="second")
p2.start()

p1.join()
p2.join()
print("all finish.....")







