"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

字符匹配:
    r'westos'


字符类:
    [pP]ython
    westos[pP]
    [aeiou]
    [a-z]
    [A-Z]
    [a-zA-Z0-9]
    [^aeiou]
    [^0-9]
特殊字符类:
    .: 匹配除了\n之外的任意字符； [.\n]
    \d:  digit--(数字)， 匹配一个数字字符， 等价于[0-9]
    \D: 匹配一个非数字字符， 等价于[^0-9]
    \s:  space(广义的空格: 空格, \t, \n, \r), 匹配单个任何的空白字符;
    \S:  匹配除了单个任何的空白字符;
    \w:  字母数字或者下划线, [a-zA-Z0-9_]
    \W: 除了字母数字或者下划线, [^a-zA-Z0-9_]

"""
import re


# 匹配数字
# pattern = r'\d'
pattern = r'[0-9]'
string = "hello_1$%"
print(re.findall(pattern, string))


# 匹配字母数字或者下划线;
# pattern = r'\w'
pattern = r'[a-zA-Z0-9_]'
string = "hello_1$%"
print(re.findall(pattern, string))

# 匹配除了字母数字或者下划线;
# pattern = r'\W'
pattern = r'[^a-zA-Z0-9_]'
string = "hello_1$%"
print(re.findall(pattern, string))

# .: 匹配除了\n之外的任意字符； [.\n]
print(re.findall(r'.', 'hello westos\n\t%$'))