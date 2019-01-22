"""
文件名: $NAME.py
日期: 22  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
import threading
from urllib.request import urlopen
from urllib.error import HTTPError
import gevent
from gevent import monkey
from concurrent.futures import ThreadPoolExecutor, wait
from mytimeit import timeit

monkey.patch_all()


def get_page_length(url):
    try:
        urlObj = urlopen(url)
    except HTTPError as e:
        print("捕获失败.....")
    else:
        pageContent = urlObj.read()
        # print("%s长度为%d" %(url, len(pageContent)))



# 做实验, 访问本地url, 因为获取网络的url与网速有关(网速不稳定)
urls = ['file:///usr/share/doc/HTML/en-US/index.html', 'file:///usr/share/doc/HTML/en-US/index.html',
        'file:///usr/share/doc/HTML/en-US/index.html', 'file:///usr/share/doc/HTML/en-US/index.html', ] * 30000


@timeit
def use_gevent():
    gevents = [gevent.spawn(get_page_length, url) for url in urls]
    gevent.joinall(gevents)
    print("协程执行结束.....")


@timeit
def use_thread():
    threads = []
    for url in urls:
        t = threading.Thread(target=get_page_length, args=(url,))
        t.start()
        threads.append(t)
    [thread.join() for thread in threads]


if __name__ == '__main__':
    use_thread()
    use_gevent()
