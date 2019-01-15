"""
文件名: .py
创建时间: 2019-01-15 14:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""
import os
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# print(date.today())
# print(datetime.now())

# 如何计算三天前的时间和三天后的时间
d = date.today()
delta = timedelta(days=3)
print(d + delta)
print(d - delta)

# 如何计算两个小时之前的时间? 两个小时之后的时间
now_hour = datetime.now()
delta = timedelta(hours=2)
print(now_hour - delta)
print(now_hour + delta)
#  返回两个时间， 想计算两个时间之间的时间差
now_time = datetime.now()  # 对象
pwd_time = os.path.getmtime('/etc/passwd')  # 时间戳
pwd_time_obj = datetime.fromtimestamp(pwd_time)


delta = now_time - pwd_time_obj
print(delta)





