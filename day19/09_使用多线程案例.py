# 1. 简单的爬虫:
import threading
import time
from urllib.request import urlopen


def timeit(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = f(*args, **kwargs)
        end_time = time.time()
        print("%s函数运行时间:%.2f" % (f.__name__, end_time - start_time))
        return res

    return wrapper


def get_addr(ip):
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
def main():
    ips = ['12.13.14.%s' % (i + 1) for i in range(10)]
    threads = []
    for ip in ips:
        t = threading.Thread(target=get_addr, args=(ip, ))
        threads.append(t)
        t.start()

    [thread.join() for thread in threads]

if __name__ == '__main__':
    main()
