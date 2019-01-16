"""
文件名: .py
创建时间: 2019-01-16 13:
作者: lvah
联系方式: 976131979@qq.com
代码描述:

sys模块：全称system，指的是解释器（os指的是操作系统）
常用操作，用于接收系统操作系统调用解释器传入的参数

- sys.argv           命令行参数List，第一个元素是程序本身路径
- sys.exit(n)        退出程序，正常退出时exit(0)
- sys.version        获取Python解释程序的版本信息
- sys.maxsize         最大的Int值
- sys.path           返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值
- sys.platform       返回操作系统平台名称


"""
import os
import sys
print(sys.argv)
# 获取脚本名称  sys.argv[0]
# 获取脚本传递的第一个参数  sys.argv[1]
# 获取脚本传递的第二个参数  sys.argv[2]


print(sys.version[:3])

# 作用， 根据python版本编写符合不同版本的程序， 使得程序可兼容；
if sys.version[0] == '2':
    print("running in python2.......")
elif sys.version[0] == '3':
    print("running in python3........")

print(sys.maxsize)
print(sys.path)


# 可以实现跨平台;
print(sys.platform)
if sys.platform == 'linux':
    os.system('ifconfig')
else:
    os.system('ipconfig')





