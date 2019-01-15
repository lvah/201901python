"""
文件名: .py
创建时间: 2019-01-15 14:
作者: lvah
联系方式: 976131979@qq.com
代码描述:

#  ***********************1. 时间表示的几种类型 ********************
#  1). 时间戳
#  2). 字符串的时间
#  3). 元组类型的时间





"""
import os
import time
# from datetime import  date
# from datetime import  time
# from datetime import  datetime

#  1). 时间戳
# print(time.time())

#  2). 字符串的时间
# print(time.ctime())

#  3). 元组类型的时间
# print(time.localtime())
# info = time.localtime()
# print(info.tm_year)
# print(info.tm_yday)




# *********************************2. 如何对于不同时间类型的转换**********************
# 将时间戳类型转换为字符串的时间
pwd_time = os.path.getmtime('/etc/passwd')
print(pwd_time)
print("文件修改时间: ", time.ctime(pwd_time))

# 将时间戳类型转换为元组类型
print(time.localtime(pwd_time))

# # 将元组类型时间转换为时间戳
# tuple_time = time.localtime()
# print(time.mktime(tuple_time))

# 将元组的时间转换为字符串时间
tuple_time = time.localtime()
print(time.strftime('%Y-%m-%d', tuple_time))
print(time.strftime('%Y-%m-%d %H:%M:%S', tuple_time))

# 将字符串的时间转换为元组
mytime = "2019/01/15"
print(time.strptime(mytime, '%Y/%m/%d'))



