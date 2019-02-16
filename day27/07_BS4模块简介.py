"""
文件名: $NAME.py
日期: 16  
作者: lvah
联系: xc_guofan@qq.com
代码描述:

# 0. 概括
- 获取页面: urllib, requests
- 解析页面信息: 正则表达式, BeautifulSoup4(BS4)


# 1. BS4简介
Beautiful Soup提供一些简单的、python式的函数用来处理导航、搜索、修改分析树等功能。它是一个
工具箱，通过解析文档为tiful Soup自动将输入文档转换为Unicode编码，输出文档转换为utf-8编码。
你不需要考虑编码方式，除非文档没有指定一个编一下原始编码方式就可以了。



# 2. BS4的4种对象



## 2-1. BeautifulSoup对象
## 2-2. Tag对象
Tag就是html中的一个标签，用BeautifulSoup就能解析出来Tag的具体内容，
具体的格式为soup.name,其中name是html下的标签。



"""
import re

from bs4 import BeautifulSoup
html = """
<html>
<head><title>story12345</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>westos</span><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister1" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())

# 1. 根据标签获取内容;


# ******************标签的常用属性************************
# # 根据格式化， 如果title只有一个， 根据标签可以获取
# print(soup.title)
# print(type(soup.title))
# print(soup.title.name)  # 标签的名称

# 获取标签里面的属性信息
print(soup.a.attrs)
print(soup.a.attrs['href'])



# # *******************标签常用的方法*************************
# #get方法用于得到标签下的属性值，注意这是一个重要的方法，在许多场合都能用到，比如你要得到<img src=”#”>标签下的图像url,那么就可以用soup.img.get(‘src’)
# print(soup.a.get('href'))
# print(soup.a.get('class'))
#
#
#
# # string得到标签下的文本内容，只有在此标签下没有子标签，或者只有一个子标签的情况下才能返回其中的内容，否则返回的是None;
# # get_text()可以获得一个标签中的所有文本内容，包括子孙节点的内容，这是最常用的方法
# print(soup.a.string)    # 标签里面的内容
# print(soup.a.get_text())
#
# # *******************对获取的属性信息进行修改***********************
# print(soup.a.get('href'))
# soup.a['href'] = 'http://www.baidu.com'
# print(soup.a.get('href'))
# print(soup.a)
#
#
#
#
# # 2. 面向对象的匹配
#
# # 查找符合条件的所有标签;
# aTagObj =  soup.find_all('a')
# print(aTagObj)
# for item in aTagObj:
#     print(item)
#

#  需求: 获取所有的a标签， 并且类名为"sister"
# aTagObj = soup.find_all('a', class_="sister")
# print(aTagObj)

# 3. 根据内容进行匹配
print(soup.find_all(text="story"))
print(soup.find_all(text=re.compile('story\d+')))