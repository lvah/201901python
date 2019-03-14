from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import  datetime
# **************************1. python3中MySQLdb报错解决方法*************************
import pymysql


pymysql.install_as_MySQLdb()

app = Flask(__name__)

# *************************2. 数据库的配置与实例化**********************************
# 对数据库操作(mysql, redis)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:redhat@localhost/UserTest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 实例化对象
db = SQLAlchemy(app)
# ***********************3. 定义数据库模型************************************
# user ==== (id, username, password, email)
class User(db.Model):
    # 默认情况下表名为类的名称， 如果想要重新设置表名， __tablename__
    __tablename__ = "用户信息"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, index=True, nullable=False)  # unique=True用户名不能重复
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), unique=True, index=True)
    # 设置默认值， 位当前用户的创建时间;
    add_time = db.Column(db.DateTime, default=datetime.now() )


if __name__ == '__main__':
    # 创建所有的表
    db.drop_all()
    db.create_all()

    # 插入数据(insert)
    u1 = User(username="粉条", password="westos", email="fentiao@qq.com")
    u2 = User(username="粉丝", password="westos", email="fensi@qq.com")
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()

    # 删除数据(delete)
    delete_user = User.query.filter_by(username="粉条").first()
    db.session.delete(delete_user)
    db.session.commit()

    # 更新数据(update)

    update_user = User.query.filter_by(username="粉丝").first()
    print(update_user.username)
    print(update_user.password)
    print(update_user.email)
    print(update_user.id)
    print("正在更新邮箱地址.......")
    update_user.email = 'fensiupdate@qq.com'
    db.session.add(update_user)
    db.session.commit()
    print(update_user.email)

    # 查看数据(select)
    users = User.query.all()
    print(users)

    # 删除所有的表;
    #db.drop_all()
