"""
## 1. 什么是Redis?

REmote DIctionary Server(Redis) 是一个key-value存储系统。使用ANSI C语言编写、遵守BSD协议、支持网络、可基于内存亦
可持久化的日志型、Key-Value数据库，并提供多种语言的API(python, php, java.....)。


它通常被称为数据结构服务器，因为值（value）
可以是 字符串(String), 哈希(Map), 列表(list), 集合(sets) 和 有序集合(sorted sets)等类型。


dict = {'name':"fentiao", "age":100, "scores": [100, 90, 100]}




# 2.Redis的优势？

- 性能极高 – Redis能读的速度是110000次/s,写的速度是81000次/s 。
- 丰富的数据类型 – Redis支持二进制案例的 Strings, Lists, Hashes, Sets 及 Ordered Sets 数据类型操作。
- 原子 – Redis的所有操作都是原子性的，意思就是要么成功执行要么失败完全不执行。单个操作是原子性的。多个操作也支持事务，即原子性，
通过MULTI和EXEC指令包起来。
- Redis支持数据的备份，即master-slave模式的数据备份。
- Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。




## 3.redis的安装
下载地址：http://redis.io/download，下载最新稳定版本。
tar xzf redis-5.0.3.tar.gz



- 启动:
make完后 redis-5.0.3目录下会出现编译后的redis服务程序redis-server,
还有用于测试的客户端程序redis-cli,两个程序位于安装目录 src 目录下：
./redis-server


也可以通过启动参数告诉redis使用指定配置文件使用下面命令启动。
./redis-server ../redis.conf


******************注意:
vim /etc/services   # 记录服务对应的端口号
常见的端口号:
    http: 80
    ssh: 22
    mysql: 3306
    redis: 6379



## 常用操作:
### 字符串(String)

127.0.0.1:6379> set views 1000
127.0.0.1:6379> INCR views
(integer) 1001
127.0.0.1:6379> get views
"1001"
127.0.0.1:6379> INCR views
(integer) 1002

127.0.0.1:6379> DECR views
(integer) 1004
127.0.0.1:6379> DECR views
(integer) 1003


###








"""