#!/home/kiosk/anaconda2/envs/2048/bin/python
"""
文件名: .py
创建时间: 2019-01-16 14:
作者: lvah
联系方式: 976131979@qq.com
代码描述:

mydiff /etc/passwd /tmp/passwd > /home/kiosk/Desktop/test.html
"""
import difflib
import sys

if len(sys.argv) != 3:
    print("""
      Usage: %s   比较的文件1  比较的文件2  [>导出的文件路径 ]     
    """ %(sys.argv[0]))
else:
    filename1 = sys.argv[1]
    filename2 = sys.argv[2]
    try:
        with open(filename1) as f1, open(filename2) as f2:
            content1 = f1.read().splitlines(keepends=True)
            content2 = f2.read().splitlines(keepends=True)
    except Exception as e:
        print("比较错误， 错误原因: ", e)
    else:
        d = difflib.HtmlDiff()
        htmlContent = d.make_file(content1, content2)
        print(htmlContent)
