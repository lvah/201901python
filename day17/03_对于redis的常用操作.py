"""
文件名: .py
创建时间: 2019-01-15 11:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""
import time

import redis

#  如何连接redis?


# *******************************第一种方式***********************************
# # redis.Redis(host='localhost', port=6379)
# conn = redis.Redis()
# #
# conn.set('name', 'fentiao', 3)
# print(conn.get('name'))
#
# print("等待3秒........")
# time.sleep(3)
# print(conn.get('name'))
#


# ******************************第二种方式*********************
# 为了减少每次建立连接， 释放连接的开销， 推荐使用连接池。
# 多个redis对象可以共用一个连接池。

pool = redis.ConnectionPool(host='localhost', port=6379)
conn = redis.Redis(connection_pool=pool)
conn.set('name', 'fentiao', 3)  # 4代表的是失效时间， 单位为秒
# 默认返回bytes类型， 如果转换， 需要解码为utf-8编码格式
print(conn.get('name').decode('utf-8'))
print("等待3秒........")
time.sleep(3)
print(conn.get('name'))














