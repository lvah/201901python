"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
import time
from multiprocessing.managers import BaseManager

# 1. 连接Master端， 获取共享的队列;ip是master端的ip， port'也是master端manager进程绑定的端口;
slave = BaseManager(address=('172.25.254.250', 4000), authkey=b'westos')

# 2. 注册队列， 获取共享的队列内容;
BaseManager.register('get_task_queue')
BaseManager.register('get_result_queue')

# 3. 连接master端;
slave.connect()

# 4. 通过网络访问共享的队列;
task = slave.get_task_queue()
result = slave.get_result_queue()

# 5. 读取管理端共享的任务， 并依次执行;
for i in range(500):
    n = task.get()
    print("slave2: 运行任务 %d ** 2: " % (n))
    res = "slave2: %d ** 2 = %d" % (n, n ** 2)
    time.sleep(1)
    # 将任务的运行结果放入队列中;
    result.put(res)

print("执行结束........")


