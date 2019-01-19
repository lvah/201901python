"""
文件名: $NAME.py
日期: 19  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

当你创建用户界面并想保持界面的可用性时，线程就特别有用。
没有线程，用户界面将变得迟钝，当你下载一个大文件或者执
行一个庞大的数据库查询命令时用户界面会长时间无响应。为
了防止这样情况发生，你可以使用多线程来处理运行时间长的
进程并且在完成后返回界面进行交互。



"""

import threading
from urllib.request import urlopen

DOWNLOAD_DIR = 'doc'
class DownloadThread(threading.Thread):
    def __init__(self, url):
        super(DownloadThread, self).__init__()
        self.url = url
    def run(self):
        try:
            urlObj = urlopen(self.url, timeout=3)
        except Exception as e:
            print("download %s error\n" % (self.url), e)
            imgContent = None
        else:
            # http://imgsrc.baidu.com/forum/w%3D580/sign=16d420cb8b01a18bf0eb1247ae2e0761/22a4462309f790520522e1d900f3d7ca7bcbd51c.jpg
            filename = self.url.split("/")[-1]
            # 'wb' === 写的是二进制文件(图片， 视频， 动图， .pdf)
            # 'ab'
            with open("%s/%s" % (DOWNLOAD_DIR, filename), 'ab') as f:
                # 如果文件特别大的时候， 建议分块下载;每次只读取固定大小， 防止占用内存过大.
                while True:
                    imgContentChunk = urlObj.read(1024 * 3)
                    if not imgContentChunk:
                        break
                    f.write(imgContentChunk)
                    # 可以添加下载的程度(百分率);

                print("%s下载成功" % (filename))

url1  = "ftp://172.25.254.250/pub/book/python/01_MIT.Introduction.to.Computation.and.Programming.Using.Python%20revised%20and%20expanded%20edition.pdf"
# url2 = "ftp://172.25.254.250/pub/book/python/01_python%E6%A0%B8%E5%BF%83%E7%BC%96%E7%A8%8B.pdf"
# url3 = "ftp://172.25.254.250/pub/book/python/02_Python%20Cookbook%EF%BC%88%E7%AC%AC3%E7%89%88%EF%BC%89%E4%B8%AD%E6%96%87%E7%89%88.pdf"
url2 = 'ftp://172.25.254.250/pub/book/python/02_interview_exercise.pdf'
url3 = "ftp://172.25.254.250/pub/book/python/02_python-data-structure-cn.pdf"

urls = [url1, url2, url3]


for url in urls:
    thread = DownloadThread(url)
    thread.start()









