"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

拷贝的原理:
    1). 读取源文件的内容;
    2). 写入新的文件中;




"""
import os
import time
import multiprocessing  # 进行进程间的通信, Queue
from queue import Queue


def copyFileTask(oldFolderName, newFolderName, filename, queue):
    """
    import os
    # 拼接生成绝对路径
    os.path.join('/mnt', 'file')
    '/mnt/file'
    os.path.join('/mnt/', 'file')
    '/mnt/file'


    :param oldFolderName: /root/day21/
    :param newFolderName: /root/day21_backup_201901
    :param filename: file1
    :return:
    """
    # 两者相同的效果， with语句执行节航速后， 自动关闭文件对象;
    # with open('/etc/passwd') as f:
    #     pass

    # f = open('/etc/passwd')
    # with f:
    #     pass

    fr = open(os.path.join(oldFolderName, filename), 'rb')
    fw = open(os.path.join(newFolderName, filename), 'wb')
    with fr, fw:
        content = fr.read(1024*3)
        while content:
            fw.write(content)
        queue.put(filename)
        # print(queue.qsize())

def main():
    # 判断备份目录是否存在
    while True:
        # oldFolderName = input("请输入备份的目录名:")
        oldFolderName ="/var/log/"
        if os.path.exists(oldFolderName):
            break

    dateName = time.strftime('_%Y_%m_%d_%H_%M')  # '2019_01_20'
    newFolderName = oldFolderName + '_备份' + dateName
    if os.path.exists(newFolderName):
        os.rmdir(newFolderName)
    # 新建备份的目录;
    os.mkdir(newFolderName)
    print("正在创建备份目录%s....." % (newFolderName))
    # 获取备份目录中的所有文件名;
    fileNames = os.listdir(oldFolderName)

    # 队列， 存储已经备份的文件;
    # ****如果是用进程池，那么就需要使用Manager().Queue()队列才能在各子进程间通信，否则沒用
    queue = multiprocessing.Manager().Queue()
    # queue = Queue()

    pool = multiprocessing.Pool(4)

    for name in fileNames:

        # 给进程池分配任务
        pool.apply_async(copyFileTask, args=(oldFolderName,
                                             newFolderName,
                                             name,
                                             queue))

    # 100个文件, 1个文件   1%


    num = 0  # 当前备份的文件数
    allNum = len(fileNames)  # 总备份的文件数
    # print(num, allNum)
    while num < allNum:
        # print(queue.qsize())
        queue.get()
        num += 1
        copyRate = num / allNum  # 0.2322
        # \r使得光标不换行;
        print("\r\r备份的进度为%.2f%%" % (copyRate * 100), end='')
    pool.close()
    pool.join()
    print("备份成功;")

if __name__ == '__main__':
    main()
