"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



gevent是第三方库,通过greenlet实现协程,其基本思想:
    当一个greenlet遇到IO操作时,比如访问网络,就自动切换到其他的greenlet,
    等到IO操作完成,再在适当的时候切换回来继续执行。由于IO操作非常耗时,经常
    使程序处于等待状态,有了gevent为我们自动切换协程,就保证总有greenlet在
    运行,而不是等待IO。



Gevent使用说明
    monkey:             可以使一些阻塞的模块变得不阻塞,机制:遇到IO操作则自动切换,
                        手动切换可以用gevent.sleep()或者yield;
    gevent.sleep(0)     (将爬虫代码换成这个,效果一样可以达到切换上下文)
    gevent.spawn        启动协程,参数为函数名称,参数名称
    gevent.joinall      等待所有的协程执行结束;
    gevent.join()

"""
import threading

from gevent import monkey
import gevent

# 可以使一些阻塞的模块变得不阻塞,x修改python内置的标准库;
monkey.patch_all()


def job(n):
    for i in range(n):
        print(gevent.getcurrent(), i, n)
        print("当前线程数:", threading.active_count())
        gevent.sleep(1)


def main():
    # 创建协程， 分配任务;
    g1 = gevent.spawn(job, 1)
    g2 = gevent.spawn(job, 2)
    g3 = gevent.spawn(job, 3)

    # #
    # g1.join()
    # g2.join()
    # g3.join()
    print("当前线程数:", threading.active_count())
    gevent.joinall([g1, g2, g3])
    print("任务执行结束.....")


if __name__ == '__main__':
    main()
