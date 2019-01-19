"""
文件名: {03_生产者_消费者模型_类的继承实现}.py
日期: {2019}-{01}-{19}  {10}-{}
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

# 需求1： 给定200个ip地址,  可能开放端口为80,  443,  7001,  7002,  8000,  8080,  
9000(flask),  9001
         以http://ip:port形式访问页面以判断是否正常访问.

         1). 构建所有的url地址；===存储到一个数据结构中
         2). 依次判断url址是否可以成功访问


实现多线程:
        1). 实例化对象threading.Thread;
        2). 自定义类, 继承threading.Thread, 重写run方法(存储任务程序);






# 什么是生产者-消费者模型?
某个模块专门负责身缠数据， 可以认为是工厂;
另外一个模块负责对生产的数据进行处理的， 可以认为是消费者.
在生产者和消费者之间加个缓冲区(队列queue实现), 可以认为是商店.

生产者   -----》缓冲区   -----》 消费者


# 优点：
    1). 解耦：生产者和消费者的依赖关系减少;
    2). 支持并发；是两个独立的个体， 可并发执行;

"""


def create_data():
    """创建测试数据,  文件中生成200个IP"""
    with open('doc/ips.txt', 'w') as f:
        for i in range(200):
            f.write('172.25.254.%s\n' % (i + 1))
        print("测试数据创建完成!")

import time
import threading
from queue import Queue
from urllib.request import urlopen

class Producer(threading.Thread):
    def __init__(self, queue):
        super(Producer, self).__init__()
        self.q = queue


    def run(self):
        """生产测试需要的url地址http://ip:port"""
        ports = [80, 443, 7001, 7002, 8000, 8080, 9000, 9001]
        with open('doc/ips.txt') as f:
            for line in f:
                ip = line.strip()
                for port in ports:
                    url = "http://%s:%s" %(ip, port)
                    time.sleep(1)
                    self.q.put(url)
                    print("生产者生产url：%s" %(url))

class Consumer(threading.Thread):

    def __init__(self, queue):
        super(Consumer, self).__init__()
        self.q = queue


    def run(self):
        
      
       url = self.q.get()
       try:
           urlObj = urlopen(url)     
       except Exception as e:
           print("%s不可访问" %(url))
       else:
           pageContentSize = len(urlObj.read().decode('utf-8'))
           print("%s可以访问, 页面大小为%s" %(url, pageContentSize))


   


def main():
    q = Queue()
    p = Producer(q)
    p.start()

    for i in range(400):
        c = Consumer(q)
        c.start()

if __name__ == '__main__':
#    create_data()
     main()




