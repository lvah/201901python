"""
文件名: .py
创建时间: 2019-01-16 13:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""
import difflib

filename1 = '/etc/passwd'
filename2 = '/tmp/passwd'

with open(filename1) as f1, open(filename2) as f2:
    content1 = f1.read().splitlines(keepends=True)
    content2 = f2.read().splitlines(keepends=True)


d = difflib.HtmlDiff()
htmlContent = d.make_file(content1, content2)

with open('doc/passwdDiff.html', 'w') as f:
    f.write(htmlContent)

