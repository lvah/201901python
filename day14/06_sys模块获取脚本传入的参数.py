import sys

# 是一个列表， 第一个元素是脚本名称，
#  后面一次是脚本后传入的参数;
# ['06_sys模块获取脚本传入的参数.py', '1', '2', '3']
# print(sys.argv)
print(sys.argv[1:])