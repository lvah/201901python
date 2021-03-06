"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


# 1.什么是进程？什么是线程？

进程是表示资源分配的基本单位，又是调度运行的基本单位。
例如，用户运行自己的程序，系统就创建一个进程，并为它分配资源，
包括各种表格、内存空间、磁盘空间、I/O设备等。然后，把该进程放
人进程的就绪队列。进程调度程序选中它，为它分配CPU以及其它有关资源，该进程才真正运行。


线程是进程中执行运算的最小单位，如果把进程理解为在逻辑上操作系统所完成的任务，
那么线程表示完成该任务的许多可能的子任务之一。例如，假设用户启子任务；在产生
工资单报表的过程中，用户又可以输人数据库查询请求，这又是一个子任务。


多线程就像是火车上的每节车厢，而进程就是火车。




# 2.多进程和多线程的区别？
- 数据共享、同步：
        1). 数据共享复杂，需要用IPC；数据是分开的，同步简单
        2). 因为共享进程数据，数据共享简单，但也是因为这个原因导致同步复杂
        各有优势
- 内存、CPU
        1). 占用内存多，切换复杂，CPU利用率低
        2). 占用内存少，切换简单，CPU利用率高
        线程占优
- 创建销毁、切换
        1). 创建销毁、切换复杂，速度慢
        2). 创建销毁、切换简单，速度很快
        线程占优
- 编程、调试
        1). 编程简单，调试简单
        2). 编程复杂，调试复杂
        进程占优
- 可靠性
        1). 进程间不会互相影响
        2). 一个线程挂掉将导致整个进程挂掉
        进程占优
- 分布式
        1). 适应于多核、多机分布式；如果一台机器不够，扩展到多台机器比较简单
        2). 适应于多核分布式
        进程占优



# 3.进程之间的通信方式以及优缺点？

管道， 信号量， 信号， 消息队列， 共享内存， 套接字


# 4.线程之间的通信方式？
锁机制：包括互斥锁、条件变量、读写锁
信号量机制(Semaphore)
信号机制(Signal)


# 5.什么时候用多线程?什么时候用多进程？
1）需要频繁创建销毁的优先用线程
2）需要进行大量计算的优先使用进程
3）可能要扩展到多机分布的用进程，多核分布的用线程
"""