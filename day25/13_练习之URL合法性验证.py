"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 


问题描述:
    检查某段给定的文本是否是一个符合需要的URL；

思路:
    1). 检查URL是否以web浏览器普遍采用的通信协议方案开头: http, https, ftp file
    2). 协议后面紧跟 ://
    3).  协议后面字符任意;




"""
import re
def isUrl(url):
    pattern = re.compile(r'^(http|https|ftp|file)://.+$')
    resObj = re.search(pattern, url)
    if resObj:
        return  True
    return  False


if __name__ == '__main__':
    print(isUrl('file:///tmp'))
    print(isUrl('http://www.baidu.com'))
    print(isUrl('https://www.baidu.com'))
    print(isUrl('ftp://www.baidu.com'))
