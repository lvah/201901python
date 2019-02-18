"""
文件名: $NAME.py
日期: 18  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

官方中文文档: https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/


下表列出了主要的解析器,以及它们的优缺点:

解析器:使用方法:优势:劣势
Python标准库
        BeautifulSoup(markup, "html.parser")
        Python的内置标准库
        执行速度适中
        文档容错能力强
        Python 2.7.3 or 3.2.2)前 的版本中文档容错能力差


lxml
    HTML 解析器	BeautifulSoup(markup, "lxml")
    速度快
    文档容错能力强
    需要安装C语言库
lxml
    XML 解析器
    BeautifulSoup(markup, ["lxml-xml"])
    BeautifulSoup(markup, "xml")
    速度快
    唯一支持XML的解析器
    需要安装C语言库

html5lib
    BeautifulSoup(markup, "html5lib")
    最好的容错性
    以浏览器的方式解析文档
    生成HTML5格式的文档
    速度慢
    不依赖外部扩展




"""