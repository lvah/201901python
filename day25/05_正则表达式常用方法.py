"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

# regular experssion
import re

# *************************match方法*************************8
#       match尝试从字符串的起始位置开始匹配;
#           - 如果起始位置没有匹配成功， 返回None;
#           - 如果起始位置匹配成功， 返回一个对象， 通过group方法获取匹配的内容;
# Try to apply the pattern at the start of the string, returning
#     a match object, or None if no match was found.
aObj = re.match(r'we', 'wetoshello')
print(aObj)
print(aObj.group())

# \d 单个数字
# \D \d的取反 , 除了数字之外
bObj = re.match(r'\d', '1westos')
if bObj:
    print(bObj.group())

bObj = re.match(r'\D', '_westos')
if bObj:
    print(bObj.group())

#  *****************************findall********************
#  findall会扫描整个字符串， 获取匹配的所有内容;
res = re.findall(r'\d\d', '阅读数为2 点赞数为10')
print(res)

# *************************search*******************8
# search会扫描整个字符串， 只返回第一个匹配成功的内容的SRE对象;
#           - 如果起始位置没有匹配成功， 返回None;
#           - 如果起始位置匹配成功， 返回一个对象， 通过group方法获取匹配的内容;

resObj = re.search(r'\d', '阅读数为8 点赞数为10')

if resObj:
    print(resObj.group())
