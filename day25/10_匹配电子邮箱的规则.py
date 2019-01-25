#!/root/anaconda3/envs/2048/bin/python
#encoding:utf-8

"""
文件名: $NAME.py
日期: 25  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



# 练习: 匹配一个163邮箱;(xdshcdshvfhdvg@qq.com)  --- 如果想在正则里面匹配真实的. , \.
#       xdshcdshvfhdvg(可以由字母数字或者下划线组成， 但是不能以数字或者下划线开头； 位数是6-12之间)

"""

import re

def isEmail(address):
    pattern = r'^[a-zA-Z]\w{5,11}@163.com$'
    res = re.findall(pattern, address)
    if res:
        return  True
    else:
        return  False

if __name__ == '__main__':
    print(isEmail('hello@163.com'))
    print(isEmail('wehello@163.com'))
    print(isEmail('wehello@163.comaa'))
