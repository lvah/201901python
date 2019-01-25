"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

import re

s = 'westos is a company'
print(s.replace('westos', 'fentiao'))
# 将westos和company都替换位cat
print(re.sub(r'(westos|company)', 'cat', s))

# 将所有的数字替换位0;
s1 = "本次转发数位100， 点赞数为80;"
print(re.sub(r'\d+', '0', s1))


def addNum(Obj):
    # num是一个字符串
    num = Obj.group()
    # newNum是一个整形数
    newNum = int(num) + 1
    return str(newNum)


# .*?
# 对于所有的数字加1；
print(re.sub(r'\d+', addNum, s1))

s2 = '1+2=3'
print(re.split(r'[+=]', s2))
