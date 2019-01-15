# encoding=utf-8
"""
文件名: .py
创建时间: 2019-01-15 09:
作者: lvah
联系方式: 976131979@qq.com
代码描述:

*****************************python2中检测*****************************



"""
import random
import MySQLdb as pymysql

# 1. 连接数据库
conn = pymysql.connect(
    host='localhost',
    user='root',
    passwd='redhat',
    db='helloTest',
    autocommit=True,
    charset='utf8'
)
# 2. 创建游标
cur = conn.cursor()

# create_db = "create database westos;"
# cur.execute(create_db)
# conn.select_db('westos')  # 连接数据库
# 3. 操作
bank_id = random.randint(10000, 20000)
print("创建银行账户%s ............" % (bank_id))
bank_pwd = raw_input("请输入用户密码:")
bank_money = float(raw_input("存储金额:"))
insert_sqli = "insert into bankData values(%d, %f , '%s')" % (bank_id, 0, bank_pwd)
cur.execute(insert_sqli)
print("创建账户成功........")
# 4. 关闭游标
cur.close()
# 5. 关闭连接
conn.close()
