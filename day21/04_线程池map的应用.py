"""
文件名: $NAME.py
日期: 20  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

import time


def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("%s函数运行时间:%.2f" % (f.__name__, end_time - start_time))
        return res

    return wrapper


# python3.2版本之后才有的;
import threading
from concurrent.futures import ThreadPoolExecutor, wait
from urllib.request import urlopen


def get_area(ip):
    url = "http://ip-api.com/json/%s" % (ip)
    urlObj = urlopen(url)

    # 服务端返回的页面信息, 此处为字符串类型
    pageContent = urlObj.read().decode('utf-8')

    # 2. 处理Json数据
    import json
    # 解码: 将json数据格式解码为python可以识别的对象;
    dict_data = json.loads(pageContent)

    print("""
                        %s
    所在城市: %s
    所在国家: %s

    """ % (ip, dict_data['city'], dict_data['country']))


@timeit
def use_ten_thread():
    #  1. 实例化线城池对象,线城池里面包含5个线程执行任务;
    pool = ThreadPoolExecutor(max_workers=10)

    # futures = []
    # for i in range(30):
    #     print("当前线程数:", threading.activeCount())
    #     ip = '12.13.14.%s' %(i+1)
    #     # 往线程池里面扔需要执行的任务， 返回的是一个对象(_base.Future())，
    #     f1 = pool.submit(get_area, ip)
    #     futures.append(f1)
    #
    # # 等待futures里面所有的子线程执行结束， 再执行主线程(join())
    # wait(futures)

    ips = ['12.13.14.%s' % (ip + 1) for ip in range(30)]
    pool.map(get_area, ips)


@timeit
def use_hundred_thread():
    #  1. 实例化线城池对象,线城池里面包含5个线程执行任务;
    pool = ThreadPoolExecutor(max_workers=100)

    # futures = []
    # for i in range(30):
    #     print("当前线程数:", threading.activeCount())
    #     ip = '12.13.14.%s' % (i + 1)
    #     # 往线程池里面扔需要执行的任务， 返回的是一个对象(_base.Future())，
    #     f1 = pool.submit(get_area, ip)
    #     futures.append(f1)
    #
    # wait(futures)

    ips = ['12.13.14.%s' % (ip + 1) for ip in range(30)]
    pool.map(get_area, ips)



if __name__ == '__main__':
    use_ten_thread()
    use_hundred_thread()
