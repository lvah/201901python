"""
文件名: $NAME.py
日期: 18  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

1. 解析页面模块比较:
        - 正则表达式是进行内容匹配，将符合要求的内容全部获取；

        - xpath()能将字符串转化为标签，它会检测字符串内容是否为标签，但是不能检
测出内容是否为真的标签；

        - Beautifulsoup是Python的一个第三方库，它的作用和 xpath 作用一样，都是用来解析html数据的相比之下;xpath的速度会快一点，因为xpath底层是用c来实现的
2.三者语法不同，正则表达式使用元字符，将所有获得内容与匹配条件进行匹配，
而xpath和bs4将获取的解析后的源码进行按条件筛选，筛选出想要的标签即根据标签属性来找到指定的标签，之后对标签进行对应内容获取;



#  xpath：全称XML PATH Language, 一种小型的查询语言;
# 支持的解析：
    XML格式
    html格式
    通过元素，和属性进行导航


"""

import lxml.etree as etree



# 1). 将html内容转化成xpath可以解析/匹配的格式;
html = """
<!DOCTYPE html>
<html>
<head lang="en">
    <title>xpath测试</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>
<div id="content">
    <ul id="ul">
        <li>NO.1</li>
        <li>NO.2</li>
        <li>NO.3</li>
    </ul>
    <ul id="ul2">
        <li>one</li>
        <li>two</li>
    </ul>
</div>
<div id="url">
    <a href="http:www.58.com" title="58">58</a>
    <a href="http:www.csdn.net" title="CSDN">CSDN</a>
</div>
</body>
</html>

"""
# print(type(html))
selector = etree.HTML(html)


# 2).
# //: 对全文进行扫描
# //div
# //div[@id="content"]
str = selector.xpath('//div[@id="content"]/ul[@id="ul"]/li/text()')
print(str)
print(type(str))

# 需求： 获取文件中div的属性id为”url“里面的所有a标签的href属性
str = selector.xpath('//div[@id="url"]/a/@href')
print(str)

# 获取符合条件的标签内容;
str = selector.xpath('//div"]').extract()
print(str)











