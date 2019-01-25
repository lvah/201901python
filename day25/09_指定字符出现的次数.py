"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



匹配字符出现次数:
    *: 代表前一个字符出现0次或者无限次；    \d*,  .*
    +: 代表前一个字符出现一次或者无限次;     d+
    ?: 代表前一个字符出现1次或者0次；   假设某些字符可省略， 也可以不省略的时候使用

第二种方式:
    {m}: 前一个字符出现m次;
    {m,}: 前一个字符至少出现m次;  * == {0,}; + ==={1,}
    {m,n}: 前一个字符出现m次到n次; ? === {0,1}




^: 以什么开头
$: 以什么结尾
"""
import re

# *: 代表前一个字符出现0次或者无限次；    \d *,.*
print(re.findall(r'\d*', '234'))
print(re.findall(r'.*', 'hello223%'))
print(re.findall(r'd*', 'ddhello223%'))


#     +: 代表前一个字符出现一次或者无限次;     d+
print(re.findall(r'd+', ''))
print(re.findall(r'd+', 'dddderrttt'))
print(re.findall(r'\d+', '阅读数: 8976 点赞数:900'))

#  ?: 代表前一个字符出现1次或者0次；   假设某些字符可省略， 也可以不省略的时候使用
# 2019-10
print(re.findall(r'\d+-?\d+', '2019-10'))
print(re.findall(r'\d+-?\d+', '201910'))
print(re.findall(r'\d{4}-?\d{1,}', '2019-1'))
print(re.findall(r'\d{4}-?\d{1,2}', '2019-10'))
print(re.findall(r'\d+-?\d+', '201910'))