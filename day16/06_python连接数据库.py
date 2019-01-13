"""
文件名: .py
创建时间: 2019-01-12 14:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""
import pymysql

# 1. 连接数据库，
conn = pymysql.connect(
    host='localhost',
    user='root',
    password='redhat',
    db='helloTest',
    charset='utf8',
    # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
)
# ****python, 必须有一个游标对象， 用来给数据库发送sql语句， 并执行的.
# 2. 创建游标对象，
cur = conn.cursor()

# 3. 对于数据库进行增删改查
# 1). ************************创建数据表**********************************
# try:
#     create_sqli = "create table hello (id int, name varchar(30));"
#     cur.execute(create_sqli)
# except Exception as e:
#     print("创建数据表失败:", e)
# else:
#     print("创建数据表成功;")


# 2). *********************插入数据****************************
# try:
#     insert_sqli = "insert into hello values(2, 'fensi');"
#     cur.execute(insert_sqli)
# except Exception as e:
#     print("插入数据失败:", e)
# else:
#     # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
#     conn.commit()
#     print("插入数据成功;")


# 3). *********************插入多条数据****************************
# try:
#     info = [(i, "westos%s" %(i)) for i in range(100)]
#
#     # *********************第一种方式********************
#     # # %s必须手动添加一个字符串， 否则就是一个变量名， 会报错.
#     # insert_sqli = "insert into hello values(%d, '%s');"
#     # for item in info:
#     #     print('insert语句:', insert_sqli %item)
#     #     cur.execute(insert_sqli %item)
#
#     # *********************第二种方式********************
#     insert_sqli = "insert into hello values(%s, %s);"
#     cur.executemany(insert_sqli, info )
# except Exception as e:
#     print("插入多条数据失败:", e)
# else:
#     # 如果是插入数据， 一定要提交数据， 不然数据库中找不到要插入的数据;
#     conn.commit()
#     print("插入多条数据成功;")
#
#


# 4). **************************数据库查询*****************************
sqli = "select * from hello;"
result = cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。
print(result)
#
# print(cur.fetchone())     # 1). 获取下一个查询结果集;
# print(cur.fetchone())
# print(cur.fetchone())

# print(cur.fetchmany(4))   # 2). 获取制定个数个查询结果集；

# info = cur.fetchall()     # 3). 获取所有的查询结果
# print(info)
# print(len(info))

# print(cur.rowcount)       # 4). 返回执行sql语句影响的行数

#  5). 移动游标指针
print(cur.fetchmany(3))
print("正在移动指针到最开始......")
cur.scroll(0, 'absolute')
print(cur.fetchmany(3))

print("正在移动指针到倒数第2个......")
print(cur.fetchall())    # 移动到最后
cur.scroll(-2, mode='relative')

print(cur.fetchall())
# 4. 关闭游标
cur.close()
# 5. 关闭连接
conn.close()
