"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


#

"""

import multiprocessing
def work(f, item, lock):
    # lock.acquire()
    try:
        with open(f, 'a+') as f:
            f.write("a %s task\n" % (item))
    except Exception as e:
        print("产生异常...")
    # finally:
        # lock.release()

def main():
    # 1). 实例化一个进程锁
    lock = multiprocessing.Lock()

    filename = 'doc/my.log'
    processes = []
    for i in range(4):
        p1 = multiprocessing.Process(target=work, args=(filename, i,lock))
        p1.start()
        processes.append(p1)

    [process.join() for process in  processes]




if __name__ == '__main__':
    main()
