"""
文件名: .py
创建时间: 2019-01-15 11:
作者: lvah
联系方式: 976131979@qq.com
代码描述:




社交网站， 每一个标签都会有自己的用户群， 通过圈子可以找到有共同特征的人(eg:
python开发， 电影。。。。。。)， 当一个用户加入一个或者多个圈子后， 系统可以
向这个用户推荐圈子中的人



"""

import redis

pool = redis.ConnectionPool(host='localhost', port=6379)
conn = redis.Redis(connection_pool=pool)
# 选择集合存储
conn.sadd("python", 'user1')
conn.sadd("python", 'user2')
conn.sadd("python", 'user3')
conn.sadd("movie", 'user1')
conn.sadd("movie", 'user6')
conn.sadd("movie", 'user7')
# 获取某个圈子的成员
print(conn.smembers('python'))
print(conn.smembers('movie'))
# 获取两个圈子共同拥有的成员
print(conn.sinter('python', 'movie'))

# 获取并集
print(conn.sunion('python', 'movie'))
