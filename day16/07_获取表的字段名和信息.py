"""
文件名: .py
创建时间: 2019-01-12 15:
作者: lvah
联系方式: 976131979@qq.com
代码描述:


"""
import time

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



# __enter__, __exit__

# with语句实现的效果是: with语句执行结束， 如果成功， 则提交改变的数据， 如果不成功， 则回滚.
with conn:
    # ****** 判断是否连接?
    print(conn.open)  # True
    # 2. 创建游标对象，
    cur = conn.cursor()
    # 3).
    sqli = "select * from hello;"
    result = cur.execute(sqli)  # 默认不返回查询结果集， 返回数据记录数。

    # 显示每列的详细信息
    des = cur.description
    print("表的描述:", des)

    # 获取表头
    print("表头:", ",".join([item[0] for item in des]))
    cur.close()


conn.close()
print("with语句之外:", conn.open)   # False