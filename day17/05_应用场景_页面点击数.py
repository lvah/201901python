"""
文件名: .py
创建时间: 2019-01-15 11:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""

import redis

pool = redis.ConnectionPool(host='localhost', port=6379)
conn = redis.Redis(connection_pool=pool)

conn.set('views', 19800)
conn.incr('views')
print(conn.get('views'))


