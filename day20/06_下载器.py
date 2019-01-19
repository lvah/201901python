"""
文件名: $NAME.py
日期: 19  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

from urllib.request import urlopen

# url = "http://imgsrc.baidu.com/forum/w%3D580/sign=16d420cb8b01a18bf0eb1247ae2e0761/22a4462309f790520522e1d900f3d7ca7bcbd51c.jpg"
# urlObj = urlopen(url)
# imgContent = urlObj.read()
# with open("doc/teiba.jpg", 'wb') as f:
#     f.write(imgContent)


DOWNLOAD_DIR = 'doc'


def download(url):
    try:
        urlObj = urlopen(url, timeout=3)
    except Exception as e:
        print("download %s error" % (url))
        imgContent = None
    else:
        # http://imgsrc.baidu.com/forum/w%3D580/sign=16d420cb8b01a18bf0eb1247ae2e0761/22a4462309f790520522e1d900f3d7ca7bcbd51c.jpg
        filename = url.split("/")[-1]
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


url = 'http://imgsrc.baidu.com/forum/w%3D580/sign=3cf8899b5d0fd9f9a0175561152cd42b/74094b36acaf2edd74ccef0e811001e93901931c.jpg'
download(url)
