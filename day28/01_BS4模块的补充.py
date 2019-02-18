"""
文件名: $NAME.py
日期: 18  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
import re

from bs4 import BeautifulSoup


html = """
<html>
<head><title class='title'>story12345</title></head>
<body>
<p class="title" name="dromouse">The Dormouse's story</p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><span>westos</span><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister1" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>

<input type="text">
<input type="password">
"""

#
soup = BeautifulSoup(html, 'html.parser')
# 需要安装第三方模块lxml；
# soup = BeautifulSoup(html, 'lxml')

# 1. 返回符合条件的第一个标签内容
print(soup.title)
print(soup.p)
print(soup.find('p', class_=re.compile(r'^ti.*?')))


# 2. 返回符合条件的所有标签内容
print(soup.find_all('p'))
print(soup.find_all('p', class_='title', text=re.compile(r'.*?story.*?')))



# 3. 获取符合条件的p标签或者a标签
print(soup.find(['title', 'a']))
print(soup.find_all(['title', 'a']))
print(soup.find_all(['title', 'a'], class_=['title', 'sister']))


# 4. CSS匹配
# 标签选择器
print(soup.select("title"))
# 类选择器(.类名)
print(soup.select(".sister"))
# id选择器(#id名称)
print(soup.select("#link1"))
# 此处不支持正则表达式;
# print(soup.select(re.compile("#link\d+")))
# 属性选择器()
print(soup.select("input[type='password']"))
