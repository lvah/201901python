"""
文件名: {utils}.py
日期: {2019}-{01}-{19}  {12}-{}
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

from urllib.error import URLError
from urllib.request import urlopen
import hashlib


def md5(input_str):
    m = hashlib.md5()
    m.update(input_str)
    return m.hexdigest()


def get_url_length(url):
    try:
        content_length = urlopen(url).read()
        if content_length:
            return int(content_length)
    except URLError as e:
        print(e)

    return -1


def get_source_size(url, retry_times=1):
    for i in range(retry_times):
        try:
            return get_url_length(url)
        except:
            print("can't get size of %s, try %d" % (url, i))
        raise Exception("can't get size of %s, try %d" % (url, i))


def readalbe_size(content_length):
    if content_length < 1024:
        return "%d b" % (content_length)

    kb = content_length / 1024.0
    if kb < 1000:
        return "%.3f Kb" % (kb)

    mb = kb / 1024.0
    if mb < 1000:
        return "%.3f Mb" % (mb)

    gb = mb / 1024.0
    if gb < 1000:
        return "%.3f Gb" % (gb)

    tb = gb / 1024.0
    return "%.3f Tb" % (tb)


def download(url, start, end, param):
    return  urlopen(url).read()


def download_chunk(url, start, end, retry_times):
    for i in range(retry_times):
        try:
            return download(url, start, end, retry_times - 1)
        except:
            print("can't download %s(%d-%d), try %d" % (
                url, start, end, retry_times))

    raise Exception("can't download %s(%d-%d), try %d" % (
        url, start, end, retry_times))
