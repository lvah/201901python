"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



url规律:
    https://tieba.baidu.com/p/5752826839?pn=1
    https://tieba.baidu.com/p/5752826839?pn=2
    https://tieba.baidu.com/p/5752826839?pn=3


图片html分析:
        <img class="BDE_Image" src="https://imgsa.baidu.com/forum/
        w%3D580/sign=8be466fee7f81a4c2632ecc1e7286029/bcbb0d338744ebf
        89d9bb0b5d5f9d72a6259a7aa.jpg" size="350738" changedsize="true"
        width="560" height="995">

        <img class="BDE_Image" src="https://imgsa.baidu.com/forum/
        w%3D580/sign=64e6bdda38a85edffa8cfe2b795609d8/4efebd315c60
        34a886086c0bc71349540b2376aa.jpg" size="286672" changedsize
        ="true" width="560" height="995">
"""

from urllib.request import urlopen
from urllib.error import URLError
import re


def get_page(url):
    """
    获取页面内容

    :param url:
    :return:
    """
    try:
        urlObj = urlopen(url)
    except URLError as e:
        print("爬取%s失败...." % (url))
    else:
        # 默认是bytes类型, 需要的是字符串, 二进制文件不能decode
        content = urlObj.read()
        return content


def parser_content(content):
    """
    解析页面内容, 获取所有的图片链接
    :param content:
    :return:
    """
    content = content.decode('utf-8').replace('\n', ' ')
    pattern = re.compile(r'<img class="BDE_Image".*? src="(https://.*?\.jpg)".*?">')
    imgList = re.findall(pattern, content)
    return imgList


def get_page_img(page):
    url = "https://tieba.baidu.com/p/5752826839?pn=%s" %(page)
    content = get_page(url)
    print(content)

    # with open('tieba.html', 'w') as f:
    #     f.write(content)
    if content:
        imgList = parser_content(content)
        for imgUrl in imgList:
            # 依次遍历图片的每一个链接, 获取图片的内容;
            imgContent = get_page(imgUrl)
            # https://imgsa.baidu.com/forum/w%3D580/sign=a05cc58f2ca446237ecaa56aa8237246/94cd6c224f4a20a48b5d83329c529822700ed0e4.jpg
            imgName = imgUrl.split('/')[-1]
            with open('img/%s' %(imgName), 'wb') as f:
                f.write(imgContent)
                print("下载图片%s成功...." %(imgName))
if __name__ == '__main__':
    for page in range(1, 11):
        print("正在爬取第%s页的图片...." %(page))
        get_page_img(page)


