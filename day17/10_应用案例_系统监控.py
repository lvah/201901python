"""
文件名: .py
创建时间: 2019-01-15 14:
作者: lvah
联系方式: 976131979@qq.com
代码描述:

需求：

    1. 获取当前主机信息， 包含操作系统名， 主机名， 内核版本， 硬件架构等


    2. 获取开机时间和开机时长；


    3. 获取当前登陆用户




"""
import os
import psutil
from datetime import  datetime
print("主机信息".center(50, '*'))
info = os.uname()
print("""
    操作系统: %s
    主机名: %s
    内核版本: %s
    硬件架构: %s
""" % (info.sysname, info.nodename, info.release, info.machine))


print("开机信息".center(50, '*'))
boot_time = psutil.boot_time()   # 返回时间戳
#  将时间戳转换为datetime类型的时间2019-01-15 08:59:01
boot_time_obj = datetime.fromtimestamp(boot_time)
# print(type(boot_time_obj))
now_time = datetime.now()
delta_time = now_time - boot_time_obj
# print(type(delta_time))
print("开机时间: ",  boot_time_obj)
print("当前时间: ", str(now_time).split('.')[0])   # str是为了将对象转换为字符串， 实现分离;
                                                  # split分离是为了去掉毫秒
print("开机时长: ", str(delta_time).split('.')[0])    # split分离是为了去掉毫秒


print("当前登陆用户".center(50, '*'))
login_users = psutil.users()
# 集合生成式实现去重
print({user.name for user in login_users})


info = psutil.users()[0]
print(info)
print(type(info))

