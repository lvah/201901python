"""
文件名: models.py
日期: 2019-03-17  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from datetime import datetime
from app import db


# 关联
#   1. 标签(1)和电影(n)：
#   2. 电影(1)和评论(n)
#   3. 用户(1)和评论(n)
#   4. 用户(1)和用户登录日志(n)
#   5. 角色(1)和权限(n)
#   6. 角色(1)和管理员(n)
# 标签表
class Tag(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), unique=True, index=True)  # 标签名称， 不能重复;
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    movies = db.relationship('Movie', backref='tag')  # 反向关联， 让Movie表多一个属性， tag

    def __repr__(self):
        return "<Tag %s>" % (self.name)


# 电影表
class Movie(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), unique=True, index=True)  # 名称，不能重复;
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    info = db.Column(db.Text)  # 电影简介
    star = db.Column(db.SmallInteger)  # 电影的星级
    area = db.Column(db.String(50))  # 地区
    length = db.Column(db.String(20))  # 片长
    release_time = db.Column(db.DateTime)  # 上映时间
    url = db.Column(db.String(200), unique=True)  # 上传电影内容的url地址;
    logo = db.Column(db.String(200), unique=True)  # 上传电影封面的url地址;
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'))  # 标签的外键关联
    comments = db.relationship('Comment', backref="movie")  # 电影和评论的反向引用

    def __repr__(self):
        return '<Movie %s>' % (self.name)


# 预告管理表
class Preview(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), unique=True, index=True)  # 名称， 不能重复;
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    logo = db.Column(db.String(200), unique=True)  # 上传预告封面的url地址;

    def __repr__(self):
        return "<Preview %s>" % (self.name)


# 会员管理数据库
class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(300))
    email = db.Column(db.String(50), unique=True)  # 邮箱地址
    phone = db.Column(db.Integer, unique=True)
    face = db.Column(db.String(50), unique=True)  # 用户头像url地址
    gender = db.Column(db.Boolean)  # 性别
    comments = db.relationship('Comment', backref='user')  # 用户和评论的反向关联
    userlogs = db.relationship('Userlog', backref='user')  # 会员和会员登录日志的反向关联


    def verify_password(self, password):
        from werkzeug.security import  check_password_hash
        # 判断密码是否正确
        return  check_password_hash(self.password, password)

    def __repr__(self):
        return "<User %s>" % (self.name)


# 电影评论数据表: 评论和用户/电影关联
class Comment(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content = db.Column(db.String(50), unique=True, index=True)  # 评论的内容
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))  # 电影和评论的外键关联
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 电影和用户的关联

    def __repr__(self):
        return "<Comment %s>" % (self.content[:6])


# 日志管理表
# 1. 会员登录日志表
# 2. 管理员登录日志表
# 3. 管理员操作日志表

#
class Userlog(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # 会员和会员登录日志之间的关联
    ip = db.Column(db.String(30))  # 用户登录的ip
    area = db.Column(db.String(50))  # 用户客户端登录所在的地理位置

    def __repr__(self):
        return 'Userlog %s' % (self.ip)


# 权限管理的数据库表
class Auth(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    name = db.Column(db.String(30), unique=True)  # 权限的名称
    url = db.Column(db.String(50), unique=True)  # 权限的url地址
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    def __repr__(self):
        return '<Auth %s>' % (self.name)


# 角色管理
class Role(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    name = db.Column(db.String(30), unique=True)  # 角色的名称
    auths = db.relationship('Auth', backref='role')
    admins = db.relationship('Admin', backref='role')

    def __repr__(self):
        return '<Role %s>' % (self.name)


# 管理员数据表
class Admin(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    name = db.Column(db.String(30), unique=True)  # 名称
    password = db.Column(db.String(100))
    is_super = db.Column(db.Boolean, default=False)  # 是否为超级管理员(可以做任何操作)， 默认不是
    role_id = db.Column(db.Integer, db.ForeignKey('role.id')) # 角色和管理员的关联
    adminlogs = db.relationship("Adminlog", backref='admin')  # 管理员登录日志
    adminOplogs = db.relationship('AdminOplog', backref='admin') # 管理员操作日志

    def __repr__(self):
        return  "<Admin %s>" %(self.name)

# 管理员登录日志
class Adminlog(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 管理员和管理员登录日志之间的关联
    ip = db.Column(db.String(30))  # 登录的ip
    area = db.Column(db.String(50))  # 客户端登录所在的地理位置

    def __repr__(self):
        return 'Adminlog %s' % (self.ip)


# 管理员操作日志
class AdminOplog(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    addtime = db.Column(db.DateTime, default=datetime.utcnow())  # 创建时间
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))  # 管理员和管理员登录日志之间的关联
    content = db.Column(db.String(30))  # 管理员操作的内容
    ip = db.Column(db.String(30))  # 登录的ip
    area = db.Column(db.String(50))  # 客户端登录所在的地理位置

    def __repr__(self):
        return 'AdminOplog %s' % (self.ip)


