"""
文件名: .py
创建时间: 2019-01-16 13:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


# 1. 什么是difflib? 用来做什么?
difflib为python的标准库模块，无需安装。作用时对比文本之间的差异。
并且支持输出可读性比较强的HTML文档，与LInux下的diff 命令相似。
在版本控制方面非常有用。

# 2. 符号理解
符号    含义
'-'     包含在第一个系列行中，但不包含第二个。
'+'     包含在第二个系列行中，但不包含第一个。
' '     两个系列行一致
'?'     存在增量差异
'^'     存在差异字符






"""


import difflib
text1 = '''  1. Beautiful is better than ugly.
       2. Explicit is better than implicit.
       3. Simple is better than complex.
       4. Complex is better than complicated.
     '''.splitlines(keepends=True)

text2 = '''  1. Beautiful is better than ugly.
       3.   Simple is better than complex.
       4. Complicated is better than complex.
       5. Flat is better than nested.
     '''.splitlines(keepends=True)

# 实现linux里面的diff命令的功能;
# d = difflib.Differ()
# print("".join(list(d.compare(text1, text2))))
d = difflib.HtmlDiff()
htmlContent = d.make_file(text1, text2)

with open('doc/diff.html', 'w') as f:
    f.write(htmlContent)