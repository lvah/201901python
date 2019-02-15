"""
文件名: $NAME.py
日期: 15  
作者: lvah
联系: xc_guofan@qq.com
代码描述:



^((https|http|ftp|rtsp|mms)?:\/\/)[^\s]+


# ^: 以什么开头
# (https|http|ftp|rtsp|mms): 代表一个分组
# [https|http|ftp|rtsp|mms]: 代表一个分组




^:
    如果没有在[]里面的时候， 代表以什么开头；
    如果在[]里面的时候，代表除了...之外;
"""
# \d ==== [0-9] === [0123456789]
import re

url = 'http://www.baidu.com'
pattern = r'^((https|http|ftp|rtsp|mms)?:\/\/)\S+'

# 进行分组的时候， findall方法只返回分组里面的内容;
# print(re.findall(pattern, url))

resObj = re.search(pattern, url)
if resObj:
    # group方法会返回匹配的所有内容;
    print(resObj.group())
    # groups方法返回分组里面的内容;
    print(resObj.groups())