"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

通配符：
    *:
    ?: 代表单个字符
    .: 当前目录
    ..:当前目录的上一级目录
    [0-9]: 单个字符为0~9
    [a-z]:
    [A-Z]
    [A-Za-z]
    [0-9A-Za-Z]

    [[:digit:]]
    [[:upper:]]
    [[:lower:]]
    [[:space:]]........




>>> import glob
>>> glob.glob('./[0-9].*')
['./1.gif', './2.txt']
>>> glob.glob('*.gif')
['1.gif', 'card.gif']
>>> glob.glob('?.gif')
['1.gif']
>>> glob.glob('**/*.txt', recursive=True)
['2.txt', 'sub/3.txt']
>>> glob.glob('./**/', recursive=True)
['./', './sub/']

>>> import glob
>>> glob.glob('*.gif')
['card.gif']
>>> glob.glob('.c*')
['.card.gif']
"""
import os
import glob

files1 = [file for file in os.listdir('.') if file.endswith('.conf')]
# 获取当前目录所有以.conf结尾的文件;
files2=  glob.glob('./*.conf')
print(files1)
print(files2)








