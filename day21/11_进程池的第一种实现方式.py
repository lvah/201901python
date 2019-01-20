"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


在使用Python进行系统管理时，特别是同时操作多个文件目录或者远程控制多台主机，
并行操作可以节约大量时间，如果操作的对象数目不大时，还可以直接适用Process类动态
生成多个进程，几十个尚可，若上百个甚至更多时，手动限制进程数量就显得特别繁琐，
此时进程池就显得尤为重要。

进程池Pool类可以提供指定数量的进程供用户调用，当有新的请求提交至Pool中时，
若进程池尚未满，就会创建一个新的进程来执行请求；若进程池中的进程数已经达到
规定的最大数量，则该请求就会等待，直到进程池中有进程结束，才会创建新的进程来
处理该请求。



"""
import multiprocessing


def job(id):
    print("start %d...." % (id))
    print("end %d...." % (id))

# 创建进程池对象
pool = multiprocessing.Pool(processes=4)

# 给进程池分配任务;
for i in range(10):
    pool.apply_async(job, args=(i + 1,))
pool.close()
# 等待所有的子进程执行结束， 关闭进程池对象;
pool.join()
print("所有任务执行结束.....")