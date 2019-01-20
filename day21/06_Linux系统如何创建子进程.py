"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

1). Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，
调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（
称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

2). 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork
出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()
就可以拿到父进程的ID。

3). Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松
创建子进程：


原理:
    父进程和子进程:, 如果父进程结束， 子进程也随之结束;
    先有父进程， 再有子进程. 类Linux系统中(redhat,mac), fork函数;


常用函数:
    os.fork()
    os.getpid()   # 获取当前进程的pid  （process id）
    os.getppid()    # 获取当前进程的父进程pid (parent process id)
"""
import os

print("当前进程(pid=%d)正在运行......." %(os.getpid()))
# 在pycharm编写代码， 程序的父进程就是pycharm;
print("当前进程的父进程为(pid=%d)正在运行....." %(os.getppid()))
print("开始创建子进程.....")

pid = os.fork()
if  pid == 0:
    print("这是子进程返回的是0， 子进程的pid为%d, 父进程为%d" %(os.getpid(), os.getppid()))
else:
    print("这是父进程返回的，返回值为子进程的pid， 为%d" %(pid))







