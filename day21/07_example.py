"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""


import os
import time
import multiprocessing
from queue import Queue

def copyFileTask(oldFolderName,newFolderName,filename,queue):
    fr = open(os.path.join(oldFolderName,filename),'rb')
    fw = open(os.path.join(newFolderName,filename),'wb')
    with fr,fw:
        content = fr.read(1024)
        while content:
            fw.write(content)

        print('write %s' %(filename))
        queue.put(filename)

def main():
    oldFolderName = input('请输入备份的目录名：')
    dateName = time.strftime('%Y_%m_%d_%H_%M')
    newFolderName = oldFolderName+'_备份'+dateName
    os.mkdir(newFolderName)
    print('正在创建备份目录%s...'%(newFolderName))
    fileNames = os.listdir(oldFolderName)
    queue = multiprocessing.Manager().Queue()
    pool = multiprocessing.Pool(2)
    for name in fileNames:
        # print("test", name)
        pool.apply_async(copyFileTask,args=(oldFolderName,
                                            newFolderName,
                                            name,
                                            queue))
    num = 0
    allNum = len(fileNames)
    while num < allNum:
        queue.get()
        num+=1
        copyRate = num/allNum
        print('\r\r备份的进度为%.2f%%'%(copyRate*100),end ='')

    pool.close()
    pool.join()
    print('备份成功')

if __name__ == '__main__':
    main()
