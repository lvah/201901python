# encoding:utf-8
"""
文件名: .py
创建时间: 2019-01-16 15:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""

with open('/etc/hosts', 'a+') as f:
    f.write('\n')
    for i in range(100):
        f.write('172.25.254.%s  foundation%s.example.com \n' % (i + 1, i + 1))
