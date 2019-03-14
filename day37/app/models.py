"""
文件名: $NAME.py
日期: 10  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 

# 存储数据库相关的操作

"""


### 用户和角色是什么关系?
#    - 一对一
#    - 一对多: 角色是一， 用户是多， 外键写在多的一端
#   - 多对多
from datetime import datetime

from app import db


class Role(db.Model):
    __tablename__ = "用户角色"
    # id号递增autoincrement=True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20))
    # 反向引用, Role表中有属性users， User类中有role这个属性;
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return "<Role %s>" % (self.name)


class User(db.Model):
    __tablename__ = "网站用户"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, index=True, nullable=False)  # unique=True用户名不能重复
    password = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), unique=True, index=True)
    # 设置默认值， 位当前用户的创建时间;
    add_time = db.Column(db.DateTime, default=datetime.now())
    # 1-男 2-女
    gender = db.Column(db.SmallInteger, default=2)
    age = db.Column(db.Integer)
    #### 重要的： 用户角色id不能随便设置， 需要从Role中查询, （外键关联）
    role_id = db.Column(db.Integer, db.ForeignKey('用户角色.id'))

    # 定义了 __repr()__ 方法,返回一个具有可读性的字符串表示模型,可在调试和测试时使用。
    def __repr__(self):
        return "<User %s>" % (self.username)






