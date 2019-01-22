"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
import random
from queue import  Queue
# BaseManager: 提供了不同机器之间共享数据的一种方法(ip:port)
from multiprocessing.managers import  BaseManager

# 1. 创建存储任务需要的队列
task_queue = Queue()

# 2. 存储任务执行结果的队列
result_queue = Queue()


# 3. 将队列注册到网上(使得其他主机也可以访问)
BaseManager.register('get_task_queue', callable=lambda : task_queue)
BaseManager.register('get_result_queue', callable=lambda : result_queue)


# 绑定ip和端口， 并且来个暗号；
manager = BaseManager(address=('172.25.254.250', 4000), authkey=b'westos')


# 4. 启动manager对象， 开始共享队列
manager.start()
# 5. 通过网络访问共享的Queue对象;
# BaseManager.register会注册一个方法, 当调用方法时， 执行函数lambda : task_queue;
task = manager.get_task_queue()
result = manager.get_result_queue()

# 6. 往队列里面放执行任务需要的数据;
for i in range(1000):
    # 模拟有1000个数字；
    n = random.randint(1, 100)
    task.put(n)
    print("任务列表中加入任务: %d" %(n))

# 7. 从result队列中读取各个机器中任务执行的结果;
for i in range(1000):
    res = result.get()
    print("队列任务执行的result: %s" %(res))


#  8. 关闭manager对象， 取消共享的队列
manager.shutdown()






